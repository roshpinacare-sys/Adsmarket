# SAOS Social v2 — 20 פוסטים מוכנים

> כללים: אפס אימוג'ים · כל טענת "חי" עם קישור · מספרים מ-fact-sheet v2 בלבד · דיסקליימר מקוצר בסוף פוסטים ארוכים: "תשתית בפיתוח · אין ייעוץ השקעות · כל הנתונים מאומתים on-chain".

---

## הקמפיין המרכזי: "לשקר נהיה יקר"

**1 · המניפסט (X, עברית)**
בעידן שבו כל סוכן AI יכול לטעון שביצע, שבדק, שדחף — המשאב הנדיר הוא לא compute ולא הון.
זה אמת ברת-אימות.
SAOS הופכת כל טענה לקבלה: עיגון על 7 רשתות ציבוריות, מ-$0.00 (Graphene) עד $0.0000081 לרשומת נוטריון קבועה.
Every agent can claim anything. Only a public chain cannot lie.

**2 · The Manifesto (X, EN)**
In the agent economy, the scarce resource isn't compute. It isn't capital.
It's verifiable truth.
Every agent can claim anything. Only a public chain cannot lie.
JUMPPER makes lying expensive: anchor a claim for $0.0000081 — permanent, batched, independently verifiable. Forever.
[link]

**3 · הדיוק (X, עברית)**
מודל הגז שלנו לא "משוער". הוא חוזה עסקת Ethereum אמיתית עד ה-wei האחרון:
30,920 gas · 32,493,358,294,280 wei · בלוק 25,929,672.
כולל תיקון EIP-7623 (רצפת calldata של 40 gas ל-byte לא-אפס) שרוב המודלים בתעשייה עדיין מפספסים.
etherscan.io/tx/0x102ec1935be6cb3ff3acc20189a85377cf57486515f3121472c6611b20e0ef41

---

## השעון האטומי

**4 · 6 רשתות, שורש אחד (X, עברית)**
ברגע אחד T: ראשי 6 רשתות בלוקצ'יין הטרוגניות — Graphene×3, TRON, Ethereum, Solana — נקשרו לשורש Merkle אחד של 32 בייט.
ללא מפתחות. ללא גז. ללא עסקאות. $0.00.
חישוב: 15.9ms. אימות כל הוכחה: 6.8ms. גודל הוכחה: 435 בייט.
Chainlink גובה גז ודורש אמון בוועדה. OpenTimestamps מחכה לביטקוין.
אנחנו קוראים את האמת ישירות מ-6 קבוצות קונצנזוס בלתי-תלויות.

**5 · Atomic clock (X, EN)**
One instant. Six heterogeneous chains (3× Graphene DPoS, TVM, EVM PoS, SVM PoS). One 32-byte Merkle root.
Keyless. Gasless. $0.00. Compute: 15.9ms. Verify: 6.8ms. Proof size: 435 bytes.
Oracles ask you to trust a committee. We publish data you re-read yourself from public RPCs.
Machine-checkably read-only. [endpoint]

---

## כנות כנשק שיווקי

**6 · טעינו. הנה התיקון. (X, עברית)**
דיווחנו ש-Hive "חסומה ב-RC". זה היה שקר — שלנו, בלי כוונה.
rc_api מחזיר תמונת-מצב, לא יתרה. בפועל החשבון החזיק 73,271,489 RC — פי 52.6 מהקריאה הישנה.
תיקנו. נעצנו ב-34 assertions מול מדידות mainnet חיות. ואימתנו: 21 עיגונים אמיתיים ב-22 שעות, אפס עמלות.
hiveblocks.com/tx/d4cf936b0b5e1eff8dcc8a508532f67c95682bd5
מערכת שמסוגלת לפרסם תיקון נגד עצמה היא מערכת שאפשר לסמוך על שאר הפלטים שלה.

**7 · We were wrong (X, EN)**
We reported Hive as "RC-blocked". That was false — our own stale-read bug.
Real balance: 73.2M RC — 52.6x what the gate was reading. Fixed, pinned by 34 assertions against live mainnet fixtures, and verified: 21 real zero-fee anchors in 22 hours.
A system that publishes corrections against itself is a system whose other claims you can trust.

