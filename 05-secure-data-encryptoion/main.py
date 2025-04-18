import streamlit as st
import hashlib, os, json, base64, time
from datetime import datetime
from cryptography.fernet import Fernet
import pandas as pd


# ──────────────────────────────────────────────────────────────────────────────
# CONFIGURATION
DATA_FILE      = "data.json"
FERNET_KEY     = b'4BtaTDwU3AgAfS1BMLA9ka_WdRMA6twLU1DK1NFlv6k='  # ← replace with your own
cipher         = Fernet(FERNET_KEY)

# PBKDF2 settings
HASH_NAME      = "sha256"
ITERATIONS     = 100_000
SALT_LEN       = 16

# Security
MAX_ATTEMPTS   = 3
LOCKOUT_SEC    = 60

# ──────────────────────────────────────────────────────────────────────────────
# UTILITIES: JSON PERSISTENCE

def load_data():
    if os.path.exists(DATA_FILE):
        return json.load(open(DATA_FILE, "r"))
    return {"users": {}}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

# ──────────────────────────────────────────────────────────────────────────────
# UTILITIES: PASSWORD HASHING

def hash_password(password, salt=None):
    """
    Hashes the password using PBKDF2 with SHA-256.
    Returns a base64-encoded string containing salt + derived key.
    """
    if salt is None:
        salt = os.urandom(SALT_LEN)  # Generate secure random salt
    dk = hashlib.pbkdf2_hmac(HASH_NAME, password.encode(), salt, ITERATIONS)
    return base64.b64encode(salt + dk).decode()  # Combine and encode

def verify_password(password, stored):
    """
    Verifies a password by decoding the stored hash,
    extracting the salt, and re-generating the derived key.
    """
    data = base64.b64decode(stored.encode())
    salt, dk_stored = data[:SALT_LEN], data[SALT_LEN:]  # Extract parts
    dk_new = hashlib.pbkdf2_hmac(HASH_NAME, password.encode(), salt, ITERATIONS)
    return dk_new == dk_stored  # Compare new and stored hashes
# ──────────────────────────────────────────────────────────────────────────────
# UTILITIES: ENCRYPT / DECRYPT

def encrypt_text(plain):
    return cipher.encrypt(plain.encode()).decode()

def decrypt_text(token):
    return cipher.decrypt(token.encode()).decode()

# ──────────────────────────────────────────────────────────────────────────────
# INITIALIZE SESSION STATE

if "data" not in st.session_state:
    st.session_state.data = load_data()

if "user" not in st.session_state:
    st.session_state.user = None

if "failed" not in st.session_state:
    st.session_state.failed = 0

if "lockout_until" not in st.session_state:
    st.session_state.lockout_until = 0

if "audit" not in st.session_state:
    st.session_state.audit = []

# Persist on every change
def persist():
    save_data(st.session_state.data)

# Log action
def log_action(action, label=""):
    st.session_state.audit.append({
        "time": datetime.utcnow().isoformat(),
        "user": st.session_state.user or "",
        "action": action,
        "label": label
    })

# ──────────────────────────────────────────────────────────────────────────────
# STREAMLIT UI

st.set_page_config("🔐 Secure Multi‑User App", layout="wide")
st.title("🔐 Advanced Secure Data Encryption System")

menu = ["Home", "Sign Up", "Log In", "Store Data",
        "Retrieve Data", "Export CSV", "Audit Log", "Logout"]
choice = st.sidebar.selectbox("Menu", menu)

# ──────────────────────────────────────────────────────────────────────────────
if choice == "Home":
    st.subheader("🏠 Welcome")
    st.markdown("""
      - **Multi‑user** accounts  
      - **PBKDF2** password hashing  
      - **Fernet** data encryption  
      - **Time‑based lockout** on 3 failed decrypts  
      - **Audit log** & **CSV export**  
    """)

