# AI assistants and agents

Covers email assistants, coaching, voice interfaces, and anything where an LLM decides what to do.

## What happened

**Email assistant (Feb–Apr 2026)**
- About 10 fix PRs in a row, all on one branch named after the first bug:
  - wrong Drive attachment picked
  - "Poll Now" ignoring the time window
  - Settings buttons broken by fragile async setup
  - wrong file again, from recency ranking
- You asked "are you sure about 1? … emails I sent myself were read". A confident claim had been made without checking the real data.
- Later: "wtf man do a research". You asked a question and got an answer from memory, not research.

**Voice layer:** a good architecture plan existed, but nothing defined what "works" meant for spoken commands.

## Rules

1. **Build an eval set before the feature.** 20–50 real examples with expected outcomes: emails, transcripts, queries, and edge cases like self-sent mail, time zones and ambiguous file names. Every change runs against it.
2. **Verify claims about data against the data.** "Read" or "unread", "the right file": check the actual API response before answering.
3. **Research means sources.** Unless it's trivial, "what's the best X" gets searched and cited, not recalled.
4. **One branch and PR per fix**, named for what it does.
5. **Show what the AI decided and why** (a decision log) so you can see wrong picks without debugging.