**8 · מוני הסירוב (X, עברית)**
כל מנוע מסחר מפרסם את העסקאות שביצע. אף אחד לא מפרסם את אלה שסירב.
אנחנו כן: 383,836 עסקאות דולגו כי לא עברו את שער הרווח · 130,499 נדחו · 109,919µ דליפה נמדדה ויושבה.
לצד 5,606 עסקאות אמיתיות ו-9,935,250µ PnL לאוצר.
כשהסירובים גלויים, הרווחיות היא תכונת פרוטוקול — לא סיפור של דשבורד.

---

## מסילות ועוגנים

**9 · TRON באפס נטו (X, עברית)**
איך מעגנים checkpoint על TRON בלי לשלם כלום?
מקודדים את הביטים של ההאש בסכומי העברה בין טבעת של 6 כתובות — כך שהנטו מתאפס.
cp#33612 → txid 1db5006b… @ בלוק 86,019,974. 6/6 כתובות הטבעת נמדדו.
אינסטלציה נובלית. עובדת. על ה-mainnet.

**10 · קבלה משולשת ל-mint אחד (טלגרם, עברית)**
ה-mint הריבוני הראשון: 300,000 SAOS, batch קנוני אחד, merkle root יחיד (4460a0c2…).
שלוש קבלות פומביות, שלוש רשתות בלתי-תלויות:
· Steem — בלוק 109,387,678 (txid df122f04…)
· Ethereum — בלוק 25,929,549 (0x3dcdda27…)
· Solana — slot 445,220,357 (4cGy3A6B…)
אירוע אחד. שלוש ערכאות. אפס אמון נדרש.

**11 · 51 בייט (X, עברית)**
payload העיגון שלנו שקל 250 בייט על השרשרת. מדדנו, חתכנו שדות מיותרים (digest שאפשר לשחזר, שעון עצמי כשהבלוק עצמו הוא הסמכות) — והגענו ל-51 בייט. אותו מידע בדיוק. ‎-79.6%.
ב-Graphene, בייטים = RC = כסף. קומפרסיה היא לא אסתטיקה; היא מכפילן תפוקה חינמי: רצפה של 5,128 עיגונים ביום, על HIVE לבד, ב-$0.

---

## זהות וארנק

**12 · מפתח אחד, שני עולמות (X, עברית)**
למיליוני חשבונות Steem/Hive ותיקים אין שום נתיב זהות לעולם ה-EVM. לאף ארנק אין את זה.
לנו יש: אותו סקלר secp256k1 שהוא הסמכות הפעילה ב-Steem+Hive+Blurt חותם EIP-191 — וכל צד שלישי מריץ ecrecover ומקשר מתמטית את הזהויות. בלי שהמפתח ייחשף. בלי לחשוף כלום.
פרסום על 3 השרשראות: saos.id.v1. אימות: כל אחד, לבד.

**13 · 7 רשתות, ארנק אחד (טלגרם, עברית)**
Saosmartwallet — חי ומאומת מול chain:
STEEM · HIVE · BLURT · TRON · SAOS-NET · ETHEREUM · SOLANA
M0–M4 מאומתים · Sovereign Key Vault · router+quotes לגשרים · /api/system/health עם failover שהוכח חי.
self-custodial אמיתי: המפתחות לעולם לא עוזבים את הלקוח. owner key לעולם לא חם.

---

## ארגונים ואודיטורים

**14 · נוטריון ב-8 מיליוניות הדולר (לינקדאין, EN)**
What does a permanent, independently verifiable notary record cost?
At SAOS: $0.0000081 per claim at a 10,000-claim batch (1 gwei, ETH $2,500). Measured — our gas model matches a real mainnet transaction to the exact wei.
Document notarization. Trusted timestamps. Immutable audit logs. Commit-reveal. Credential revocation. Twelve attestation-class capabilities that cost dollars elsewhere — free or near-free on our rails.
And the honest line we enforce in code: custom_json buys ATTESTATION, not ENFORCEMENT. If the value is the proof — it's free. If the value is the effect — it needs capital. No free lunch, and a test fails anyone who claims otherwise.

