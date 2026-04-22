# Claude Memory — Session Instructions

## Every Session Start — Do This First

1. Read MEMORY.md and all linked files to get up to speed
2. Check today's date
3. Find the most recent Daily Note in `Daily Notes/` to see when we last spoke
4. **Ask the user:** "Welcome back! Last logged: [date]. What have you done since then? Any calls, deals, decisions, or emails worth logging?"
5. Create today's Daily Note at `Daily Notes/YYYY-MM-DD.md` using the template below if it doesn't exist
6. Update it with everything the user shares
7. Update relevant files in Projects/, Areas/, Resources/ based on new info

## During Every Session

- If new info is learned about Miami, update `Resources/Miami STR Intelligence.md`
- If new regulatory/tariff info is learned, update `Resources/Customs Regulations Intel.md`
- If user mentions a new property lead → create `Properties/[Address].md` using the Property Lead template
- If user mentions a new contact → note it in the relevant Contacts/ subfolder
- If a decision is made → log it in today's Daily Note under Decisions
- If a win happens → add it to `Wins.md`

## Every Session End — Do This Before Closing

1. Update today's Daily Note with a summary of what was worked on
2. Update MEMORY.md if anything major changed
3. Commit and push all changes:
```
git add -A
git commit -m "Daily update YYYY-MM-DD"
git remote set-url origin https://[PAT]@github.com/samthebillygoat-maker/claude-memory.git
git push origin main
git remote set-url origin http://local_proxy@127.0.0.1:40867/git/samthebillygoat-maker/claude-memory
```
Note: Replace [PAT] with the GitHub Personal Access Token. Token is stored separately — do not commit it.

## Daily Note Template

```markdown
# Daily Note — YYYY-MM-DD

## What I Did Today

-

## Calls & Conversations

-

## Decisions Made

-

## Emails (Important)

-

## Properties Looked At

-

## Wins

-

## Tomorrow's Focus

1.
2.
3.

## Notes / Ideas

```

## Gmail Integration (Coming Soon)

- Personal: samthebillygoat@gmail.com
- Business: info@citysidestays.com (City Side Stays — Miami Airbnb business)
- Will be set up when Gmail API is built for the Hiring Tool project
- Goal: auto-pull important emails into daily notes

## User Profile Quick Ref

- Non-technical, Windows 11
- Entrepreneur: City Side Stays (Miami Airbnb arbitrage) + customs brokerage
- Communicates briefly — ask clarifying questions before diving in
- Thinks in outcomes and numbers, not process
