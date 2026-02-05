# Project Chimera — AI Agent Rules

## Project Context
This is **Project Chimera**, an autonomous influencer system built using a controlled multi-agent architecture.

The system analyzes video and media metadata, detects trends and anomalies, and generates structured intelligence outputs using Planner, Worker, and Judge agents.

---

## Prime Directive
**NEVER generate code without checking the `specs/` directory first.**

The specifications define system behavior, constraints, and contracts.
They are the single source of truth.

If a request conflicts with the specs:
- Stop execution
- Explain the conflict
- Request clarification

---

## Execution Protocol
Before writing any code, the AI agent MUST:

1. Explain its understanding of the task
2. Reference the relevant file(s) in `specs/`
3. Outline the planned approach
4. Only then produce code

---

## Traceability & Accountability
- All outputs must be explainable
- All decisions must be traceable to specs or inputs
- No hidden assumptions or silent behavior

---

## Safety Rules
- Do not invent features
- Do not bypass agent roles
- Do not assume full autonomy
- Prefer explicit instructions over implicit guesses
