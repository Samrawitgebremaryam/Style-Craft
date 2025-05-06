# ✨ StyleCraft Chatbot

[![Live Demo](https://img.shields.io/badge/Live-Demo-blue)](https://stylecraft-chatbot.streamlit.app/)

## 📝 Overview

StyleCraft is a personalized AI writing assistant that helps users generate high-quality content tailored to specific writing styles, audience types, formality, emotional tone, complexity, and prompting strategies. Whether you're writing a professional email, a social media post, or academic content, StyleCraft provides smart and context-aware AI outputs using Google's Gemini API.

Designed for writers, marketers, students, and professionals, StyleCraft makes AI-generated writing more controlled, user-centric, and adaptable to real-world communication needs.

## 🚀 Project Highlights

- **Configurable Writing Styles**: Choose from Professional, Casual, Persuasive, Empathetic, or Creative tones
- **Audience Customization**: Tailor content for General Public, Industry Experts, Academics, Teens, or Elderly
- **Prompt Engineering Techniques**: Zero-Shot, Few-Shot, and Chain-of-Thought prompting modes
- **Real-Time Adjustments**: Dynamic sliders for formality, complexity, and emotional tone
- **Learning Style Toggle**: Optional tooltips for understanding writing decisions

## 💡 Idea Behind the App

The core idea behind StyleCraft is to make AI-generated writing context-aware and communication-effective. While most text generation tools focus solely on the topic, StyleCraft goes further by allowing users to define the style, audience, and thought process behind the writing.

> It's not just about generating text—it's about creating the right text for the right reader in the right tone.

## 🧠 Prompting Techniques

### Zero-Shot Prompting

- The AI is given the task with instructions only
- Ideal for general use when simplicity is needed

### Few-Shot Prompting

- Sample examples are appended to the prompt
- Guides the AI in format, tone, and clarity

### Chain-of-Thought Prompting

- Encourages step-by-step thinking
- Improves logic and depth in responses

## ⚙️ Parameters

### Formality Level (1-10)

- Controls formal/casual tone
- Adapts to business, education, or social media contexts

### Complexity Level (1-10)

- Adjusts vocabulary and sentence structure
- Scales from general audience to academic/technical writing

### Emotional Tone (1-10)

- Modulates emotional intensity
- Perfect for persuasive or empathetic writing

### Prompting Strategy

- Zero-Shot
- Few-Shot
- Chain-of-Thought

## ✨ Features

- ✅ Style and Tone Selector
- ✅ Target Audience Picker
- ✅ Prompting Type Dropdown
- ✅ Learning Mode Toggle
- ✅ Minimal Input UI
- ✅ Compact Design

## 🛠️ Tech Stack

- **Frontend/UI**: Streamlit
- **Backend & Prompt Logic**: Python 3
- **AI Model**: Google's Gemini API
- **Deployment**: Streamlit Cloud

## 🚀 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/stylecraft-chatbot
cd stylecraft-chatbot
```

2. Install required libraries:

```bash
pip install -r requirements.txt
```

3. Add your Gemini API key to `.env`:

```ini
GEMINI_API_KEY=your_key_here
```

4. Run the app:

```bash
streamlit run app.py
```

## 🎯 App Preview

### Key Features:

- 🎯 Generate content tailored to style, tone, and audience
- 🧠 Learn the impact of writing decisions via Learning Mode
- 🧩 Explore advanced prompt engineering techniques

---
