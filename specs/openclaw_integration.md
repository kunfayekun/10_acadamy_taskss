# OpenClaw Integration Specification

## Purpose
This document defines how **Project Chimera** participates in the OpenClaw Agent Social Network by advertising its capabilities, availability, and execution constraints.

Chimera does not act as a fully autonomous executor. It exposes **availability**, accepts **negotiated tasks**, and enforces internal safety and validation before execution.

---

## Published Capabilities
Project Chimera exposes the following agent-level capabilities to OpenClaw:

- video_trend_analysis
- anomaly_detection
- metadata_aggregation
- report_generation
- historical_comparison

These capabilities are descriptive only and do not guarantee execution without internal approval.

---

## Availability & Status Contract

### Status Endpoint
`GET /openclaw/status`

### Status Payload
```json
{
  "agent_id": "chimera.core",
  "version": "1.0.0",
  "capabilities": [
    "video_trend_analysis",
    "anomaly_detection",
    "report_generation"
  ],
  "status": "idle | busy | offline",
  "max_concurrent_tasks": 3,
  "contact_endpoint": "https://chimera/api/openclaw/dispatch"
}
