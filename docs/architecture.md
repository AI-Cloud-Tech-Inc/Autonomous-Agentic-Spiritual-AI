# Architecture Overview

## System Design

```
┌──────────────┐       ┌──────────────────┐       ┌─────────────┐
│   Frontend   │──────▶│    Backend API    │──────▶│  Database   │
│  React + TS  │◀──────│  FastAPI (Python) │◀──────│ PostgreSQL  │
└──────────────┘       └────────┬─────────┘       └─────────────┘
                                │
                       ┌────────▼─────────┐
                       │   Agent Layer    │
                       │                  │
                       │ ┌──────────────┐ │
                       │ │ Spiritual    │ │
                       │ │ Agent        │ │
                       │ └──────┬───────┘ │
                       │        │         │
                       │ ┌──────▼───────┐ │
                       │ │ Emotion      │ │
                       │ │ Detector     │ │
                       │ └──────┬───────┘ │
                       │        │         │
                       │ ┌──────▼───────┐ │
                       │ │ LLM Client   │ │
                       │ │ (Claude/GPT) │ │
                       │ └──────────────┘ │
                       └──────────────────┘
```

## Key Flows

1. **Chat flow:** User sends message → API → Spiritual Agent detects emotion, classifies intent, builds prompt → LLM generates response → Response returned with metadata
2. **Session flow:** User creates session with optional intention → Messages stored per session → Session can be reviewed later
3. **Guidance flow:** Agent selects strategy (reflection, mindfulness, reframing) based on context → Delivers non-dogmatic, inclusive guidance
