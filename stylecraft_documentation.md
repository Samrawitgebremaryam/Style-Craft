
# 📄 Project Documentation: StyleCraft – Tailored Writing Assistant

## 🧠 Overview

**StyleCraft** is a Streamlit-based AI-powered web application that leverages Google's Gemini language model to generate personalized, high-quality written content. Users can adjust writing style, audience, tone, formality, and prompting method for highly tailored outputs. The application is particularly useful for content creators, marketers, educators, and businesses aiming for stylistically aligned content generation.



## ⚙️ Features

- **Multiple Writing Styles**: Professional, Casual, Persuasive, Empathetic, Creative
- **Audience Awareness**: General Public, Teens, Academics, Industry Professionals, Elderly
- **Prompt Engineering Techniques**: Zero-Shot, Few-Shot, and Chain-of-Thought prompting
- **Learning Mode**: Explains why and how selections affect generation
- **Parameter Tuning**: Formality, Complexity, and Emotional Tone (1–10 scale)



## 🧩 Prompt Engineering Techniques Used

### 1. **Zero-Shot Prompting**
**Definition**: A single, descriptive prompt is provided without examples.  
**Use Case**: Best for well-understood or general topics.  
**Template**:
```
You are a writer crafting content in the {style} style. Your target audience is {audience}.
Maintain the following tone and complexity: Formality: {formality}/10, Complexity: {complexity}/10, Emotional Tone: {emotion}/10.
Writing Style Description: {style_description}
Audience Description: {audience_description}
Now, write about the following topic:
{topic}
```

### 2. **Few-Shot Prompting**
**Definition**: The prompt includes example responses to guide generation.  
**Use Case**: Improves specificity or format in niche use cases (e.g., emails, social media).  
**Template**: Extends the zero-shot prompt with:
```
Example 1: A professional email...
Example 2: A casual blog intro...
```

### 3. **Chain-of-Thought Prompting**
**Definition**: The model is guided to reason through a task step-by-step.  
**Use Case**: Best for nuanced or complex writing tasks.  
**Template**:
```
To generate a well-crafted response, I will first analyze the style, tone, and audience.
Then, I will carefully choose the vocabulary and structure to suit the requirements.

Let's begin...

[Insert zero-shot prompt here]
```



## ✅ Test Cases and Results

| Test Case | Style | Audience | Prompt Type | Expected Output | Observed Output | Result |
|-----------|-------|----------|-------------|------------------|------------------|--------|
| 1 | Professional | Industry Professionals | Zero-Shot | Concise, formal, industry terms | ✅ Met expectations | Pass |
| 2 | Casual | Teens | Few-Shot | Relatable, upbeat, emojis | ✅ Included slang, emojis | Pass |
| 3 | Empathetic | Elderly | Chain-of-Thought | Gentle tone, clear, supportive | ✅ Thoughtful and calm | Pass |
| 4 | Creative | General Public | Chain-of-Thought | Vivid, imaginative, flowing | ✅ Rich metaphors and narrative flow | Pass |
| 5 | Persuasive | Academics | Few-Shot | Logical, strong claims, references | ⚠️ Slightly informal tone | Mixed – needs tweaking |



## 🔍 Analysis & Reflections

### Prompt Engineering Effectiveness:
- **Zero-Shot** worked reliably for straightforward topics and general audiences but lacked formatting control.
- **Few-Shot** improved output format (especially for niche styles) but made prompts longer and slower.
- **Chain-of-Thought** produced the most nuanced, coherent long-form writing, especially for emotionally or stylistically complex tasks.

### Observations:
- Combining style and audience descriptions directly in the prompt improves model grounding.
- Longer prompts (Few-Shot & Chain-of-Thought) benefit from faster models like `gemini-1.5-flash` to reduce latency.

### Challenges:
- Ensuring alignment between emotion level sliders and actual output tone requires subjective evaluation.
- Prompt token length with Few-Shot can occasionally truncate longer responses.



