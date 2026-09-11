# How We Guard the Keys

*Reading time: 3 minutes · technical background required: none · about SAOS security architecture*

---

## In a world where everything gets breached, the boring answer is the strongest one

Ask any crypto company "how do you protect the keys?" and you'll usually get the same answer: "We have a strong firewall, a security team, insurance."

Translation: **we have a strong door.** And every strong door is an invitation to break it.

Our approach is different. We didn't build a stronger door. We built an architecture where **there is nothing to steal**. Here are the seven layers, in plain language:

## Layer 1: Keys never touch the repo

Not in code. Not in files. Not in git history. Every push passes an automated secret scan, and the full history was verified clean. A key that doesn't exist in a file cannot leak from a file.

## Layer 2: Entry goes through a gate that verifies against the chain itself

THE-GATE: when a key is presented, the system doesn't check "did I save this somewhere." It asks the blockchain itself, **does this key control this account, right now, on-chain**. Authority is the chain, not a file. That's the difference between "I remember you" and "I recognize you."

## Layer 3: The vault doesn't live in one house

An encrypted vault (AES-256-GCM, with cryptographic tag verification) lives in three homes, replicated, synchronized, self-healing. If one home falls, the vault doesn't fall with it. And every check passed: 144 of 144 files decrypt successfully.

## Layer 4: Money moves only with seven of eleven

Releasing funds requires signatures from 7 of 11 agents, different keys, different machines, different chains. **Stealing one key is worth nothing.** Even two. Even six.

## Layer 5: Every sensitive action passes a permission gate

Ten critical operations (key derivation, vault opening, anchor broadcasting…) go through declarative fail-closed policy: no explicit approval, no action. Nine attack vectors were tested live from the UI, phishing, foreign destination, authority crossing, rate burst, **all blocked**. Every decision is written to a redacted journal.

## Layer 6: Every outgoing link passes an anti-phishing gate

Nothing suspicious leaves the system. The gate is fail-closed: when in doubt, there is no doubt, it doesn't go out.

## Layer 7: 21 crypto-hygiene rules tested in both directions

Every rule is calibrated so it **fires on defective code** and **stays silent on correct code**. A rule not tested in both directions isn't a rule, it's a suggestion.

## The bottom line

Real security isn't a higher wall. It's an architecture with nothing to steal:
**no keys in files · the chain is the authority · the vault lives in three homes · money moves only by majority · and every sensitive action passes a gate.**

And every word here is checkable. That, in the end, is the whole difference.

---

*SAOS is technology infrastructure in active development. Describing security layers is not a claim of absolute immunity, no system in the world has that. Nothing here is investment advice.*