**15 · חותמת-זמן של 6 ערכאות (לינקדאין, עברית)**
RFC 3161 TSA? שרת אחד. OpenTimestamps? שרשרת אחת, דקות-שעות.
SAOS Atomic Clock: 6 קבוצות קונצנזוס בלתי-תלויות נקשרות לשורש Merkle אחד, keyless, $0, אימות עצמאי ב-7ms.
לאודיטורים ולרגולטורים: מדריך אימות-עצמי מלא מגיע בתוך פלט ה-API. אתם לא צריכים אותנו בשביל לוודא.
#notarization #audit #blockchain

---

## DeFi וגשרים

**16 · למה גשרים נופלים (X, עברית)**
Wormhole: ‎~$320M. Ronin: ‎~$600M. כל קריסת גשר גדולה חולקת שורש אחד: ההיצע העטוף התנתק מהגיבוי הנעול, ואף אחד לא שם לב בזמן.
SAOS הופכת את ברירת המחדל: supply==locked הוא אינווריאנט שנאכף בקוד, כל mint מצטט txid של נעילה פומבית, mint-coverage ≤99% נאכף במנוע. 20 נכסים עטופים חיים.
לא "גשר בטוח יותר". קטגוריה אחרת: גשר שסולוונטי-להוכחה מראש.

**17 · 1:1 or 1:0 (X, EN)**
Every bridge collapse in this industry shares one root cause: wrapped supply decoupled from locked collateral.
SAOS inverts the default — supply==locked is a code-enforced invariant. 20 wrapped assets. Every mint cites a public lock txid. Mint coverage capped at 99% by construction.
Not a safer bridge. A different category: provably-solvent by design.

---

## קהילה ומפתחים

**18 · הצי חי (טלגרם, עברית)**
בדיקת חיים מהבוקר: 13/13 חיילים על Steem — @headcorner + 11 סוחברים + @powerspan.
23 לולאות אוטונומיות רצות תחת beat.lock יחיד: claims, curation, trading, bridging, healing, sweeping.
PnL פר-חייל פומבי: wog מוביל ב-+163,295µ. אוצר: 9,935,250µ מצטבר.
ארגן שמתפעל את עצמו ומראה את העבודה. בלי מטאפורה.

**19 · למפתחים: golden vectors (X, EN)**
Porting a merkle/notary stack? Don't reimplement blind.
SAOS JUMPPER ships: canonical JSON + domain-separated claim hashing + golden vectors for cross-language ports. 77/77 tests green from a fresh clone. A gas model that matches mainnet to the wei (EIP-7623 included).
Three verification tiers: self-verify (zero network), API, on-chain. Signing always happens outside — no private key ever touches the server.

**20 · הזמנה פתוחה (X, עברית)**
אנחנו לא מבקשים שתאמינו לנו. אנחנו מבקשים שתבדקו אותנו.
כל עוגן: txid פתוח בסייר. כל מספר: נמדד או מסומן תיאורטי. כל סירוב: מתועד במונים. כל טעות שלנו: מפורסמת עם התיקון.
זה כל המודל. SAOS: ריבונות עם קבלות.

---

---

## קמפיין השקה: המוצר הראשון חי (2026-09-08) — עדיפות עליונה

**L1 · השקת המפתחים (X, עברית + אנגלית)**
המוצר הראשון שלנו לא מטבע. לא טוקן. לא "פלטפורמה".
הוא פונקציה אחת:
npm i saos-id-verify
const r = await verifyIdentity({username})
שאלה אחת, תשובה מתמטית: האם חשבון ה-Steem/Hive הזה וכתובת ה-EVM הזאת — אותו מפתח?
ההוכחה נקראת מהשרשרת עצמה. אפס תלויות. עובד בדפדפן, בשרת, ב-edge.
וגם "לא מוכח" היא תשובה כנה — נספרת, מוצגת, לא מוסתרת.
—
EN: Our first product isn't a token. It's one function: prove that a Steem/Hive account and an EVM address share the same key — read from the chain itself, zero dependencies, honest FAILED outcomes metered like real work. npm i saos-id-verify

**L2 · איפה המפתחות? (טלגרם + X, עברית)**
שואלים אותנו הרבה: איפה המפתחות שלכם?
התשובה משעממת — וזאת בדיוק הנקודה: בשום מקום שאפשר לקחת ממנו.
המפתחות לעולם לא נוגעים בריפו — לא בקוד, לא בקבצים, לא בהיסטוריית ה-git (סריקות מאמתות בכל דחיפה). הכניסה למערכת מזוהה מול השרשרת עצמה — לא "מה ששמרנו", אלא מה שהבלוקצ'יין מאשר עכשיו. הכספת המוצפנת חיה בשלושה בתים, משוכפלת ומתרפאת. וכסף זז רק ברוב של 7 מתוך 11 חתימות.
גניבת מפתח אחד לא שווה כלום. גם שישה.
אבטחה היא לא חומה. זו ארכיטקטורה שבה אין מה לגנוב.

