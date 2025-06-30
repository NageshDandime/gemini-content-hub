import streamlit as st
import google.generativeai as genai

#........................................................................Configure Gemini API key
genai.configure(api_key="AIzaSyCm0MILP-xGBYghTAyTpxxv55FT8q4LMJw")

# Load Gemini model
model = genai.GenerativeModel('gemini-2.5-flash-preview-04-17')

#........................................................................ Streamlit page config
st.set_page_config(page_title="Gemini Chat", page_icon="💬", layout="wide")

# Sidebar
with st.sidebar:
    st.title("🤖 Gemini Chat")
    st.markdown("""
    Welcome to Gemini-powered Chat!
    
    👉 **Instructions:**
    - Type your message below.
    - Press Enter to get an answer.
    - Clear chat anytime.
    """)
    if st.button("🗑️ Clear Conversation"):
        st.session_state["messages"] = []
        st.rerun()
    st.markdown("---")
    st.caption("Powered by Google Gemini API")
    st.caption('Developed By:- Nagesh Dandime')

#....................................................... Main title
st.title("💬 Gemini Chat Interface")

# .......................................................Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

#......................................................... Display previous messages
for message in st.session_state["messages"]:
    if message["role"] == "user":
        st.markdown(f"🧑‍💻 **You:** {message['content']}")
    else:
        st.markdown(f"🤖 **Gemini:** {message['content']}")

# ..............................................................Input box for new user question
prompt = st.text_input("Type your message and press Enter...", key="input")

# .................................................................When user submits
if prompt:
    #................................................................. Save user message
    st.session_state["messages"].append({"role": "user", "content": prompt})
    
    #.................................................................... Generate Gemini response
    with st.spinner("Gemini is thinking..."):
        response = model.generate_content(prompt)
        answer = response.text.strip()
    
    #......................................................................... Save Gemini response
    st.session_state["messages"].append({"role": "gemini", "content": answer})
    
    # ...........................................................................Rerun to display updated history
    st.rerun()
