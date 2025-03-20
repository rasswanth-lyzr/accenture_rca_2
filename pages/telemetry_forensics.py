import uuid

import streamlit as st

from agent import chat_with_sql_agent

st.title("Telemetry Forensics (SQL Agent)")
st.write("This is an SQL Agent that performs query on the database and verifies the machine's data is within the threshold or not")

if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4().hex)


vin_number = st.text_input("VIN Number", value="MAR3DXS4E03464631")
issue_description = st.text_input("Issue Description", value="Engine is overheating")

if st.button("Submit"):
    user_message = (
        f"""VIN Number: {vin_number}, Issue Description: {issue_description}"""
    )
    agent_output = chat_with_sql_agent(user_message, st.session_state.session_id)
    st.write(agent_output)
