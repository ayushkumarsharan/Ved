# 🧠 Ved - Personal Local AI Assistant

> *"Just like Jarvis, but it lives entirely on your local machine."*

Ved is a completely private, offline, 100% local AI assistant optimized for lower-end hardware (8GB RAM, CPU-only inference). It features a polished web interface, voice interaction, document memory (RAG), and anonymous web searching.

## 🚀 Features
- **100% Local & Private:** No telemetry, no API keys, no cloud data leaks.
- **Optimized for 8GB RAM:** Uses Qwen 2.5 3B (`qwen2.5:3b`) for fast CPU inference.
- **RAG / Document Memory:** Upload PDFs, DOCX, and text files. Uses `nomic-embed-text`.
- **Web Search:** Anonymous internet searching via DuckDuckGo.
- **Voice I/O:** Talk to Ved using your microphone and hear responses.
- **LAN Access:** Access Ved from your phone or tablet on the same Wi-Fi network.

## 🏗️ Architecture
- **Engine:** [Ollama](https://ollama.com/)
- **Interface:** [Open WebUI](https://github.com/open-webui/open-webui)
- **Package Manager:** `uv` (for isolated, fast Python environments)

## 🛠️ Installation
If you are cloning this repository to set it up on a new Windows machine:

1. Install [Ollama](https://ollama.com/download) and Python.
2. Run `pip install uv`.
3. Create the directories: `mkdir ollama_models`, `mkdir openwebui_data`.
4. Run `Start_Ved.bat` (copy it from your Desktop into this folder if needed).

## 📱 Accessing from your Phone
Because `HOST=0.0.0.0` is set in the batch file, you can access Ved from any device on your Wi-Fi. Look at the terminal output when starting Ved to find your local IP address (e.g., `http://192.168.1.5:8080`).

---
*Created for personal use. Feel free to fork and modify!*
