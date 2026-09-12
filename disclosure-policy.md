# Disclosure policy: what we publish, what we never publish, and why

> The binding document for anyone writing in SAOS's name. It was born from this understanding:
> **Honesty means every claim we publish is a verifiable truth. Honesty is not broadcasting every internal event.**

---

## The guiding principle

Our brand is "receipts, not promises", and that applies to **product claims**. But security is the one domain where silence is part of the defense. Publishing a security event is not honesty, it is handing attackers a map: what was breached, when, how, and what is still exposed.

## What we publish: and why

| We publish | Why |
|---|---|
| Capabilities + receipts (txids, measurements, charts) | The heart of the brand: every claim is independently verifiable |
| Product status including limitations ("awaiting funding", "small TVL", "not yet deployed") | Prevents over-promising and builds long-term trust |
| Correction of a technical claim we ourselves published (like the RC read bug) | We published a wrong claim, the correction is part of honesty |
| Operational failures that are product lessons (self-healing, chaos, HALT in development) | Shows resilience as a feature without exposing an attack vector |
| Security doctrine as a design principle ("keys never in the repo") | Strengthens trust without telling what led to it |

## What we never publish: and why

| We never publish | Why |
|---|---|
| Security events: key leaks, loss of access, intrusions, emergency rotations | A map for an attacker + damage to trust even when the event is resolved |
| Recovery details, forensics, or restoration methods | The same map, in more detail |
| Wallet addresses holding funds, key structure, internal operating procedures | Painting a target |
| An ongoing event of any kind | A partial picture creates misleading panic |
| Any personal detail of the owner (seeds, passwords, chat contents) | Self-explanatory |

## How much do we reveal?

**Up to the capability level, not the event level.**
- Allowed: "The keys were never in the repo, the whole history was checked and clean (0 keys in 32 commits)."
- Forbidden: "...because we lost the keys on a Tuesday."
- Allowed: "On-chain key rotation is a proven capability with public receipts."
- Forbidden: the story of what made the rotation necessary.
- The numbers that demonstrate strength are published (14/14 verifications, 3 homes for the vault, THE-GATE). The story behind them is not.

## How do we phrase it? (phrasing laws)

1. **Positive, not scarred:** doctrine as a design principle from day one, "keys never touch the repo", not "after the leak we removed the keys".
2. **Capability, not event:** rotation, recovery and purging are shown as tested muscles, without a trigger.
3. **A direct journalist question:** the press-kit answer is the doctrine + "we do not comment on specific operational events, that is itself the security policy."
4. **The internal fact-sheet records everything** (including events, tagged internally as warning items), so the team learns and no lesson is lost, and so no marketing cut touches the tagged sections.

## The three-question test before every publication

1. **Is the claim true and verified?** No, we do not publish.
2. **Does the publication expose a weakness, timing, or method to an attacker?** Yes, we do not publish.
3. **Is this a correction of something we ourselves published?** Yes, we must publish. That is honesty.

## Three new rules (born in the roast of 2026-09-10: roast/2026-09-10-truth-gaps.md)

1. **The availability rule:** we do not publish an install command, URL, or endpoint without a real liveness check against an external user (npm registry / browser / curl). A published command that returns 404 is a false claim at the brand level, exactly the sin the brand speaks against.
2. **The snapshot rule:** every measured number is attached to a measurement date. A version-tagged number (v28) or a monotonic counter is marked "as of X". A snapshot presented as live is a lie waiting to be measured again.
3. **The inside/outside rule:** "live and proven inside the system" is not "available today to anyone". The phrasing must distinguish the two explicitly, always.

4. **The read-verification rule (added after the confabulation event, 2026-09-10):** when a tool read fails or returns an error, **no content from the read's "memory" is written and no conclusion drawn from it is published**. Pull again, or do not write. Text written from a failed read is an invention, however good the intention. (Zero damage to the repo, reported to the operator as self-correction #3, see fact-sheet 10.31.)

## Retroactive

Event content already published in the kit was deleted or rephrased according to the policy (done upon adopting the document: article 07 was deleted, post L12 was removed, L2 was rephrased as doctrine, the press-kit and the landing pages were corrected). What was not published will not be published.
