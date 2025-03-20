import uuid

import streamlit as st

from agent import add_feedback_accenture_agent, chat_with_accenture_agent

st.title("Adaptive Learning Demo")

st.write("The agent returns 3 simple steps to resolve your issue. You can give feedback to the agent to improve its performance. NOTE: The agent is not trained on any data, it is just a demo.")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4().hex)

user_input = st.text_input("Agent Input")
if st.button("Chat with agent"):
    st.session_state.user_input = user_input
    agent_output = chat_with_accenture_agent(user_input, st.session_state.session_id)
    st.session_state.agent_output = agent_output
    st.write(agent_output)

agent_feedback = st.text_input("Agent Feedback")
if st.button("Give feedback to agent"):
    feedback_output = add_feedback_accenture_agent(
        agent_feedback, st.session_state.user_input, st.session_state.agent_output
    )
    st.write(feedback_output)
