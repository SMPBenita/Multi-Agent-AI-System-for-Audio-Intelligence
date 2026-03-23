# 🤖 Multi-Agent AI System for Audio Intelligence

## 🚀 Overview
This project demonstrates a production-style multi-agent AI system for processing audio data into actionable insights.

## 🧠 Architecture
Audio Input  
↓  
Transcription Agent (Whisper)  
↓  
Summarization Agent (BART Transformer)  
↓  
Insight Agent (Keyword Extraction)  

## 🤖 Multi-Agent Design
- Agent 1: Transcription Agent
- Agent 2: Summarization Agent
- Agent 3: Insight Agent
- Orchestrator: Controls workflow

## ⚙️ Tech Stack
- Python
- Hugging Face Transformers
- Whisper (ASR)
- PyTorch
- FastAPI
- KeyBERT

## 🔥 Features
- Modular multi-agent architecture
- End-to-end ML pipeline
- API deployment using FastAPI
- Real-world production design

## 📦 How to Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload