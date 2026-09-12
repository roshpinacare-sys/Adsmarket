# Press Kit: SAOS · Kit for Press and Researchers

> Updated 2026-09-08 · every fact here is backed by fact-sheet.md with verification links.
> Policy: we answer every question, including the hostile ones. We send the mistakes journal before being asked.

---

## Boilerplate: Hebrew (for copy)

SAOS is a sovereign fact-proving infrastructure: a system that anchors every event, every state seal, every claim, every refusal, in independent public ledgers (Steem, Hive, Ethereum, Solana, TRON), so that any third party can verify it independently and for free. The system operates as a deterministic state machine (74,907+ blocks as of 2026-09-09 05:00Z), anchors proofs at a cost of zero to a fraction of an agora (batch recording: $0.0000081 per record, measured), and also publishes what it refused to do, including public corrections of its own mistakes. Its products: a multi-network wallet (7 networks), a batch proof notary (JUMPPER), a keyless multi-network atomic clock, and an internal exchange with code-enforced honesty rules.

## Boilerplate: English (for copy)

SAOS is a sovereign proof infrastructure: a deterministic state machine (74,907+ blocks at last audit, 2026-09-09) that anchors every state seal, claim and refusal to independent public ledgers (Steem, Hive, Ethereum, Solana, TRON), making every operational claim independently verifiable for free. Batch notarization costs $0.0000081 per record (measured on mainnet); its keyless Atomic Clock binds six heterogeneous networks into a single 32-byte root in under 16 ms at zero cost. SAOS publishes its own refusals (383,836 skipped trades) and its own corrections, honesty enforced as a code invariant, not a slogan.

## Headline numbers (verified)