elif choice == "Sign Up":
    st.subheader("🆕 Create Account")
    u = st.text_input("Username")
    p = st.text_input("Password", type="password")
    q = st.text_input("Security Question")
    a = st.text_input("Answer", type="password")
    if st.button("Sign Up"):
        users = st.session_state.data["users"]
        if not all([u,p,q,a]):
            st.error("All fields required.")
        elif u in users:
            st.error("User exists.")
        else:
            users[u] = {
                "pwd": hash_password(p),
                "q": q,
                "ans": hash_password(a),
                "entries": {}
            }
            persist()
            st.success("Account created!")

elif choice == "Log In":
    st.subheader("🔑 Log In")
    u = st.text_input("Username", key="li_user")
    p = st.text_input("Password", type="password", key="li_pwd")
    if st.button("Log In"):
        users = st.session_state.data["users"]
        if u in users and verify_password(p, users[u]["pwd"]):
            st.session_state.user = u
            st.session_state.failed = 0
            st.session_state.lockout_until = 0
            log_action("login")
            st.success(f"Welcome, {u}!")
        else:
            st.error("Invalid credentials.")

elif choice == "Store Data":
    if not st.session_state.user:
        st.warning("🔒 Please log in first."); st.stop()
    st.subheader("📂 Store Data")
    lbl = st.text_input("Label", key="lbl_store")
    txt = st.text_area("Text to Encrypt", key="txt_store")
    pk  = st.text_input("Passkey", type="password", key="pk_store")
    if st.button("Encrypt & Store"):
        if all([lbl,txt,pk]):
            token = encrypt_text(txt)
            hashed_pk = hash_password(pk)
            user = st.session_state.user
            st.session_state.data["users"][user]["entries"][lbl] = {
                "token": token, "pk": hashed_pk
            }
            persist(); log_action("store", lbl)
            st.success("Stored!"); st.code(token)
        else:
            st.error("All fields required.")

elif choice == "Retrieve Data":
    if not st.session_state.user:
        st.warning("🔒 Please log in first."); st.stop()
    # lockout
    if time.time() < st.session_state.lockout_until:
        rem = int(st.session_state.lockout_until - time.time())
        st.error(f"⏳ Locked out for {rem}s."); st.stop()
    st.subheader("🔍 Retrieve Data")
    user = st.session_state.user
    ents = st.session_state.data["users"][user]["entries"]
    if not ents:
        st.info("No entries.")
    else:
        lbl = st.selectbox("Select Label", list(ents.keys()))
        pk  = st.text_input("Passkey", type="password", key="pk_ret")
        if st.button("Decrypt"):
            rec = ents[lbl]
            if verify_password(pk, rec["pk"]):
                val = decrypt_text(rec["token"])
                st.success("Decrypted:"); st.code(val)
                st.session_state.failed = 0
                log_action("decrypt", lbl)
            else:
                st.session_state.failed += 1
                rem = MAX_ATTEMPTS - st.session_state.failed
                st.error(f"Wrong passkey! {rem} left.")
                if st.session_state.failed >= MAX_ATTEMPTS:
                    st.session_state.lockout_until = time.time() + LOCKOUT_SEC
                    st.error(f"⛔ Locked for {LOCKOUT_SEC}s.")

elif choice == "Export CSV":
    if not st.session_state.user:
        st.warning("🔒 Please log in first."); st.stop()
    st.subheader("📤 Export Entries as CSV")
    user = st.session_state.user
    ents = st.session_state.data["users"][user]["entries"]
    df = pd.DataFrame([
        {"label":l,"token":e["token"],"time":datetime.utcnow().isoformat()}
        for l,e in ents.items()
    ])
    st.download_button("Download CSV", df.to_csv(index=False), "data.csv")

elif choice == "Audit Log":
    st.subheader("📝 Audit Log")
    df = pd.DataFrame(st.session_state.audit)
    st.dataframe(df)

elif choice == "Logout":
    st.session_state.user = None
    st.session_state.failed = 0
    st.session_state.lockout_until = 0
    st.success("Logged out.")

# Persist on every run
persist()
