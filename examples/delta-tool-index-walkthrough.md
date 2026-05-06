# Delta Tool Index Stack Walkthrough

I use this file as a small checklist before changing the Python implementation.

| Case | Focus | Score | Lane |
| --- | --- | ---: | --- |
| baseline | file span | 188 | ship |
| stress | terminal width | 111 | watch |
| edge | argument risk | 181 | ship |
| recovery | report density | 157 | ship |
| stale | file span | 225 | ship |

Start with `stale` and `stress`. They create the widest contrast in this repository's fixture set, which makes them better review anchors than the middle cases.

The useful comparison is `file span` against `terminal width`, not the raw score alone.
