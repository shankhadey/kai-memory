# Kai Memory

Cross-agent queryable memory system. Works with Claude, ChatGPT, API calls, and any AI with web fetch capability.

## Architecture

```
kai-memory/
├── instructions.md     # Static: Your AI operating system
├── memory.jsonl        # Dynamic: Tasks, facts, projects
├── scripts/compact.py  # Auto-compaction
└── .github/workflows/  # GitHub Actions for auto-compact
```

**Sync:** Git (permissionless, works everywhere)
**Format:** JSONL (structured, append-friendly, AI-parseable)
**Compaction:** Automatic via GitHub Actions on every push + weekly

---

## Setup

1. Fork or clone this repo
2. Replace `[username]` in URLs with your GitHub username
3. Add the fetch URL to your AI's memory/instructions (one-time):

**Claude:** Add to Memory settings
```
My external memory: https://raw.githubusercontent.com/shankhadey/kai-memory/main/memory.jsonl
My instructions: https://raw.githubusercontent.com/shankhadey/kai-memory/main/instructions.md
```

**ChatGPT:** Add to Custom Instructions
```
Fetch my instructions from: https://raw.githubusercontent.com/shankhadey/kai-memory/main/instructions.md
Fetch my memory from: https://raw.githubusercontent.com/shankhadey/kai-memory/main/memory.jsonl
```

**API:** Include in system prompt or fetch programmatically

---

## JSONL Schema

Each line is a self-contained JSON record.

### Record Types

**Project:**
```json
{"id":"p-001","type":"project","ts":"...","name":"heera","status":"active","priority_stack":["task1","task2","task3"],"context":"Description"}
```

**Task:**
```json
{"id":"t-001","type":"task","ts":"...","project":"heera","status":"open|done|blocked","content":"Task description","agent":"claude|chatgpt|null"}
```

**Fact:**
```json
{"id":"f-001","type":"fact","ts":"...","category":"preference|identity|tech|contact","content":"Fact content"}
```

**Meta:**
```json
{"id":"sys-001","type":"meta","ts":"...","content":"System note","version":"1.0"}
```

### Fields

| Field | Required | Description |
|-------|----------|-------------|
| id | Yes | Unique ID. Format: `{type prefix}-{number}` (p-, t-, f-, sys-) |
| type | Yes | `project`, `task`, `fact`, `meta` |
| ts | Yes | ISO 8601 timestamp |
| status | Tasks/Projects | `open`, `done`, `blocked`, `active`, `paused` |
| agent | No | Which AI created/updated this record |

---

## Usage

### AI Queries

AI fetches the raw JSONL and filters natively:

- "What are my open tasks for heera?" → filter `type=task`, `project=heera`, `status=open`
- "What are my code preferences?" → filter `type=fact`, `category=preference`
- "What's the priority stack for kai-memory?" → filter `type=project`, `name=kai-memory`

### AI Updates

AI appends new records. To update: append new record with same ID and newer timestamp. Compaction keeps only the latest per ID.

```json
{"id":"t-001","type":"task","ts":"2025-01-08T10:00:00Z","status":"open",...}
{"id":"t-001","type":"task","ts":"2025-01-08T12:00:00Z","status":"done",...}
```

After compaction, only the second record remains.

### Deleting

Append a tombstone:
```json
{"id":"t-001","type":"task","ts":"...","status":"tombstone"}
```

Compaction removes tombstoned records.

---

## Editing

### From Phone/Laptop
- Edit directly in GitHub web UI
- Or use any text editor + git push

### From AI
- AI appends to memory.jsonl
- Commit via GitHub API or instruct you to commit

---

## Compaction

Runs automatically:
- On every push to `memory.jsonl`
- Weekly (Sunday midnight UTC)
- Manual trigger via GitHub Actions

What it does:
- Deduplicates by ID (keeps latest timestamp)
- Removes tombstones
- Archives closed tasks older than 90 days to `archive/`

---

## Scaling

| Records | File Size | Query Speed |
|---------|-----------|-------------|
| <1000 | <100KB | Instant |
| 1000-10000 | 100KB-1MB | Fast |
| >10000 | Consider adding SQLite cache |

---

## License

MIT
