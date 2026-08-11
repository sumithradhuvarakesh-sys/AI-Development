# UC2 – Iterative Web Research Agent
 **AI Development – Cycle 1 | Agent Loop**

An AI-powered web research agent that searches the web, evaluates the retrieved information, refines the search query when required, and generates a final answer with a source citation.

---

## 1. Problem Statement

Traditional web search returns multiple links, but the user still needs to inspect the results and decide whether the available information is sufficient.

This project implements an iterative web research agent that can search the web, fetch relevant information, evaluate the evidence, refine the search when required, and generate a cited final answer.

---

## 2. Use Case

### UC2 – Iterative Web Research Agent

The agent accepts a research question from the user and performs iterative web research until sufficient information is found or the maximum iteration limit is reached.

---

## 3. What the Agent Does

The agent follows this loop:

1. Understand the research question
2. Create a search plan using Gemini
3. Search the web
4. Fetch the top webpage
5. Evaluate the fetched information
6. Refine the search query if information is insufficient
7. Repeat the process when required
8. Generate a final answer with the source URL

---

## 4. User Flow

```text
User enters research question
          |
          v
       Perceive
          |
          v
   Plan using Gemini
          |
          v
      Web Search
          |
          v
     Fetch Webpage
          |
          v
   Observe / Evaluate
          |
          v
 Is information sufficient?
       /           \
     YES            NO
      |              |
      v              v
Final Answer      Refine Query
+ Source URL          |
                      v
                Next Iteration
```
# Architecture

The architecture diagram is available in the `diagrams/` folder(architecture.png)
## 5. Agent Stages

### Perceive

Receives and understands the current research question.

### Plan

Gemini decides the next research action and generates a search query.

### Act

The agent uses the available web tools:

- `search_web()`
- `fetch_page()`

### Observe

Gemini evaluates the fetched webpage and returns either:

```text
SUFFICIENT
```

or

```text
REFINE: <new search query>
```

### Final Answer

When sufficient information is available, Gemini generates the final answer and includes the source URL.

---

## 6. Tools

### `search_web(query)`

Searches the web and returns relevant search results.

### `fetch_page(url)`

Fetches a webpage and extracts readable text from the page.

## 7.. Technology Stack
Component	          Technology
Programming Language - Python
LLM	                 - Google Gemini
Google GenAI SDK	 - 2.17.0
Web Search	         - DuckDuckGo HTML
HTTP Requests	     - Requests 2.34.2
HTML Parsing	      -BeautifulSoup4 4.15.0
Environment Variables -python-dotenv 1.2.2
Logging	              -JSON
Version Control	      -Git / GitHub

---

## 8. Project Structure

```text
AgentLoop/
|
|-- main.py
|-- planner.py
|-- tools.py
|-- logger.py
|-- requirements.txt
|-- README.md
|-- .env
|-- .gitignore
|
|-- logs/
    |-- agent_trace.json
```
# File Description
File	  Purpose
main.py	     Runs the agent loop
planner.py   planning ,observation,final answer 
tools.py	 Provides web search and webpage fetching
logger.py	 Records agent execution steps
requirements.txt	Lists project dependencies
agent_trace.json	Stores execution logs
---

## 9. Setup

### 1. Create a virtual environment

```bash
python -m venv venv
```
### 2. Activate the environment
Windows:

```bash
venv\Scripts\activate
```
### 3. Install dependencies

```bash
pip install -r requirements.txt
```
### 4. Configure Gemini API
Create a `.env` file:
```env
GEMINI_API_KEY=your_api_key_here
```
Do not commit the `.env` file or expose the API key.
---
## 10. Run the Agent
Run:
```bash
python main.py
```
Enter a research question when prompted.
Example:

```text
Enter your research question: What is artificial intelligence?
```
---
## 11. Example Output

```text
Perceive:
Understanding research question...
Plan:
SEARCH: artificial intelligence
Act:
Search result: ...

Fetch result: ...

Observe:
Observation: SUFFICIENT

Final Answer:

Artificial Intelligence (AI) refers to ...

Source:
https://example.com/source

Research completed successfully.
```
---
## 12. Iterative Refinement
When the fetched information is not sufficient, the agent creates a better search query and continues to the next iteration.
Example:

```text
Iteration: 1
Observation: REFINE: latest artificial intelligence developments
                         |
                         v
Iteration: 2
Plan: SEARCH: latest artificial intelligence developments
                         |
                         v
                       Search
                         |
                         v
                        Fetch
                         |
                         v
                       Observe
```
---
## 13. Recovery and Termination

### Tool Failure Recovery

If a search or webpage fetch fails, the agent records the failure and attempts to continue with a refined search.

### Maximum Iterations

The agent is limited to:

```python
MAX_ITERATIONS = 5
```
The agent stops when:
- Sufficient information is found, or
- The maximum number of iterations is reached.
---
## 14. Logging
Agent execution details are stored in:

logs/agent_trace.json

The log records:

- Iteration number
- Time
- Agent stage
- Actions
- Observations
- Recovery events
- Final answer
- Success status

---
## 15. Testing

The agent has been tested for:

- Normal web research
- Web search and webpage fetching
- Final answer generation
- Source citation
- Query refinement
- Multiple iterations
- Tool failure recovery
- Maximum iteration termination
- Execution logging

---
## 16. Status

**Cycle 1 – Agent Loop**

**UC2 – Iterative Web Research Agent**
---
Component  Status-completed
Agent Loop
Web Search  
Webpage Fetching 
LLM Observation 
Query Refinement  
Final Cited Answer  
Failure Recovery  
Iteration Limit 
Logging  Complete 
MVP Testing 
Documentation 
--- 
## 18. Security
- API keys are stored in `.env`
- `.env` is excluded using `.gitignore`
- API credentials are not committed to the repository
---
## 19. Project Status
**UC2 MVP: Complete**:

The core iterative web research agent has been implemented, tested, and pushed to GitHub.