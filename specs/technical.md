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


---

## JSON Schemas

### Agent Task Request (JSON Schema)
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AgentTaskRequest",
  "type": "object",
  "required": ["task_id", "agent_type", "input"],
  "properties": {
    "task_id": {"type": "string", "format": "uuid"},
    "agent_type": {"type": "string", "enum": ["planner", "worker", "judge"]},
    "input": {
      "type": "object",
      "properties": {
        "query": {"type": "string"},
        "filters": {"type": "object"},
        "time_range": {
          "type": "object",
          "properties": {
            "from": {"type": "string", "format": "date-time"},
            "to": {"type": "string", "format": "date-time"}
          },
          "required": ["from", "to"]
        }
      },
      "required": ["query", "time_range"]
    }
  }
}
```

### Trend Result (JSON Schema)
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "TrendResult",
  "type": "object",
  "required": ["platform", "topic", "trend_score", "timestamp"],
  "properties": {
    "platform": {"type": "string"},
    "topic": {"type": "string"},
    "trend_score": {"type": "number"},
    "timestamp": {"type": "string", "format": "date-time"}
  }
}
```

---

## Data Storage & DB Schema

Primary analytical store: **Elasticsearch** (time-series, high-cardinality video metadata).

Recommended index: `video_metadata_v1`

Example Elasticsearch mapping (minimal):
```json
{
  "mappings": {
    "properties": {
      "video_id": {"type": "keyword"},
      "platform": {"type": "keyword"},
      "title": {"type": "text"},
      "description": {"type": "text"},
      "published_at": {"type": "date"},
      "views": {"type": "long"},
      "likes": {"type": "long"},
      "tags": {"type": "keyword"},
      "geo": {"type": "geo_point"},
      "category": {"type": "keyword"},
      "ingest_timestamp": {"type": "date"}
    }
  }
}
```

Notes:
- Use `keyword` for fields used in aggregations (platform, tags, category).
- Use `date` fields with proper timezone-normalized ISO-8601.
- Create time-based index rotation (monthly/daily) depending on ingest volume.

Relational fallback / metadata catalog (ERD stub):

- Table: `videos`
  - `id` (pk, uuid)
  - `platform` (varchar)
  - `video_id` (varchar)
  - `title` (text)
  - `published_at` (timestamp)
  - `ingest_timestamp` (timestamp)

- Table: `video_metrics` (time series)
  - `id` (pk)
  - `video_id` (fk -> videos.id)
  - `metric_ts` (timestamp)
  - `views` (bigint)
  - `likes` (bigint)

Use PostgreSQL for low-volume, strongly consistent use-cases; prefer Elasticsearch for analytics and high-cardinality aggregations.

---

## Indexing & Retention

- Retention policy: keep raw events 90 days, rollup monthly aggregates to long-term store.
- Create ILM (Index Lifecycle Management) policies in Elasticsearch to automate rollover and deletion.
