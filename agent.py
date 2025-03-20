import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

LYZR_DEV_API_KEY = os.getenv("LYZR_DEV_API_KEY")
LYZR_PROD_API_KEY = os.getenv("LYZR_PROD_API_KEY")

AGENT_DEV_CHAT_URL = os.getenv("AGENT_DEV_CHAT_URL")
FEEDBACK_URL = os.getenv("FEEDBACK_URL")
AGENT_PROD_CHAT_URL = os.getenv("AGENT_PROD_CHAT_URL")

FEEDBACK_AGENT_ID = os.getenv("FEEDBACK_AGENT_ID")
FEEDBACK_RAG_ID = os.getenv("FEEDBACK_RAG_ID")
TICKET_AGENT_ID = os.getenv("TICKET_AGENT_ID")

KNOWLEDGE_BASE_AGENT_ID = os.getenv("KNOWLEDGE_BASE_AGENT_ID")

SQL_AGENT_ID = os.getenv("SQL_AGENT_ID")


def chat_with_agent(url, api_key, user_id, agent_id, session_id, message):
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
    }

    payload = json.dumps(
        {
            "user_id": user_id,
            "agent_id": agent_id,
            "session_id": session_id,
            "message": message,
        }
    )
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"Other error occurred: {err}")
        return None


def add_feedback(rag_id, feedback, user_input, agent_output):
    url = FEEDBACK_URL

    params = {"feedback_rag_config_id": rag_id}

    headers = {
        "Content-Type": "application/json",
        "x-api-key": LYZR_DEV_API_KEY,
    }

    payload = json.dumps(
        {
            "feedback": feedback,
            "user_input": user_input,
            "agent_output": agent_output,
        }
    )

    try:
        response = requests.request(
            "POST", url, params=params, headers=headers, data=payload
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"Other error occurred: {err}")
        return None


def chat_with_accenture_agent(user_message, session_id):
    url = AGENT_DEV_CHAT_URL
    response = chat_with_agent(
        url,
        LYZR_DEV_API_KEY,
        "default_user",
        FEEDBACK_AGENT_ID,
        session_id,
        user_message,
    )
    return response["response"]


def add_feedback_accenture_agent(feedback_message, user_input, agent_output):
    response = add_feedback(FEEDBACK_RAG_ID, feedback_message, user_input, agent_output)
    return response


def chat_with_knowledge_base_agent(user_message, session_id):
    url = AGENT_DEV_CHAT_URL
    response = chat_with_agent(
        url,
        LYZR_DEV_API_KEY,
        "default_user",
        KNOWLEDGE_BASE_AGENT_ID,
        session_id,
        user_message,
    )
    return response["response"]


def chat_with_sql_agent(user_message, session_id):
    url = AGENT_PROD_CHAT_URL
    response = chat_with_agent(
        url, LYZR_PROD_API_KEY, "default_user", SQL_AGENT_ID, session_id, user_message
    )
    return response["response"]


def chat_with_ticket_agent(user_message, session_id):
    url = AGENT_DEV_CHAT_URL
    response = chat_with_agent(
        url, LYZR_DEV_API_KEY, "default_user", TICKET_AGENT_ID, session_id, user_message
    )
    return response["response"]
