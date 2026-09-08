# SAOS Fact Sheet v2 — מקור האמת השיווקי

> סריקה מלאה של 11 הריפואים · תאריך אימות: 2026-09-08 23:30Z (v3) · כל פריט מגובה בקוד, מדידה או קבלה משורשרת.
> **חדש ב-v3:** המוצר הראשון למפתחים חי (Identity API + SDK) · רוטציית מפתחות חיה אחרי דליפה · פלטפורמה v24 (מגן אנטי-פישינג).
> **תיקונים מ-v1:** HIVE חי (באג stale-read תוקן) · TRON: מסילת אפס-עמלה חיה באקוסיסטם · תפוקה: 32,603 tx/s נמדד בריפליי ארכיון אמיתי.

## 1. הגדרה (הרפורם הנכון)

**SAOS היא מערכת הפעלה ריבונית: מכונת מצב דטרמיניסטית (SAOS-NET) שהביטחון שלה מושכר מ-7 רשתות ציבוריות, עם מנוע כלכלי שנאכף-מבנית, צי סוכנים אוטונומי, ומוצרים (ארנק, נוטריון, DEX) שמפרנסים את כולם.**

לא "עוד בלוקצ'יין". לא גשר. **Sovereign Notarized Ledger** — ריבונות עם קבלות.

## 2. הליבה — SAOS-NET (נמדד)

| מדד | ערך |
|---|---|
| גובה שרשרת | 54,983 בלוקים · 1,507 txs מאומתים · 64 צ'קפוינטים |
| תפוקת מנגנון | **32,603 tx/s** — 65,238 עסקאות ארכיון אמיתיות ב-2,001ms (נמדד 2026-09-07) |
| תקרת מנגנון | ~2.82 מיליארד tx/יום (תיאורטי — תמיד לסמן) |
| DEX kernel | 26,490 ops/sec נמדד (bench נפרד של מנוע ה-DEX) |
| בלוק חי (DEX) | 3 שניות · seal כל 12 · stateRoot = sha256(canonical) = bytes32 נטיבי ל-EVM |

## 3. שכבת הנוטריון — כל המסילות, סטטוס נכון

