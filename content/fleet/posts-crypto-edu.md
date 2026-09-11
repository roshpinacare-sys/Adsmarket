# Crypto education posts: six publish-ready drafts

Chain mechanics explained for real audiences. All numbers are public chain facts or published measurements. Strong candidates for LEO Finance (finance angles) and dev communities.

---

## C1 · Resource Credits, explained like the phone plan they are

Tags: steem, hive, blockchain

Steem and Hive transactions cost nothing, and that sentence confuses people until someone explains the actual mechanism. So here it is, without the jargon.

Both chains run on stake. When you hold powered-up tokens, the network grants you a pool of Resource Credits. Think of it as a monthly data plan paid for by holding the asset. Every operation you broadcast burns some RC: a vote burns a little, a transfer burns a little, a custom_json burns an amount that scales with its byte size. A compact 247-byte payload runs about 1.36 billion RC. The pool refills continuously, fully regenerated every five days.

That's the whole economy. No fees to a miner, no gas auction. You pay with patience and stake, not with tokens leaving your wallet.

One trap worth knowing, because it bites everyone eventually. The RC API returns your stored balance as of its last update timestamp, not your balance right now. If an account hasn't transacted in a while, the stored number can be wildly below the truth. The real figure is:

effective = min(max_rc, stored + (max_rc / 432000) * seconds_since_update)

We once read a stored balance of about 1.4 million RC, concluded an account was too poor to broadcast, and built an entire gate around that conclusion. The regenerated balance was 73 million. Fifty-two times higher. The chain was never the problem. Our reading of it was.

If you build on Graphene chains, compute the effective balance or you will eventually declare yourself broke while sitting on a full tank.

---

## C2 · What a merkle root actually is, and why chains are obsessed with them

Tags: blockchain, cryptography, education

Blockchains store a lot and prove things with almost nothing. The trick behind that asymmetry is a structure called a merkle tree, and it deserves a better explanation than most docs give it.

Take a dataset. Any dataset: a thousand account balances, a day of transactions, the full state of an application. Hash each entry. Now pair the hashes, hash each pair, pair those results, hash again. Keep going until one hash remains. That final hash is the merkle root, and it has a remarkable property: it is a fingerprint of the entire dataset. Change one entry anywhere, even one digit of one balance, and the root changes completely. There is no edit small enough to hide.

The second property is why it matters for money. You can prove a single entry belongs to the dataset without revealing the dataset. The proof is just the sibling hashes along the path from your entry to the root. For a million entries, that path is about twenty hashes, a few hundred bytes. A verifier recomputes upward and either the root matches or it doesn't.

This is how light wallets verify payments without downloading chains. It's how rollups commit state to Ethereum. It's how any system that produces a lot of data can publish one small commitment and let strangers verify any piece of it later.

The honest caveat, because there is always one: a merkle root proves consistency, not correctness. If whoever built the tree lied about the entries, the root faithfully fingerprints the lie. Roots are receipts. They tell you what was claimed, immutably. Whether the claim matches reality is a separate check, and systems that skip that check are just notarizing fiction.

---

## C3 · The calldata floor nobody talks about, and why your gas estimates drift

Tags: ethereum, gas, eip7623

If your gas estimates for data-heavy Ethereum transactions are consistently low, you are probably not alone, and you are probably not stupid. The pricing rules changed under everyone's feet.

Quick refresher on the normal rules. Calldata is priced per byte: 4 gas for a zero byte, 16 for a non-zero byte. That's the number in every tutorial and every library default. A transaction that writes a 200-byte memo to the chain pays for those bytes and moves on.

Then came EIP-7623, which introduced a floor. The transaction now pays the greater of two amounts: the classic per-byte cost, or a floor computed at 40 gas per non-zero byte (and 10 per zero) minus a fixed allowance. For small payloads nothing changes. For data-heavy transactions, the floor wins, and suddenly the real cost is about two and a half times what the naive formula predicts.

Why does the floor exist? Data availability. Blobs made bulk data cheap for rollups, and the floor keeps regular calldata from becoming the new cheap dumping ground that congests the chain.

Practical consequences, if you anchor data or run an oracle: estimate with the floor in mind or your transactions sit underpriced on busy days. Test your estimator against real receipts, not against documentation, because libraries lag behind forks for months. And log predicted versus actual on every send. We calibrated one estimator against a live receipt down to the wei, 30,920 gas exact, and it has matched seven consecutive sends since. The calibration took an afternoon. The confidence is permanent.

---

## C4 · How a batch auction kills the sandwich

Tags: defi, mev, trading

Sandwich attacks are the tax nobody votes for. You submit a swap. A bot sees it in the mempool, buys before you, lets your trade push the price, and sells into your slip. You pay, the bot profits, the chain calls it a free market.

