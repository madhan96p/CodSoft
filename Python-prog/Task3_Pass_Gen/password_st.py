import streamlit as st
import random
import string
import pyperclip

st.title("🔐 Password Generator")

length = st.number_input("Password Length", min_value=4, max_value=50, value=12)
use_upper = st.checkbox("Include Uppercase")
use_lower = st.checkbox("Include Lowercase")
use_digits = st.checkbox("Include Digits")
use_symbols = st.checkbox("Include Symbols")

def generate(length, use_upper, use_lower, use_digits, use_symbols):
    chars = ""
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    if not chars:
        return "⚠️ Select at least one option!"
    return ''.join(random.choice(chars) for _ in range(length))

if st.button("Generate Password"):
    password = generate(length, use_upper, use_lower, use_digits, use_symbols)
    st.code(password)
    pyperclip.copy(password)
    st.success("✅ Password copied to clipboard! Try Ctrl+V to paste below 👇")
    st.text_input("Paste Here:", value="", placeholder="Try Ctrl+V here")

st.markdown(
    """
    <div style='text-align: center; font-size: 0.85rem; color: gray;'>
        Created by <a href='https://pragadeeshfolio.netlify.app/' target='_blank'>Pragadeesh Srinivasan</a>
    </div>
    """,
    unsafe_allow_html=True
)