| Number | What it is | Where to verify |
|---|---|---|
| $0.0000081 | Fixed notary recording cost (a batch of 10K) | docs/ECONOMICS in saos-jummper + a mainnet transaction |
| 32,603 tx/s | Engine throughput, measured in a replay of 65,238 real transactions | grid98-state |
| 15.9 ms | The atomic clock computation (6 networks → one root) | a documented run, foundry BREAKTHROUGH.md |
| 383,836 | Transactions the system refused to execute, and published | the live grid98 counters |
| 0 | Inaccuracies in hundreds of read-back verifications against public RPC | the relay journals |
| 52.6× | The size of our reporting error on HIVE, published and publicly corrected | FREE-OPERATIONS.md |
| Zero-dependency SDK | The first developer product: `saos-id-verify`, cross-network identity proof in one call, PROVEN live against block 109,389,994 · the package is live in the repo; publishing to npm = an owner action in progress | packages/saos-id-verify |
| 36s | Self-recovery from a kernel OOM kill, zero human touch, a full append-only journal | v26 SHOMER, live measurement 23:58→23:59 |
| 9/9 | Authorization attack vectors blocked live (phishing, a foreign target, crossing authorities, a burst) | v25 RESHUT self-test from the UI |
| 9/10 | Anchor-fleet soldiers verified live on Hive (multi-account anchoring) | SETTLE-13 |
| 153 → 8 | Our real anchor transactions scanned by forkwatch → 8 contradictory heights on HIVE, published voluntarily · root: a per-process counter · structural fix: an epoch namespace · 24 assertions on the real fork | JUMPPER forkwatch + ONCHAIN-FORKS |
| $0.40 | Measurement update (09-12): the official gas request broadcast to 11/11 repos + issue 003 (owner-action): ~$0.40 lights 6 dark EVM doors (BSC · POL · Arbitrum · AVAX · xDAI · SKALE) · it was $0.94 for 7 doors at v52, the gas has cooled · the scanner measures every 60 seconds and fires on its own when funded | platform v78 THE ETH CALL |
| 23 assertions | Our own solvency tool refuses our own data: a real value_lock rejected (4 critical) after fixing an attest() that checked only one field | JUMPPER attestation |
| 5/5 | Mainnet anchors of all funded networks verified read-only directly from the chains: ETH block 25,944,802 · BSC 121,011,726 · SOL slot 445,822,974 · TRON 86,124,584 · XRPL 106,890,679, the "anchor wall" | platform v50 |
| 2 roots · 5 networks | 6097f929… engraved on ETH/BSC/SOL · 39575b3b… on TRON/XRPL, one key, full cross-verification | v49-v50 |
| #12 | The first anchor signed with an identity restored independently from a single root, Ethereum mainnet block 25,983,946 · stateRoot verified · the XRP gap honestly marked declared-not-verified | platform v53 THE SEED |
| The Tower | Our own Ethereum block explorer, where the sovereign anchor is verified and visible, the proof loop closes without a third party (E2E across 3 flows + screenshots) | steem R18/R19 |
| ~250 | Additional free broadcasts, RC capacity measured after MEGAPHONE's first live receipt (Steem block 109,496,567 · rc_cost 1,358,232,384 against a balance of 339,603,439,104) | JUMPPER MEGAPHONE |
| 5-7× | Full work cycles: 244-336s → 32.9-47.2s (a three-legged receipt race, 21 live rescues in the first cycle, a 408ms median) · GET shifts from 10.5s → 2.29 cold / 15ms warm | platform v59 |
| 9s → 2.52s | The health check that impersonated healthy, a parallel route + stale-while-revalidate with the honesty flag refreshing:true · forced: 4.81s with 5/5 truth rails | platform v60 |
| digest 1 · 2 chains | A double live anchor: STEEM block 109,471,513 (tx d43ed97d…) + BLURT block 63,534,293 (tx 2aa81fbc…) · HIVE refused honestly on RC (106M against ~385M) with a new pre-check | wallet r20 ANCHOR PLANE |
| 0 collisions | epochguard, fork prevention instead of reporting: on the real 15-height sequence, 15 unique (epoch,height) pairs versus 2 collisions without it · the arc is complete: measure → publish → prevent | JUMPPER epochguard |
| 46ed2f58 | The txid of the first live conversion on the HIVE rail (agent-swap + rail-exec with an RC rate) · the fleet 11/11 · RC economics balanced | Task 73 |
| 831 bytes · 17 roots | All 8 forked heights and their 17 roots encoded into one correction anchor, ready to sign (zero fee, POSTING authority), 10.1% of the free 8192 budget, a single feeless custom_json, published exactly where the forks live · the system refuses to declare canonical without evidence and rejects an invented root · 24 assertions · the original anchors stay readable | JUMPPER remedy |
| 31 modules | The harness extends itself: a new module that arrived without coverage declared itself RED until a test was registered for it | JUMPPER harness |
| 8 gates | net_health.cjs, a sovereign network-health verifier across eight gates · a paymaster that stood up to testing | steem R18e-4 |
| 30,032 → 0 | Phantom compile errors in a 426,719-line log, a 20.5-hour-old process compiled a stale bundle; a clean restart → zero recurrence, measured | foundry roast(72) |
| 4 → 1 | A service that loaded four different versions of itself on four endpoints, a single SIGNER_VERSION constant now feeds every surface, measured uniform · the derived-or-silence principle | roast(72) |
| 69 | Incomplete runs went through forensics → the detached-spawn doctrine: the fleet's lifetime does not depend on the operator's session · the estate grew from 8 to 12 repos · expansion candidates live-verified (SKALE with free gas · NOSTR · Vara) | wallet r18 + platform v58 |
| 687 → 0 | Files monitored in the sovereign secrets scan (cross-checking the vault against live public data) → 0 real holes · a double gate verified | steem R18e |
| derived-or-silence | An enforced interface principle: every claim is derived from live data or not shown · audit 71 caught a "version lie" (a commit declared 2.4.5, the code served 2.4.4) and frozen text, all fixed and published | foundry roast(71) |
| oracle in consensus | The canonical price oracle is included in the stateRoot itself, the price is signed and anchored with every seal · the coin door: WTRX/WSOL deposit-backed + a live market/redemption | Task 72 THE-COIN-DOOR |
| 1481s → 238s | A full work cycle: 31 silent waiting gates found in the source code and closed with a 15s deadline · two consecutive cycles measured live (285.1s + 238.1s) · no hardware upgrade | platform v56 PACE ENGINE |
| 10/10 | All assets sovereign-routable · atomic conversion (no stranded intermediate assets) · exact-to-quote settlement measured live (STEEM→USDS 2268µ) · the treasury opened 3 pools through a zero-gas channel | DEX roast-71 |
| 6/6 | All rails cut in the chaos suite (upgraded from 3) · honest A6 evidence · a preflight leak sealed | DEX Roast-69 |
| 30/30 | JUMPPER tests calibrated against the real APIs (introspection) after it turned out some had been testing "remembered APIs", the banner was removed only when everything passed | JUMPPER harness calibration |
| 88ms · p50 | A sovereign SOL↔TRX conversion circuit proven live: 5 runs · 65/65 atomic legs (both legs in the same block) · versus 10-90 minutes under third-party custody, the money does not move, the mirror is 1:1 | platform v53 the conversion room |
| ~1.6 TRX | A phantom gap silently accumulated from anchor gas, found and honestly burned pro-rata (supply==locked enforced against ourselves too) | v53 mirror-sync |
| 8 / 162 | Real anchors on HIVE scanned: 8 forked heights published in an open census (forks.json) + a machine-readable remediation record · every forked height = AMBIGUOUS, canonicalRoot=null, no root declared without evidence | JUMPPER heightguard |
| 0 exposed | The error contract enforced: zero raw 500s across every surface, every throw lands as 200 {ok:false, coarseError} · UI "failure-as-success" bugs fixed | foundry roast(63) |
| h20808 | The first live HALT of the fail-fast invariants: a phantom LP caught (a drift of -4,448µ) · the root found and fixed within hours · an honest drift declaration published, the safety net proven in production | saos-dex roast-66 |
| 5/5 ok=true | The realMoney flag fixed after being structurally false (two conflicting critics), live on every rail · an amount-verification hole in the SOL bridge closed fail-closed | roast-66 |
| 0 gas | wrap_mint/wrap_burn dropped from 250 to 0 (bridge rails = protocol rails) + an auto-claim keeper (ZFB) · live pool yields transparent: 651/1454bps · POL 15%/24% | roast-66 |
| 535 | Real mainnet transactions checked against TRON's own protobuf encoder before the first broadcast · and a published cost model, refuted and published (0.6 predicted → 2.1 measured) | v49 |
| @130,000 | A planned fork executed cleanly: 4 economic kernel bugs fixed + anti-poison/fork guards · the chain runs at 133,259+ | steem 117p8-R8 |
| 40+ | Truth gaps closed with live proofs in a single day of ecosystem self-audit (19 foundry + 21 wallet) · including a split-view audit of our own history, published voluntarily | roast(53-56) · ROAST r4/r5 · ONCHAIN-ROAST |
| seed 1 → 5 | EVM+SOL+TRON+BTC/XRP reconstructed exactly from 24 words (every derivation live-verified) · a first SOL mainnet anchor: 5z46xVFc… slot 445,822,974 | platform v47 |
| 0.5% | The cost of moving dust as a percent of the dust itself, after the "gas costs more than the value" blocker dissolved against a live measurement (0.068 gwei). ETH+BNB swept to the treasury home: tx 0x6ef5f0… / 0xa8e43d…, the source addresses emptied to 0 | v30 TIZUZA |
| 4× tesSUCCESS | Live heartbeats on XRPL, an AccountSet with an engraved Hebrew memo, sequence 57785945→47, verified in the browser (a UI button → real transaction 57785947) | v30 |
| BURN-SYNC | Wrapped supply follows gas actually burned (WRXP -0.000035 · WBNB -0.0000013), the 1:1 invariant pinned in both directions | v30 |
| 5s | Measured self-healing by the supervisor for every service death · and a new corroboration layer: every claim requires live confirmation from an independent component, never from a frozen file (the 39-hour lesson) | roast(61)/r8/65 |
| double broadcast prevented | A request-id bug caught in audit: a retry would have broadcast the same transaction twice, fixed with a deterministic requestId + a structural rejection classification (never an automatic retry on 400/403/429) | roast(61) THE MONEY ONE |
| 470 hex | Bit-exact verification against the node's own serializer before the first broadcast · and the fleet builds daily: an autonomous post+vote with chain evidence (post: tx c64766e7… @ block 109,443,160 · vote: tx 048b3162…), posting authority only, which the network protocol cannot use to move funds | SOVEREIGN-VOICE |
| structurally sandwich-immune | Uniform per-block CoW settlement: one clearing price, the surplus to the traders, no queue to attack · live-verified pro-rata | DEX Task 58 |
| @h772 | A live launchpad graduation: born on a bonding curve → an AMM pool with 100% POL | DEX Task 58 |
| +50,468µ | Measured real profit of ProtoRev (end-of-block two-sided arbitrage, an atomic batch) | DEX Task 58 @h871 |
| create+cancel | SOVEREIGN-HAND E2E: the agent builds, the vault signs through the gate, tx 5798c77c… (block 109,441,448) + cancellation tx 085916fa… (109,441,504), verified against a public node | wallet E2E evidence |
| 40% | Of profits bought back and burned every 600 blocks, deterministic code in consensus, capped by measured profit (ve(3,3) + bonds at a 3% discount + dynamic fees 4-1500bps) | DEX Task 54, economyTick live |
| 63,502,020 | The BLURT block of the first live anchor (anchor-pulse: seal→sign→broadcast→verify, a fee of 0.129 BLURT) | foundry Task 40 |
| ×3 | Full self-restore from the vault after an environment rebuild, proven three times · the build-loss window from ~30 minutes to about a minute | platform v33-v35 |
| 9→15 | Network capabilities wired into the autonomous agents · an honest limits audit: 9 limits, 4 fixed, 3 intentionally capped, 2 documented | wallet SOVEREIGN-EYES + LIMITS-AUDIT |
| escalation-only | Risk classification: a reader can raise an action level, never lower it (32 bidirectional assertions) | JUMPPER riskgate |
| 7/7 | Consecutive accurate gas predictions on live Ethereum anchors (32,680 gas each), a model that calibrated itself to the wei | wallet anchors #4-#6, tx 0x4f27c008… blk 25,937,568 |
| +459%→+24.7% | A premium restrained by a sovereign TWAP micro-rail, 16 measured doses, net +133kµ | SETTLE-16 |
| 72+ | Real trades on the sovereign exchange live on our own network (v28 BIRSA) · an arb proof: WETH sold at a 5.04% deviation against a live oracle · a harvest to payroll with a tx | platform v28, tx 0xbaf0771a… browser-verified |
| 66 | Broadcast-capable daemons, all dry-by-default (LIVE-GATE) · going live = a double conscious arming | security(28-b), a shared live_gate |
| $258.46 | The published cornerstone treasury map (including STEEM SP; a separate scope from the v29 live radar: 16 assets, $61.37), radical transparency as brand policy | v28 cornerstone panel |

