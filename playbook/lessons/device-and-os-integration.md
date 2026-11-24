# Device and OS integration

Covers TVs, screen and webcam capture, and anything else where the hard part is how hardware or the OS behaves.

## What happened

**TV remote (Nov 2026, 6 days, v0.2 → v1.5.5)**
- For four days you were the test loop: build an APK, install it, try it on the TV, paste Diagnostics.
- Turn-on, opening apps and clicks on tiles each took several rounds.
- Once the simulated TV existed, regressions dropped sharply.
- Unknowns were discovered one at a time by trial: Wi-Fi turn-on, Quick Start+, two different MAC addresses, how each streaming app accepts a title.

**Screen recorder (Apr 2026)**
- About 10 commits over 4 days titled "Fix recursive Lense UI", each a different patch for the same symptom: the recorder captures its own window.
- No way to reproduce the bug except you recording your own screen.
- The session ended with the task unfinished and you understandably angry.
- Afterwards, 15 small hand edits in the browser to fix library imports (importmap, TTS model ID, a 401). Nothing had verified that the deployed page actually loaded.

## Rules

1. **Map the device before UI.** For each capability, list how it works, what the docs say, what really happens and how it fails. Fill the table from docs, forums and direct tests.
2. **Build a simulator that fails like the real thing.** Examples:
   - a fake TV that ignores commands while booting
   - a canvas test that switches tabs, windows and native apps
   - a headless browser that loads the deployed page and plays audio
3. **Same symptom twice = stop.** Write a test that reproduces it, list the root-cause hypotheses, and rule them out one by one. No third patch.
4. **Test the deployed artefact, not just the code.** Load the real URL or install the real APK in CI and check the browser console for errors. Pin library versions.
5. **The real device is checked once per milestone**, against a checklist, never as the debugger.
