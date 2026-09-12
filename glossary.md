# SAOS glossary: every scary word, translated into human

> The rule: when writing for a broad audience, use the "our language" column.
> The technical column exists only so professionals and journalists can find the original term when they search.

| The scary term | Our language | One-sentence explanation |
|---|---|---|
| Blockchain | Public ledger | A giant account book open to everyone, and no one can delete a line from it |
| State root / Merkle root | Mathematical fingerprint | A unique sequence of signs generated from all the data; change one comma and the fingerprint changes completely |
| Seal / Checkpoint | Signed snapshot | Every 36 seconds the system "photographs" everything and signs the photo |
| Anchor / Anchoring | Registration with witnesses | Sending the fingerprint to public ledgers so it cannot be altered later |
| Multi-chain / Cross-chain | Several registries | The same proof is recorded in several independent ledgers at the same time |
| Gas / Fee | Stamp duty | What you pay so a record enters the ledger; with us: agorot or free |
| Resource Credits (RC) | Included minutes bundle | On the Steem/Hive networks: a renewing allowance of free actions for whoever holds a balance |
| EIP-1559 / calldata | Envelope with a note | A way of sending information to Ethereum inside the transaction itself |
| SPL Memo | Note on the receipt | A cheap way to record a short message on a Solana transaction |
| Bit-encoding (TRON) | Message encoded in amounts | Encoding the proof in tiny transfer amounts so the net cost is zero |
| Wallet / Private key | Vault key | A secret that proves ownership; with us it never leaves the owner's machine |
| Self-custody | The keys stay with you | No one else, including us, can touch your assets |
| Threshold signatures (7/11) | Seven out of eleven | Releasing money requires seven different guardians to sign; stealing one key is not enough |
| Escrow | Money locked aside | Before a trade, both sides lock theirs; no one can run away midway |
| Order book | The order board | The list of all waiting buyers and sellers, open to everyone |
| AMM / Pool | Shared cash box | A pool of assets that allows trading without waiting for one specific counterparty |
| Wrapped asset | Backed wrapper | An asset from one network appearing on another network, backed one to one by a lock |
| Oracle | Price reporter | A service bringing information from the world into the system; ours: signed and honestly reporting failures |
| Circuit breaker | Electrical fuse | When something breaks in an external network, the system disconnects it temporarily instead of taking the risk |
| Fail-fast / HALT | Emergency stop | Accounting inconsistency? The system stops immediately and publishes the reason |
| Invariant | Iron rule | A condition that must always hold (for example: wrapped = locked); the code checks it on every action |
| Deterministic replay | A film you can rerun | Anyone running the same history reaches exactly the same result |
| Chaos testing | Breaking on purpose | Tests where connections are cut and data faked on purpose, to make sure the system survives |
| Audit | External check | An independent party examines the code; ours: the package is packed and waiting |
| Notarization | Notary stamp | Proof that "this thing existed on this date", without storing the content itself |
| Timestamping | Time stamp | Recording when something happened, so no one can claim otherwise later |
| Proof of existence | Proof of existence | "This file existed then", without exposing the file |
| Keyless | Without keys | A proof built from public data only, no secret involved |
| RPC | Service counter | The point where you ask a public network questions and read the ledger |
| Txid / Signature | Receipt number | The unique identifier of every record in the ledger, the link you are given to check |
| Explorer (Etherscan and similar) | The receipts site | A public site where anyone can see every receipt on every network |
| Gas model | Stamp duty calculator | An exact prediction of what a record will cost; ours is verified to the last digit |
| Batch / Merkle batching | Shared shipment | Thousands of proofs are collected into one seal, everyone shares the cost |
| Sovereign chain | Independent network | A system that runs itself and asks no one for permission |
| Shadow-L1 / Anchored chain | Network with witnesses | An independent network whose security comes from registering with public networks, not from paid validators |
| CoW batch (Coincidence of Wants) | Uniform-price batch settlement | All the orders in a block settle together at a single clearing price, there is no queue, so there is no sandwich |
| POL | Protocol-owned liquidity | The liquidity does not wait for someone external, it belongs to the system itself (100% at graduation) |
| ve(3,3) | The vote-and-reward model | You lock, you vote, you get a share of the fees, and the profits buy and burn |
| TWAP | Time-weighted average price | Not a single manipulable moment price, an average over time |
| HALT | Honest stop | Inconsistency detected? The chain stops in place and publishes the reason |
| Corroboration | Live confirmation from an independent component | A claim does not rely on a stored file; another component verifies it against a live source |
| AMBIGUOUS / canonicalRoot=null | Conflict flagged, no ruling | When there are two roots for the same height, it is marked "undecided" instead of arbitrarily picking the "right" one |
| Fleet / Soldiers | The autonomous crew | Autonomous agents operating the system 24/7, with a public performance report |
| Refuse counters | Refusal counters | Publishing how many transactions the system refused to execute, the opposite of boasting |
| Zero-mock | No fakes in tests | Internal rule: tests must not simulate success; either truth or a visible failure |

## How to use this in writing

1. Write the sentence with the human term.
2. If the technical term is required (for a professional audience or the press), add it in parentheses once only: "mathematical fingerprint (state root)".
3. Never start a sentence with a technical term.
4. If a term does not appear here, it probably does not belong in text for a broad audience.
