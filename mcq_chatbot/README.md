# my_chatbot

## Project Structure
my_chatbot/
├─ .adk/ # ADK runtime artifacts (if any)
├─ session.db # local session storage (if used)
├─ main.py # app entry
├─ mcq_chatbot/
│ ├─ init.py
│ ├─ agent.py # agent orchestration
│ └─ tools.py # tool functions (generate/check/explain/etc.)
├─ .env # environment variables (not committed)
└─ .gitignore


## Run
```bash
python main.py
