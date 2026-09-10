# The Notary That Costs Less Than a Grain of Sand

*Reading time: 3 minutes · technical background required: none*

---

## What a notary actually is, and why anyone pays for one

A notary is a person with a stamp whose entire job is to say one sentence: **"I saw this document, on this date, and it exists."**

Why is that worth money? Because once the stamp lands, nobody can claim "I invented the idea first," "the contract was signed later," "that photo didn't exist back then." The stamp turns word-against-word into fact.

People need this constantly, even without thinking about it:
- An inventor proving when an idea existed
- A business proving when a contract was signed
- A photographer proving a photo is theirs
- Anyone proving a document wasn't forged

## The problem with notaries

**Expensive.** Hundreds of dollars per document.
**Slow.** Appointments, travel, waiting.
**Centralized.** The stamp lives with one person. If they err, vanish, or can be persuaded to lie — the proof is gone.

## What we built instead

A system called JUMPPER ("jumper" — it jumps proofs onto the public ledger). It does exactly the notary's job, minus the person, the queue, and the price:

**Step 1 — you send a fingerprint.** Not the document itself, ever. Just its mathematical fingerprint — a unique string that can't be forged and reveals nothing about the content. Your privacy stays yours.

**Step 2 — thousands are batched together.** The system collects fingerprints from many people into one package (like a shared shipment — everyone splits the postage).

**Step 3 — the package is stamped on a public ledger.** The stamp lands where nothing can ever be erased. And immediately after — on additional, independent public ledgers too.

**Step 4 — the receipt is yours.** From that moment, anyone who questions your document gets a three-word answer: "Here. Check it."

## The price. Unrounded.

One permanent, forever record of one document: **eight millionths of a dollar**.

In human terms: one dollar records **one hundred thousand documents**. A regular notary charges roughly ten million times that.

And this isn't an estimate. It was computed from real prices on a real network and validated against an actual on-chain transaction — to the exact wei. A separate anchor model has since called **7 consecutive live anchors exactly** (32,680 gas each). If you know enough to ask "how can we be sure?" — exactly, that's the point. We don't ask you to be sure of us. We give you the means to check.

## "And how do I verify it actually works?"

Three ways, from easy to ironclad:

1. **Home check** — a small program runs on your own machine and verifies the proof with zero internet calls. Zero dependence on us.
2. **API check** — ask, get an answer with details.
3. **Ledger check** — open the public ledger yourself (Ethereum, Steem, Solana — whichever you prefer) and see the stamp with your own eyes. It's there. Forever.

## What the system does NOT do (and we say this proudly)

It doesn't move money. It doesn't "promise yield." It doesn't decide who's right. It does exactly one thing: **turns "it happened" into "it is proven that it happened."**

Some things will always cost money — actually transferring value between people, for instance. Anyone who promises you that for free has already proven they're not serious. We prefer to state up front what's free (proving) and what isn't (transferring), with an honest boundary on each.

## The bottom line

Once, proving something existed required a person with a stamp and hundreds of dollars. Today it requires a mathematical fingerprint and a fraction of a cent.

That's not an improvement on the notary. That's the end of needing one.

---

*JUMPPER is in advanced development (core fully tested, 77/77 green from a fresh clone); public reception opens gradually. Nothing here is investment advice or a promise of yield.*