Every defense you've heard attacks a symptom. Private mempools hide the order. Encrypted intents hide the amount. Commit-reveal schemes hide both, at the cost of latency and a whole new ceremony. All of them still settle orders one at a time, in sequence, and sequence is exactly what the sandwich needs. Someone is always first and someone is always last, and the gap between them is the attack surface.

Batch auctions remove the sequence itself. Here is the mechanism. Orders accumulate for a fixed window, say one block. At the close, the auction computes a single uniform clearing price, typically the midpoint between the best bid and the best ask. Every matched order executes at that one price. Not at the price when you submitted, not at the price after the whale's order, at the single computed clearing price.

Now walk through the attack. The bot wants to buy before you and sell after you. But there is no "before you" and no "after you." All orders in the batch are peers at one price. The bot can join the batch, and joining means its order clears at the same midpoint as everyone else's. There is no position to exploit, because position no longer exists.

Buyers who bid above the clearing price pay the lower clearing price. Sellers who asked below it receive the higher clearing price. That difference is the surplus, and in well-designed batches it stays with the traders instead of leaking to block producers.

The tradeoff is honesty stated plainly: you give up instant execution for fair execution. Your order waits for the window to close. For anything that isn't a liquidation panic, that is usually a trade worth making, and the math of the sandwich dying is not a matter of bot sophistication. It's structural. You cannot ambush a queue that doesn't exist.

---

## C5 · Wrapped assets: the 1:1 promise, and every way it breaks

Tags: defi, bridges, security

Every bridge collapse of the last few years, and there were billions of dollars worth, shares one root cause. Not weak crypto. Not exotic exploits. The wrapped supply drifted from the locked collateral, and nobody noticed in time.

The promise of a wrapped asset is one sentence: for every W-something in circulation, one real something sits locked somewhere. The failure modes are all variations on breaking that sentence quietly.

Mode one: the custodian quietly rehypothecates. The locked assets back a loan, the loan backs another promise, and the wrap is now a fractional reserve wearing a 1:1 costume. Mode two: the bridge mints on a message it didn't fully verify. A replayed proof, a signature from a compromised validator, and new wrapped tokens exist with nothing behind them. Mode three: the drift-by-accounting. Fees, rounding, gas paid from the vault, small corrections that never hit the mint ledger. Each one tiny. The sum eventually large.

What survives scrutiny is boring, and that's the point. Supply equals locked, enforced in code rather than in audits. Every mint references a specific, public lock transaction. Every burn releases against a verified deposit. The coverage ratio capped below 100% so the system refuses to mint at the margin instead of trusting its own arithmetic. And a read-back loop that queries the chains themselves, because your own database will always tell you what you hoped.

If you hold wrapped anything today, here is the five-minute check. Find the wrapper's attestation page or its on-chain registry. Compare circulating supply against published reserves. Look for the date of the last proof, not the date of the last marketing post. If the project cannot answer "show me the lock for the coin I hold" with a transaction hash, you don't hold a wrapped asset. You hold an IOU with good graphic design.

---

## C6 · DPoS, PoS, and PoW: one honest comparison, no tribalism

Tags: blockchain, consensus, education

Ask three chain communities which consensus is best and you'll get three religions. Here's the comparison nobody's marketing department will print.

Proof of work buys security with energy. Attackers must out-spend the honest network in hardware and power, continuously, forever. It works, it's battle-tested, and the bill is enormous. Throughput stays low because every node re-verifies everything and block times are constrained by propagation physics. Bitcoin can settle finality slowly because its job is to be an anchor, not a highway.

Proof of stake replaces energy with capital. Validators lock tokens; misbehavior gets slashed. Security scales with the value at stake, which is elegant until you notice the feedback loop: the chain is secure because the token is valuable, and the token is valuable partly because the chain is secure. PoS also enables features PoW structurally cannot: delegation, on-chain governance, fast finality.

Delegated proof of stake compresses PoS further. Token holders elect a small set of block producers, twenty-one on Steem, twenty on Hive. Block times drop to three seconds, transactions get cheap enough to be free, and applications that would be unthinkable on Ethereum become routine. The cost, stated plainly: fewer producers means a smaller set to corrupt or DDoS, and cartel behavior is a documented historical fact, not a hypothetical. DPoS trades some censorship resistance for throughput that consumer apps can actually use.

The honest summary. PoW for storing value against adversaries with nation-state budgets. PoS for general-purpose settlement with economic finality. DPoS for applications where a three-second block and zero fees matter more than theoretical maximal decentralization: social networks, games, high-frequency attestation.

The real question isn't which is best. It's what you're building and what an attacker would profit from breaking. A chain that's over-engineered for its threat model is paying for security nobody needs. A chain that's under-engineered is a honeypot with good branding.
