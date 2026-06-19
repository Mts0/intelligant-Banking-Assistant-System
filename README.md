# IntelliBank Assistant

AI-powered banking assistant built with FastAPI, LangGraph, LangChain, Gemini, and RAG.

## Overview

IntelliBank Assistant is a modular banking assistant that combines:

- Multi-Agent Architecture
- Retrieval-Augmented Generation (RAG)
- Banking Policy Search
- Conversational AI
- Vector Search
- FastAPI Backend
- LangGraph Workflows

The system routes customer requests to specialized banking agents and can answer questions using bank policy documents stored in PDF format.

---

## Features

### Banking Agents

- Account Agent
- Loan Agent
- Card Agent
- Policy Agent
- General Assistant

### RAG Pipeline

- PDF Document Loading
- Document Chunking
- Embedding Generation
- FAISS Vector Database
- Semantic Search
- Context-Aware Answers

### AI Workflow

- Question Classification
- Intelligent Routing
- Agent Execution
- Response Generation

### API Layer

- REST API
- Swagger Documentation
- JSON Responses

---

## Technology Stack

### Backend

- Python 3.11+
- FastAPI
- Uvicorn

### AI Frameworks

- LangChain
- LangGraph

### LLM

- Gemini 2.5 Flash

### RAG Components

- Google Embeddings
- FAISS
- PyPDF

### Database

- SQLite
- SQLAlchemy

### Utilities

- Python Dotenv
- Jinja2
- Aiofiles

---

## System Architecture

```text
                        ┌───────────────┐
                        │    User       │
                        └───────┬───────┘
                                │
                                ▼
                    ┌─────────────────────┐
                    │  FastAPI Endpoint   │
                    └─────────┬───────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │     LangGraph       │
                    │     Workflow        │
                    └─────────┬───────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │   Classifier Node   │
                    └─────────┬───────────┘
                              │
         ┌────────────────────┼────────────────────┐
         ▼                    ▼                    ▼
 ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
 │ AccountAgent │    │  LoanAgent   │    │  CardAgent   │
 └──────────────┘    └──────────────┘    └──────────────┘
                              │
                              ▼
                     ┌────────────────┐
                     │ Policy Agent   │
                     └───────┬────────┘
                             │
                             ▼
                     ┌────────────────┐
                     │  Retriever     │
                     └───────┬────────┘
                             │
                             ▼
                     ┌────────────────┐
                     │     FAISS      │
                     └───────┬────────┘
                             │
                             ▼
                     ┌────────────────┐
                     │     Gemini     │
                     └────────────────┘
```

---

## Project Structure

```text
intelliBank/
│
├── backend/
│   │
│   ├── main.py
│   │
│   ├── api/
│   │   ├── chat.py
│   │   ├── auth.py
│   │   └── execute.py
│   │
│   ├── agents/
│   │   ├── supervisor.py
│   │   ├── account_agent.py
│   │   ├── loan_agent.py
│   │   ├── card_agent.py
│   │   └── policy_agent.py
│   │
│   ├── graph/
│   │   ├── state.py
│   │   ├── nodes.py
│   │   ├── router.py
│   │   └── workflow.py
│   │
│   ├── tools/
│   │   ├── balance_tool.py
│   │   ├── transfer_tool.py
│   │   ├── loan_tool.py
│   │   └── policy_tool.py
│   │
│   ├── rag/
│   │   ├── ingest.py
│   │   ├── retriever.py
│   │   └── vector_store/
│   │
│   ├── database/
│   │   ├── db.py
│   │   ├── models.py
│   │   └── bank.db
│   │
│   ├── services/
│   │   ├── llm.py
│   │   └── embeddings.py
│   │
│   └── config/
│       └── settings.py
│
├── docs/
│   │
│   ├── policies/
│   │   ├── accounts.pdf
│   │   ├── loans.pdf
│   │   └── cards.pdf
│   │
│   └── references/
│       └── accounts.txt
│
├── frontend/
│   │
│   ├── css/
│   │   └── style.css
│   │
│   ├── html/
│   │   └── index.html
│   │
│   └── js/
│       └── app.js
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Mts0/intelligant-Banking-Assistant-System.git
cd intelliBank assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## Build Vector Database

```bash
python -m backend.rag.ingest
```

---

## Run Application

```bash
uvicorn backend.main:app --reload
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## Example Request

### POST /chat

Request:

```json
{
  "message": "What are the requirements for a personal loan?"
}
```

Response:

```json
{
  "answer": "..."
}
```

---

## Future Enhancements

- Customer Authentication
- Real Banking Database Integration
- Transaction History
- Balance Inquiry
- Loan Eligibility Checker
- Card Management
- Human Approval Workflow
- Audit Logging
- Admin Dashboard
- Docker Deployment
- Kubernetes Deployment

---

## Learning Objectives

This project demonstrates:

- LangGraph Workflows
- LangChain Integration
- Multi-Agent Systems
- RAG Architecture
- Vector Databases
- FastAPI Development
- Prompt Engineering
- Banking AI Use Cases

---

## License

MIT License

---

## Author

Mostafa Mattash

AI Engineer | Backend Developer | LangChain & LangGraph Enthusiast