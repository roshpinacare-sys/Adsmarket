# SAOS ecosystem map: the complete map of what actually exists

> Written after a deep scan of all 10 repos (2026-09-08). This is the framing document for all marketing.
> Sources: saos-strategy.md · saos-breakthroughs.md · saos-capabilities.md (Saosmartwallet) · JUMPPER README+FREE-OPERATIONS · foundry BREAKTHROUGH.md · saos-dex WORKLOGs · platform README v13.

## The central reform: SAOS is the product. The 7 networks are the footprint.

Until today the world (and we too) described SAOS through its host chains: "a DEX on Steem", "a relay to Ethereum". The full scan proved the real architecture is the opposite:

| Layer | What it is | Components |
|---|---|---|
| **Core** | SAOS-NET, a sovereign deterministic state machine | Height 74,907+ (measured 2026-09-09 05:00Z) · 1,507+ verified txs · persistent stateRoot |
| **Notary** | The multi-chain anchoring layer | Steem/Hive/Blurt (free RC) · TRON (zero-fee bit-encoding) · Ethereum (calldata) · Solana (memo) · the atomic clock (6 networks, keyless, $0) |
| **Economic engine** | grid98 + DEX + the wrap economy | 32,603 tx/s measured (real archive replay) · 14 pools · 20 wrapped assets supply==locked · public refuse counters |
| **Workforce** | Autonomous fleet | 13 soldiers live on Steem (13/13 verified) · 23 self-running operation loops · per-soldier PnL measured |
| **Products** | What the user meets | **Identity Verification API + SDK saos-id-verify, the first product, live and metered, ready for commercialization (SDK publication and public gateway are owner actions in progress)** · Saosmartwallet (7 networks, M0-M4) · JUMPPER (batch notary) · the institutional DEX terminal |

## The key marketing sentence (from JUMPPER: the strongest in the whole ecosystem)

> **"Every agent can claim anything. Only a public chain cannot lie."**
> Any agent can claim anything. Only a public chain cannot lie.
> JUMPPER makes lying expensive: anchor a claim for a fraction of a cent, and from that moment it cannot be rewritten, denied, or faked.

## The five non-obvious breakthroughs (with an honest limit for each)

1. **Cross-paradigm identity**, the same secp256k1 scalar is the active authority in Steem+Hive+Blurt and also an EVM address; any third party runs ecrecover and links them mathematically, without the key ever being exposed. Target market: millions of veteran Steem/Hive accounts that no EVM wallet knows how to serve.
   *Honest limit: proves control; not yet wired into an automatic login/recovery product.*
2. **An anchored shadow-L1**, a sovereign chain whose security is "rented" from host chains at a cost of about zero: instead of paying validators millions, every checkpoint is signed in a free custom_json and in zero-fee bit-encoding on TRON (6-address ring, Nobel-grade plumbing).
   *Honest limit: finality is inherited from the hosts; there is no independent token economy yet.*
3. **grid98, a market where profitability is enforced structurally and the refuse counters are the proof**, no other product publishes the transactions it refused to execute. Ours: 383,836 edge skips · 130,499 rejections · 109,919µ of measured and settled slippage, alongside 5,606 transactions and 9,935,250µ PnL to the treasury.
   *Honest limit: the mechanism ceiling (32,603 tx/s) was measured; the live trading rate is budget limited (dust-scale).*
4. **A 1:1 wrap economy with measured locks**, every bridge collapse in the industry (>2B$) came from supply drifting away from the backing. Ours: supply==locked is an invariant enforced in code: 20 wrapped assets, every mint cites the txid of a public lock, mint-coverage ≤99% is enforced.
   *Honest limit: the total locked value is small today (hundreds of dollars); the ETH/SOL rails to the contracts await deployment.*
5. **The system that documents itself honestly**, every operational claim ships with a verification handle (txid, counter, endpoint). Including public corrections against the owner's own claims. zero-mock enforced as an invariant.
   *Honest limit: external credibility (a third-party audit) is still ahead of us.*

## Audience × value proposition (from saos-strategy.md)

| Audience | The sentence |
|---|---|
| **Steem/Hive veterans** | "Your identity and your coins finally enter Ethereum, Solana and Bitcoin, and come back home, without giving up your keys." |
| **The agent economy (AI/Agents)** | JUMPPER: any agent can claim anything; only a public chain cannot lie. A permanent notary record at $0.0000081 per claim (batch of 10,000). |
| **Organizations/auditors/regulators** | A timestamp with 6 independent consensus groups, $0, keyless; an automated treasury with every refusal in the records; wrap solvency as an invariant, not as an audit finding. |
| **DeFi/bridge users** | "The bridge that is provably solvent in advance", exactly what every bridge audit looks for, already built in. |

## New proof assets that were not in the previous kit

- **JUMPPER**: a gas model that predicted a real mainnet transaction **to the wei** (30,920 gas · 32,493,358,294,280 wei · block 25,929,672) including the EIP-7623 correction; 77/77 tests green from a fresh clone; compression 250B to 51B (-79.6%); a free HIVE floor of 5,128 anchors per day (measured: 21 live anchors in 22 hours).
- **The atomic clock (Foundry)**: the heads of 6 heterogeneous networks resolved into one 32B Merkle root, keyless, $0.00, 15.9ms compute, 6.8ms verification, a 435B proof. Documented run: root 0896c3c6... with 5 witnesses (STEEM #109,307,680 · HIVE #109,722,158 · TRON #86,063,739 · ETH #25,929,640 · SOL #445,219,905).
- **The HIVE honesty fix**: the "RC block" was a stale-read bug, the account held 73.2M effective RC (52.6 times the old read). 21 live anchors verified on mainnet. This is marketing material on its own: we found a mistake that hurt us and published it.
- **TRON live at zero fee**: cp#33612 → txid 1db5006b... @ block 86,019,974 · 6/6 ring addresses measured.
- **13/13 soldiers live** on Steem (get_accounts verified 2026-09-08) · per-soldier PnL (wog leads with +163,295µ) · 23 autonomous loops under one beat.lock.
- **A signed hourly oracle**: 15 live quotes with src+ref+at · honest skips on network failure (no invented price).

## v2 update (2026-09-08 23:30Z): Model 1 enters execution

- **Week 1 shipped:** the Identity Verification API, metered (SHA-256-only keys, quota 1,000/day, full ledger)
- **Week 2 shipped:** the official SDK saos-id-verify, zero dependencies, dogfooded 3/3 live paths
- **Week 3 ready:** an outreach kit with 10 real verified targets (Splinterlands, MEXC, Gate, SimpleSwap, PeakD...)
- **Security as proven capability:** on-chain key rotation demonstrated with public receipts · the "keys never in the repo" doctrine · THE-GATE · a multi-home vault
