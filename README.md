# AI Customer Support Automation

## Overview

AI Customer Support Automation is a Proof of Concept (POC) that demonstrates how multiple AI agents can collaborate to provide intelligent customer support, order assistance, and product recommendations.

The system is built using **FastAPI**, **CrewAI**, **Groq**, and **Ollama**, allowing it to generate AI-powered responses while supporting a fallback mechanism for improved reliability.

---

# Features

* Multi-Agent Architecture
* AI-powered Customer Support
* Order Management Assistant
* Product Recommendation Assistant
* Groq Cloud LLM Integration
* Ollama Local LLM Fallback
* FastAPI Backend
* Interactive Chatbot UI
* Modular and Scalable Project Structure

---

# Technology Stack

| Component            | Technology            |
| -------------------- | --------------------- |
| Backend              | FastAPI               |
| AI Agent Framework   | CrewAI                |
| Primary LLM          | Groq                  |
| Fallback LLM         | Ollama                |
| Frontend             | HTML, CSS, JavaScript |
| Programming Language | Python 3.10+          |
| Data Storage         | JSON                  |

---

# Project Structure

```text
Customer_Support_Automation/

├── agents/
│   ├── query_agent.py
│   ├── order_agent.py
│   └── recommendation_agent.py
│
├── services/
│   ├── groq_service.py
│   ├── ollama_service.py
│   └── llm_service.py
│
├── Frontend/
│   ├── index.html
│   ├── styles.css
│   └── chat.js
│
├── data/
│   └── sample_data.json
│
├── docs/
│   ├── Phase1_AI_Research_Evaluation.pdf
│   ├── Phase2_Prototype_POC.pdf
│   └── Phase3_Recommendation_Report.pdf
│
├── app.py
├── config.py
├── requirements.txt
├── .env.example
└── README.md
```

---

# System Workflow

```text
Customer

    │

    ▼

Chatbot Frontend

    │

    ▼

FastAPI Backend

    │

    ▼

Query Router

    │

────────────────────────────────────

│                 │                │

▼                 ▼                ▼

Query Agent   Order Agent   Recommendation Agent

────────────────────────────────────

                │

                ▼

           LLM Service

                │

          ┌─────┴─────┐

          ▼           ▼

        Groq       Ollama

                │

                ▼

         AI Generated Response
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd Customer_Support_Automation
```

---

## Create Virtual Environment

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

Example:

```env
GROQ_API_KEY=your_groq_api_key
OLLAMA_URL=http://localhost:11434/api/generate
MODEL_NAME=llama3.2
```

---

# Running Ollama

Install Ollama and download the required model.

```bash
ollama pull llama3.2
```

Start Ollama service.

```bash
ollama serve
```

---

# Run the Application

```bash
python3 app.py
```

or

```bash
uvicorn app:app --reload
```

Open your browser:

```
http://127.0.0.1:8000
```

---

# Example Queries

### Customer Support

```
What are your support hours?
```

### Order Management

```
Where is my order?
```

### Product Recommendation

```
Recommend a phone under ₹30,000.
```

---

# AI Agents

## Query Agent

Responsible for:

* General customer support
* FAQs
* Basic assistance

---

## Order Agent

Responsible for:

* Order tracking
* Refund information
* Cancellation requests
* Delivery status

---

## Recommendation Agent

Responsible for:

* Product suggestions
* Personalized recommendations
* Purchase guidance

---

# LLM Service

The application uses a hybrid AI model strategy.

## Primary Model

* Groq Cloud LLM

## Fallback Model

* Ollama Local LLM

If Groq is unavailable, the system automatically switches to Ollama to ensure uninterrupted service.

---

# API Endpoints

| Method | Endpoint | Description            |
| ------ | -------- | ---------------------- |
| GET    | /        | Chatbot UI             |
| POST   | /chat    | Process customer query |

---

# POC Scope

This project demonstrates:

* Multi-agent AI workflow
* AI-powered customer support
* Hybrid LLM integration
* FastAPI backend development
* Modular software architecture

This implementation is intended as a Proof of Concept and can be extended with databases, authentication, vector search, and enterprise deployment strategies.

---

# Future Enhancements

* PostgreSQL Integration
* Vector Database Support
* Retrieval-Augmented Generation (RAG)
* Authentication & Authorization
* Conversation Memory
* Docker Deployment
* CI/CD Pipeline
* Analytics Dashboard
* Multi-language Support

---

# Documentation

The project includes:

* **Phase 1:** AI Research & Evaluation
* **Phase 2:** Prototype / POC Documentation
* **Phase 3:** Recommendation Report

---

# Author

**AI Customer Support Automation**

Proof of Concept demonstrating multi-agent AI orchestration using FastAPI, CrewAI, Groq, and Ollama.
