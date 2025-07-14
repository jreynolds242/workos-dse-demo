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


2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

If you do not have a requirements.txt file, you can run:
pip install flask workos python-dotenv

4. Create a .env file with the following contents
WORKOS_API_KEY=sk_test_your_key_here
WORKOS_CLIENT_ID=client_01ABC123XYZ
CONNECTION_ID=conn_test_01XYZABCDEF
REDIRECT_URI=http://127.0.0.1:5000/callback

5. Run the app locally

(1) python3 app.py
(2) Open the browser to http://127.0.0.1:5000
(3) Click 'Sign in with SSO' 
(4) Complete the form in the WorkOS Test Provider
(5) You’ll be redirected to a page showing user and organization info

Example Customer Email Responses

Email 1: Mark (Product Manager, prospective customer)

Hey Mark,
Thanks for reaching out. WorkOS acts as the Service Provider (SP) in the SAML flow, not the Identity Provider (IdP). That’s why you won’t see any IdP metadata XML coming from WorkOS. Instead, you would need to connect an external IdP (like Okta, Azure AD, or others) by uploading your metadata to WorkOS.
If you are trying to configure SSO for a tool like SparkNova and you’re looking to have WorkOS act as the IdP in the middle, that setup likely won’t align with how WorkOS is designed. In that case, SparkNova would be the SP, and you would connect your IdP directly to them. WorkOS would not sit between the two.
Here’s a quick overview that breaks down where WorkOS fits in a typical SAML setup: SSO Overview – WorkOS Docs (https://workos.com/docs/sso)
Also, here is a link for more details: https://workos.com/docs/sso/2-configure-a-redirect-uri/identity-provider-initiated-sso.



Email 2: Julia (Software Engineer, current standalone Single Sign-On customer)

Hey Julia,
Thank you for reaching out. Yes, WorkOS supports passing custom data through the SSO flow using the state parameter. It’s included in your initial auth request and returned to your app after authentication. This is perfect for things like tracking IDs or internal references.

Here’s a quick Python example using Flask and the WorkOS SDK:
auth_url = workos.sso.get_authorization_url(
    connection="conn_123",
    redirect_uri="https://yourapp.com/callback",
    state="custom_id_ABC123"
)
Then in your callback:
state = request.args.get("state")
# Use state as needed in your app

You can also grab the user profile with get_profile_and_token at this point.
For More detail here in the SSO guide (https://workos.com/docs/sso/1-add-sso-to-your-app/add-a-callback-endpoint).




 
