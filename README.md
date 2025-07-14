# WorkOS DSE Take-Home — SSO Demo App

This is a simple Flask application that demonstrates Single Sign-On (SSO) integration using the WorkOS Test Provider. It simulates the SSO experience that a real identity provider (IdP) like Okta or Google Workspace would provide, without requiring any external setup.

---

### Demo Video

[Click here to watch the demo on Loom](https://www.loom.com/share/2a373e014e2b464c8b95b13cd84aa5d9?sid=2100c5a6-7b45-4500-b63a-44e4ad35a6f7)

---

## What This App Does

- Initiates an SSO flow via the WorkOS Test Provider
- Authenticates a user and retrieves profile information
- Displays:
  -  First name
  -  Last name
  -  Email
  -  Organization ID
  -  Organization name (**Bonus**)

---

## Tech Stack

- Python 3 (Flask)
- WorkOS Python SDK
- HTML (Jinja2 templates)
- `python-dotenv` for config

---

## Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/workos-dse-demo.git
cd workos-dse-demo

### 2.Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

** if youdont have reqyurements.txt just run
pip install flask workos python-dotenv


### 4. Create a .env file with the following contents
WORKOS_API_KEY=sk_test_your_key_here
WORKOS_CLIENT_ID=client_01ABC123XYZ
CONNECTION_ID=conn_test_01XYZABCDEF
REDIRECT_URI=http://127.0.0.1:5000/callback

### 5. Run the App locally

(1) python3 app.py
(2) Open the browser to http://127.0.0.1:5000
(3) Click 'Sign in with SSO' 
(4) Complete the form in the WorkOS Test Provider
(5) You’ll be redirected to a page showing user and organization info






 
