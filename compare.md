# SAOS vs the alternatives: an honest comparison

> Document rules: every line of ours is backed by a measurement or a receipt. Every competitor line is marked as "order of magnitude from public documentation" if we did not measure it ourselves. **And there is a "when not to use us" section, because anyone who does not have one is probably selling something.**

---

## The main table

| Need | The accepted solution | SAOS | What we do not claim |
|---|---|---|---|
| **Permanent proof of existence for a document** | Notary: 400 shekels and up, hours of work, a single point of trust · OpenTimestamps: free but anchored to Bitcoin alone, minutes to hours | $0.0000081 per record (batch of 10K, measured) · 5 independent rails · self-verification without a network | This is attestation, not enforcement: we prove existence, we do not force compliance |
| **Cross-network state proof** | Chainlink CCIP / LayerZero / Wormhole: gas + a signed verification committee you have to trust (history: Wormhole ~$320M, Ronin ~$600M) | Atomic clock: 6 networks resolved into one 32B root, keyless, $0, 15.9ms compute, 6.8ms verification, the other side reads the same public RPCs itself | Does not replace a price oracle with an SLA commitment; per-network finality reported as it is |
| **Moving assets between chains** | Custodial/multisig bridges, the most-hacked category in the industry (> $2B) | We are not a bridge in that sense: 1:1 wraps as a code invariant (supply==locked, 20 assets, every mint cites a lock) + SOVEREIGN-HAND (a building agent, the vault stamps through a gate) | The ETH contracts and the SOL software are in staging, not deployed; the total locked is small today (hundreds of dollars), published |
| **Moving value between networks (speed)** | A third-party bridge/custodian: 10 to 90 minutes + fees + one big point of trust | The sovereign conversion room: the money does not move, a 1:1 mirror on our network · measured live: 65/65 atomic legs, p50 88ms · external consolidation as an alternative honest route | The mirror requires our network as the arena; a live cutoff of balances (not a proof of external capital depth) |
| **Trading without MEV sandwich** | DEXs with an open mempool, sandwiches are a fact of life | Uniform CoW settlement per block: one clearing price, surplus returned to traders, **structural immunity** (there is no queue to attack) · verified live | TVL is honestly tiny ($13.91 · v28 snapshot 09.09), the mechanism is proven, the scale is not |
| **Proving AI agent execution** | Nothing exists, an agent claims "I did it" and there is no receipt | JUMPPER + live anchoring: every claim becomes a seal on a public ledger · SOVEREIGN-VOICE: an agent post/vote with a real tx (c64766e7... @ 109,443,160) | A new category, no industry standard yet to compare against |
| **Running a "chain" without paying validators** | L1/L2: a security budget of millions, or testnet forever | Shadow-L1: every checkpoint signed at $0 (Graphene RC) / agorot (ETH calldata) / zero-net (TRON bit-encoding), 74,907+ blocks | Finality is inherited from the hosts; no independent validator set; independent tokenomics not yet defined |
| **A wallet for veteran Graphene identity** | MetaMask-style wallets do not know Steem/Hive; steem-js wallets do not bridge | Cross-paradigm identity: one Graphene key = an EVM address, an ecrecover proof without exposing anything · API+SDK live in the repo and proven E2E (external release in progress) | Full automatic login/recovery is still being built |

*Competitor values = orders of magnitude from public documentation, not measured by us. Our rows: every number measured or anchored, with a link in the fact-sheet.*

## When **not** to use SAOS (yes, really)

1. **Need legal enforcement?** We prove, we do not enforce. Go to court, with our receipts.
2. **Need Ethereum's own finality for large funds today?** Use Ethereum directly. We are a proof layer, not a replacement for a network with deep capital.
3. **Looking for a custodian to manage assets for you?** We are the exact opposite of a custodian: your keys stay with you, and your proofs are public.
4. **Expecting "returns"?** None. There never were. Anyone promising them is not connected to us.
5. **Need economic scale today?** Our economics are dust-scale; the mechanisms are proven at small scale. If you need millions in flow, come back in a year, or come be part of proving it works slowly and safely.

## Three questions any competitor can be asked against us

1. **"Show me your refusals."** Ours: 383,836 skips + 130,499 rejections documented, live in an API. How many products publish what they did *not* do?
2. **"Show me your mistakes."** Ours: published self-corrections (the RC bug at 52.6 times, a wallet audit marked SUPERSEDED, a recommendation we retracted ourselves). The log is open.
3. **"How do I verify without trusting you?"** Ours: 3 tiers (self-verify without a network / API / on-chain) + an open receipts table on the landing page. If a product cannot answer this question in one line, that is the answer.

## Using this document

- For journalists/analysts: take any line, tap the fact-sheet, open the receipt. Found an inaccuracy? We publish a correction, as always.
- For the marketing team: this table is background material. For publishing, cut single sentences only, always with the link.
- For everyone: the "when not" section is not modesty. It is the filter that makes sure the right people reach us.
