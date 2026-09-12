# Identity Verification API · Reference and Integration Guide

> Status, honestly: the SDK and the metered API are **live and dogfooded** (3/3 paths through the live API, zero mock data). Two owner actions stand between this and public self-serve: **npm publish** and a **public gateway URL**. Until then, integration works against a deployed instance (baseUrl you are given). Everything below is verified against the shipped code.

---

## What it proves

One question, one mathematical answer: **do this Steem/Hive account and this EVM address belong to the same key?**

The verification chain, all read from the blockchain itself:
1. The user's identity anchor (`saos.id.v1` custom_json) is fetched from the chain
2. Its EIP-191 signature is recovered (ecrecover) to an elliptic point
3. The point is matched against the account's **live active authority** on Steem and Hive, and against the claimed EVM address

No key ever touches the API. No KYC. No trust in us: the proof is re-readable by anyone from public chain state.

## Install

```bash
# npm publish is a pending owner action; install from the repo until then:
# packages/saos-id-verify (dist + README included, zero runtime dependencies)
```

Works on Node 18+, Bun, Deno, browsers, and edge runtimes. Plain fetch under the hood.

## Quickstart

```ts
import { verifyIdentity } from "saos-id-verify";

const r = await verifyIdentity({
  baseUrl: "https://<your-saos-gateway>",   // required; the client refuses to invent one
  apiKey: process.env.SAOS_API_KEY!,
  username: "someaccount"
});

if (r.ok) {
  console.log(r.meta.outcome);      // "PROVEN" | "FAILED"
  console.log(r.anchor.block);      // chain block of the proof
  console.log(r.anchor.explorer);   // open it yourself
}
```

## Outcomes (honesty as a spec)

| Outcome | Meaning | Metered? |
|---|---|---|
| `PROVEN` | Full chain of proof: anchor found, signature recovered, live authority matched per chain | yes |
| `FAILED` | **Real work performed, honest negative** (no anchor, or no active key match). Not an error. | yes |
| `401 SaosAuthError` | Missing/invalid/revoked API key. Fail-closed. | no |
| `429 SaosQuotaError` | Daily quota exhausted. `retryAt` = next UTC midnight. | no |

Known honest edge: the 429 branch is coded to spec but has not been burned live (burning it costs 1,000 real calls).

## Metering and security model

- Quota: **1,000 calls per UTC day** per key
- Every response carries `{used, limit, remaining, resetAt}` plus headers and measured latency
- Server stores **only the SHA-256 of your API key**; the plaintext is shown once at creation
- A full call ledger is kept server-side (auditability)
- The client **refuses to guess a baseUrl**: no silent defaults, ever

## Integration patterns

**Exchange / swap (deposit attribution):** before crediting a deposit that arrived from a Graphene account, call verify with the memo-sourced username and your custodial EVM address. `PROVEN` attributes the deposit cryptographically; `FAILED` routes to manual review. Cost: one metered call per attribution.

**Game / anti-sybil:** gate airdrops or rewards behind a `PROVEN` per claimed identity. Multi-account farming dies when every claim must match a live on-chain authority.

**Content frontend ("prove you are @account"):** one call replaces password auth for legacy Graphene users; they never expose keys, you never store passwords.

## Verify us (do this, please)

Every `PROVEN` response includes `anchor.block` and `anchor.explorer`. Open the explorer link, find the `saos.id.v1` custom_json, recover the signature yourself with any EIP-191 tool, and compare the recovered point with the account's active authority via any public API node. The reference live proof: **PROVEN against Steem block 109,389,994**.

## What this API is not

- Not custody, not a wallet, not a transfer rail
- Not a KYC provider: it proves key control, nothing about identity documents
- Not a mock: there is no demo mode; every test path ran against the live API

---

*SAOS is technology infrastructure in active development. Nothing here is investment advice. Source of truth for all numbers: fact-sheet.md in this repository.*
