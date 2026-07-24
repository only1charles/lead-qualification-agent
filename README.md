# Lead Qualification & Scoring Agent

A sales agent that takes raw lead information — a form submission, call
notes, email inquiry, or CRM record — and produces a BANT-based
qualification score with written reasoning and a recommended next action.

Built with **LangChain** + **Anthropic Claude**.

## How it works

1. You provide raw lead information as text (pasted notes, a form
   submission, etc.).
2. `agent.py` sends it to Claude along with detailed instructions
   (`system_prompt.md`) that define exactly how to score it and what
   format to respond in.
3. It returns a structured score (0-100), a Hot/Warm/Cold temperature,
   a BANT breakdown, reasoning, and a recommended next action.

## Files

- `agent.py` — the main script: takes lead text, calls the model, prints the assessment
- `system_prompt.md` — the agent's instructions/behavior definition
- `requirements.txt` — Python dependencies

## Running locally

```bash
pip install -r requirements.txt
```

Set the ANTHROPIC_API_KEY environment variable to your Anthropic API key, then run:

```bash
python agent.py "Name: Jane Doe. Company: Acme Corp. Message: Looking for a solution to automate our onboarding process, need something in place before Q3. Budget range not mentioned. Jane is Head of Operations."
```

Or pass a text file with lead notes:

```bash
python agent.py --file lead_notes.txt
```

## Notes

- The agent never invents details (budget figures, titles, timelines)
  that weren't actually provided — missing information is marked
  "Unknown" rather than assumed.
- No data is stored — each run is a fresh, one-off assessment.
