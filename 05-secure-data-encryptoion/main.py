import streamlit as st
from cryptography.fernet import Fernet
import hashlib

# ----------------- CONSTANT SETUP -------------------
# 🔐 Use a fixed Fernet key (generate once via Fernet.generate_key().decode())
KEY = b'4BtaTDwU3AgAfS1BMLA9ka_WdRMA6twLU1DK1NFlv6k='  # Replace with your own key for production
cipher = Fernet(KEY)

# In-memory storage (RAM only)
if "stored_data" not in st.session_state:
    st.session_state["stored_data"] = {}  # format: {"label": {"encrypted_text": str, "passkey": str}}

if "failed_attempts" not in st.session_state:
    st.session_state["failed_attempts"] = 0

# ----------------- ENCRYPTION UTILS -------------------
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted_text, passkey, stored_passkey):
    if hash_passkey(passkey) == stored_passkey:
        st.session_state["failed_attempts"] = 0
        return cipher.decrypt(encrypted_text.encode()).decode()
    else:
        st.session_state["failed_attempts"] += 1
        return None

# ----------------- UI PAGES -------------------
st.set_page_config(page_title="🔐 Secure Data App")
st.title("🔐 Secure Data Encryption System")

menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigate", menu)

# 🏠 Home
if choice == "Home":
    st.subheader("🏠 Welcome to Secure Data System")
    st.write("This app helps you securely store and retrieve sensitive information using passkeys.")

# 📂 Store Data
elif choice == "Store Data":
    st.subheader("📂 Store Data Securely")

    label = st.text_input("Label for Your Data (e.g., 'Email Password')")
    text = st.text_area("Enter Text to Encrypt")
    passkey = st.text_input("Enter Passkey", type="password")

    if st.button("Encrypt & Store"):
        if label and text and passkey:
            encrypted = encrypt_data(text)
            hashed = hash_passkey(passkey)
            st.session_state["stored_data"][label] = {"encrypted_text": encrypted, "passkey": hashed}
            st.success("✅ Data Stored Successfully!")
            st.code(encrypted, language="text")
        else:
            st.error("⚠️ All fields are required!")

# 🔍 Retrieve Data
elif choice == "Retrieve Data":
    st.subheader("🔍 Retrieve Encrypted Data")

    if st.session_state["failed_attempts"] >= 3:
        st.warning("🚫 Too many failed attempts. Redirect to Login.")
        st.stop()

    stored_data = st.session_state["stored_data"]
    if not stored_data:
        st.info("ℹ️ No data stored yet.")
    else:
        label = st.selectbox("Select Label", list(stored_data.keys()))
        passkey = st.text_input("Enter Passkey to Decrypt", type="password")

        if st.button("Decrypt"):
            record = stored_data[label]
            decrypted = decrypt_data(record["encrypted_text"], passkey, record["passkey"])
            if decrypted:
                st.success("✅ Decrypted Data:")
                st.code(decrypted, language="text")
            else:
                remaining = 3 - st.session_state["failed_attempts"]
                st.error(f"❌ Wrong passkey! Attempts left: {remaining}")

# 🔑 Login
elif choice == "Login":
    st.subheader("🔑 Reauthorization Required")
    master_pass = st.text_input("Enter Master Password", type="password")

    if st.button("Login"):
        if master_pass == "admin123":
            st.session_state["failed_attempts"] = 0
            st.success("✅ Access Restored! You can now try again from 'Retrieve Data'.")
        else:
            st.error("❌ Incorrect Master Password.")
