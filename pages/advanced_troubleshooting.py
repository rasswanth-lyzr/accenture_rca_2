import uuid

import streamlit as st

from agent import (
    chat_with_knowledge_base_agent_dumb,
    chat_with_knowledge_base_agent_smart,
)

st.title("Knowledge Base Comparision")
st.write("This Agent contains all the advanced troubleshooting data")

if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4().hex)

user_input = st.text_input("Agent Input")
if st.button("Chat with agent"):
    agent_output = chat_with_knowledge_base_agent_smart(
        user_input, st.session_state.session_id
    )

    st.write("### LYZR RAG (with preprocessing)")
    st.write(agent_output)

    dumb_agent_output = chat_with_knowledge_base_agent_dumb(
        user_input, st.session_state.session_id
    )

    st.write("### LYZR RAG (without preprocessing)")
    st.write(dumb_agent_output)
