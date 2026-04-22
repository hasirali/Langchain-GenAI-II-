# Langchain-GenAI-II-
<img width="1918" height="869" alt="image" src="https://github.com/user-attachments/assets/b8bbb93c-57ca-44d9-8807-f9e2202d718c" />

# 🔬 AI Smart Research Tool

An intelligent research assistant powered by **Google Gemini 2.5 Flash** and **LangChain**. This tool allows users to quickly summarize complex academic papers or custom research topics with adjustable writing styles and lengths.

---

## ✨ Features
- **Pre-loaded Research:** Quick-select famous AI papers (Transformer, GANs, GPT-4 study).
- **Custom Queries:** Input any research topic or technical question.
- **Dynamic Styling:** Choose between *Professional*, *Friendly*, or *Hinglish* tones.
- **Custom Length:** Generate Short, Medium, or Long summaries.
- **Structured Output:** Every analysis includes an Executive Summary, Core Concepts, Real-world Significance, and Future Implications.

## 🛠️ Tech Stack
- **Frontend:** [Streamlit](https://streamlit.io/)
- **LLM Orchestration:** [LangChain](https://www.langchain.com/)
- **Model:** [Google Gemini 2.5 Flash](https://ai.google.dev/)
- **Environment:** Python (dotenv)

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/smart-research-tool.git](https://github.com/your-username/smart-research-tool.git)
cd smart-research-tool
2. Install Dependencies
Bash
pip install streamlit langchain-google-genai python-dotenv
3. Setup Environment Variables
Create a .env file in the root directory and add your Google API Key:

Code snippet
GOOGLE_API_KEY=your_gemini_api_key_here
4. Run the Application
Bash
streamlit run app.py
