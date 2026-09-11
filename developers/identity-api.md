# Identity Verification API: reference and integration guide

> Status (honest, as of 2026-09-11): the API and SDK are live, metered and dogfooded end-to-end (PROVEN, FAILED and 401 paths all executed against the running service). Two owner actions are in progress before external self-serve: publishing the SDK to the npm registry and opening a public gateway. Until then, integrators run against an instance URL provided by the team.

---

## What it proves

One question, one mathematical answer: **does this Steem/Hive account and this EVM address belong to the same secp256k1 key?**

The proof is read from the chains themselves, not from our database:

1. The user published an identity anchor once: a `saos.id.v1` custom_json on Steem/Hive, signed per EIP-191 with the same scalar that is their live active authority.
2. The service recovers the signing point (ecrecover) from that anchor.
3. It matches the recovered point against the account's **live active authority** on each chain, and against the EVM address derived from the same scalar.
4. All match: `PROVEN`. Any link missing: `FAILED`. Both are honest, metered results.

No key ever touches the service. No KYC. No custody. The user can revoke by rotating their on-chain authority, and the next verification fails accordingly.

---

## Quickstart (SDK)

The official client is `saos-id-verify`: zero dependencies, plain fetch, runs on Node 18+, Bun, Deno, browsers and edge runtimes.

```bash
npm i saos-id-verify    # live in the repo now; npm registry publish pending (owner action)
```

```ts
import { verifyIdentity } from "saos-id-verify";

const r = await verifyIdentity({
  baseUrl: "https://<your-saos-gateway>",   // required; the client refuses to invent an endpoint
  apiKey: process.env.SAOS_API_KEY!,        // saos_live_... from the developer console
  username: "someaccount"
});

if (r.ok) {
  console.log(r.meta.outcome);        // "PROVEN"
  console.log(r.verify.sameScalarProof);
  console.log(r.anchor.block, r.anchor.explorer);
} else {
  console.log(r.meta?.outcome, r.error);   // "FAILED" is a real answer, not an exception
}
```

Client form, when you want to reuse the connection:

```ts
import { SaosIdentity } from "saos-id-verify";

const client = new SaosIdentity({ baseUrl, apiKey });
const r = await client.verify("someaccount");
if (r.ok) {
  r.chains.forEach((c) => console.log(c.chain, c.sameKeyAsSteem));
}
```

Options: `timeoutMs` (default 30000), injectable `fetch` (custom agents, edge runtimes, proxies).

---

## Endpoint reference

```http
POST /api/v1/identity/verify
Authorization: Bearer saos_live_...
Content-Type: application/json

{ "username": "someaccount" }
```

### Outcomes

| HTTP | outcome | meaning | metered |
|---|---|---|---|
| 200 | `PROVEN` | full chain: on-chain anchor found, EIP-191 recovery matches the live active authority per chain | yes |
| 200 | `FAILED` | real work happened and honestly failed (no anchor, or no matching active key). Not an error | yes |
| 401 | `SaosAuthError` | key missing, malformed or revoked. Fail-closed | no |
| 429 | `SaosQuotaError` | UTC-day quota exhausted; `e.retryAt` is the epoch second of the next UTC midnight | no |

### Every 200 carries

- `meta.quota`: `{ used, limit, remaining, resetAt }` straight from the metering ledger
- `meta.latencyMs`: server-measured end-to-end latency
- `rateLimit`: parsed `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset` headers
- `anchor`: `{ block, explorer, txid }` for the on-chain anchor the proof was read from

### Authentication model

Keys are created in the SAOS DEVELOPER console with the `saos_live_` prefix. The plaintext is shown **exactly once**; the server stores only its SHA-256. Revocation is immediate and fail-closed: a revoked key gets 401 from that moment on.

---

## Integration guide: the 30-minute path

### For games (anti-sybil)

Reward farming dies when one human cannot claim to be many. Gate rewards, airdrops or ranked ladders behind `verifyIdentity`: each game account must PROVEN-link to a distinct on-chain identity. Cost per check: one metered call. Cheaters pay real keys, not email addresses.

### For exchanges and swap services (deposit attribution)

Deposits arriving from Graphene accounts carry a memo, not an address. When a user proves `username ↔ EVM address` once, every future Graphene deposit from that username maps deterministically to their account. Fewer support tickets, fewer attribution frauds.

### For social frontends and communities

"I am really @account" as a verified badge that cannot be forged and cannot be taken down by us: the badge is math against live chain state. If the user loses the key, the badge dies with it. That is the point.

### Step-by-step

1. Get a `baseUrl` and an API key (team-issued until the public gateway opens).
2. Install the SDK from the repo (npm publish pending) or call the endpoint with plain fetch.
3. Call `verify` for a known-anchored account and confirm `PROVEN` with the anchor block in an explorer.
4. Call for an unanchored account and confirm you handle `FAILED` as a normal result.
5. Wire the 401 and 429 paths (key rotation and `retryAt` backoff).
6. Ship. Total time with our tests: under 30 minutes.

---

## Independent verification (don't trust the API either)

Any PROVEN response names the anchor block and explorer link. A skeptical integrator can:

1. Open the anchor transaction in a public explorer (steemworld / hiveblocks).
2. Extract the `saos.id.v1` payload and signature.
3. Run ecrecover locally and compare against the account's active authority from a public RPC.

If our answer and yours disagree, ours is wrong and we want the report. The reference PROVEN capture (2026-09-08, Steem block 109,389,994) was verified this way.

---

## Honest limitations

- `baseUrl` is required by design: the client refuses to invent or default an endpoint.
- The 429 branch is coded and unit-tested per spec but was never live-burned (burning it costs 1,000 real calls). We say so instead of claiming full path coverage.
- Blurt participation follows the on-chain claim; per-chain coverage depends on what the user actually anchored.
- npm registry install and a public self-serve gateway are pending owner actions. Everything else above runs today.

---

*This document is derived from the shipped SDK and the live metered service, verified 2026-09-11. Corrections welcome and will be published like everything else.*
