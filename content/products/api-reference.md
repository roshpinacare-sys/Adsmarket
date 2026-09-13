# Identity Verification API: reference and integration guide

For developers, exchanges, game studios, and frontend teams. Every fact here mirrors the shipped SDK (packages/saos-id-verify) and the live metered API it was captured from (2026-09-08, PROVEN against Steem block 109,389,994).

## What the API proves

One question, one mathematical answer:

> Do this Steem/Hive account and this EVM address belong to the same secp256k1 key?

The proof is read from the chain itself, never from our database:

1. The account's on-chain identity anchor (`saos.id.v1` custom_json) is fetched from the public chain
2. Its EIP-191 signature is recovered (ecrecover) to an elliptic-curve point
3. That point is matched against the account's LIVE active authority on each chain, and against the EVM address

If everything matches: `PROVEN`. If anything fails: `FAILED`, which is an honest, metered result, not an error. Nobody's keys are requested, stored, or seen at any point.

## Availability (honest status)

- The SDK is live in the repository: `packages/saos-id-verify`, zero dependencies, strict TypeScript, builds clean with declarations
- `npm publish` and the public gateway are owner actions in progress. Until then, install from the repo (dist + README ship in the package)
- The API itself is metered, key-authenticated, and dogfooded end to end: PROVEN path, FAILED path, and 401 path all executed through the SDK against the running service

## Quickstart (3 lines)

```bash
npm i saos-id-verify        # active once published; today: install from repo
```

```ts
import { verifyIdentity } from "saos-id-verify";

const r = await verifyIdentity({
  baseUrl: "https://<your-saos-gateway>",   // required; the client refuses to invent an endpoint
  apiKey: process.env.SAOS_API_KEY!,        // saos_live_… from the SAOS DEVELOPER console
  username: "headcorner"
});

if (r.ok) {
  console.log(r.meta.outcome);              // "PROVEN"
  console.log(r.verify.sameScalarProof);    // the scalar-equivalence proof
  console.log(r.anchor.block, r.anchor.explorer);
}
```

API keys: created in the developer console, plaintext shown exactly once, only the SHA-256 is stored server-side.

## Client form (reusable instance)

```ts
import { SaosIdentity } from "saos-id-verify";

const client = new SaosIdentity({ baseUrl: "...", apiKey: "..." });
const r = await client.verify("someaccount");
if (r.ok) r.chains.forEach((c) => console.log(c.chain, c.sameKeyAsSteem));
```

Options: `timeoutMs` (default 30,000) and an injectable `fetch` for custom agents or edge runtimes.

## Outcomes and errors

| Result | Meaning | Metered |
|---|---|---|
| `r.ok === true`, outcome `PROVEN` | Full chain: anchor found, signature recovered, live authority matched per chain | yes |
| `r.ok === false`, outcome `FAILED` | Real work happened and honestly failed (no anchor / no active key). Not an error | yes |
| `SaosAuthError` (401) | Key missing, malformed, or revoked. Fail-closed | no |
| `SaosQuotaError` (429) | UTC-day quota exhausted. `e.retryAt` = epoch seconds of next UTC midnight | no |

Every 200 response carries metering transparency: `r.meta.quota` (`used`, `limit`, `remaining`, `resetAt`), `r.rateLimit` (parsed from `X-RateLimit-*` headers), and `r.meta.latencyMs` (server-measured end to end).

Known honest gap: the 429 branch is coded to spec but has not been live-burned (burning it costs 1,000 real calls). It is tested by construction, not yet by production.

## Integration patterns

**Game studio (sybil resistance):** before awarding airdrops or tournament seats, call `verify` on the player's claimed legacy account. One human, many wallets, still one key: duplicates collapse to the same proof. Cost per check: one metered call.

**Exchange / swap (deposit attribution):** deposits arriving from Graphene accounts have no EVM memo standard. Verify the depositor's account-to-address binding once, then attribute with math instead of support tickets.

**Frontend / community (login-ish flows):** "prove you are @account" without OAuth, without custody, without a password reset flow. The chain is the identity provider; the API just reads it.

## What this is not

- Not a wallet-connect: no signing sessions, no key handling
- Not custodial: nothing is held, moved, or escrowed
- Not an oracle: it proves identity binding, not prices
- Not magic: an account with no on-chain anchor returns FAILED, honestly and permanently, until anchored

## Verification (trust nothing here either)

The types mirror the live API byte-for-byte as captured on 2026-09-08. The PROVEN fixture references a real block (109,389,994) you can open in any Steem explorer. The dogfood script (`tools/m1-w2-sdk-dogfood.ts`) runs all three paths against the live metered API. Run it, or ask us to run it on a call. Receipts over promises applies to our own SDK too.
