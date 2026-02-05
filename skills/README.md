# Chimera Agent Skills

## Definition
A **Skill** is a self-contained capability package that an agent can invoke to perform a specific task.

Each skill defines:
- Purpose
- Inputs (contract)
- Outputs (contract)
- Constraints

Skills are **not autonomous**.  
They are orchestrated by Planner and validated by Judge agents.

---

## Skill 1: skill_fetch_video_metadata

### Purpose
Retrieve video metadata from Elasticsearch for analysis.

### Input Contract
```json
{
  "index": "string",
  "filters": {},
  "time_range": {
    "from": "ISO-8601",
    "to": "ISO-8601"
  }
}
