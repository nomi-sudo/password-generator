import random
import string
import streamlit as st

st.set_page_config(page_title="Password Generator", page_icon="🔐")
st.title("🔐 Password Generator")

c1, c2, c3 = st.columns(3)
nl = c1.number_input("Letters", 0, 50, 8)
ns = c2.number_input("Symbols", 0, 50, 2)
nn = c3.number_input("Numbers", 0, 50, 2)

if st.button("Generate", type="primary"):
    chars = ([random.choice(string.ascii_letters) for _ in range(nl)]
             + [random.choice("!@#$%^&*()/") for _ in range(ns)]
             + [random.choice(string.digits) for _ in range(nn)])
    random.shuffle(chars)
    st.write("Your password is:")
    st.code("".join(chars) or "(empty)")
