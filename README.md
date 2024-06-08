# 📚 EduGen: Make the most of educational videos

This project uses AI to convert YouTube video transcripts into educational content, including detailed notes, summaries, and quizzes. Leveraging the capabilities of Google's Generative AI, it processes YouTube video transcripts to generate comprehensive and organized educational materials.

## Features

- Generate detailed notes from YouTube video transcripts.
- Summarize the main points of a YouTube video.
- Create quizzes based on the content of a YouTube video.

## Installation

To run this application locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/S-a-m-93/EduGen.git
    cd EduGen
    ```
2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Create a .env file in the root directory and add your Google API key:**
   ```bash
   GOOGLE_API_KEY=your_google_api_key
   ```
    
## Usage

1. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

2. **Open your web browser** and navigate to `http://localhost:8501`.
3. **Enter the YouTube video clean link in the provided text box. It is important to upload the right format of the link.**
4. **Select the type of content you want to generate (Notes, Summary, Quiz) from the dropdown menu.**
5. **Click the "Generate Content" button to retrieve and display the content.**

## Acknowledgements

- **Streamlit** for providing an easy-to-use framework for building interactive web applications in Python.
- **YouTube Transcript API** for enabling seamless extraction of transcripts from YouTube videos.
- **Google Generative AI** for its powerful capabilities in generating educational content from text prompts.

---

Happy studying! May your grades be stellar and your knowledge ever-expanding! 📚🌟
