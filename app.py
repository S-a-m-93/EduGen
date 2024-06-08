import streamlit as st
import os

import google.generativeai as genai

from youtube_transcript_api import YouTubeTranscriptApi

# Define different prompts
prompts = {
    "Notes": "You are a YouTube video notes maker for students. You will be taking the transcript text and generate notes for the entire video. You will give all the important concepts given in the video in a concise and organized format without missing anything. The transcript text is:",
    "Summary": "You are a YouTube video summary maker for students. You will be taking the transcript text and generate a summary for the entire video. You will provide a concise overview of the main points discussed in the video. The transcript text is:",
    "Quiz": "You are a YouTube video quiz maker for students. You will be taking the transcript text and generate a quiz for the entire video. You will provide several questions and answers based on the key concepts discussed in the video. The transcript text is:",
}


## Getting the transcript from YouTube videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        print(video_id)
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]
        return transcript
    except Exception as e:
        st.error(f"Error extracting transcript: {e}")
        return None


## Generating content based on the selected type
def generate_gemini_content(transcript_text, content_type):
    try:
        prompt = prompts[content_type]
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt + transcript_text)
        return response.text
    except Exception as e:
        st.error(f"Error generating content: {e}")
        return None


st.title("📚 EduGen: Make the most of educational videos")

youtube_link = st.text_input("Enter the YouTube Video Link")
content_type = st.selectbox("Select content type", ["Notes", "Summary", "Quiz"])

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Generate Content"):
    transcript_text = extract_transcript_details(youtube_link)
    if transcript_text:
        content = generate_gemini_content(
            transcript_text=transcript_text, content_type=content_type
        )
        st.markdown(f"## {content_type}:")
        st.write(content)
