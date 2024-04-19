import streamlit as st
from openai import OpenAI

# Postavljanje API ključa
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Ovde menjate naslov i podnaslov Chatbot aplikacije
st.title("📧 Pisac najboljih newsletter naslova")
st.caption(
    "Vaš lični asistent za pisanje newsletter naslova 📧🚀 made by [@nikolanewsletter](https://www.instagram.com/nikola.newsletter/)"
)
# Postavljanje inicijalne poruke u session_state
if "messages" not in st.session_state:
  st.session_state["messages"] = [{
      "role":
      "assistant",
      "content":
      "Ti si ekspert za kopirajting. Tvoja uska specijalnost su naslovi za newslettere. Tvoj zadatak je da mi napišeš po 10 naslova u buletima jedan ispod drugog. Napomena: svaki naslov treba da sadrži najviše 40 karaktera.  Neophodno je da naslovi sadrže bar jedan emoji. Naslove piši na osnovu branše koju ti budem svaki put zadavao. Odgovore daj na srpskom jeziku koristeći gramatiku srpskog jezika."  # Prompt za programiranje ChatGPT-a
  }]

# Prikazivanje poruka osim prve inicijalne
for msg in st.session_state.messages[1:]:
  st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(
    "Unesi ovde branšu"):  # Dodavanje placeholder teksta
  st.session_state.messages.append({"role": "user", "content": prompt})
  st.chat_message("user").write(prompt)

  with st.spinner(
      "🤔 Kreiram newsletter naslove za tebe! ❤️ Evo pozdravlja te moj tvorac @nikola.newsletter 👋"
  ):
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=st.session_state.messages)  # ChatGPT model
    msg = response.choices[0].message.content

  st.session_state.messages.append({"role": "assistant", "content": msg})
  st.chat_message("assistant").write(msg)
