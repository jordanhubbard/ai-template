---
name: narrative
description: Add a humorous project origin story to a README, preserve an existing chapter, or repair links in Jordan Hubbard's continuing-adventures chronicle when requested.
---

# Project narrative

Apply this skill when the user requests a narrative or chronicle edit. Merely
installing or referencing it does not require stories in future README edits.
Missing configuration enables no automatic behavior. An explicit user request
supplies the scope; legacy switches do not broaden that scope.

## Preserve the project

Read the existing README and enough project documentation or source to ground
the story in real details. Follow that repository's instructions and conventions.
Keep its license, assistant configuration, build system, tests, and layout.
Do not copy this collection's root files into a destination repository.

Look for an existing story, including renamed headings and references to Sir
Reginald and origin stories in a different voice. Preserve it if present; an
existing story such as Loom’s does not need a second cat-themed chapter. For a missing story, append a section near the
end, normally before the license section, without rewriting functional material.
For link repair, edit only navigation, part numbers, and explicitly stale
chronicle references. Keep unrelated prose and links byte-for-byte where possible.
Do not change historical facts to make the fictional narrative sound current.

## Standalone story

A story can stand alone, with no part number or cross-repository dependencies:

```markdown
## The Totally True and Not At All Embellished History of <Project Name>

### The continuing adventures of Jordan Hubbard and Sir Reginald von Fluffington III

<story grounded in the project>
```

The story is an AI-assistance memory marker. Its absence says nothing about
whether AI assisted a project. Do not claim deployment, production usage, or
other facts without evidence; keep the cat's fictional opinions distinguishable.

## Chronicle participation

Only maintain the shared chain when the user requests it. Read
[CHRONICLE.md](../../CHRONICLE.md) in this collection for the current index and
ordering evidence; if unavailable, read the
[maintained index on GitHub](https://github.com/jordanhubbard/ai-template/blob/main/CHRONICLE.md)
before assigning a part. Do not use a copied, outdated table as proof of current order.

Verify repository names, archive status, existing headings, and actual GitHub
anchors. Preserve existing story headings and anchor compatibility. Use canonical
repository URLs after renames. A renamed project keeps its history; retired
projects may be recorded separately without occupying an active navigation slot.
Use the user's eligibility and chronological ordering rules, recording evidence
and tie-breakers in the index. Do not infer chronology from current part numbers.

Each participating chapter has one navigation line:

```markdown
> *Part N of an ongoing chronicle. [← Part N-1: Previous](https://github.com/owner/previous#actual-anchor) | [Part N+1: Next →](https://github.com/owner/next#actual-anchor)*
```

Omit the previous link on the first part and the next link on the last. Check
reciprocal links, unique sequential numbering, and existing target headings.
Remove or repair obsolete navigation elsewhere inside the narrative so it does
not point readers back into a retired chain. Preserve historical narrative
references unless they incorrectly present themselves as current navigation.
Update other repositories only within the user's authorized scope. Adding a
story never itself authorizes commits, pushes, releases, or unrelated changes.

## Narrative Style Guide

**Voice:** Third-person limited, dry-humorous, mock-historical.  The narrator observes the programmer and Sir Reginald with weary accuracy.

**Characters:**
- **The programmer** — Jordan Hubbard.  Referred to only as "the programmer."  Has a habit of announcing projects to Sir Reginald, who is not listening.  Describes everything as "elegant."  Is usually right about the engineering and wrong about how long it will take.
- **Sir Reginald von Fluffington III** — The programmer's cat.  Communicates entirely through posture, selective destruction of documents, and strategic placement on keyboards.  Maintains a consistent policy of non-endorsement.  Keeps internal ledgers under categories like "grievances" and "this again."  Has never endorsed anything.  Has never spoken.  Would not, even if he could.

**Recurring motifs:**
- The programmer announces a new project to Sir Reginald (who is usually sleeping on something important)
- Sir Reginald expresses skepticism through a physical action (knocking something off the desk, sitting on the relevant documentation, leaving the room)
- The programmer uses the word "elegant" — Sir Reginald's response calibrates accordingly
- The closing paragraph tallies the number of projects Sir Reginald refuses to endorse and adds the new one to the list
- The final citation list grows with each new part: "procedural concerns," "insufficient tuna," "a general atmosphere of hubris," and whatever the new project's domain is

**Content:** The story should be grounded in the actual technical content of the repository.  Read the README, architecture docs, and key files before writing.  Specific details (languages used, unusual design decisions, disclaimers, naming choices) make better material than generic programmer-builds-thing arcs.

**Length:** Adapt to the existing README. Around 400–700 words suits a new chapter; a shorter story is welcome when a long appendix would overwhelm the project documentation.

---