## Sample receipts (to hand journalists as links)

- Ethereum: etherscan.io/tx/0x102ec1935be6cb3ff3acc20189a85377cf57486515f3121472c6611b20e0ef41
- Solana: solscan.com/tx/2M1rkRggRcaePk6vMZpgSaM3WVWQU92RZAs1v7PtNeMLsxLmZoqBNCeEtuY7Rkj5aPbs4jS1g2wUQXCnoejUM2M9
- Steem: steemworld.org/tx/390bcfc2586def1ef02cc40a0e983c8dd8fce177
- Hive: hiveblocks.com/tx/d4cf936b0b5e1eff8dcc8a508532f67c95682bd5
- TRON (block): tronscan.org/#/block/86019974

## Visual assets

- Logo/cover for sharing: `assets/og-cover.png` (a golden hexagon seal + a Merkle tree + "SAOS· PROOF OVER PROMISES")
- Color palette: background #09090b · gold #d4af37 · system purple #a78bfa · live green #22c55e
- Typography: numbers and codes always in monospace; clean sans headings; zero emoji in any official material

## Hard questions: our ready answers

**"Do you promise returns?"** No, and we never have. Anyone promising returns in our name is impersonating us.
**"Have you had an external audit?"** Not yet. The audit package (code byte-identical to production + a MANIFEST) is packaged and waiting; we will publish the findings when they arrive, including if they are harsh.
**"What happens if you disappear tomorrow?"** Everything already recorded stays recorded in the public ledgers. The proofs do not depend on our existence.
**"Why not just use Chainlink?"** Because they ask for trust in a committee plus gas; we publish data anyone can read on their own, keyless and free. The difference is philosophy, not price.
**"Your numbers sound too good"** True, which is why every one of them is backed by links. If a single link fails, our whole building falls, and that is exactly the idea.
**"How do you protect the keys?"** Defense-in-depth as architecture, not as a wall: keys never touch the repo, the code, the files, or the git history (verified scans on every push, history checked clean) · THE-GATE: login verified against the chain itself (paste → on-chain verification → vault-first) · an encrypted multi-home vault, three homes, mirrored, self-healing, 144/144 recovered (v31) · fund release at a 7/11 threshold (EIP-712) · fail-closed authorization gates on 10 sensitive operations, 9/9 red vectors blocked live (RESHUT) · an anti-phishing gate on every outbound link (MAGEN) · an isolated external sealer for broadcasts. Zero secrets in any push, ever. Internal policy: security incidents are handled and documented internally; externally, the architecture is what we show.
**"Has your system ever crashed?"** Yes. On 2026-09-08 23:58 the kernel killed the web layer (OOM, 1.79GB/4GB, proven in dmesg). The keeper we added revived it within ~36 seconds, without a human touch, with a full trail in an append-only journal. There is also mutual watchdogging (the runner revives the keeper, proven live) and a zombie detector ("a live process is not truth, block progress is the truth"). The full incident story is shown in the "Keeper" view in the terminal, including the incident itself.
**"Is there a product one can buy/install today?"** The product is live and proven end to end inside the system: an Identity Verification API + a zero-dependency SDK, metered with a daily quota and a full ledger. For full external availability, two owner actions remain in progress: publishing the package to npm and opening a public gateway. We draw a loud line between internal and external availability; that is our disclosure policy.

## Quoting rules

- You may quote any number from the table above together with its link.
- Please do not call SAOS a "coin", an "investment" or a "bridge"; it is proof infrastructure; wrapped assets exist inside it as a component, not as an essence.
- Please state that the system is in development and that some rails await deployment/funding; that honesty is part of the brand.
