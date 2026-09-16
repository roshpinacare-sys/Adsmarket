# Crisis Communication Playbook

Four real precedents made this document: the RC stale-read correction, the key-rotation era, the wall-link-integrity catch, and our own confabulation incident. The pattern that worked every time: detect fast, verify against ground truth, publish the correction with evidence, institutionalize the lesson. This playbook turns that pattern into procedure.

---

## Decision tree (first 60 minutes)

1. **What broke?** Classify: (a) public claim that turned out wrong, (b) product defect visible to users, (c) security event (keys, access, funds), (d) internal-only failure nobody outside can observe.
2. **Class (a) or (b): publish.** Wrong public claims get corrected publicly, same day, with the evidence trail. Template below.
3. **Class (c): freeze, then decide.** Security events follow the disclosure policy: never narrate incidents externally. Capabilities and doctrine are publishable; the event itself is not. Internal record always.
4. **Class (d): internal record.** Fix, test, log. Publish only if it changes a public claim.

## Verification before communication

No statement leaves without ground truth: re-read the commit, re-run the query, re-open the receipt. The confabulation incident (roast G13) happened exactly because analysis was written from a failed read instead of a re-fetch. Rule 4 of the disclosure policy exists for this moment.

## Correction template (class a/b)

> **Correction, [date]:** On [date] we published [the claim]. Ground-truth verification showed [what is actually true, with the evidence: commit, txid, measurement]. The correction: [what changed]. What we changed so it cannot repeat: [the rule, test, or gate]. The original text is preserved below / in the roast archive.

Never silently edit a wrong claim. The correction is the asset.

## Who decides what

| Decision | Owner |
|---|---|
| Publish a correction to a public claim | Marketing module, immediately, no approval needed (corrections are mandatory under policy rule 3) |
| Any statement about a security event | Owner only. Default answer: the doctrine line from the press kit |
| Pause a campaign mid-flight | Marketing module (pause first, discuss after) |
| Rewrite history of a published roast | Nobody. Roasts are append-only |

## Standing answers for hard moments

- "Did you get hacked?" -> "We don't discuss specific operational events; that is itself the security policy. Here is the doctrine that governs keys: [press-kit answer]."
- "Your numbers changed." -> "Numbers are dated snapshots by policy. Here is the measurement date and the current one: [fact-sheet]."
- "You published something false." -> "Yes. Here is the correction, the evidence, and the rule that prevents the repeat: [correction template]."
- "Is the system down?" -> status truth only: what is measured, since when, what is being done. Never "everything is fine" without a fresh measurement.

## After-action (within 48h)

1. Roast entry archived (roast/ folder, numbered).
2. If the cause was process: a new numbered rule in disclosure-policy.md or brand.md.
3. If the cause was code: the fix commit linked in the fact-sheet with its measurement date.
4. One line in the next daily report so every agent learns it.

## The one sentence that governs all of it

A correction published with evidence builds more trust than a claim that was never wrong, because the audience never sees the claims you got right by luck. They only ever test the ones where you were caught. Get caught honestly.
