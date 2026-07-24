"""
Lead Qualification & Scoring Agent
------------------------------------
Takes raw lead information (form submission, call notes, email, CRM
record) and produces a BANT-based qualification score with reasoning
and a recommended next action.

Built with LangChain + Anthropic Claude.
"""

import os
import sys
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage


def load_system_prompt() -> str:
    prompt_path = os.path.join(os.path.dirname(__file__), "system_prompt.md")
    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()


def qualify_lead(lead_info: str) -> str:
    system_prompt = load_system_prompt()

    llm = ChatAnthropic(
        model="claude-sonnet-4-6",
        max_tokens=1500,
        api_key=os.environ.get("ANTHROPIC_API_KEY"),
    )

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Lead information:\n\n{lead_info}\n\nProduce the qualification assessment as instructed."),
    ]

    response = llm.invoke(messages)
    return response.content


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python agent.py \"<lead information text>\"")
        print("Or: python agent.py --file <path_to_text_file>")
        sys.exit(1)

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: Set the ANTHROPIC_API_KEY environment variable before running.")
        sys.exit(1)

    if sys.argv[1] == "--file" and len(sys.argv) > 2:
        with open(sys.argv[2], "r", encoding="utf-8") as f:
            lead_text = f.read()
    else:
        lead_text = " ".join(sys.argv[1:])

    result = qualify_lead(lead_text)
    print(result)
