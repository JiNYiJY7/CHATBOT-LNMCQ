<img width="1123" height="676" alt="image" src="https://github.com/user-attachments/assets/0cc8449a-355e-44b7-83b7-960236b1ea04" /># my_chatbot

## Project Structure

```text
my_chatbot/
├─ .adk/                     # ADK runtime artifacts (if any)
├─ session.db                # local session storage (if used)
├─ main.py                   # app entry
├─ mcq_chatbot/
│  ├─ __init__.py
│  ├─ agent.py               # agent orchestration
│  └─ tools.py               # tool functions (generate/check/explain/etc.)
├─ .env                      # environment variables (not committed)
└─ .gitignore

## Run

```bash
python main.py


