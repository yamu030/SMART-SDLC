import streamlit as st
import requests

st.set_page_config(page_title="SmartSDLC – Requirement Analyzer", layout="wide")

st.title("📄 SmartSDLC – AI Requirement Analyzer")
st.markdown("Upload a **requirement document (PDF)** to automatically classify SDLC phases and generate user stories using IBM Watsonx AI.")

# File upload
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("🔍 Analyzing document... Please wait..."):
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}

        try:
            response = requests.post("http://127.0.0.1:8000/upload-pdf/", files=files)
            response.raise_for_status()
            result = response.json()

            st.success("✅ Analysis Complete!")

            # Display classified text
            st.subheader("📘 AI-Classified Text:")
            st.code(result.get("classified_text", "No classified text found."), language="markdown")

            # Display generated user stories
            user_stories = result.get("user_stories", [])
            if user_stories:
                st.subheader("📝 Generated User Stories:")
                for i, story in enumerate(user_stories, start=1):
                    st.markdown(f"**{i}.** {story}")
            else:
                st.warning("No user stories could be extracted.")

        except requests.exceptions.RequestException as e:
            st.error(f"❌ Error contacting backend: {e}")
