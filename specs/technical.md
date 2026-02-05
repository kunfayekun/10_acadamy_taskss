# Technical Specification

## Architecture Overview
- Backend: Django
- Analytics Engine: Elasticsearch
- Agents communicate via JSON-based contracts
- Reports generated as JSON, HTML, or PDF

---

## API Contracts

### Agent Task Request
```json
{
  "task_id": "uuid",
  "agent_type": "planner | worker | judge",
  "input": {
    "query": "string",
    "filters": {},
    "time_range": {
      "from": "ISO-8601",
      "to": "ISO-8601"
    }
  }
}
