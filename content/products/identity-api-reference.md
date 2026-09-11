# Identity Verification API: reference & integration guide

Status: live and metered inside the sovereign platform. Public gateway and npm registry publication are pending owner actions; until then the SDK installs from the repository (dist + README included, build green). This document is written so an integration engineer can ship against it in under an hour.

---

## What it answers

One question, one mathematical answer:

> Does the Steem/Hive account `@username` belong to the same secp256k1 key as a given EVM address?

The proof is read from the chains themselves, not from our database:

1. The user's identity anchor (`saos.id.v1` custom_json) is fetched from the chain. The user published it once, with their own active key.
2. The EIP-191 signature inside it is recovered (ecrecover) to an elliptic-curve point.
3. That point is matched against the LIVE active authority of the account on Steem and Hive, and against the claimed EVM address derivation.

All three must agree. The answer is PROVEN with evidence, or FAILED with the reason. A negative answer is an honest metered result, not an error.

## Endpoint

```
POST {baseUrl}/api/v1/identity/verify
Authorization: Bearer <apiKey>
Content-Type: application/json

{ "username": "headcorner" }
```

`baseUrl` is mandatory by design: the SDK refuses to invent an endpoint. Keys are stored server-side as SHA-256 only; the plaintext is shown exactly once at creation.

## Responses

| Outcome | Meaning | Counted in quota |
|---|---|---|
| `PROVEN` | Full chain of proof: anchor found, signature recovered, live authority matched on each chain | yes |
| `FAILED` | Real work performed, honest negative (no anchor, no active key, mismatch). Includes the reason | yes |
| 401 `SaosAuthError` | Missing, invalid, or revoked API key. Fail-closed | no |
| 429 `SaosQuotaError` | Daily quota exhausted (1,000 calls per UTC day). `retryAt` = next midnight UTC | no |

Every response carries metering transparency: `{ used, limit, remaining, resetAt }` plus headers and measured latency. Each call is written to an append-only ledger.

Response shape (success):

```json
{
  "ok": true,
  "meta": { "outcome": "PROVEN", "latencyMs": 812, "used": 41, "limit": 1000, "remaining": 959, "resetAt": "..." },
  "anchor": { "block": 109389994, "txid": "...", "explorer": "https://steemworld.org/tx/..." },
  "chains": { "steem": { "matched": true }, "hive": { "matched": true } },
  "evm": { "address": "0x..." }
}
```

## SDK (zero dependencies)

```bash
# until npm publication (owner action in progress): install from the repo
npm i saos-id-verify        # activates on registry publication
```

```ts
import { verifyIdentity } from "saos-id-verify";

const r = await verifyIdentity({
  baseUrl: process.env.SAOS_BASE_URL!,
  apiKey: process.env.SAOS_API_KEY!,
  username: "someaccount",
});

if (r.ok && r.meta.outcome === "PROVEN") {
  // r.anchor.block, r.anchor.explorer, r.chains, r.evm.address
} else {
  // FAILED is a real answer: handle it, don't retry blindly
}
```

Runs on Node 18+, Bun, Deno, browsers, and edge runtimes. Plain fetch, no polyfills. Live-proven end to end (PROVEN vs Steem block 109,389,994; the FAILED path metered as real work; 401 fail-closed verified). The 429 branch is coded to spec; burning it live would cost a real 1,000 calls, so it stays lab-verified until organic traffic reaches it.

## Integration patterns

### Exchange: attributing Graphene deposits
On each inbound STEEM/HIVE transfer with a memo, call verify on the sender account. PROVEN binds the deposit to an EVM address the user controls; credit accordingly. FAILED routes to manual review. No custody of user keys at any point.

### Game: sybil resistance
Require a PROVEN result linking the game wallet to a Steem/Hive account with real history (account age and reputation come free with the anchor). One human, many alts, collapses: each alt needs its own aged chain identity.

### Frontend: "prove you are @account"
One-click proof for community apps, airdrops, governance snapshots. The user signs nothing new at verification time; the anchor was published once, and every verifier re-reads it from the chain.

## Operational notes

- Rate budget: design for the quota. Batch verification jobs should queue, not burst; on 429 read `retryAt` and back off to it.
- Caching: anchors are immutable chain data. Cache PROVEN results keyed by (username, anchor.block). Re-verify on authority changes if your risk model needs it (the API always reads live authorities, so a fresh call reflects chain state).
- Privacy: the API never asks for, receives, or stores private keys. Neither should your integration. If a user offers you a key "to verify," that is a red flag on their side and a liability on yours.
- Honesty contract: FAILED is metered because real chain reads happened. We do not hide negatives or fake positives; design your UX for both outcomes.

## What this is NOT

Not a login session manager (yet; automated login/recovery is on the documented roadmap). Not a funds-movement API. Not a KYC provider: it proves key control, nothing about real-world identity. Not published to npm at the time of writing; the registry install line activates the moment the owner publishes, and this document will say so.

---

*Every claim above traces to the shipped SDK README, the platform's metering code, or live verification runs. Corrections welcome through the usual channels: if this document ever disagrees with the chain, the chain wins and we fix the document publicly.*
