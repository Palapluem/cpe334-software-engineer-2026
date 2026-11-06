# เตรียม Project Deliverable 1

**งานส่ง:** Engineering baseline and working Sprint 1 · **กำหนดส่ง:** 8 พฤศจิกายน 2026 เวลา 23:59 · **คะแนน:** 80 คะแนน (8% ของรายวิชา)

อ่านจาก [handout 8 หน้า](project_deliverable_1_v1.pdf) โดยตรง และใช้ Theme 7 ใน [master specification หน้า 7–8](../group_work_specs_v1.pdf#page=7) ประกอบ ไฟล์นี้เป็นคู่มือและ draft allocation ก่อนเริ่มงาน ยังไม่มีการรับรองว่าแอปหรือเอกสารออกแบบเสร็จแล้ว

## ผลลัพธ์ที่ต้องมี

Parts A–D อธิบาย **ทั้งผลิตภัณฑ์ 3 sprints** ส่วน Parts E–F ออกแบบและพิสูจน์ **Sprint 1** ต้องมี domain journey จริงผ่าน UI → API → database, login/logout/current user, อย่างน้อย 2 meaningful roles, กฎธุรกิจที่ปฏิเสธข้อมูลผิดได้ และ reviewed release บน `main`

Docker, completed CI/CD และ GCP เป็นงาน Lab 5 ไม่ต้องสร้าง cloud เพื่อให้ Deliverable 1 ดูสมบูรณ์ แต่ต้องออกแบบ configuration/storage ให้พร้อมย้ายไปได้ Self-registration, password recovery และ advanced administration ไม่ใช่สิ่งบังคับใน Sprint 1 (handout §2)

## Rubric และไฟล์ที่ควรมีใน product repository

ชื่อ path ด้านล่างเป็นตำแหน่งที่ handout แนะนำ ปรับโครงได้ถ้ายังตรวจตามได้ แต่ต้องเก็บเอกสารฉบับจริงใน product repo ไม่ใช่อาศัย course preparation เพียงอย่างเดียว

| Part | คะแนน | สิ่งที่ต้องเขียน/พิสูจน์ | ตำแหน่งที่แนะนำ |
| --- | ---: | --- | --- |
| A | 10 | ปัญหา/บริบท, actors, scope/exclusions, FR/BR IDs, measurable NFR, assumptions/decisions | `docs/srs.md` |
| B | 10 | feature IDs, dependencies, ทุก FR/BR/important NFR → feature/responsibility → sprint; เปิดเผย gaps/changes | `docs/features.md`, `docs/traceability.md` |
| C | 15 | UI/API/DB architecture, schema/ownership/constraints, UI/error conventions, role matrix, auth lifecycle, env/secrets, delivery plan | `docs/system-sds.md` |
| D | 5 | goal, feature allocation, dependencies และ completion outcome ของ 3 sprints | `docs/sprints/plan.md` |
| E | 20 | contract ของ Sprint 1 ทุก feature: SDS, applicable UI/API/data, stable AC, STS, DoD; ประวัติก่อน implementation | `docs/sprints/sprint-1/` |
| F | 20 | working release, real tests, reproducible setup, selected demonstrations, substantive reviews, integration/history, contributions, limits | source/tests, `README.md`, release record และหลักฐานจริง |

```text
<team-product-repository>/
├── README.md
├── .gitignore
├── .env.example                  # หรือแยกตาม UI/API; placeholders เท่านั้น
├── docs/
│   ├── srs.md
│   ├── features.md
│   ├── traceability.md
│   ├── system-sds.md
│   └── sprints/
│       ├── plan.md
│       └── sprint-1/
│           ├── <feature-contracts>.md
│           └── <verification-and-release-record>.md
├── <application-source>/
└── <automated-tests>/
```

สร้างไฟล์ตามข้อมูลจริงเมื่อเริ่ม product repo ไม่มี requirement ให้ใช้จำนวนเอกสาร/feature/commit ตามตัวอย่าง หรือสร้างโครง UI/API ทั้งหมดล่วงหน้า

## Theme 7 ต้องครอบคลุมอะไร

| ข้อกำหนดจาก stakeholder brief | ต้องอยู่ใน baseline / verification |
| --- | --- |
| Private financial records ของหลายผู้ใช้ | owner scope ของบัญชี transaction ทุก allocation line, favourites และ summaries; backend บังคับสิทธิ์ |
| Financial account 5 ประเภท | Cash, Loan Given, Loan Taken, Income, Expense; bank/wallet เป็น Cash และ credit card เป็น Loan Taken |
| Make a payment or record a charge | source เป็น cash/bank/credit-card/loan-taken; allocation ไป expense, repayment of loans taken, loans given หรือ transfer ไป cash/bank ตามกติกาที่ตกลง |
| Receive money | receiving cash/bank; allocation จาก income, repayment of loans given, new borrowing หรือ transfers จาก cash/bank |
| Allocation totals และ balance effects | หนึ่ง transaction มีอย่างน้อยหนึ่ง allocation; ผลรวมต้องเท่ากับ total; ทุกยอดที่เกี่ยวข้องเปลี่ยนถูกต้อง |
| Opening balances และ transaction dates | ระบุวันที่และผลต่อยอด โดยไม่นับ opening balance เป็น Income/Expense |
| Transfers, borrowing และ repayments | ไม่ถูกนับเป็นรายได้/รายจ่าย; ไม่ double-count การจ่ายหนี้บัตรเครดิต |
| Balances, outstanding loans, card debt, summaries และ history | อ่านข้อมูลที่ persist จริงและได้ผลคำนวณตาม contract |
| Favourite และ Duplicate | ทำเครื่องหมายรายการเดิม, ดูรายการที่ชอบ และสร้าง editable transaction ใหม่จากรายละเอียดเดิม |
| Administrator | จัดการ platform users/access รวมการเปิด/ปิดใช้งาน แต่ดูหรือแก้ financial data/summaries ไม่ได้ |
| Out of scope ที่โจทย์ระบุ | period budgets, shared budgets, automatic recurring transactions และ bank integration |

ใช้ [product GLOSSARY](https://github.com/Palapluem/pocket-ledger/blob/main/GLOSSARY.md) แยกความหมายของ account และอ่านร่าง docs/decisions.md กับ contracts ใน [PR #4](https://github.com/Palapluem/pocket-ledger/pull/4) ก่อนกำหนดข้อยกเว้นเอง Stack และ financial policies ยังเป็นข้อเสนอที่ทีมไม่ได้ยืนยัน

## Sprint 1 ที่ต้องพิสูจน์

ยึดขั้นต่ำเทียบเท่าตัวอย่าง Theme 7: seed ผู้ใช้และ bank/credit-card/income/expense accounts, บันทึก opening bank balance, รับ salary เข้า bank, ซื้อด้วย credit card แบบแยก dining/groceries, ชำระบัตรจาก bank แล้วดู bank balance, card debt, income/expense summary และ transaction history

Auth ต้องเป็นของจริง มี User และ Administrator ที่มีความรับผิดชอบมีความหมาย ตรวจ valid/invalid login, unauthenticated protected requests, cross-user access และ Admin access to financial data การเลือก user/role จาก frontend แทน login หรือซ่อนปุ่มอย่างเดียวไม่เพียงพอ

**Draft feature allocation เพื่อคุยกับทีม ไม่ใช่ scope ที่อนุมัติแล้ว:**

| Proposed feature | Sprint 1 | ส่วนที่ต้องจัดต่อใน Sprint 2/3 |
| --- | --- | --- |
| F-01 Identity and access | login/logout/current user, session/token lifecycle, ownership/role enforcement | hardening ที่ตรวจตาม NFR |
| F-02 Platform user administration | งานดูแล access ขั้นต่ำที่ตกลง เช่น enable/disable seeded users และการห้าม financial access | ส่วนขยายเฉพาะที่อยู่ใน approved scope |
| F-03 Financial accounts and opening balances | seeded account foundation และ opening bank balance | account create/manage ครบประเภทและ opening-balance management |
| F-04 Receive money | salary received into bank พร้อม allocation validation | incoming loan/repayment/transfer cases |
| F-05 Payment and charge | split credit-card purchase และ bank-to-card repayment | remaining payment, loans given และ transfer cases |
| F-06 Balances, summaries and history | ผลยอด/หนี้/รายรับรายจ่ายและ persisted history ของตัวอย่างหลัก | search/filter, category spending และ reports |
| F-07 Transaction correction | จัด policy ไว้ใน design; ไม่อ้างว่า implement แล้ว | implementation และผลต่อ balances/history |
| F-08 Favourites and duplicate | จัดไว้ใน inventory | favourite list และ editable duplicate journey |

การแบ่งแบบนี้ช่วยให้ scope ทั้งผลิตภัณฑ์ไม่หายเมื่อจำกัด Sprint 1 หากจะเปลี่ยน vertical slice ให้ต่างจากตัวอย่าง ต้องขอ instructor/TA agreement ตาม master §6 ไม่ลดรายละเอียดที่ยากออกเงียบ ๆ

## ทดสอบและเก็บหลักฐานตั้งแต่ต้น

รอบนี้ยังไม่มี executable tests หรือจำนวนผลผ่าน กรณีต่อไปนี้เป็น **แผนเสนอ** ต้องจับคู่ AC/STS กับ interface จริงเมื่อกำหนด contract แล้ว

- Rule tests: allocation sum, compatible account types, opening balance/transfer/borrowing/repayment ไม่ปน Income/Expense และ worked balances ที่มี expected values อิสระ
- API + real test database: เขียนแล้วอ่าน transaction/balances/history กลับมาได้; invalid request ไม่ทิ้ง partial transaction; ownership ตรวจทุกบัญชีที่อ้าง ไม่ใช่แค่ source account
- Access tests: valid/invalid login, unauthenticated, User A/B isolation, forbidden role operations, Admin denied financial records/summaries และ logout ตาม session/token design
- Selected UI/E2E: salary → split card charge → repayment → summary/history และ meaningful rejection ที่ดูผลได้
- Seed/setup: เริ่มจากสภาพสะอาดได้ และหากออกแบบให้ seed ซ้ำได้ ต้องไม่ reset/rewrite financial activity ที่มีอยู่
- TDD: หนึ่ง behavior → failing test ด้วยเหตุผลที่ตั้งใจ → minimal implementation → pass เก็บ versions/output ห้ามทำให้ required tests อ่อนลงเพื่อเขียว

ผลจริงแต่ละแถวต้องมี `AC → planned TEST ID → actual file/test name → command/run → tested SHA → result` รวม passing/failing/skipped counts พร้อมอธิบาย manual checks แยกจาก automated tests

## ลำดับทำงานที่เสนอจากวันที่ 3 พฤศจิกายน

| ช่วง | งานที่ควรจบ | Exit condition |
| --- | --- | --- |
| 3 พ.ย. | ยืนยันทีม/repo/stack, financial decisions, baseline A–D และ scope Sprint 1 | ไม่มีการเดากติกาที่เปลี่ยนผลยอดหรือ privacy |
| 4 พ.ย. | review Sprint 1 contracts และเริ่มทีละ vertical slice | contract/test design มี version ก่อน implementation ของ slice นั้น |
| 5–6 พ.ย. | ทำ domain journey + auth/access tests, สลับ implement/review | seed/setup และ journey อ่าน persisted result ได้ |
| 7 พ.ย. | integrate, test, แก้ defects และประกอบ PDF A–F | ทั้งสองคนตรวจตาม rubric; ไม่มี required test ถูกข้าม |
| 8 พ.ย. ก่อน 23:59 | accepted main release, final verification และส่ง PDF | release SHA/tag, navigation, content และ evidence ตรงกัน |

นี่เป็นแผนเสนอ ไม่ใช่หลักฐานว่าทำเสร็จหรือตารางที่อาจารย์บังคับ เตรียม configuration/CI/cloud design ควบคู่ได้ แต่ Lab 5 ต้องเริ่มจาก Sprint 1 release ที่ยอมรับแล้ว

## รายงาน: ห้ามใช้รูปแบบ Lab 5 แทน Deliverable 1

ใช้ [report outline](report-outline.md) ตาม handout §4–5:

- หน้าต้นมีทีม/IDs, theme/context, repository และ immutable release; มี contents/navigation พร้อม page range A–F จริง
- Parts A–E ใส่เอกสารวิศวกรรม **ครบโดยตรงใน PDF** ลิงก์ repo เป็นทางตรวจเพิ่ม ไม่ทดแทนเนื้อหา
- Part F แสดง normal journey + persisted retrieval, rejection, login/logout + forbidden operation พร้อม feature/AC, role, preconditions, steps, expected/actual และ release
- มี build/test output, AC-to-test results, test excerpts จริง 2 ส่วน: domain rule และ role/ownership โดยให้เห็น setup/assertion/result
- เลือก Issues/PRs ที่เสร็จ 2 ตัวอย่าง แสดง branch/author/reviewer/ข้อคิดเห็นจริง/staging/main พร้อม contract-before-code history และ final board status
- มี contribution table, AI-use declaration สั้น ๆ ตามจริง และ limitations/failed/skipped tests ห้ามใส่ full transcript หรือ reflection ยาวโดยคิดว่าเป็นคะแนนบังคับ
- ใช้ข้อความ/ตาราง/diagram ที่อ่านได้โดยไม่ซ้ำหลายรูปแบบ ไม่มี quota ของหน้า และไม่เพิ่ม appendix output ยาวโดยไม่จำเป็น

## Ready-to-submit checklist

- [ ] A–D ครอบคลุมทั้ง baseline; E ครบทุก Sprint 1 contract พร้อม pre-implementation history
- [ ] User/Admin มี meaningful role behavior และ privacy ถูกตรวจจาก backend
- [ ] Domain journey ครบตัวอย่างที่ตกลง ยอดและ history ถูกต้องและ persist จริง
- [ ] Build/tests รันบน release ที่ส่ง มี counts/output/file names และไม่ซ่อน failures/skips
- [ ] มี actual test excerpts และ TDD evidence ที่ตรวจ versions ได้
- [ ] Feature PRs, substantive teammate reviews, integration และ release PR ครบ
- [ ] PDF A–F มี engineering content ครบ, actual navigation/page numbers และหลักฐาน readable
- [ ] README มี dependencies/env/setup/migrate/seed/run/build/test; บัญชีทดสอบเป็น synthetic และส่ง secret ผ่านช่องทางส่วนตัว
- [ ] ทั้งสองคนตรวจตัวอย่าง requirement → feature → AC → test → result ได้

Product คือ **PocketLedger**, repo **[Palapluem/pocket-ledger](https://github.com/Palapluem/pocket-ledger)** และ local code checkout อยู่ที่ `project/pocket-ledger/` แบบ independent Git ชื่อกลุ่มใน LEB2 ยืนยันว่า **2-Nor**; section/เลขกลุ่มแยก, stack, financial policies และการแบ่งงานยังเปิดอยู่ใน docs/decisions.md ของ [PR #4](https://github.com/Palapluem/pocket-ledger/pull/4)