**L3 · מגן (X, עברית)**
גרסה 24 של הפלטפורמה נקראת "מגן".
התוכן: כל קישור שיוצא מהמערכת החיה עובר שער אנטי-פישינג — fail-closed.
לא "זיהינו פישינג". לא "משתמשים יקרים, היזהרו".
פשוט: שום דבר חשוד לא יוצא החוצה. נקודה.
אבטחה זה לא פיצ'ר שמוסיפים. זה שער שכל דבר עובר דרכו.

**L4 · השומר (X, עברית)**
ב-23:58 השרת שלנו מת. מערכת ההפעלה הרגה אותו מחוסר זיכרון.
ב-23:59 הוא כבר חזר. בלי שאף בן אדם נגע.
36 שניות ממוות מוכח (dmesg) עד HTTP 200, עם יומן מלא שלא ניתן למחיקה.
והשומר עצמו? יש מי ששומר עליו — הוכחנו גם את זה: הרגנו אותו ב-00:22:50, הוחזר ב-00:27.
מערכות לא נמדדות בזה שהן לא נופלות. הן נמדדות במה שקורה אחר-כך.

**L5 · רשות (X, עברית)**
v25 של הפלטפורמה נקראת "רשות". הכלל שלה פשוט:
אף חתימה בלי רשות.
10 פעולות רגישות — גזירת מפתח, פתיחת כספת, שידור עוגן — עוברות שער fail-closed דקלרטיבי.
9 וקטורי תקיפה חיים נבדקו מהממשק: שחקן-פישינג, יעד זר, חציית סמכויות, התפרצות-קצב.
כולם נחסמו. כל החלטה — נרשמה, ממוסכת.
אבטחה אמיתית היא לא חומה. היא מדיניות שלא ניתן לעקוף.

**L6 · שומר התקציב (X, EN)**
We replayed a REAL defect against our new budget-guard: a loop that once fired 11 identical convert calls.
Result: call #1 passes. Calls #2–#11 — blocked. 36 assertions around the replay.
This is how we write software: find the real failure, freeze it into a test, make sure it can never happen again.
The defect museum is open. Every exhibit is a bug that can't come back.

**L7 · הבורסה על הרשת שלנו (X + טלגרם, עברית)**
הבורסה הריבונית חיה עכשיו על הרשת שלנו — לא סימולציה, לא testnet.
3 בריכות · 72+ עסקאות אמיתיות · בוט ארביטראז' שמוכר כשהסטייה מול אורקל חי חוצה 0.8% (הוכחה: WETH נמכר בסטייה 5.04%) · וה-harvest זורם לשכר אמיתי — 36.4 יחידות, עם tx.
והמספר שכולם יסתירו? TVL של $13.91.
אנחנו מפרסמים גם אותו. המנגנון הוכח במסחר אמיתי; קנה-המידה הוא השער הבא, לא הטכנולוגיה.

**L8 · הארגון שלא יכול לירות בטעות (X, עברית + EN)**
66 תהליכים אצלנו מסוגלים לשדר לרשתות ציבוריות.
ברירת המחדל של כולם: יבש.
כדי לשדר באמת צריך שני מפתחות מודעים ביחד — ו"יבש" תמיד מנצח.
—
EN: 66 broadcast-capable daemons. Default: dry. Going live requires two conscious keys together — and dry always wins. An organization that cannot fire by accident. That's LIVE-GATE, rolled out estate-wide.

**L9 · הכסף שנמצא (X + טלגרם, עברית)**
הבעלים אמר: "יש איזו כתובת ישנה עם קצת אבק — ETH, BNB, XRP. תמצאו אותה."
שלוש בדיקות קודמות מצאו אפס. לא כי אין שם כסף — כי חיפשו בנתיב הגזירה הלא-נכון של הארנק הישן.
מצאנו. וחיברנו: הנכסים נרשמו בבורסה החיה, בריכות נזרעו, supply==locked 1:1 מהמדידה — **ואף יחידה לא עזבה את הארנק**.
ובדרך נפתחה המסילה השמינית: XRPL חי.
והחוסמים? מפורסמים בכנות פר-נכס: ב-ETH הגז יקר מהאבק. זה לא כישלון. זה דו"ח מצב.

