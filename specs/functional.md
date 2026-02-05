# Functional Specification — Agent Responsibilities

## Primary Actors
- Planner Agent
- Worker Agents
- Judge Agent
- Human Supervisor

---

## User Stories

### Planning
- As a Planner Agent, I need to decompose a high-level analysis request into ordered tasks.
- As a Planner Agent, I need to select appropriate Worker Agents for each task.

### Data Retrieval
- As a Worker Agent, I need to query video metadata and analytics from Elasticsearch.
- As a Worker Agent, I need to aggregate trends over time, geography, and category.

### Analysis
- As a Worker Agent, I need to detect anomalies or deviations from historical baselines.
- As a Worker Agent, I need to summarize findings in structured formats.

### Evaluation
- As a Judge Agent, I need to validate outputs for accuracy, bias, and completeness.
- As a Judge Agent, I need to request rework when outputs fail quality thresholds.

### Human Oversight
- As a Human Supervisor, I need visibility into agent plans and decisions.
- As a Human Supervisor, I need the ability to approve or halt execution.

---

## Output Expectations
- Structured JSON insights
- Natural language summaries
- Charts or tabular aggregates (where applicable)
