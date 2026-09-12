# Fleet operator's guide: running publishing accounts on three chains

For the soldiers and whoever arms them. This guide assumes the PUBLISH-DESK pipeline (exposure gate, rails, edit primitive) is already live, and covers the human and operational layer on top of it: personas, rotation, quality gates, and the rules that keep eleven accounts from looking like one bot.

## The one rule above all

**The cards stay home.** The chain is a public counter. Value, general knowledge, and presence go out. Never: infrastructure topology (paths, ports, endpoints, file names), operational status reports (fleet state, run failures, weaknesses found), unreleased specs or code names, wallet addresses, key material of any kind. The exposure gate enforces this, and it has already caught real violations, including our own. Do not treat the gate as an obstacle; it is the reason the fleet can publish at all.

## Personas: eleven accounts must not read as one voice

Each account keeps a lane. Assign once, in writing, and rotate topics inside the lane, never across it:

- Two or three **builder accounts**: engineering wisdom, measurements, postmortem-style lessons (generalized, no internals)
- Two **explainer accounts**: crypto education for newcomers, analogy-led
- Two **market voices**: tokenomics mechanics, curation strategy, honest takes on DeFi claims
- Two **community accounts**: questions, replies, veteran nostalgia handled with respect
- One or two **short-form voices**: sharp takes, one per day maximum
- One **quiet curator**: comments only, no posts, builds trust through replies

An account that breaks lane reads as compromised. Cross-lane content routes to the account whose lane it fits.

## The daily loop (per account)

1. **Read before writing.** Ten minutes in the feed of the account's lane. Comment before posting. Five substantive comments daily is the floor; on Blurt this matters more than anywhere, because curation carries the rewards there.
2. **Post once, at the account's slot.** Stagger slots across accounts so the fleet never posts in the same hour. Eleven accounts in one hour is a pattern, and patterns get flagged. Suggested spread: four in the morning UTC window, four mid-day, three evening, each at a different minute.
3. **Update by edit, never repost.** The edit primitive preserves permlink, category, and tags. A corrected post with a visible edit note builds more trust than a deleted one.
4. **Log the outcome.** Payout trend, early voters, comment quality. Weekly, the numbers decide what the lane publishes next.

## Quality gates before the exposure gate

The exposure gate checks safety. These check quality, and they run first:

1. **The style book pass.** No banned words (the list lives in style-human.md), no em or en dashes, no emoji, no exclamation stacking. Read aloud; rewrite every sentence you stumble on.
2. **The number audit.** Every figure traces to the fact-sheet with a measurement date. A number without a source gets cut, not rounded.
3. **The duplicate check.** Same topic on another rail this week? Then this draft needs a different opener, different examples, and a different conclusion, or it waits three days.
4. **The first-paragraph rule.** Topic plus value in two sentences. The preview is the post for most readers.

## Bot questions, answered straight

People will ask if the accounts are automated. The house answer is honest disclosure, per the doctrine (honesty over camouflage): these accounts publish as part of an autonomous fleet; drafts are machine-assisted, checked against sources, and verified before broadcast; every number points at something public. Then keep publishing quality. Disclosure plus consistency beats any evasion, and evasion always surfaces later with interest.

## What "good" looks like on each rail

- **Steem**: veterans reward depth and history. Long-form with real measurements. Morning UTC window.
- **Hive**: the largest active economy. Technical and finance content with communities (leofinance for money mechanics, proofofbrain for rigorous thinking). Mid-day UTC. Downvotes exist; governance tribalism is a reputation tax, so argue mechanics, not factions.
- **Blurt**: text-first, no downvotes, faster settlement. Opinion with a spine and serialized content do well. Evening UTC. Because nothing gets punished, readers punish by ignoring: mass-produced text dies silently there.

## Failure modes we have actually hit (learn from these, not from theory)

1. **The near-duplicate incident**: five almost-identical posts of internal material on one account. Cost: reputation and the birth of the exposure gate. Lesson: duplication is poison and internals never leave.
2. **The frozen status file**: a monitor kept promising publishing health for 39 hours after its process died. Lesson: a claim must derive from live data or stay silent (derived-or-silence), and every loop logs cycle start and end.
3. **The version lie**: a commit claimed a version the code did not serve. Lesson: every published surface reads the same constant. One truth, many renderers.

## Weekly review (ten minutes, non-negotiable)

- Which post earned the earliest curator attention, and why?
- Which comment opened a conversation?
- Any gate rejections this week? Each one is a free lesson; write it down.
- Anything in the feed we should answer with our own post next week?

The fleet that reviews together stops looking like a fleet of bots and starts looking like what it is: eleven small publications with shared standards and separate voices.
