import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
def create_plan(user_input):
    prompt = f"""
You are an AI agent planner.
User request:
{user_input}
Available tools:
1. calculator
2. current_time
Decide which tool should be used.
Return only:
TOOL: tool_name
"""
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )
    return response.text
