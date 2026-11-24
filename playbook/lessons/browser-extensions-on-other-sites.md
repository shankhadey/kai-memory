# Browser extensions on sites we don't control

Covers extensions like the live meeting coach that read Meet captions, the mic and the page.

## What happened

**Meeting coach (Feb–Apr 2026)**
- You asked "how confident are you that the mic energy feature will work?" and "what would you want me to do to test?". That means the confidence and the test plan came after the code, not before.
- `DEBUG_FORCE_*` flags were left in place of a test harness.
- In April, after a real call: the other speaker's captions weren't captured at all. Meet's obfuscated class names and caption layout don't match what the code expected.
- The fix needed multiple fallback strategies. Nothing had ever been tested against a real recorded Meet page.

## Rules

1. **Record the real page first.** Save Meet's actual DOM, with captions on, two speakers, the self view and settings panels, as test fixtures. Re-record when the site changes.
2. **Prefer stable hooks.** Use ARIA roles, `aria-live` regions and data attributes, not generated class names. Keep a canary test that fails loudly when the site changes.
3. **Before building, state confidence and the test plan:** "70%, because X. Here's how we'll know."
4. **Test with two people early.** A single-person test can't catch "the other side isn't captured".