| מסילה | סטטוס | מנגנון | קבלה |
|---|---|---|---|
| **STEEM** | חי — כל חותם | custom_json · RC · $0 | [390bcfc2…](https://steemworld.org/tx/390bcfc2586def1ef02cc40a0e983c8dd8fce177) בלוק 10,937,394 |
| **HIVE** | **חי — 21 עיגונים ב-22 שע' אומתו** | custom_json · RC אפקטיבי 73.2M | [d4cf936b…](https://hiveblocks.com/tx/d4cf936b0b5e1eff8dcc8a508532f67c95682bd5) · טווח בלוקים 109,708,562–109,734,678 |
| **ETHEREUM** | חי — mainnet | EIP-1559 calldata | [0x102ec193…](https://etherscan.io/tx/0x102ec1935be6cb3ff3acc20189a85377cf57486515f3121472c6611b20e0ef41) בלוק 25,929,261 |
| **SOLANA** | חי — mainnet-beta | SPL Memo v2 | [2M1rkRgg…](https://solscan.com/tx/2M1rkRggRcaePk6vMZpgSaM3WVWQU92RZAs1v7PtNeMLsxLmZoqBNCeEtuY7Rkj5aPbs4jS1g2wUQXCnoejUM2M9) |
| **TRON (אקוסיסטם)** | **חי — אפס עמלה נטו** | ביט-אנקודינג בצמודי-העברה, טבעת 6 כתובות | cp#33612 → txid `1db5006b…` @ בלוק 86,019,974 · 6/6 כתובות נמדדו |
| **TRON (DEX relay)** | חמוש · ממתין 0.3 TRX | זהות נגזרת + extra_data | מוצג בכנות ב-UI |
| **BLURT** | עוגן היסטורי | חתימה קנונית low-s | מתועד ב-platform README |

**עקביות בין-שרשרתית:** אותו stateRoot (`d4970bb5…`, h2388) עוגן בו-זמנית ב-ETH (בלוק 25,929,269) וב-SOL (slot 445,209,689) — אומת bit-for-bit משתי קריאות RPC נפרדות.

## 4. תיקון הכנות של HIVE (נכס שיווקי בפני עצמו)

"חסימת ה-RC" שדווחה הייתה **באג stale-read שלנו**: rc_api מחזיר תמונת-מצב, לא יתרה. בפועל החשבון החזיק **73,271,489 RC** — פי 52.6 מהקריאה הישנה. גילינו, פרסמנו, תיקנו, ו-34 assert נעצו את התיקון למדידה החיה. רצפה נמדדת: **5,128 עיגונים חינמיים ביום** על HIVE לבד.

## 5. השעון האטומי (Foundry) — מדידה מתועדת 2026-09-08T02:04Z

- מצב-ראש של **6 רשתות הטרוגניות** (Graphene×3 · TVM · EVM · SVM) → **שורש Merkle אחד 32B**
- keyless · $0.00 · אפס עסקאות · אפס חתימות · read-only ברמת המכונה
- חישוב **15.9ms** · אימות 5 הוכחות **6.8ms** · גודל הוכחה **435B JSON / 160B גלם**
- ריצה מתועדת: root `0896c3c6…` · עדים: STEEM #109,307,680 · HIVE #109,722,158 · TRON #86,063,739 · ETH #25,929,640 · SOL #445,219,905 (BLURT נופה בכנות — endpoint לא נגיש)
- השוואה: OpenTimestamps = דקות–שעות, שרשרת אחת · Chainlink/LayerZero = גז+ועדת אמון · אנחנו = ms, $0, 6 קבוצות קונצנזוס, בלי לסמוך על אף אחד

## 6. JUMPPER — נוטריון הוכחות אצווה

- **$0.0000081 לרשומת נוטריון** (אצווה של 10,000 טענות · 1 gwei · ETH $2,500) — נמדד, לא מוערך
- מודל-גז שחוזה עסקת mainnet אמיתית **עד ה-wei**: 30,920 gas · 32,493,358,294,280 wei · בלוק 25,929,672 (כולל תיקון EIP-7623: רצפת calldata של 40 gas/byte לא-אפס)
- קומפרסיית payload: 250B → **51B** (-79.6%) — הוכחה round-trip
- 77/77 טסטים ירוקים מ-clone טרי · golden vectors לפורטים בין-שפתיים
- 3 טיירות אימות: self-verify (אפס רשת) · API · on-chain
- חתימה תמיד מחוץ למערכת — אף מפתח פרטי לא נוגע בשרת
- **12 פעולות attestation חינמיות** (נוטריון מסמכים, חותמת-זמן, audit-log, commit-reveal, revocation, quorum, Merkle batch, heartbeat, name-claim, relay בין נקודות שלך, license registry, data availability קטן) מול **5 שלעולם לא חינמיות** (escrow, העברת נכסים...) — מטריצה כנה בקוד עם טסט שמונע זליגה

## 7. המנוע הכלכלי — grid98 + DEX + עטיפות

| רכיב | נמדד |
|---|---|
| מוני-סירוב פומביים | **383,836** דילוגי-edge · **130,499** דחיות · 109,919µ דליפה מדודה ומיושבת |
| מסחר ו-PnL | 5,606 עסקאות · **9,935,250µ** PnL מצטבר לאוצר · 282 עסקאות היום · PnL פר-חייל (wog +163,295µ) |
| סולם רצפה מגובה | 9 מדרגות · כל מדרגה עם גיבוי µ מדויק ברשומות · ≤0.5% לצעד · floor 0.01688→0.017567 |
| עמלות | 30bps · 70% LP / 30% אוצר · harvest rail עם txid פומבי (`1d148959…`) |
| עטיפות | **20 נכסים · supply==locked לאינווריאנט** · mint מצטט txid נעילה (WSTEEM `2ad481ac…`) · 9 חוזי TRC20 אומתו חיים על TRON · mint-coverage ≤99% נאכף |
| DEX | ספר עם escrow מלא · מילוי במחיר-מייקר · ארנה אוטונומית 4 מצטטים · ספרד נמדד 12–82bps |
| אורקל | 15 ציטוטים חתומים שעתיים עם src+ref+at · דילוג כן על כשל רשת — אף מחיר מומצא |

## 8. הצי וכוח העבודה האוטונומי

- **13/13 חיילים חיים על Steem** (get_accounts אומת 2026-09-08): @headcorner + 11 סוחברים + @powerspan
- **23 לולאות תפעול אוטונומיות** תחת beat.lock יחיד (אפס file-races) — claims, curation, trading, bridging, healing, sweeping
- **רישום צי**: 12 סוכנים × EVM(7 רשתות)+TRON+SOL+BTC · מניפסט מעוגן on-chain (`9f593bdc…`) · זהויות EVM זהות בכל הרשתות → מוכן ל-CREATE2
- **סף מתוכנן**: 7/11 לשחרורים (EIP-712) · כוונות גזלס EIP-191 + gas-tank
- RPC discipline: 5 לולאות = קריאה אחת לחלון 15s · DRY_RUN ברירת-מחדל · מפתחות לעולם לא עוזבים את המכונה

## 9. עמידות, אבטחה, ביקורת

- Chaos suite 13/13 (DEX) · invariants חיות: 8/רגל-מילוי + 4/חותם · HALT + haltReason פומבי
- verifyOnChain read-back אחרי כל שידור · circuit breakers · backoff+jitter · 0 mismatches
- audit-package: byte-identical + MANIFEST.sha256 + FIDELITY.diff · 13 אינווריאנטות · 9 הנחות קריפטוגרפיות
- כספת AES-256-GCM · סריקות סודות על כל דחיפה · 0 דליפות
- bit-exact serialization: 30/30 oracle PASS (מול bytes אמיתיים מ-api.steemit.com)

## 10. מוצרים — מה פוגש המשתמש

1. **Saosmartwallet** — ארנק self-custodial ל-7 רשתות חיות (STEEM/HIVE/BLURT/TRON/SAOS-NET/ETH/SOL) · M0–M4 מאומתים מול chain · Sovereign Key Vault · שכבת גשרים עם router+quotes חיים · System Owner: /api/system/health + failover הוכח
2. **JUMPPER** — נוטריון הוכחות אצווה לטענות של סוכנים/ארגונים (Phase 1 ירוק; API+explorer ב-Phase 3)
3. **SAOS DEX** — טרמינל מסחר מוסדי עם עיגון חי ואימות עצמאי בכפתור
4. **Atomic Clock demo** — `/api/saos/breakthrough-demo` — פקודה אחת, הוכחה חיה

## 10.5 המוצר הראשון למפתחים — Identity Verification API (חי, ממוטר)

| רכיב | עובדות מאומתות |
|---|---|
| ה-API | `POST /api/v1/identity/verify` — מפתחות API (נשמר SHA-256 בלבד, plaintext מוצג פעם אחת) · quota 1,000 קריאות/יממה UTC · ledger של כל קריאה · headers שקופים |
| מה הוא מוכיח | שחשבון Steem/Hive וכתובת EVM שייכים לאותו סקלר secp256k1 — עוגן `saos.id.v1` על-השרשרת → EIP-191 ecrecover → התאמת active-authority חיה פר-שרשרת |
| הוכחה חיה | PROVEN מול בלוק Steem **109,389,994** · נתיב FAILED (חשבון לא-מעוגן) נספר כמדידה אמיתית · 401 fail-closed |
| ה-SDK | `saos-id-verify` (npm) — **אפס תלויות**, plain fetch · Node≥18 / Bun / Deno / דפדפנים / edge · dogfooded חי 3/3 נתיבים |
| גבול כן | ענף ה-429 מקודד לפי ספק אך לא נשרף חי (יעלה 1,000 קריאות אמיתיות) · `npm publish` עצמו = פעולת בעלים · baseUrl חובה — הלקוח מסרב להמציא endpoint |
| GTM מוכן | ערכת outreach עם **10 יעדים אמיתיים שנבדקו חיים** (Splinterlands, MEXC, Gate, SimpleSwap, Changelly, Godex, Ecency, InLeo, PeakD…) — כל אחד עם וקטור-חשיפה מתועד ל-Steem/Hive |

## 10.6 אירוע אבטחה שטופל נכון — רוטציית מפתחות חיה (SETTLE-10)

דלפו מפתחות. הטיפול כולו על השרשרת, עם קבלות:
- **headcorner סובב ב-Steem+Hive** (owner/active/posting/memo) — חתימה אחרונה של המפתח הישן, ואז המפתחות הישנים מתים on-chain
- קבלות: STEEM tx `8313cdcb…` בלוק **109,410,651** · HIVE tx `92654439…` בלוק **109,745,168** · 8/8 רשויות חדשות אומתו חיות
- מפתחות חדשים: עץ HMAC מזרע מאסטר טרי (SAOS-ROT1/acct/chain/role) · אפס סודות בריפו
- **כנות הצי:** חייל אחד (wic) סובב בהצלחה · 9 לא ניתן היה לסובב (מפתחות חיים לא היו בכספת — השרשרת דחתה עם tx_missing_owner_auth, וזה דווח כפי שהוא)
- ה-relay חומש מחדש ואומת: breakers closed, 0 mismatches

## 10.7 אבני דרך חדשות בפלטפורמה (v18.1 → v24)

- **v24 מגן (MAGEN):** שער אנטי-פישינג fail-closed על כל קישור יוצא חי
- **v23 שושנים (ROSES):** רוטציית סוכני-צי every 120s cycle
- **v22 CORNERSTONE:** זרע הבעלים (24 מילים) נחתם כשורש תפעולי כפול
- **v21 FLOW:** מכ"ם נזילות (12 נכסים / 8 דומיינים / USD חי) + מפת זרימת ערך
- **v20 MICROGRID:** grid98 על השרשרת (חוזה 9, mesh link #6)
- **foundry task-23:** סריקת שרשרת אספקה — **0 קוד זר בכל 10 הריפואים**
- **foundry task-26:** שירות חותם חיצוני (:3033) מחובר חי — חתימות מופרדות מהמערכת, כפי שתוכנן

## 11. גבולות כנים (מה עוד לא — חובה בכל חומר)

- כלכלת הטוקן של SAOS-NET: טרם הוגדרה במסמך economics (נמצא בשלב S2, דורש אישור בעלים)
- חוזי גשר ETH ותוכנת Solana: מוכנים ב-staging, פריסה = החלטת בעלים תקציבית
- Identity API: חי וממוטר, אך פרסום ה-SDK ל-npm Registry ופתיחת gateway ציבורי = פעולות בעלים
- ביקורת צד-שלישי: החבילה ארוזה, טרם בוצעה
- סדר גודל כלכלי: dust-scale כיום — התקרה טכנולוגית, הכלכלה בהזנקה
- JUMPPER שידור חי: דורש חותם חיצוני + אישור בעלים (by design)

## 12. קישורי אימות עצמאי

steemworld.org (Steem) · hiveblocks.com (Hive) · etherscan.io (ETH) · solscan.com (SOL) · tronscan.org (TRON)
חשבון עוגן: @headcorner — סמכות active מאומתת מול RPC חי ב-Steem, Hive ו-Blurt (אותו מפתח)
