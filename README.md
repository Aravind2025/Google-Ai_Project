# X-ray Analysis and Interpretation Tool

## Project Overview
The X-ray Analysis and Interpretation Tool is a Flask-based web application that allows users to upload X-ray images and receive an analysis of potential fractures and other medical conditions. The application leverages a generative AI model, powered by Google's Gemini API, to automatically process the images and generate a text-based interpretation. It is designed for educational purposes, offering orthopedic surgeons, radiologists, and healthcare professionals a tool to quickly assess X-ray images and form an initial diagnostic hypothesis.

## Key Features
- Image Upload: Users can upload X-ray images in common formats (e.g., JPG, PNG) through a simple web interface.
- Text Prompt: An optional text prompt allows users to provide additional instructions or context for the AI analysis.
- AI-Powered Interpretation: The system uses the Gemini AI model to analyze the X-ray images and generate a detailed text report, identifying fractures, dislocations, and other relevant medical conditions.
- User Interface: A responsive, user-friendly front-end built using HTML, Bootstrap, and JavaScript that allows easy image uploads and displays the results in a clean, readable format.
- Real-Time Feedback: The results are displayed immediately on the same page after the image is processed, offering real-time insights into the analysis.
- Error Handling: Detailed error messages and logs to ensure smooth user experience and troubleshooting.

## Technical Stack
- Backend: 
  - Flask: A lightweight Python web framework used to build the backend. It handles file uploads, API calls, and serves the HTML pages.
  - Google Gemini API: Used to perform advanced image analysis using machine learning models. The API is leveraged to generate content based on X-ray images and text prompts.
  - Pillow: A Python Imaging Library (PIL) fork, used for handling image processing and manipulation.
  - Google Auth & OAuth: Implements headless authentication using a service account to interact with Google Cloud services.

- Frontend:
  - HTML/CSS: Basic structure and styling of the web interface.
  - Bootstrap: Provides a responsive, mobile-friendly design for the front-end.
  - JavaScript (AJAX): Handles asynchronous form submissions, allowing users to upload images and receive analysis without refreshing the page.

- Containerization:
  - Docker: The app is containerized using Docker for easy deployment and scalability. The Dockerfile ensures that all dependencies are installed and the app can run in any environment without configuration issues.

## How It Works
1. Image Upload: The user uploads an X-ray image through a simple HTML form.
2. Optional Text Prompt: Users can optionally enter a text prompt that instructs the AI model on how to analyze the image (e.g., "Check for fractures in the tibia").
3. Processing: The backend Flask application processes the uploaded image using the Google Gemini API. The model analyzes the X-ray and generates a response.
4. Result Display: The generated analysis text is returned and displayed on the webpage in a formatted and readable manner, providing insights into the potential fractures, dislocations, or other abnormalities.
5. Deployment: The app is deployed in a Docker container, ensuring portability and ease of deployment across various platforms, including cloud services.

## Technical Challenges Addressed
- Image Processing: Efficient handling of image files in various formats and sizes. The integration of Pillow ensures that images are processed correctly before being sent to the AI model.
- Real-Time Interaction: AJAX allows for seamless, non-blocking interaction between the front-end and back-end, ensuring a smooth user experience without page reloads.
- Authentication: Headless authentication using a Google service account allows the app to securely interact with the Gemini API without requiring user interaction for login.

## Potential Use Cases
- Orthopedic Surgeons: Quickly review X-ray images to assess fractures, dislocations, or other issues in bones.
- Radiologists: Supplement radiological evaluations with AI-generated interpretations to assist in diagnostics.
- Medical Education: Educational tool for students and medical professionals to understand how AI models analyze medical images.

## Deployment and Scalability
- Docker: The app is packaged in a Docker container, allowing it to be deployed easily on any platform that supports Docker, including cloud environments like Heroku, AWS, or Google Cloud.
- Cloud Integration: The application can be deployed in a cloud environment, ensuring high availability and scalability for more intensive use cases.

## Future Enhancements
- Advanced AI Models: Integrating more advanced or domain-specific AI models for deeper image analysis (e.g., detecting different types of fractures, bone diseases).
- Multiple Image Analysis: Allow users to upload multiple images at once for batch processing.
- User Authentication: Implement user authentication for saving reports and personal data securely.
- Improved UI/UX: Enhance the front-end design with more sophisticated visualizations and interactive features.

## How to Obtain the API and Service Account Credentials

For this project, you need to obtain the **Google Gemini API credentials** and **Google Cloud service account keys** to interact with Google's machine learning services. 

### 1. **Google Gemini API Key**:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create or select a project.
   - Enable the **Google Gemini API** for the selected project.
   - Go to the **Credentials** section of your Google Cloud Console.
   - Click **Create credentials** and select **API key**. Copy the API key.
   - Replace the `API_KEY` in the code with this key.

### 2. **Google Cloud Service Account**:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create or select a project.
   - Go to **IAM & Admin > Service Accounts**.
   - Create a new service account and grant it the necessary permissions (e.g., access to Google Cloud APIs for image processing).
   - Once the service account is created, click on it and go to the **Keys** tab.
   - Create a new JSON key and download it to your local machine.
   - **Important**: This key contains sensitive information and should never be pushed to a public repository.
   - Save this file as `service_account.json` and **never expose it publicly**. Ensure it is listed in your `.gitignore`.

### How to Use the Credentials:
- Place the downloaded `service_account.json` file in the project directory where your Flask app resides.
- Replace any placeholder API keys or service account paths in your project with the appropriate values.

**Important Note**: Ensure that `client_secret.json` and `service_account.json` are listed in your `.gitignore` file to prevent them from being pushed to your GitHub repository.
<img width="1294" alt="Screenshot 2024-12-14 at 11 58 49 PM" src="https://github.com/user-attachments/assets/9e4bf00b-314d-47a0-8cd4-7202be47dab0" />

