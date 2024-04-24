import streamlit as st
from openai import OpenAI

# Postavljanje API ključa
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Naslov i podnaslov aplikacije
st.title("📧 Pisac najboljih newsletter-a")
st.caption(
    "Vaš lični asistent za pisanje newsletter-a 📧🚀 made by [@nikolanewsletter](https://www.instagram.com/nikola.newsletter/)"
)

# Inicijalizacija promenljivih preko input polja
if "inputs_set" not in st.session_state:
  st.session_state.inputs_set = False

if not st.session_state.inputs_set:
  ekspertiza = st.text_input("Unesite ekspertizu")
  tema = st.text_input("Unesite naslov newslettera")
  ciljna_grupa = st.text_input("Unesite ciljnu grupu (kome se obraćate)")
  bolne_tacke = st.text_input(
      "Unesite bolne tačke klijenata (navedite problem sa kojim se suočavaju)"
  )
  cta = st.text_input("Unesite poziv na akciju (na šta ih pozivate)")
  if st.button("GENERIŠI NEWSLETTER"):
    st.session_state.ekspertiza = ekspertiza
    st.session_state.tema = tema
    st.session_state.ciljna_grupa = ciljna_grupa
    st.session_state.bolne_tacke = bolne_tacke
    st.session_state.cta = cta
    st.session_state.inputs_set = True
    if st.session_state.inputs_set:
      prompt = f'''
        Ponašaj se kao dugogodišnji {st.session_state.ekspertiza}.
    
        Napiši mi newsletter na temu: {st.session_state.tema} 
    
        Moja ciljna grupa su: {st.session_state.ciljna_grupa}. Takvim ljudima pomažem pri rešavanju problema. 
    
        Razmišljaj o tome da su njihove bolne tačke {st.session_state.bolne_tacke}.
    
        Želim da mi napišeš newsletter post koji se obraća u prvom licu jednine. Napiši 5 pasusa po 200 reči.
    
        Na kraju newslettera je potrebno da pozoveš na akciju. CTA: {st.session_state.cta}.
        '''
      with st.spinner(
          "🤔 Kreiram newsletter za tebe! ❤️ Pozdravlja te moj tvorac @nikola.newsletter 👋"
      ):
        response = client.chat.completions.create(model="gpt-3.5-turbo-0125",
                                                  messages=[{
                                                      "role": "system",
                                                      "content": "start"
                                                  }, {
                                                      "role": "user",
                                                      "content": prompt
                                                  }])
        msg = response.choices[0].message.content
        st.session_state.last_response = msg
        st.success("Newsletter je spreman!")

        # Prikaz rezultata
        st.write(msg)
