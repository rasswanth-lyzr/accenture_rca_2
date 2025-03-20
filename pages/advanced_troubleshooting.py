import uuid

import streamlit as st

from agent import chat_with_knowledge_base_agent

st.title("Knowledge Base")
st.write("This Agent contains all the advanced troubleshooting data")

if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4().hex)

st.write("### LYZR RAG")
user_input = st.text_input("Agent Input")
if st.button("Chat with agent"):
    agent_output = chat_with_knowledge_base_agent(
        user_input, st.session_state.session_id
    )
    st.write(agent_output)

    st.session_state.agent_output = agent_output
    st.session_state.user_input = user_input