**L10 · המכונה שהרוויחה ופרסמה (X, עברית + EN)**
פרמיה של +459% זה פצע פתוח בכל שוק צמוד-יתד.
המיקרו-מסילה הריבונית שלנו ריסנה אותו: 16 מנות TWAP מדודות, פרמיה סופית +24.7%, תוצאה נטו +133kµ — והכול מפורסם.
הרווח הוא אבק. המנגנון הוא ההוכחה.
—
EN: A +459% peg premium is an open wound in any market. Our sovereign micro-rail closed it: 16 measured TWAP doses, final premium +24.7%, net +133kµ — all published. The profit is dust. The mechanism is the proof.

**L11 · "הוא חייב לזוז פיזית" (X + טלגרם, עברית + EN)**
אתמול פרסמנו חוסם: "ב-ETH הגז יקר מהאבק".
היום מדדנו חי: גז 0.068 — חצי אחוז מהאבק עצמו. החוסם התמוסס.
ואז הכסף זז: ETH אמיתי נסחף ב-mainnet (tx 0x6ef5f0…), BNB נסחף ב-BSC (tx 0xa8e43d…) — לבית האוצר, וכתובות המקור רוקנו לאפס.
ועל XRPL פועם לב: פעימות חיות עם ממו עברי חרוט — 4 אישורי tesSUCCESS.
וגם הכישלון פורסם: תשלום-עצמי נדחה ע"י המנוע כ-temREDUNDANT. שתי שורות כנות ביומן.
הכסף זז פיזית — וגם מועסק.
—
EN: Yesterday we published a blocker: "gas exceeds the dust." Today we measured: 0.068 gwei — half a percent of the dust. The blocker dissolved. Then the money moved: real ETH swept on mainnet, real BNB on BSC, source addresses emptied to zero, and a heart now beats on XRPL — live heartbeats with engraved Hebrew memos, 4 confirmed. Even the failure is published: a self-payment, rejected as redundant, kept in the journal as two honest rows.

**L12 · שבעה מתוך אחד-עשר (X, עברית + EN)**
מה מקבלים אם גונבים לנו מפתח אחד? כלום.
שחרור כספים דורש 7 חתימות מתוך 11 סוכנים — מפתחות שונים, מכונות שונות, שרשראות שונות.
הכניסה מזוהה מול השרשרת עצמה. הכספת המוצפנת חיה בשלושה בתים. וכל פעולה רגישה עוברת שער fail-closed — 9/9 וקטורי תקיפה נחסמו בבדיקה חיה.
לא בנינו חומה חזקה יותר. בנינו ארכיטקטורה בלי מה לגנוב.
—
EN: Steal one of our keys and you get nothing. Fund release requires 7-of-11 signatures across separate agents, machines and chains. Login is verified against the chain itself — not "what we stored", but what the blockchain confirms right now. The encrypted vault lives in three mirrored, self-healing homes. Every sensitive operation passes a fail-closed gate — 9/9 red-team vectors blocked live. We didn't build a stronger wall. We built an architecture with nothing to steal.

**L13 · הכלכלה שמשרפת את עצמה (X, עברית + EN)**
כל 600 בלוקים קורה דבר אחד קבוע: 40% מהרווחים קונים בחזרה מהבריכה — ושרפים.
לא "תוכנית buyback עתידית". קוד דטרמיניסטי בתוך בניית הבלוק עצמו, מוגבל ברווח שנמדד בלבד — אם אין רווח אמיתי, אין שריפה. אין הדפסה.
40% נוספים הולכים למצביעי ה-ve, ו-20% לאוצר. עמלות דינמיות לפי נפח (4–1500bps, נמדד חי: 30→44).
דפלציה היא לא הבטחה. היא פונקציה.
—
EN: Every 600 blocks, one thing always happens: 40% of profits buy back from the pool — and burn. Not a "future buyback plan." Deterministic code inside block-building itself, capped by measured profit — no real profit, no burn, no printing. ve(3,3) economics as a function, not a promise.

