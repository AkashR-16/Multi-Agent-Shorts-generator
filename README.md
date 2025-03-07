# 📽️ Multi-Agent Shorts generator
This repository contains a multi agent system for generating short videos with external API integration. It integrates text generation, text-to-speech, and video creation capabilities for dynamic content production.

## 🎬 Features
- 🤖 **Multi-Agent System**: Script Writer, Voice Actor, Graphic Designer, and Director agents working together.
- 🎙️ **Text-to-Speech**: Converts AI-generated scripts into voiceovers.
- 🎞️ **Video Generation**: Assembles narration and visuals into a final video.
- 🏡 **Local LLM Support**: Leverages Ollama for offline AI processing.
- 🎮 **Interactive Console**: Allows users to input prompts and generate videos dynamically.

## 📂 Folder Structure
```
ai-shorts-creator/
│── tools.py               # Utility functions for text-to-speech and video generation
│── main.py                # Entry point for running the workflow
│── requirements.txt       # Dependencies for the project
│── README.md              # Documentation
```

## 🚀 Quick Start

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/AkashR-16/Shorts-Style-Multi-Agent-System.git
cd Multi-Agent-Shorts-generator
```

### 2️⃣ Create & Activate a Virtual Environment
For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up API Keys
Create a `.env` file and add your API keys:
```
ELEVENLABS_API_KEY=your-elevenlabs-api-key
STABILITY_API_KEY=your-stability-ai-api-key
```
### 5️⃣ Create Required Accounts  
Before running the workflow, you'll need to create accounts for the following services:  

- **ElevenLabs (Text to Speech)**: [Sign up here](https://try.elevenlabs.io/)
- **Stability AI (Image Generation)**: [Sign up here](https://platform.stability.ai/)  

These accounts provide API access for text-to-speech and image generation, which are required for the agents to function.

### 6️⃣ Run the Workflow
```bash
python main.py
```
You'll be prompted to enter a topic, and the agents will generate a script, voiceover, and video dynamically.

## 🛠️ How It Works
1️⃣ Script Writer Agent generates structured captions.
2️⃣ Voice Actor Agent converts text to speech.
3️⃣ Graphic Designer Agent creates images based on captions.
4️⃣ Director Agent orchestrates the final output.

### 🎯 Example Usage
**User Prompt:**
> "Create a short AI-generated video about renewable energy."

**Generated Response:**
```json
{
    "topic": "Renewable Energy",
    "takeaway": "Sustainable power is the future!",
    "captions": [
        "Solar panels harness the sun's energy.",
        "Wind turbines generate electricity.",
        "AI optimizes energy distribution.",
        "Clean energy reduces carbon footprint.",
        "The future is green!"
    ]
}
```
✅ **Voiceovers are generated**
✅ **Video is created**
✅ **Final output is assembled**



