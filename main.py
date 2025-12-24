import asyncio
import os

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from mcq_chatbot.agent import root_agent


APP_NAME = "mcq_chatbot_local"
USER_ID = os.getenv("ADK_USER_ID", "user_1")
SESSION_ID = os.getenv("ADK_SESSION_ID", "session_001")


async def call_agent_async(query: str, runner: Runner, user_id: str, session_id: str) -> str:
    """Send one user message and return the agent's final response text."""
    content = types.Content(role="user", parts=[types.Part(text=query)])

    final_text = "[No final response]"
    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
        if event.is_final_response():
            if event.content and event.content.parts:
                final_text = event.content.parts[0].text or final_text
            elif getattr(event, "error_message", None):
                final_text = f"[ERROR] {event.error_message}"
            break
    return final_text


async def main():
    load_dotenv()  # loads DEEPSEEK_API_KEY etc. from .env

    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )

    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    print("MCQ Chatbot is running. Type 'exit' to quit.\n")

    while True:
        user_msg = input("You: ").strip()
        if not user_msg:
            continue
        if user_msg.lower() in {"exit", "quit"}:
            print("Bye!")
            return

        reply = await call_agent_async(user_msg, runner=runner, user_id=USER_ID, session_id=SESSION_ID)
        print(f"Bot: {reply}\n")


if __name__ == "__main__":
    asyncio.run(main())
