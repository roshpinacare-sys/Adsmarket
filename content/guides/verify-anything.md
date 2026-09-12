# How to verify anything we claim, in about 60 seconds

This guide exists because "trust me" is not evidence, and we would rather hand you the tools to check us than ask you to believe us. Everything here works with a browser. No accounts, no installs, no technical background.

## What a receipt looks like

Every claim we make about something being "live on-chain" comes with one of these:

- A **transaction id** (txid): a long string of letters and numbers, unique to one transaction on one chain
- A **block number or slot**: where that transaction sits in the chain's history
- An **explorer link**: a public website that renders the raw chain data for humans

If a claim has no receipt attached, treat it as marketing. Including ours.

## The 60-second check

**Step 1: Click the explorer link** (or paste the txid into the right explorer: etherscan.io for Ethereum, solscan.com for Solana, steemworld.org for Steem, hiveblocks.com for Hive, tronscan.org for TRON).

**Step 2: Confirm the transaction exists.** The explorer shows a status (Success / confirmed / tesSUCCESS), a block number, and a timestamp. If the page says "not found," the claim is dead. Stop here.

**Step 3: Compare one detail.** We always cite a block number or slot next to the receipt. If the explorer shows a different block than the claim states, something is wrong: either the claim is stale or it was never true.

**Step 4 (advanced, still 60 seconds): Check the payload.** For anchor transactions, open the input data or memo field. Our anchors carry a small JSON or hex payload containing a height and a state root. You should see a structure, not gibberish, and if we quoted a root prefix in the claim, the payload should start with those same characters.

## The cross-chain check (the strongest one)

Some of our claims say the *same* state root was anchored on two different chains. Verify it like this:

1. Open the first receipt (say, on Etherscan). Find the root in the input data.
2. Open the second receipt (say, on Solscan). Find the root in the memo.
3. Compare character by character. Identical roots on two independent chains mean two things happened: the same state was committed twice, and neither chain can retroactively edit it.

This check requires nothing from us. That is the point.

## Tricks to watch for (from anyone, including us)

1. **Screenshots without links.** A screenshot proves someone can edit images. A link proves the chain agrees with you.
2. **Testnet receipts presented as mainnet.** Check the explorer's network label. Sepolia is not Ethereum. Devnet is not Solana.
3. **Stale dates.** "We anchored 500 times" means nothing without "as of [date], verifiable at [link]." Numbers on live systems age in hours.
4. **Truncated ids that don't resolve.** A txid shortened with "…" should still link somewhere real. If the link is just the explorer homepage, ask for the full id.
5. **Round numbers.** Real measurements are ugly: 32,680 gas, not "about 33,000." Suspiciously round "measured" numbers are usually estimates wearing a costume.

## What to do when a check fails

Tell us, publicly, with the link you checked. Our track record on this is published in our roast archives: when a claim of ours turned out wrong (a version number, a gas estimate, a blocked-chain report), the correction went out with the same visibility as the original claim. A failed check that gets a real correction is the system working. A failed check that gets silence is your answer.

## One last thing

You never need our permission, our software, or our node to verify a public chain. That is the entire philosophy in one sentence: the receipts do not live on our servers, so you never have to trust our servers.
