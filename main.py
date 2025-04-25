import streamlit as st
from agents.query_analyzer import analyze_query
from agents.web_search import search_web
from agents.web_scraper import scrape_text
from agents.content_analyzer import analyze_content
from agents.synthesizer import synthesize_summaries

# --- Page setup ---
st.set_page_config(page_title="🔍 Web Research Chatbot", layout="wide")
st.markdown("<h1 style='text-align: center;'>💬 Web Research Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Ask anything and I’ll find reliable answers from the web.</p>", unsafe_allow_html=True)
st.divider()

# --- Session state ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "history" not in st.session_state:
    st.session_state.history = []

# --- Sidebar options ---
with st.sidebar:
    st.header("⚙️ Controls")
    if st.button("🔄 Reset Chat"):
        st.session_state.messages = []
        st.session_state.history = []
        st.rerun()
    st.markdown("---")
    st.markdown("✅ **Powered by Google Gemini + BeautifulSoup**")
    st.markdown("📚 Keeps short memory of last 10 queries.")

# --- Display chat history ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Chat input ---
user_query = st.chat_input("Ask me anything (e.g. 'What are the latest trends in AI research?')")

if user_query:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    # Analyze the user query
    analysis = analyze_query(user_query)
    curr_keywords = set(analysis["keywords"])
    previous_topics = [item["query"] for item in st.session_state.history]
    prev_keywords = set(" ".join(previous_topics).lower().split())
    has_context_overlap = bool(curr_keywords.intersection(prev_keywords))

    with st.chat_message("assistant"):
        with st.spinner("⏳ Thinking, researching, and analyzing..."):
            summaries = []

            if has_context_overlap:
                st.success("🔁 Reusing relevant past conversation for better response...")
                related_summaries = [item["summary"] for item in st.session_state.history]
                summaries.extend(related_summaries)
            else:
                st.info("🌐 Searching the web for fresh sources...")
                links = search_web(user_query, num_results=5)
                for idx, url in enumerate(links, 1):
                    st.write(f"🔗 ({idx}) Scraping: {url}")
                    content = scrape_text(url)
                    summary = analyze_content(content, user_query)
                    summaries.append(summary)

            # Combine results and show response
            final_response = synthesize_summaries(summaries, user_query)
            st.success("✅ Here's what I found:")
            st.markdown(final_response)

            # Store conversation
            st.session_state.messages.append({"role": "assistant", "content": final_response})
            st.session_state.history.append({
                "query": user_query,
                "summary": final_response
            })

            # Limit memory size
            MAX_HISTORY = 10
            if len(st.session_state.history) > MAX_HISTORY:
                st.session_state.history = st.session_state.history[-MAX_HISTORY:]
