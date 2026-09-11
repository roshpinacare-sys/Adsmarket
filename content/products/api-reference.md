# Identity Verification API: Reference and Integration Guide

> For developers, exchanges, game studios, and frontends. Everything here mirrors the live API surface as dogfooded through the official SDK. Status section at the bottom is honest about what is live and what awaits an owner action.

---

## What the API proves

One question, one mathematical answer:

**Do this Steem/Hive account and this EVM address belong to the same secp256k1 key?**

The proof is read from the chain itself, not from our database:

1. The user published an identity anchor on-chain once (`saos.id.v1` custom_json, signed with their active key)
2. The API recovers the signing point via EIP-191 (`ecrecover`)
3. The recovered point is matched against the **live active authority** of the account on Steem and Hive, and against the EVM address derivation

If everything matches: `PROVEN`, with the anchor block and an explorer link. If not: `FAILED`. A FAILED is real work honestly metered, not an error. Nothing is faked, cached as truth, or invented: the SDK refuses to run without a `baseUrl`, and the server refuses to answer without an on-chain read.

## Authentication

- Header: `Authorization: Bearer saos_live_...`
- Keys are created in the SAOS DEVELOPER console. The plaintext is shown **exactly once**; the server stores only its SHA-256
- Missing, malformed, or revoked key: `SaosAuthError` (401), fail-closed, not metered

## Endpoint

```http
POST /api/v1/identity/verify
Authorization: Bearer saos_live_...
Content-Type: application/json

{ "username": "someaccount" }
```

### Response (200)

```jsonc
{
  "ok": true,                      // or false for an honest FAILED
  "meta": {
    "outcome": "PROVEN",           // PROVEN | FAILED
    "quota": { "used": 12, "limit": 1000, "remaining": 988, "resetAt": 1789999999 },
    "latencyMs": 843
  },
  "verify": { "sameScalarProof": true },
  "chains": [ { "chain": "steem", "sameKeyAsSteem": true }, { "chain": "hive", "sameKeyAsSteem": true } ],
  "anchor": { "block": 109389994, "explorer": "https://steemworld.org/tx/..." }
}
```

Every 200 also carries parsed rate-limit headers (`X-RateLimit-Limit / Remaining / Reset`) and the server-measured latency.

### Errors

| Status | Meaning | Metered |
|---|---|---|
| 401 `SaosAuthError` | key missing, malformed, or revoked; fail-closed | no |
| 429 `SaosQuotaError` | UTC-day quota exhausted; `retryAt` = epoch seconds of next UTC midnight | n/a |

Quota: **1,000 calls per UTC day per key**, ledger-backed. The 429 branch is coded per spec; it has not been live-burned yet because burning it costs 1,000 real calls (honest gap, documented).

## SDK: three lines

```bash
npm i saos-id-verify
```

```ts
import { verifyIdentity } from "saos-id-verify";

const r = await verifyIdentity({
  baseUrl: "https://<your-saos-gateway>",
  apiKey: process.env.SAOS_API_KEY!,
  username: "someaccount"
});
if (r.ok) console.log(r.meta.outcome, r.anchor.block, r.anchor.explorer);
```

Zero dependencies (plain fetch). Runs on Node 18+, Bun, Deno, browsers, and edge runtimes. Options: `timeoutMs` (default 30000), injectable `fetch` for custom agents.

### Client form (reuse across calls)

```ts
import { SaosIdentity } from "saos-id-verify";

const client = new SaosIdentity({ baseUrl: "https://<your-saos-gateway>", apiKey: process.env.SAOS_API_KEY! });
const r = await client.verify("someaccount");
if (r.ok) {
  r.chains.forEach((c) => console.log(c.chain, c.sameKeyAsSteem));
} else {
  console.error("not proven:", r.error, r.meta?.outcome);
}
```

## Integration patterns

### Game studios (sybil resistance)

Reward airdrops and tournaments attract multi-accounting. Gate participation: before crediting a player, verify that their claimed Steem/Hive identity and their payout address are the same key. One call per player per season. Cost: one quota unit, a fraction of a cent of your infra time. Accounts without an anchor simply get FAILED: route them to manual review or to the anchor flow, don't blacklist them.

### Exchanges and swaps (deposit attribution)

Deposits arriving from Graphene-based wallets carry account names, not addresses. Attribute them cryptographically: verify the account-to-address binding at first deposit, store the mapping, and re-verify on any change. The proof is on-chain, so your compliance team can re-run it independently at any time.

### Social frontends and content platforms

"Prove you are @account" without passwords and without OAuth: the user signs one EIP-191 digest with the key they already use on Steem/Hive; your backend confirms the binding through the API. No key material ever touches your servers.

## Security model (what we never do)

- The API **never sees or stores private keys**. It reads public chain state
- Server stores only SHA-256 of your API key; plaintext shown once
- No custody, no fund movement, no wallet-connect flows
- Every response is reproducible: the anchor block and explorer link let any third party re-derive the same verdict without trusting us

## Status (honest, as of 2026-09-11)

| Component | State |
|---|---|
| API logic + metering + ledger | live and dogfooded (PROVEN @ Steem block 109,389,994; FAILED path metered honestly; 401 fail-closed) |
| SDK `saos-id-verify` | publish-ready in the repo (strict TS build, dist + README only). **npm registry publication is an owner action in progress**: until then, install from the repo |
| Public gateway | owner action in progress. `baseUrl` is required by design: the client refuses to invent an endpoint |
| 429 branch | coded per spec, not live-burned (would cost 1,000 real calls) |

Questions, pilots, and partnership: see the press kit contact section. We answer with receipts, not slides.
