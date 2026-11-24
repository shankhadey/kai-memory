# The playbook

Six phases. Each one ends at a **gate**: a checkable condition. A phase can take 15 minutes, but we don't skip it.

The pattern behind every slow project so far: **we built first and found out later.** The lessons show it happening each time:
- what the device or site really does
- who the product is for
- where it will be sold
- how we would know it works

Each phase below moves one of those discoveries to the front.

---

## Phase 1: Brief (you, about 15 min; Kai asks, you answer)

Answer these once, even the ones that feel months away:

1. **Who is it for, and what are the top 3 jobs?** Each job should be one sentence with a measurable result, e.g. "pick something to watch in under 30 seconds".
2. **Where will it run, eventually?**
   - platforms and devices
   - brands or sites it must work with
   - countries and languages
   - just for us, or sold to others
3. **Business model and distribution.** Free, paid, subscription, ads or no ads. Which store. Your own account or a company account. This decides the package name, the legal pages and the API keys.
4. **Non-negotiables.** Defaults so far:
   - design first
   - fix root causes, not symptoms
   - nothing household-specific hardcoded
   - English logs
   - radical simplicity
5. **Done for v1.** One sentence a stranger could check, e.g. "works on a stranger's TV, first try, no help".
6. **What we already know.** Hardware models, accounts, existing code, links to similar products.

**Gate:** Kai writes the brief into the repo's `CLAUDE.md` (template in `templates/`), and you confirm it in one reply.

## Phase 2: Investigate before building (Kai, about 1 hour)

1. List the **risky unknowns**: the things code can't tell us.
   - how the device or site behaves
   - API limits and terms
   - permissions and store policies
   - whether the AI can actually do the task well enough
2. Research each one. Read the docs, find prior art, and test it directly where possible. **Answer from sources, not memory.** Say how confident you are and why.
3. **Build the simulator.** This is the fake that behaves like the real thing, including its failures:
   - a simulated TV
   - a recorded Meet DOM
   - a sample inbox
   - a set of test videos

   If something can't be simulated, write down exactly what you'll need to check on the real thing, and why.

**Gate:**
- a list of unknowns, each marked answered, simulated, or needs-real-device
- the simulator runs in CI or with one command
- if a feature can't reach "will work" confidence, we say so here, not after building it

## Phase 3: Design (Kai shows, you choose)

- Show 2–3 options as images (screenshots, mockups or a clickable page) before writing any real UI.
- Cover the hard states: empty, error, offline, first run, and the longest translated text.

**Gate:** you pick one, and the choice goes into `CLAUDE.md`.

## Phase 4: Build in milestones

- `BACKLOG.md` holds the plan. Each item has a **done** line, e.g. "Done = from TV off, one tap opens Netflix, 10/10 in the simulator".
- Every change runs the full test suite and the simulator before it reaches you. You never get a build Kai hasn't verified.
- **One session per workstream** (e.g. "power and connection", "picks", "launch"). Strategy and business questions get their own session. `CLAUDE.md` and `BACKLOG.md` are the memory between sessions.
- **When something breaks twice, stop patching.** Write a test that reproduces it, find the root cause, then fix it once. Ten "fix X" commits for the same bug mean the problem wasn't understood yet.

**Gate per milestone:** Kai sends a short checklist, and you test the real thing once, against that checklist.

## Phase 5: Launch

Follow `lessons/launch-and-marketing.md`. In short:
- name and package checked early
- legal pages
- listing with generic screenshots
- demo built from a script
- closed test

**Gate:** the store accepts it, and a stranger installs it and completes the top job without help.

## Phase 6: Retro (10 min, at the end and after any painful loop)

Kai answers three questions in writing:
1. Where did the time go? Count the rounds, not the hours.
2. Which question, if asked on day 1, would have prevented it?
3. Where does that lesson belong? A `lessons/` file, or this playbook if it applies everywhere.

Then commit the change.

---

## How we talk during a project

- **Requests:** what you want + why + what "done" looks like. See `templates/request.md`.
- **Bug reports:** what you did, what you expected, what happened, plus Diagnostics or a screenshot. See `templates/bug-report.md`.
- **Kai's claims:** "it works" means verified, and Kai says how. "Should work" means not verified, and Kai says what's missing. If Kai isn't sure, Kai says so before you test, not after.
- **When you're frustrated:** say "stop and step back". Kai then stops patching and writes down:
  - what we know
  - what we've tried
  - the root-cause hypotheses
  - how to test each one
