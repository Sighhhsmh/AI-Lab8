# SwiftReply AI - Email Assistant (Streamlit Version)

SwiftReply AI is a lightweight web application that helps users convert rough notes into polished, professional emails using Google's Gemini AI. Built with Streamlit for easy deployment.

## App Purpose
The goal of this application is to streamline email drafting. Instead of worrying about tone, structure, or formal greetings, users can provide the core message and select a desired tone, and the AI handles the rest.

## How to Use
1. **Set up environment variables:**
   - Create a `.env` file or set the environment variable `GEMINI_API_KEY` with your Google Gemini API key.
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   streamlit run streamlit_app.py
   ```
4. **Generate an email:**
   - Enter your notes in the text area.
   - Choose a tone (Professional, Friendly, or Urgent).
   - Click "Generate Draft".

## Deployment
This app is ready for deployment on **Streamlit Cloud**:
1. Push this code to a GitHub repository.
2. Connect the repository to [share.streamlit.io](https://share.streamlit.io).
3. Add your `GEMINI_API_KEY` to the **Secrets** section in the Streamlit Cloud dashboard.

## Limitations
- **Model Constraints:** Uses `gemini-1.5-flash-latest`, which may have token limits or occasional hallucinations.
- **Dependency:** Requires an active internet connection to communicate with the Google Generative AI API.
