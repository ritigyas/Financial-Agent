# Financial AI Multi-Agent System

## Overview

Financial AI Multi-Agent System is an Agentic AI application built using the **Phidata Agent Framework** and **Groq LLMs** to perform autonomous financial research and web intelligence. The system demonstrates a collaborative multi-agent architecture where specialized AI agents coordinate to solve complex financial queries through tool calling and task delegation.

The project integrates real-time financial market data from **Yahoo Finance** and live web search capabilities through **DuckDuckGo**, enabling the agents to provide comprehensive financial insights, analyst recommendations, stock fundamentals, and recent market news.

---

## Features

- Multi-Agent AI Architecture
- Autonomous Task Delegation
- Financial Market Analysis
- Real-Time Stock Data Retrieval
- Analyst Recommendation Analysis
- Company Fundamentals Extraction
- Latest Financial News Retrieval
- Tool Calling using Function Calling
- Streaming Responses
- FastAPI-based Playground Interface
- Groq LLM Integration
- Modular Agent Design

---

## Agent Architecture

The system consists of two specialized AI agents coordinated through the Phidata Playground.

### Financial Agent

Responsible for:

- Stock Price Analysis
- Company Fundamentals
- Analyst Recommendations
- Financial News
- Market Insights

**Tool Used**

- Yahoo Finance Toolkit

---

### Web Search Agent

Responsible for:

- Live Internet Search
- Company News
- Market Events
- General Financial Information

**Tool Used**

- DuckDuckGo Search

---

## Agent Workflow

```
                        User Query
                             │
                             ▼
                    Multi-Agent Orchestrator
                             │
              ┌──────────────┴──────────────┐
              ▼                             ▼
      Financial Agent               Web Search Agent
              │                             │
              ▼                             ▼
      Yahoo Finance API           DuckDuckGo Search
              │                             │
              └──────────────┬──────────────┘
                             ▼
                   Response Aggregation
                             │
                             ▼
                     Final AI Response
```

The orchestrator dynamically determines which specialized agent should execute each task and combines the outputs into a single coherent response.

---

## Technology Stack

### Agent Framework

- Phidata
- FastAPI
- Uvicorn

### Large Language Model

- Groq
- Llama 3.3 70B Versatile

### AI Capabilities

- Agentic AI
- Multi-Agent Systems
- Function Calling
- Tool Calling
- Task Delegation
- Autonomous Reasoning

### Financial Intelligence

- Yahoo Finance

### Web Intelligence

- DuckDuckGo Search

### Programming Language

- Python 3

---

## Frameworks and Libraries

- Phidata
- FastAPI
- Uvicorn
- Groq
- python-dotenv
- yfinance
- duckduckgo-search

---

## Project Structure

```
Financial-Agent/
│
├── financial_agent.py
├── playground.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/ritigyas/Financial-Agent.git

cd Financial-Agent
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file inside the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Running the Playground

```bash
python playground.py
```

The application launches a FastAPI-powered Playground where users can interact with the AI agents.

---

## Example Query

```
Summarize analyst recommendations for AAPL stock and provide a brief overview of the company's recent news for NVDA.
```

The orchestrator automatically delegates:

- Financial analysis to the Financial Agent
- News retrieval to the Web Search Agent

before generating a unified response.

---

## Agentic AI Concepts Demonstrated

- Multi-Agent Collaboration
- AI Task Routing
- Tool-Augmented Language Models
- Autonomous Tool Selection
- Function Calling
- Specialized AI Agents
- Agent Orchestration
- Financial AI
- Retrieval-Augmented Tool Usage
- Modular AI Architecture
- Streaming LLM Responses

---

## Future Enhancements

- Memory-enabled Agents
- Persistent Chat Sessions
- RAG over Financial Reports
- SEC Filing Analysis
- Portfolio Recommendation Agent
- Risk Assessment Agent
- Stock Comparison Agent
- Multi-LLM Support
- Vector Database Integration
- Real-time Market Monitoring
- Interactive Financial Dashboard

---

## Repository

**GitHub**

https://github.com/ritigyas/Financial-Agent

---

## Keywords

Agentic AI, Multi-Agent Systems, AI Agents, Financial AI, Autonomous Agents, Phidata, Groq, Llama 3.3, FastAPI, Function Calling, Tool Calling, AI Orchestration, Financial Analysis, Yahoo Finance, DuckDuckGo Search, Large Language Models, AI Automation, Python.
