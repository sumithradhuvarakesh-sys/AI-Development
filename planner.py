import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
def create_plan(user_input):

    prompt = f"""
You are an AI agent planner for a web research agent.
User research question:
{user_input}
Available tools:

1. search_web
2. fetch_page

Decide the next action.

Return only one of these formats:

SEARCH: <search query>

FETCH: <url>

ANSWER: <final answer>
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text