from flask import Flask, redirect, request, render_template
from dotenv import load_dotenv
from workos import WorkOSClient
import os

# Load env vars
load_dotenv()

# Initialize WorkOS SDK
workos = WorkOSClient(
    api_key=os.getenv("WORKOS_API_KEY"),
    client_id=os.getenv("WORKOS_CLIENT_ID")
)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login")
def login():
    auth_url = workos.sso.get_authorization_url(
        connection_id=os.getenv("CONNECTION_ID"),
        redirect_uri=os.getenv("REDIRECT_URI"),
        state="debug-state"
    )
    return redirect(auth_url)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    if not code:
        return "Missing `code` in callback URL", 400

    profile_data = workos.sso.get_profile_and_token(code)
    profile = profile_data.profile

   
    first_name = profile.first_name
    last_name = profile.last_name
    email = profile.email
    organization_id = profile.organization_id

   
    org = workos.organizations.get_organization(organization_id)
    org_name = org.name

    return render_template(
        "profile.html",
        first_name=first_name,
        last_name=last_name,
        email=email,
        organization_id=profile.organization_id,
        org_name=org_name
    )

if __name__ == "__main__":
    app.run(debug=True)

