import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(page_title="SwiftReply AI - Email Assistant", page_icon="📧")

# Header section
st.title("📧 SwiftReply AI")
st.markdown("Convert your notes into a polished email instantly.")

# API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("API Key not found! Please set the GEMINI_API_KEY environment variable.")
    st.stop()

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-flash-lite-latest')

# Input UI
with st.container():
    tone = st.selectbox("Choose Tone", ["Professional", "Friendly", "Urgent"])
    user_notes = st.text_area("What do you want to say?", placeholder="e.g. Ask Dave for the project updates by Friday...", height=150)

    if st.button("Generate Draft", use_container_width=True):
        if not user_notes:
            st.warning("Please enter some notes first!")
        else:
            with st.spinner("Generating your email..."):
                try:
                    # Advanced Prompt Engineering
                    full_prompt = (
                        f"Act as a professional email writing assistant. "
                        f"Convert the following notes into a polished email with a {tone} tone. "
                        f"Include a clear subject line and a formal closing. "
                        f"Notes: {user_notes}"
                    )

                    # Call Gemini API
                    response = model.generate_content(full_prompt)
                    ai_output = response.text

                    # Output display
                    st.subheader("Generated Email:")
                    st.markdown("---")
                    st.write(ai_output)
                    
                    # Option to copy
                    st.button("Copy to Clipboard", help="Copying functionality depends on your environment", disabled=True)
                    
                except Exception as e:
                    st.error(f"Failed to connect to AI service: {e}")

# Footer
st.markdown("---")
st.caption("Powered by Google Gemini AI | Built with Streamlit")

