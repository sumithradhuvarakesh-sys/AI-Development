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

    return response.text.strip()


def observe_page(user_query, page_content):

    prompt = f"""
You are an AI web research evaluator.

User research question:
{user_query}

Fetched webpage content:
{page_content}

Evaluate whether this webpage contains enough relevant
information to answer the user's research question.

If the information is sufficient, return:

SUFFICIENT

If the information is not sufficient, create a better
search query and return:

REFINE: <new search query>

Return ONLY one of these formats:

SUFFICIENT
REFINE: <new search query>
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text.strip()