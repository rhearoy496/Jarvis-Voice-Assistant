# Jarvis – AI Voice Assistant

Jarvis is a local AI-powered voice assistant built using Python.  
It supports wake-word activation, natural language question answering, neural voice responses, and local news retrieval.

---

## 🚀 Features

- 🎤 Wake word activation ("Jarvis")
- 🧠 Local LLM integration using Ollama (Phi / Mistral)
- 🗣 Neural Text-to-Speech (Microsoft Edge TTS)
- 📰 Kolkata local news headlines
- 🎵 Music playback support
- 🧠 Context-aware conversation memory
- 🔒 Secure API key handling using environment variables
- 💤 Auto sleep mode after inactivity

---

## 🏗 Architecture

Voice Input → SpeechRecognition → Command Processing →  
Ollama (Local LLM) → Edge TTS → Audio Output  

---

## 🛠 Technologies Used

- Python 3.13
- SpeechRecognition
- Ollama (Local LLM)
- Edge-TTS
- Requests
- News API
- Git & GitHub

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Jarvis-Voice-Assistant.git
cd Jarvis-Voice-Assistant
