# Natural-Language-to-SQL-Converter-using-LLM-GEN-AI-GEMINI

A smart, AI-driven Streamlit application that transforms plain English queries into **Druid-compatible SQL** using **Google Gemini** (Generative AI). Built with a focus on clean design, secure architecture, and real-world data analytics use cases.

---

## 🚀 Project Overview

This application simplifies the process of querying Druid databases by converting natural language inputs into structured SQL queries. By leveraging **Google's Gemini 1.5 Pro API**, the tool supports dynamic query generation based on user intent, eliminating the need for manual SQL writing.

---

## 🎯 Key Features

- Converts user-friendly English prompts into valid Druid SQL
- Secure and flexible runtime API key entry (no hardcoding)
- Powered by Gemini 1.5 Pro LLM for accurate, context-aware SQL
- Clean, responsive interface with Streamlit
- Supports complex filters, aggregations, and conditional logic
---

## Why This Project?

In modern data analytics workflows, **bridging the gap between business logic and SQL syntax** is essential. This project demonstrates:

- Proficiency in integrating **LLM APIs** (Gemini) into production-ready tools
- Solid understanding of **data querying, prompt engineering, Gen AI**
- A **secure, modular, and readable codebase** ideal for team environments

---

## Tech Stack

- **Python** – Core programming language
- **Streamlit** – Interactive frontend
- **Google Gemini API** – Natural Language Processing
- **Prompt Engineering** – Structured instructions for accurate SQL output
---

## Project Structure

GeminiDruidSQL/
├── GeminiSQL.py # Main application logic
├── requirements.txt # Python dependencies
├── Few Outputs 
├── README.md # Project documentation


## How It Works

1. The user enters a natural language question (e.g., *"List students who scored above 80 in subject 8EC08"*).
2. The prompt template guides Gemini to understand context and map it to the correct columns in the `studentmemo` table.
3. Gemini returns a syntactically correct Druid SQL query (e.g., `SELECT * FROM "studentmemo" WHERE "8EC08_TOT" > 80`).
4. The query is displayed in the UI with no backend database execution, ensuring security and focus on query generation only.


## Who Can Use This

- **Data Analysts** – Save time writing repeated queries  
- **Non-Technical Stakeholders** – Ask questions in natural English  
- **Students** – Learn SQL patterns by observing AI-generated queries  
- **Startups & Product Teams** – Integrate LLMs into internal tools

## Learning Outcomes

- Real-world integration of LLMs using Gemini API
- Structuring prompts for domain-specific SQL generation
- Building a secure, interactive AI app using Streamlit
- Designing AI tools that are business-friendly and technically robust

