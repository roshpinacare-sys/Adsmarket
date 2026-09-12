# SAOS FAQ v2: human questions, human answers

> Updated 2026-09-08 after a full scan: HIVE and TRON statuses corrected against live measurements, and "what does this mean for me" questions added.
> Principle: no answer dodges. If something does not work yet, we write it exactly as it is.

---

## The basics

**Q: Wait, what is SAOS in one line?**
A: A system where everything that happens in it gets a public receipt that cannot be deleted. Instead of "trust me", "check me".

**Q: Is this yet another crypto coin?**
A: No. SAOS is infrastructure, like a road, not like a car. It has economic components (trading fees, wrapped assets), but the product itself is a proof layer: records, timestamps, verification. If someone sells you a "SAOS coin", they are not from us and were never given any authority by us.

**Q: Why would I even need this?**
A: Because almost everything you do online rests on blind trust: that the product was shipped, that the file was not altered, that the bot really executed. SAOS gives each of these a receipt. You do not have to use it directly, but every service you rely on can use it, and then you can check that service yourself.

**Q: Is it complicated? I am not technical.**
A: To use it, no more than sending an email. To understand it in depth, we have an 8-scene animated explainer that requires no prior knowledge (content/explainer/index.html). If after two minutes there something is still unclear, that is our problem, not yours.

---

## Money and free

**Q: Wait, if recording is free, what is the catch?**
A: There is no catch, there is physics. Some networks (Steem, Hive) work on a "staked resources" model: whoever holds a balance on the network gets a renewing allowance of free actions, like a mobile plan with included minutes. We hold such a balance, so our records there are free. On other networks (Ethereum, Solana) every record costs agorot, and the real price is measured: less than a hundredth of an agora per record in batch.

**Q: So why can't someone flood the system with free garbage?**
A: Because the "free" is limited by an allowance that renews slowly, and the allowance is tied to a real balance on the network. To flood means to hold a lot of balance, which means to invest a lot of real money. That is exactly what makes spam expensive and proofs cheap.

**Q: What about my document? Do you keep it on your side?**
A: No. The system never sees your document. It receives only a mathematical "fingerprint", a sequence of signs from which the content cannot be reconstructed, but which also cannot be faked. Your privacy stays with you; the proof goes to the public ledger.

**Q: Do you promise returns? Profits?**
A: No. Never. Anyone promising returns in crypto is either lying or risking your money. SAOS earns from real trading fees, and that is all. If you see someone promising "profits from SAOS", that is not us.

---

**Q: You have a live exchange? Really?**
A: Yes, and the numbers are published without filters. The sovereign exchange (v28) is live on our network: 72+ real transactions (snapshot of 09.09), an arbitrage bot that reacts to deviations against a live oracle (proof: a WETH sale at a 5.04% deviation), and harvest flowing to real payroll with receipts. And yes, we publish the TVL too: $13.91. Tiny? Absolutely. The mechanism is proven in real trading; scale is a budget gate, not a technology gate. Anyone publishing TVL in the millions without a measurement mechanism should explain themselves. We prefer the opposite direction.

**Q: Has the system actually earned anything real?**
A: Yes, on a dust scale, and we publish that too: the sovereign micro-rail tamed an extreme price premium (+459% down to +24.7%) across 16 measured TWAP batches, with a net result of +133kµ. The treasury accumulated 9,935,250µ over time, and every refusal (383,836 of them) is documented alongside the profits. We do not tell "passive income" stories; we show a mechanism that works, measures, and publishes.

**Q: Is there something you can actually use today?**
A: Yes, our first product is live and proven inside the system: an identity verification API. One question ("does this Steem/Hive account and this EVM address belong to the same person?"), a mathematical answer read from the chain itself. Developers have an official SDK with zero dependencies (saos-id-verify); the code lives in the repo and is verified end to end; the npm publication and the public gateway are owner actions in progress, and anyone running an instance of the system already uses it today. The measurement is transparent: a daily call quota, a record of every call, and even a negative answer is a real result that gets counted, not an error that gets hidden. What is still ahead: publishing the SDK to the official npm store and opening a public gateway; those are owner actions, and they are in progress.

## The real status (yes, including what does not work yet)

**Q: Which networks actually work right now?**
A: As of the last scan: **Ethereum, Solana, Steem, fully live** (anchoring in every seal). **Hive, live in RC pulses**: 21 real anchors verified in 22 hours (measured 09.09 00:29Z) (we once reported it as "blocked", that was our own read error, we published and corrected it). **TRON, live at zero fee** on the ecosystem rail (bit-encoding on an address ring), and its DEX rail is armed and waiting for tiny funding. **Blurt, a historical anchor**, waiting for the fleet's gate to open. All of these statuses are updated by measurements, not declarations.

**Q: What still does not work?**
A: Gladly: the bridge contracts to Ethereum and the Solana software are ready in code but not deployed to mainnet (that is an owner budget decision, not a technical limit); the identity login/recovery product is being built; the SAOS-NET token economy is not yet defined in an official document; and an external security audit has not been done yet, the package is packed and waiting. We prefer "not yet" over "soon".

**Q: What happens if the system crashes?**
A: It is designed to stop honestly, not to crash quietly: if an accounting inconsistency is detected, the system halts and publishes the reason. And what it already recorded stays recorded in the public ledgers; those cannot be deleted even if all our computers disappear tomorrow.

**Q: Who already uses this? Do you have users?**
A: The honest answer: the first users are our 13 autonomous agents and the internal economy, and that is exactly the planned dogfooding stage. Everything they do (trading, anchoring, conversions, publishing) is measured and proven publicly, so one real user with us is more transparent than "ten thousand users" in a project that reports numbers without receipts. External users will arrive through the two documented bottlenecks: the SDK and gateway release (owner actions in progress) and the gas budget that opens 7 more EVM doors for 94 cents. We do not invent a community that does not exist.

**Q: Who is behind this anyway?**
A: A small team with a fleet of 13 autonomous agents and 23 operation loops running 24/7. We do not hide behind "an anonymous community": the operations journal is open, mistakes included. And in any case, you do not need to trust us, only the ledgers.

---

## Trust and scrutiny

**Q: How do I know you are not faking your numbers?**
A: Because the important numbers are not held by us. They sit in public ledgers anyone can read: open the receipt on Etherscan, on Solscan, on Steemworld, and you will see the same data we quote. If tomorrow we change something retroactively, the signed snapshots will not match and everyone will see it.

**Q: I heard crypto bridges got hacked for billions. What stops you from being next?**
A: Two things. First, we are not a bridge in the usual sense: there is no "vault on one side holding everything", there are proof records. Second, where wrapped assets do exist, the iron rule is supply==locked enforced as a code invariant: not a single unit can be minted beyond what is locked, and the locks are cited in public receipts. That is exactly what every bridge audit demands; with us it is built in from the start.

**Q: What is the difference between you and Chainlink or LayerZero?**
A: They ask you to trust a signed committee of verifiers (and to pay its gas). We do not sign anything for you: we publish public data that everyone reads and verifies on their own, with no keys and no fees. Our atomic clock ties 6 networks to one root in 16 thousandths of a second, at zero cost, without anyone having to believe us.

**Q: I am a journalist or a researcher. How do I verify you without reading code?**
A: Three quick ways: (1) open three random receipts from the fact-sheet in the public explorers; (2) compare the same stateRoot that appears on two different networks, it must be identical bit for bit; (3) ask us for the mistakes log. If we send it to you gladly, that is a good sign.

---

*SAOS is a technology infrastructure in development. The FAQ contains no investment advice and no promise of returns.*
