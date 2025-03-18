import streamlit as st
import random
import string


BLACKLISTED_PASSWORDS = {"password", "123456", "qwerty", "password123", "123456789", "admin", "welcome"}

def generate_password(length=12):
    """Generates a strong password with random characters"""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def calculate_score(password):
    """Calculates password strength score based on multiple factors"""
    score = 0
    messages = []

    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)


    
    if password in BLACKLISTED_PASSWORDS:
        return 0, ["🚨 This is a commonly used weak password. Choose something unique."]

   
    if length >= 8: score += 2
   

    if has_upper: score += 2
    else: messages.append("Include at least one uppercase letter.")

    if has_lower: score += 2
    else: messages.append("Include at least one lowercase letter.")

    if has_digit: score += 2
    else: messages.append("Add at least one number (0-9).")

    if has_special: score += 2
    else: messages.append("Include at least one special character (!@#$%^&*).")


    return score, messages

def check_score(password):
    if not password:
        return  

    score, messages = calculate_score(password)
    progress = score / 10
    st.progress(progress)


    if messages:
        for msg in messages:
            st.warning(msg)
    
    if score >= 9:
        st.success("🔥 **Very Strong Password!** You're secure. ✅")
    elif score >= 7:
        st.success("💪 **Strong Password!** Consider adding more length for better security.")
    elif score >= 5:
        st.warning("⚠️ **Moderate Password.** Improve by adding more variety.")
    elif score >= 3:
        st.error("❌ **Weak Password!** Add uppercase, numbers, and special characters.")
    else:
        st.error("🚨 **Very Weak Password!** Easily guessable. Try a stronger passphrase.")



st.title("~~~ Advanced Password Strength Meter ~~~")


password = st.text_input("Enter your password", type="password")
check_score(password)

if st.button("Generate Strong Password"):
    strong_password = generate_password(14) 
    st.text(f"Suggested Strong Password: `{strong_password}`")
    st.info("Copy this password and use it securely.")

st.caption("🔹 **Tip:** Use a password manager to securely store and manage your passwords.")
