# app.py
import streamlit as st
from password_generator import generate_password

def main():
    st.title("Streamlit Password Generator")

    length = st.slider("Select the length of the password:", 4, 32, 12)

    use_letters = st.checkbox("Include letters", value=True)
    use_numbers = st.checkbox("Include numbers", value=True)
    use_symbols = st.checkbox("Include symbols", value=True)

    if st.button("Generate Password"):
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        st.success("Your Password: {}".format(password))

if __name__ == "__main__":
    main()
