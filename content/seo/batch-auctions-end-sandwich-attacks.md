---
seo-title: "How Batch Auctions End Sandwich Attacks on DEXs (Structurally, Not Defensively)"
meta-description: "Sandwich attacks tax every sequential DEX trade. Private mempools and commit-reveal schemes treat symptoms. Uniform clearing price batch auctions remove the sequence itself. The mechanism, the math, and the honest tradeoff."
keywords: sandwich attack, MEV protection, batch auction, uniform clearing price, CoW swap, DEX fairness
---

# How Batch Auctions End Sandwich Attacks on DEXs

If you have traded on a decentralized exchange, you have probably paid a tax you never agreed to. Your buy order enters the mempool, a bot sees it, buys the same asset a block earlier, lets your trade push the price up, and sells into your slip a moment later. You paid more; the bot profit is carved out of your execution. This is a sandwich attack, and on sequential DEXs it is not a bug. It is the natural behavior of a visible queue.

## Why sequential order flow makes sandwiches inevitable

A conventional AMM or order book settles trades one at a time, in arrival order. That sequence is the entire attack surface: someone is always first, someone is always last, and everything in between has a position relative to your trade. Bots do not need to break anything. They only need to observe the queue and insert themselves around you. Every defense that keeps the queue and hides it is a delaying action:

- **Private mempools** hide the order until inclusion, but the inclusion order itself still leaks value, and privacy becomes a paid service controlled by whoever runs the dark pool.
- **Commit-reveal schemes** hide amounts behind a two-phase ceremony, adding latency and a new failure mode (reveals can be withheld) while still settling sequentially.
- **Encrypted intents** move the trust problem to whoever holds the decryption keys.

All three preserve the thing the attack needs: a sequence.

## The structural fix: remove the sequence

A batch auction settles an entire window of orders at once, at one price. The mechanism, stripped to its parts:

1. Orders accumulate for a fixed window (one block, in the implementations we run).
2. At window close, the auction computes a single **uniform clearing price**, typically the midpoint between the best bid and best ask among the collected orders.
3. Every matched order executes at that one price, with quantities allocated pro-rata where the two sides are unequal.
4. Surplus stays with the traders: a buyer who bid above the clearing price pays the lower clearing price; a seller who asked below it receives the higher clearing price. In well-designed batches, that surplus is returned, not captured by the protocol or the block producer.

Now walk the sandwich through this machine. The bot wants to buy before you and sell after you. There is no before and after. All orders in the batch are peers at one computed price. The bot can participate, and participation means clearing at the same midpoint as everyone else. There is no position to exploit because position no longer exists as a concept. The immunity is not probabilistic ("harder to sandwich") and not adversarial ("we outbid the bots"). It is structural: you cannot ambush a queue that was never formed.

## The math that keeps it honest

Two properties separate a real batch auction from marketing:

**Deterministic allocation.** When buy volume and sell volume differ, the matched quantity is the smaller side, distributed pro-rata with integer arithmetic. Canonical implementations use floor division plus a bounded remainder to the last order in a deterministic sort, so replaying the same batch always produces identical fills. No floats, no randomness, no timestamp dependence inside the settlement.

**Verifier-visible surplus.** The difference between each trader's limit price and the uniform clearing price is computable by anyone from the batch inputs. A batch that silently keeps the surplus is a fee wearing a fairness costume. Ours reports it as a measured counter (surplus returned, in base units) alongside matched volume, per batch.

## The honest tradeoff

Batch auctions are not free. You give up instant execution: your order waits for the window to close. For market orders during a fast-moving minute, that latency is a real cost, and anyone who tells you otherwise is selling something. What you get in return is execution fairness that no bot can tax, plus price discovery that aggregates the whole window instead of rewarding whoever paid the most gas to be first.

In practice this means batches suit most flows (rebalancing, entry and exit at a fair reference price, recurring orders) and not every flow (leveraged liquidations racing a ticking price). Mature designs keep a sequential fallback for the residual and route the rest through the batch.

## What to check before trusting any "MEV-protected" venue

1. Is settlement truly simultaneous at one price, or is it a priority queue with extra steps? Ask what happens to two identical orders arriving 10ms apart. In a real batch: identical treatment. In a disguised queue: one fills first.
2. Where does the clearing-price surplus go? Traders, protocol, or block producer? Get the answer in basis points, not adjectives.
3. Is allocation deterministic and replayable? Feed the same batch to their contract and to your own reimplementation; results must match to the integer.
4. Is there a live counter of batches settled, volume matched, and surplus returned? Numbers that update beat adjectives that persuade.

## The bottom line

MEV extraction on sequential DEXs is an arms race the trader always loses, because the trader pays for every round of it. Batch auctions end the race by deleting the track: one window, one price, no positions, surplus home. The idea is not new (traditional finance has used closing auctions for exactly this reason), and the on-chain implementations have now been running long enough to be measured rather than admired. Fairness you can verify beats protection you must rent.
