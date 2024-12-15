import os
from flask import Flask, request, jsonify, render_template
from google.oauth2 import service_account
from google.auth.transport.requests import Request
import google.generativeai as genai
from io import BytesIO
from PIL import Image

# Flask app setup
app = Flask(__name__)

# Path to the OAuth2 client secret file (for Google AI Studio) for headless authentication
SERVICE_ACCOUNT_FILE = "/app/service_account.json"  # Replace with your service account file path
# API_KEY = "AIzaSyDiin8Rbxrclub0ERZNW4CgxzKCJIJKxxE"  # Replace with your actual API key

# Function to authenticate and get an access token for Google AI Studio (OAuth2)
def get_access_token():
    try:
        # Use the service account credentials for headless authentication
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE,
            scopes=["https://www.googleapis.com/auth/generative-language.tuning"]
        )

        # Refresh the credentials if they are expired
        if credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())

        print(f"Access token: {credentials.token}")  # Log the token for debugging
        return credentials.token
    except Exception as e:
        print(f"Authentication failed: {e}")
        raise Exception(f"Failed to authenticate: {e}")

# Function to configure the Gemini API with API Key
def configure_genai():
    try:
        genai.configure(api_key=API_KEY)
        print("Gemini API configured successfully.")
    except Exception as e:
        print(f"Failed to configure Gemini API: {e}")
        raise Exception(f"Failed to configure Gemini API: {e}")

# Route to serve the UI
@app.route("/")
def index():
    return render_template('index.html')

# Endpoint to analyze an X-ray image and text input
@app.route("/analyze", methods=["POST"])
def analyze_image_and_text():
    # Authenticate and get access token for Google AI Studio
    try:
        access_token = get_access_token()
        configure_genai()  # Set up the API key for Gemini
    except Exception as e:
        return jsonify({"error": f"Authentication failed: {e}"}), 500

    # Check if file is uploaded
    if "file" not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    # Get uploaded file
    file = request.files["file"]

    # Convert the file to a PIL image
    try:
        image = Image.open(file)
        print(f"Image opened successfully: {file.filename}")
    except Exception as e:
        print(f"Failed to open image: {e}")
        return jsonify({"error": f"Failed to open image: {e}"}), 500

    # Get optional text input (use provided text or default)
    text_input = request.form.get("text", "")
    if not text_input:
        text_input = "You are an orthopedic surgeon, check if the X-ray has any issues."
    
    # Make sure content field is included
    content_input = text_input  # Use the provided text for context

    try:
        # Generate content using the image and text input
        result = genai.GenerativeModel("gemini-1.5-pro-latest").generate_content(
            [content_input, image]  # Only send necessary arguments
        )

        # Convert the result to a serializable format (e.g., a dictionary)
        response_content = {
            "generated_text": result.text  # Assuming 'text' is the attribute you need
        }
        return jsonify(response_content)

    except Exception as e:
        print(f"Error generating content with Gemini: {e}")
        return jsonify({"error": f"Failed to generate content: {e}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

