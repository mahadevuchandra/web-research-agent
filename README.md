# 🌐 Web Research Agent 🤖

An AI-powered research assistant that uses Gemini to search the web, extract content, analyze it, and deliver concise answers — all in a chat-like interface powered by Streamlit.

## 🚀 Features

- 🔍 Smart web search (mock-based for easy deployment)
- 🧠 Gemini-powered summarization and synthesis
- 📄 Respectful scraping with `robots.txt` checks
- 💬 Chat UI with conversation memory
- ⚡ Fast and light using `gemini-2.0-flash`

---

## 🛠 Setup

### 1. Clone the Repo

```bash
git clone git@github.com:mahadevuchandra/web-research-agent.git
cd web-research-agent
```

### 2. Create & Activate Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory with the following content:

```
GEMINI_API_KEY=your_api_key_here
```

> 💡 Replace `your_api_key_here` with your actual Gemini API key.

---

## 🧪 Running Tests

Run all unit tests with:

```bash
python -m unittest discover -s tests
```

> ✅ All tests are located in the `tests/` directory and use `unittest`.

---

## 💻 Run the App

Launch the chatbot locally:

```bash
streamlit run main.py
```

---

## 📁 Project Structure

```
web-research-agent/
├── agents/               # Core app modules (search, scrape, analyze, synthesize)
├── tests/                # Unit tests
├── .env                  # API key (not committed)
├── main.py               # Streamlit UI
├── requirements.txt      # Python dependencies
└── README.md             # You're here!
```

---

## 🧠 Powered By

- [Google Gemini](https://ai.google.dev/)
- [Streamlit](https://streamlit.io/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Requests](https://docs.python-requests.org/)

---

## 📜 License

MIT License © 2025 Mahadevu. Chandra Paul
