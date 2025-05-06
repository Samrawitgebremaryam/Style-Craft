import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("API key not found. Please set the GEMINI_API_KEY environment variable.")
    st.stop()
genai.configure(api_key=api_key)

# Define writing styles
style_descriptions = {
    "Professional": "Formal, clear, and concise language suitable for business communications.",
    "Casual": "Informal and friendly tone, ideal for social media or personal blogs.",
    "Persuasive": "Engaging and convincing language aimed at influencing the reader's opinion or behavior.",
    "Empathetic": "Compassionate and understanding tone, appropriate for sensitive topics.",
    "Creative": "Imaginative and artistic language, perfect for storytelling or poetry."
}

# Define audience types
audience_descriptions = {
    "General Public": "Content is tailored for a wide audience with varying backgrounds.",
    "Industry Professionals": "Language is technical and assumes familiarity with industry-specific terms.",
    "Academics": "Formal and scholarly tone, suitable for research papers or academic publications.",
    "Teens": "Casual and relatable language, appealing to a younger audience.",
    "Elderly": "Clear and respectful language, considering the preferences and needs of older readers."
}

# Prompting type descriptions
prompt_type_descriptions = {
    "Zero-Shot": (
        "No examples are provided. The model generates a response based solely on the prompt's instructions. "
        "This approach relies on the model's pre-existing knowledge and understanding of the task."
    ),
    "Few-Shot": (
        "A few examples are provided to guide the model's response. "
        "This helps the model understand the desired output format and improves accuracy."
    ),
    "Chain-of-Thought": (
        "The model is instructed to reason step-by-step before arriving at a conclusion. "
        "This technique enhances logical reasoning and is particularly useful for complex tasks."
    )
}

# Streamlit app layout
st.set_page_config(page_title="StyleCraft: Tailored Writing Assistant", layout="wide")
st.title("📝 StyleCraft: Tailored Writing Assistant")
st.write(
    "Welcome to StyleCraft, your personalized writing assistant. Configure your desired settings, and enter your topic or sentence below to generate tailored content."
)

# Sidebar for user selections
with st.sidebar:
    st.header("Configuration")

    # Writing style selection
    selected_style = st.selectbox("Select a Writing Style:", list(style_descriptions.keys()))
    st.markdown(f"**Description:** {style_descriptions[selected_style]}")

    # Audience selection
    selected_audience = st.selectbox("Select Your Target Audience:", list(audience_descriptions.keys()))
    st.markdown(f"**Description:** {audience_descriptions[selected_audience]}")

    # Prompting type selection with descriptions
    prompt_type = st.selectbox("Select Prompt Type:", list(prompt_type_descriptions.keys()))
    st.markdown(f"**Description:** {prompt_type_descriptions[prompt_type]}")

    # Tone and complexity adjustments
    formality = st.slider("Formality Level", 1, 10, 5)
    complexity = st.slider("Complexity Level", 1, 10, 5)
    emotion = st.slider("Emotional Tone", 1, 10, 5)

# Function to construct prompt based on user selections
def construct_prompt(style, audience, topic, formality, complexity, emotion, prompt_type):
    style_description = style_descriptions[style]
    audience_description = audience_descriptions[audience]

    # Base prompt
    prompt = (
        f"You are a writer crafting content in the {style} style. "
        f"Your target audience is {audience}. "
        f"Maintain the following tone and complexity: "
        f"Formality: {formality}/10, Complexity: {complexity}/10, Emotional Tone: {emotion}/10.\n\n"
        f"Writing Style Description: {style_description}\n\n"
        f"Audience Description: {audience_description}\n\n"
        f"Now, write about the following topic:\n{topic}"
    )

    # Apply the selected prompt type
    if prompt_type == "Zero-Shot":
        return prompt

    elif prompt_type == "Few-Shot":
        examples = (
            "\n\nExample 1: A professional email for a job interview confirmation.\n"
            "Dear [Name],\nI hope this email finds you well. I would like to confirm my attendance at the job interview scheduled for [date]. Looking forward to discussing the opportunity further.\n\n"
            "Example 2: A casual post for social media promoting a new blog post.\n"
            "Hey everyone! I just published a new blog post on [topic], check it out here: [link]. Would love to hear your thoughts!\n\n"
        )
        return prompt + examples

    elif prompt_type == "Chain-of-Thought":
        chain_of_thought = (
            "To generate a well-crafted response, I will first analyze the style, tone, and audience. "
            "Then, I will carefully choose the right vocabulary and structure to suit the given requirements.\n\n"
            "Let's begin...\n\n"
        )
        return chain_of_thought + prompt

# User input at the bottom
with st.container():
    st.markdown("---")
    user_input = st.text_area("Enter a topic or sentence:", key="user_input")

    if st.button("Generate Response"):
        if user_input.strip() == "":
            st.warning("Please enter a topic or sentence.")
        else:
            prompt = construct_prompt(selected_style, selected_audience, user_input, formality, complexity, emotion, prompt_type)
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            st.markdown(f"### Generated Response ({prompt_type})")
            st.write(response.text)
