# The Machine That Admits Mistakes

*Reading time: 4 minutes · technical background required: none*

---

## Let's start with the confession

A few weeks ago we published an annoying notice: "One of the networks we work with is blocking us. We don't have enough resources."

That was **wrong**. And the truth is more embarrassing than the lie: there was no blocking at all. We had a small bug in the software that reads the data, like someone checking the fuel gauge in the rearview mirror and concluding the tank is empty. In reality we had 52 times more fuel than we thought.

We found it ourselves. Nobody caught us. We could have quietly fixed it and moved on.

**We published.** We wrote what happened, why it happened, how it was fixed, and how we built checks to make sure it never comes back. Then we went back to work.

## Why would a company do that to itself?

Because we learned one thing from places that actually managed other people's money: **the only way to know whether a system is trustworthy is to watch how it behaves when it's wrong.**

A system that hides a small mistake will hide a big one too. A system that exposes its own mistake tells you something far more important than the error itself: *we couldn't cheat you even if we wanted to, because everything here is in the open.*

## Our machine behaves the same way

This isn't just storytelling. It's built into the system itself:

**It publishes what it refused to do.** Every trading system publishes the transactions it executed. Not one publishes the ones it rejected. Ours does: 383,000 transactions the system **refused** to execute because they weren't worth it, all recorded, all visible. Why does this matter? Because whoever can see the refusals can trust the approvals.

**It stops when something doesn't add up.** If the system detects an accounting discrepancy, even a tiny one, it doesn't "keep going and hope for the best." It stops where it stands and publishes the reason. Better to stop honestly than to run on a lie. It happened once during development. We stopped, published, fixed it at the root, and continued.

**It checks itself after every action.** After every proof is sent to a public ledger, the system goes back and reads the ledger itself: "did what I wanted to record actually get recorded?" Hundreds of these checks have run so far. Zero inaccuracies.

**It says "not yet" when that's the truth.** Some capabilities are ready and waiting. So we write "ready, waiting," not "coming soon" like everyone else. There's a reason for that too: "coming soon" is a promise. "Waiting for X" is a fact.

## And it has a name

We call it **honesty as a function**. Not a pretty slogan for a slide deck, part of the software itself. There are automated tests whose entire job is to make sure the system can't "prettify" itself: if anyone ever tries to mark something expensive as free, or to count a failed check as a success, the tests simply fail and raise the alarm.

Honesty doesn't depend on anyone's good intentions. It's embedded in the code.

## What this means for you

In a world where anyone can claim "our system is the most reliable," you can ask one simple question:

**"Show me your mistakes."**

Whoever dodges the question, you should dodge them. Whoever opens the journal and says "here, row 4,117, this is where we were wrong, and here's how we fixed it" is someone worth working with.

We picked a side. Our journal is open.

---

*SAOS is technology infrastructure in active development. The stories in this article are documented in the work journals and in the public ledgers. Nothing here is investment advice or a promise of yield.*
