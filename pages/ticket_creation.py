import datetime
import uuid

import streamlit as st

from agent import chat_with_ticket_agent

st.title("Ticket Creation")
st.write("This is a ticket creation agent that creates a ticket in the required format")

if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4().hex)

vin_number = st.text_input("VIN Number", value="MAR3DXS4E03464631")
issue_description = st.text_input("Issue Description", value="Engine is overheating")
if st.button("Submit"):
    todays_date = datetime.date.today()
    user_message = f"""VIN Number: {vin_number}, Issue Description: {issue_description}, Today's Date: {todays_date}"""
    agent_output = chat_with_ticket_agent(user_message, st.session_state.session_id)
    st.write(agent_output)
