# Identity Verification API: Reference and Integration Guide

> Status, honestly: the API is live and metered inside the sovereign deployment, proven end to end against Steem block 109,389,994. Two owner actions stand between it and the public: npm publish of the SDK and a public gateway URL. Until then, install from the repo (dist and README ship in packages/saos-id-verify). Everything below reflects the shipped code, captured byte-for-byte from the live API.

---

## What it proves

One question in, one mathematical answer out:

**Does this Steem/Hive account and this EVM identity belong to the same secp256k1 key?**

The proof chain, all read from public chains, no trust in us required:

1. The user published an identity anchor once: a `saos.id.v1` custom_json operation on Steem (and Hive, and Blurt per the on-chain claim)
2. The server recovers the EIP-191 signature inside that anchor (ecrecover) to an elliptic-curve point
3. The point is matched against the account's **live active authority** on each chain, and against the EVM address derivation (keccak256 of the uncompressed public key, last 20 bytes)
4. Match on all legs = PROVEN, with the anchor block number and an explorer link you can open yourself

No private key is ever requested, seen, or stored. The user signs nothing at verification time; the anchor is a one-time past action.

---

## Endpoint

```
POST /api/v1/identity/verify
Authorization: Bearer saos_live_...
Content-Type: application/json

{ "username": "<steem-or-hive-account>" }
```

**Auth:** API keys carry the `saos_live_` prefix and are created in the SAOS DEVELOPER console. The plaintext is shown exactly once. The server stores only its SHA-256. There is no recovery of a lost key by design; mint a new one.

**Quota:** 1,000 calls per UTC day per key. Both PROVEN and FAILED outcomes are metered (they are real work). 401 and 429 responses are not metered.

---

## Outcomes

| Result | Meaning | Metered |
|---|---|---|
| `r.ok === true` (`outcome: "PROVEN"`) | Full proof chain verified: anchor on-chain, EIP-191 recovery, live active-authority match per chain | yes |
| `r.ok === false` (`outcome: "FAILED"`) | Real work happened and honestly failed (no anchor, or no matching active key). Not an error. A negative answer is an answer | yes |
| `SaosAuthError` (401) | Key missing, malformed, or revoked. Fail-closed | no |
| `SaosQuotaError` (429) | UTC-day quota exhausted. `e.retryAt` carries the epoch seconds of next UTC midnight | no |

Every 200 response also carries:

- `r.meta.quota`: `{ used, limit, remaining, resetAt }` from the metering ledger
- `r.rateLimit`: parsed `X-RateLimit-Limit / Remaining / Reset` headers
- `r.meta.latencyMs`: server-measured end-to-end latency

---

## SDK: three lines

Install (from the repo until npm publish):

```bash
git clone <saos-repo> && cd packages/saos-id-verify && npm run build
```

Use:

```ts
import { verifyIdentity } from "saos-id-verify";

const r = await verifyIdentity({
  baseUrl: "https://<your-saos-gateway>",   // required; the client refuses to invent an endpoint
  apiKey: process.env.SAOS_API_KEY!,
  username: "headcorner"
});

if (r.ok) {
  console.log(r.meta.outcome);              // "PROVEN"
  console.log(r.verify.sameScalarProof);    // the cross-paradigm proof object
  console.log(r.anchor.block, r.anchor.explorer);
} else {
  console.log("not proven:", r.error, r.meta?.outcome);  // "FAILED" is a valid, metered answer
}
```

Client form for repeated calls:

```ts
import { SaosIdentity } from "saos-id-verify";

const client = new SaosIdentity({ baseUrl: "https://<your-saos-gateway>", apiKey: process.env.SAOS_API_KEY! });
const r = await client.verify("someaccount");
if (r.ok) r.chains.forEach((c) => console.log(c.chain, c.sameKeyAsSteem));
```

Options: `timeoutMs` (default 30,000) and an injectable `fetch` (custom agents, edge runtimes). Zero dependencies: plain fetch, runs on Node 18+, Bun, Deno, browsers, and edge.

---

## Integration patterns

**Blockchain game (sybil resistance):** before paying rewards, verify the claiming account. Multi-account farmers cannot mint anchors for accounts they do not control, because the anchor requires the account's real active authority. One PROVEN check per payout, well inside the free quota for most games.

**Exchange or swap service (deposit attribution):** a deposit arrives from a Graphene account memo; you need to tie it to a user's EVM withdrawal address. One call gives you the cryptographic tie, with the anchor block as your audit trail.

**Community frontend ("I am really @account"):** let users prove ownership of their legacy Steem/Hive identity to your app without passwords, without OAuth, and without you storing anything secret. The receipt (block + txid) is yours to keep as evidence.

---

## Honest boundaries (read before integrating)

1. The 429 branch is coded to spec but was not live-burned (burning it costs 1,000 real calls). It will behave per spec; it just has no production scar yet
2. `baseUrl` is mandatory. The client refuses to guess an endpoint. This is deliberate: invented endpoints are how integrations silently talk to attackers
3. The public gateway URL does not exist yet. Self-hosted deployments work today; the hosted gateway is an owner action in progress
4. Blurt verification follows the on-chain claim's scope; Steem and Hive are the primary verified legs
5. The proof binds keys, not humans. It answers "same key?", never "same person?". KYC is out of scope by design

---

## Support

Questions, integration help, or a found discrepancy: open an issue in the SDK repo or reach the team through the official channel listed on the landing page. If this document ever disagrees with the shipped code, the code wins and we want to hear about it. That is not a disclaimer; that is the bug-reporting culture.
