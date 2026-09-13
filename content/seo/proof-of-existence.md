---
seo-title: "Proof of Existence: How to Timestamp Any Document for Under a Cent"
meta-description: "Permanent, independently verifiable document timestamping for $0.0000081 per record, or free on stake-based chains. How proof of existence works, what it proves, and how to check any receipt yourself."
keywords: proof of existence, document timestamping, blockchain notary, cheap notarization, trusted timestamp
---

# Proof of Existence: How to Timestamp Any Document for Under a Cent

Someone claims they had the idea first. A contract's signing date is disputed. A photo's origin is questioned. These arguments all share one shape: word against word, with no neutral record of what existed when.

Proof of existence is the fix, and it is older than blockchains. A notary stamps a document and the date stops being arguable. The problem was never the concept. It was the price, the queue, and the fact that the whole proof rests on one person with a stamp.

## How blockchain timestamping actually works

You never put the document on a chain. You compute its cryptographic fingerprint (a hash): a short string, unique to that exact file, where changing a single pixel or comma produces a completely different string. Then you publish that fingerprint in a transaction on a public ledger.

From that moment, three things are true forever:

1. The document (in that exact form) existed no later than that block's timestamp.
2. Nobody can backdate a competing version, because the ledger does not allow edits.
3. Nobody can read your document from the fingerprint. The hash reveals nothing about the content.

Verification works in reverse: anyone who holds the document recomputes the hash and finds it inside the public block. Match means the document is the one that was stamped. That check needs no permission from anyone, including whoever published it.

## What it costs (measured, not quoted)

Two working models exist, and we have receipts for both.

**Batched on Ethereum.** Thousands of fingerprints are combined into one merkle tree, and the tree's single root goes on-chain. Your document is then provably inside that root with a small inclusion proof. At a 10,000-claim batch, one permanent record costs about **$0.0000081** (eight millionths of a dollar), computed from a gas model that was calibrated against a real mainnet transaction to the exact wei: 30,920 gas at block 25,929,672, including the EIP-7623 calldata floor most estimators miss. One dollar records roughly 123,000 documents.

**Free on stake-based chains.** Steem and Hive charge no fees at all. Transactions burn Resource Credits, which regenerate from staked tokens. A compact 247-byte attestation costs about 1.36 billion RC, and a live receipt exists for exactly such a broadcast: Steem block 109,496,567, with the account's RC balance afterward still covering roughly 250 more broadcasts of the same size. Free, here, is a measurement with a block number, not a marketing word.

## Three ways to verify a record, from easiest to strongest

1. **Offline self-verification.** Recompute the hash locally, check the inclusion proof against the published root. Zero network calls, zero trust in anyone.
2. **API lookup.** Ask the service; get the root, the block, and the proof back with details you can re-check.
3. **On-chain.** Open the block in a public explorer (etherscan.io, steemworld.org, hiveblocks.com) and find the payload yourself. This tier does not depend on the service existing at all.

A timestamping service that cannot offer tier 3 is asking you to trust it. That defeats the purpose.

## The honest boundary: attestation is not enforcement

Proof of existence establishes that content existed at a time. It does not force anyone to honor a contract, pay a debt, or respect a copyright. It is evidence, and evidence still needs a decision-maker: a court, a platform, a community, a counterparty. Anyone selling "enforcement on-chain" for free is selling confusion. The value is real but specific: disputes that used to be unprovable become provable, for less than the paper they were printed on.

## When you would actually use this

- **Creators**: timestamp drafts, designs, and code commits before sharing them externally.
- **Freelancers and agencies**: stamp delivery artifacts; "we delivered on the 14th" stops being a memory contest.
- **Businesses**: stamp contract versions, audit exports, and inventory snapshots. Regulatory inquiries get a verifiable timeline instead of a filing cabinet.
- **Developers**: stamp software builds and configuration states; incident reviews get ground truth about what version existed when.
- **Anyone in a dispute**: the side with the earlier verifiable timestamp negotiates from a different universe.

## The bottom line

For most of history, proving "this existed then" required a person you paid and trusted. Today it requires a hash and a public ledger, at a cost between zero and a hundredth of a cent, verifiable by strangers decades from now without asking anyone's permission. The technology is the boring part. The shift is that the price of provable honesty fell to roughly nothing, and institutions built on expensive proof have not adjusted yet.

If you check one thing after reading: open any receipt this site cites in a public explorer and compare a single character. That habit, more than any product, is the actual point.
