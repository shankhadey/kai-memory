# Launch playbook

How Kai and I take an idea from first message to a launched product with as few iterations as possible.

It's a working document. Both of us edit it, and both of us follow it.

## How to use it

**Starting a project.** Say *"Kai, run the playbook for <idea>"*. Kai then:
1. walks through `PLAYBOOK.md` phase by phase, asking only the questions that aren't answered yet
2. reads the matching file in `lessons/`
3. writes the answers into the new repo's `CLAUDE.md` and `BACKLOG.md`

**During a project.** Each phase ends at a gate. We don't move on until the gate is met.

**After a project, or after any painful loop.** Run the retro in `PLAYBOOK.md`. Kai adds what we learned to `lessons/`, and to this playbook if it applies to every project.

## Files

| File | What it's for |
|---|---|
| `PLAYBOOK.md` | The phases, the questions to answer and the gates |
| `lessons/device-and-os-integration.md` | TVs, cameras, screen capture, OS behaviour: anything you can't see from code |
| `lessons/browser-extensions-on-other-sites.md` | Extensions that read sites we don't control (Meet, Gmail) |
| `lessons/ai-assistants-and-agents.md` | Email, coaching and other apps where an LLM makes decisions |
| `lessons/ui-prototypes.md` | Clickable prototypes and redesigns |
| `lessons/research-and-benchmarks.md` | Evaluation sets and research code |
| `lessons/launch-and-marketing.md` | Store listings, demo videos, naming, pricing |
| `templates/` | CLAUDE.md skeleton, request format, bug-report format |

Everything here is written to be safe in a public repo. No names, keys, emails or household details.
