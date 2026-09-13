# Identity Verification API: reference and integration guide

> Status, honestly: the API runs and is metered inside the system; the SDK is live in the repo and dogfooded end to end. **npm publication and a public gateway are pending owner actions.** Everything below describes the shipped code, byte-for-byte against the live API as captured 2026-09-08.

## What it proves

One question, one mathematical answer: **does this legacy Steem/Hive account and this EVM address belong to the same key?**

The proof is read from the chain itself, never from our word:

1. The account published an identity anchor on-chain (`saos.id.v1` custom_json, one time)
2. The service recovers the signer from the anchor's EIP-191 signature (ecrecover to an elliptic point)
3. The point is matched against the account's **live** active authority on each chain, and against the EVM address

No key material ever touches the service. No KYC. No trust in us: every step is reproducible from public chain state.

## Install

```bash
npm i saos-id-verify        # active once published to the registry
# until then, from the repo:
git clone <saos repo> && cd Saosmartwallet/packages/saos-id-verify && npm i && npm run build
```

Zero dependencies. Plain fetch. Runs on Node 18+, Bun, Deno, browsers, and edge runtimes.

## Quickstart (3 lines)

```ts
import { verifyIdentity } from "saos-id-verify";

const r = await verifyIdentity({
  baseUrl: "https://<your-saos-gateway>",   // required; the client refuses to invent an endpoint
  apiKey: process.env.SAOS_API_KEY!,        // saos_live_... from the DEVELOPER console
  username: "headcorner"
});

if (r.ok) {
  console.log(r.meta.outcome);            // "PROVEN"
  console.log(r.verify.sameScalarProof);  // the math result
  console.log(r.anchor.block, r.anchor.explorer);
}
```

## Client form (reuse across calls)

```ts
import { SaosIdentity } from "saos-id-verify";

const client = new SaosIdentity({ baseUrl, apiKey, timeoutMs: 30_000, fetch: customFetch });
const r = await client.verify("someaccount");

if (r.ok) {
  for (const c of r.chains) console.log(c.chain, c.sameKeyAsSteem);
} else {
  console.error("not proven:", r.error, r.meta?.outcome);
}
```

Options: `timeoutMs` (default 30000), `fetch` (injectable for custom agents or edge runtimes).

## Outcomes (the honesty table)

| Result | Meaning | Metered? |
|---|---|---|
| `r.ok === true`, outcome `PROVEN` | Full proof chain: on-chain anchor, EIP-191 recovery, live active-authority match per chain | Yes |
| `r.ok === false`, outcome `FAILED` | **Real work happened and honestly failed** (no anchor, or no active key match). Not an error. | Yes |
| `SaosAuthError` (401) | Key missing, malformed, or revoked. Fail-closed. | No |
| `SaosQuotaError` (429) | UTC-day quota exhausted. `e.retryAt` = epoch seconds of next UTC midnight | No |

Every 200 response carries metering transparency:

- `r.meta.quota`: `{ used, limit, remaining, resetAt }` from the metering ledger
- `r.rateLimit`: parsed `X-RateLimit-Limit / Remaining / Reset` headers
- `r.meta.latencyMs`: server-measured end-to-end latency

## API keys

Created in the SAOS DEVELOPER console. Format: `saos_live_...`. The plaintext is shown **exactly once**; only its SHA-256 is stored server-side. Revocation is immediate and fail-closed (401 on next call).

## Error handling that respects the design

```ts
import { verifyIdentity, SaosAuthError, SaosQuotaError } from "saos-id-verify";

try {
  const r = await verifyIdentity({ baseUrl, apiKey, username });
  if (r.ok) grantAccess(r.chains);           // PROVEN: act on it
  else logHonestFailure(r.meta?.outcome);    // FAILED: real work, honest no
} catch (e) {
  if (e instanceof SaosQuotaError) scheduleRetry(e.retryAt * 1000);
  else if (e instanceof SaosAuthError) alertOperator("key rejected, fail-closed");
  else throw e;
}
```

Note the asymmetry by design: `FAILED` is a **result** (and metered, because chain reads happened), while 401/429 are **errors** (and not metered, because no work was done).

## Integration patterns (what the first partners will use it for)

1. **Sybil resistance for games and airdrops (Hive/Steem ecosystems):** one legacy account, one reward identity. Prove account-to-EVM linkage before counting a participant twice.
2. **Deposit attribution for exchanges:** incoming Graphene-side activity tied to a user's EVM identity without custodial bridging.
3. **Frontend authentication for community apps:** "I am really @account" verified against live chain authorities, no password ever seen by your backend.

## What it does NOT do (scope, honestly)

- Not a wallet connect; no signing, no custody, no fund movement
- Not a KYC provider; it proves key linkage, not personhood
- The XRP derivation path is marked declared-not-verified (published gap); EVM and Solana derivations are exact-verified
- A FAILED result does not mean the account is fake; it means the anchor or authority match is absent **right now**

## Provenance

Types mirror the live API byte-for-byte as captured 2026-09-08. Live proof points: PROVEN against Steem block 109,389,994; FAILED against an unanchored account (honest metering); 401 fail-closed. The package is dogfooded against the running metered API by its own test tooling (3/3 paths). The 429 branch is coded to spec and pinned by tests, not yet burned in production (burning it costs 1,000 real calls; we say so instead of implying otherwise).