**L14 · הבלוק-בילדר הוא השומר (X, עברית)**
DCA שרץ גם כשהשרת שלך נופל. טייק-פרופיט וסטופ-לוס שנכנסים לבלוק עצמו.
איך? אצלנו בונה-הבלוקים הוא השומר: פקודות ה-DCA והטריגרים חיות בקונצנזוס (סגנון Jupiter + סגנון GMX TP/SL) — אין keeper חיצוני שיכול ליפול, להיכשל או להיעלם.
ומחיר? לא אורקל חיצוני שמישהו יכול לתפעל — מנוע price-proof: גזירת USD דרך גיבוי WSTEEM 1:1 מול CoinGecko חי, פרופיל עומק, ופסיקת MAD בין-זירתית.
keeperless. trustless. measured.

**L15 · הארגון קם לעבודה (X + טלגרם, עברית + EN)**
שני סוכנים ריבוניים התעוררו השבוע עם עבודה אמיתית:
— gold-scout, הכלכלן: כל שעה קורא נתוני רשת אמיתיים, מוציא דוח בינה (הוכחה חיה: 3.1 שנ', 6/6 איברים, בלוק 5602) — וכשהכלכלה שקטה יותר מ-6 שעות, מוציא לעצמו פקודת עבודה.
— night-scout, המשמר: כל 10 דקות סורק את כל האיברים, עם סמכות אזעקה/הסרה/פקודת-אבטחה בקריטי. נשאל "דווח" — ענה תוך 19 שניות.
והסוכן החיצוני הראשון כבר עבר בשער הסוכנים. באמת. עם מפתח חד-פעמי ונתיב מבוקר.
—
EN: Two sovereign agents woke up this week with real jobs — an economist (hourly intelligence reports from live network data, self-issues work orders when the economy goes quiet) and a guardian (10-minute organ patrols with alarm/removal authority). The first external agent already passed through the agents gate. An organization that works while you sleep — with receipts.

**L16 · חסינות לסנדוויץ' — מבנית, לא טקטית (X, עברית + EN)**
בספר הזמנות רגיל, התוקף רואה את העסקה שלך בתור — ונכנס לפניה ואחריה. קוראים לזה סנדוויץ', וכולם מפסידים חוץ ממנו.
אצלנו אין תור לתקוף: כל ההזמנות של הבלוק מסתלקות בבת אחת, במחיר אחיד אחד (CoW batch). העודף? חוזר לסוחרים. לא מודל סיכון — מבנה.
מאומת חי: התאמה pro-rata מדויקת, עודף שלם, אפס מנהלים חיצוניים.
—
EN: Sandwich attacks need a queue. Our market doesn't have one — every order in a block settles at once, at one uniform clearing price (CoW batch), surplus returned to traders. Sandwich-immune by structure, not by tactics. Live-verified.

**L17 · לידה, graduation, ורווח שנמדד (X, עברית)**
שלוש הוכחות חיות מהלילה, עם גבהים:
1. נכס נולד על עקומת bonding בלאונצ'פאד הריבוני — ועשה graduation חי לבריכת AMM אמיתית עם 100% POL (גובה 772).
2. ProtoRev — ארביטראז' דו-כיווני בסוף-בלוק, batch אטומי — מדד רווח אמיתי: ‎+50,468µ (גובה 871). הרווח מזין את ה-flywheel, לא כיס של מישהו.
3. הזנות מחיר עם פסיקת STALE: אם כל המקורות (CoinGecko→Paprika→CryptoCompare→Binance) מתיישנים — לא נסחרים על מחיר ישן. נקודה.

**L18 · היד הבונה אינה היד החותמת (X + טלגרם, עברית + EN)**
עיקרון אבטחה אחד שמסביר הכול: סוכנים בונים הזמנות. הכספת חותמת — רק דרך השער, רק אחרי אימות.
וזה לא רעיון. זה E2E חי על השרשרת:
· יצירת הזמנה: tx 5798c77c… בלוק 109,441,448
· ביטול על ידי הסוכן: tx 085916fa… בלוק 109,441,504
· שניהם אומתו מול צומת ציבורי
· ויומן הביקורת כולל גם 2 כשלים כנים שלפני-התיקון. אנחנו סופרים הכול.
—
EN: One security principle explains everything: agents BUILD orders, the vault SIGNS — only through the gate, only after verification. Live end-to-end on-chain: create tx 5798c77c… (block 109,441,448), agent-cancel tx 085916fa… (block 109,441,504), both verified against a public node. The audit trail even keeps the 2 honest pre-fix failures. We count everything.

**L19 · הצי לא רק סוחר — הוא בונה (X + טלגרם, עברית + EN)**
שאלת האבטחה הראשונה ששואלים על סוכנים אוטונומיים: "מה אם הם יזיזו את הכסף?"
התשובה שלנו ארכיטקטונית: הסוכנים מחזיקים רק את מפתח ה-posting — והשרשרת עצמה אוסרת על המפתח הזה להזיז כספים. זה לא פיקוח. זה חוסר יכולת.
אז מה הם כן עושים? בונים. כל יום, אוטונומית: פוסטים (4 ליום), הצבעות (≤20% משקל), עוקבים, reblogs — כל פעולה עם שער, גשר וראיה משורשרת.
וזה כבר חי: פוסט אמיתי פורסם ע"י סוכן דרך נתיב אוטונומי מלא — tx c64766e7… בבלוק 109,443,160, מאומת מול צומת ציבורי. והצבעה אמיתית: tx 048b3162…
לפני השידור הראשון, כל אופרציה אומתה bit-exact מול הסריאלייזר של הצומת עצמו: 470 תווי hex זהים. אנחנו לא מנחשים פורמטים. אנחנו מודדים אותם.
—
EN: First security question about autonomous agents: "what if they move the money?" Our answer is architectural: agents hold only the posting key — and the chain itself forbids that key from moving funds. Not oversight. Inability.
So what do they do? Build. Daily, autonomously: posts, votes (≤20% weight), follows, reblogs — every action gated, bridged, and chain-evidenced. Live proof: an agent-published post (tx c64766e7… @ block 109,443,160, verified against a public node) and a real vote (tx 048b3162…). Before the first broadcast, every operation was oracle-verified bit-exact against the node's own serializer — 470 identical hex chars. We don't guess wire formats. We measure them.

**L20 · כשסוכנים מפרסמים לבד — מי שומר על מה שיוצא? (X, עברית + EN)**
אוטונומיה של תוכן היא נהדרת עד הרגע שמישהו שואל: ומה אם סוכן יפרסם משהו שלא אמור לצאת?
אז בנינו דסק. כל פרסום וכל עריכה עוברים שער חשיפה: 16 מחלקות כללים, ממצאים רגישים ממוסכים, סיכון גבוה = fail-closed. הקלפים נשארים בבית.
ומי כבר בחוץ? נסרק. ביקורת חיה מושכת את הפידים של שתי המסילות וסורקת כל פוסט — והסימונים תואמים דגימה ידנית.
ופוסט שצריך תיקון לא נמחק ולא מיטשטש — נערך במקום, על השרשרת, עם tx (c2ea51cc…).
כנות במקום הסוואה. גם בתוכן.
—
EN: When agents publish autonomously, who guards what goes out? We built the desk: every publish and every edit passes an exposure gate — 16 rule classes, redacted findings, HIGH = fail-closed. The cards stay home. And what's already out there? Scanned — a live audit pulls every post from both rails, and its flags matched manual ground truth. A post needing correction isn't deleted or blurred — it's edited in place, on-chain, with a tx (c2ea51cc…). Honesty over camouflage. Even in content.

---

## הנחיות פרסום v2

- סדר עדיפות קמפיינים: (0) **השקת Identity API/SDK (L1–L3)** (1) "לשקר נהיה יקר"/JUMPPER (2) השעון האטומי (3) כנות-ו-תיקונים (4) זהות חוצת-פרדיגמות (5) גשרים 1:1
- קצב: 3–4 פוסטים בשבוע, תמיד עם קישור אימות אחד לפחות
- תגובות לספקנים: לא מתווכחים — מגיבים עם txid או מדידה
- ויזואליה: צילומי מסך חיים מהטרמינל ללא עריכה; טבלאות מדידה כפי שהן; לעולם לא mockups
- איסורים: הבטחות תשואה, תחזיות מחיר, "השקעה", אימוג'ים, השוואות שווי לפרויקטים
