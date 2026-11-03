# เตรียม Project Deliverable 2

**PocketLedger · Sprint 2 completion and Sprint 3 progress · ส่ง 29 พฤศจิกายน 2026 เวลา 23:59 · 70 คะแนน (7%)**

อิง [handout 5 หน้า](project_deliverable_2_v1.pdf) ที่อ่านครบ รวมเวลาส่งใน §4 ใช้ทีม/repo/theme เดิมและเก็บ approved scope changes

## Checkpoint ที่ต้องถึง

- Sprint 2 **ทุก feature ที่วางแผนไว้ต้อง complete/reviewed/integrated/verified** ไม่ย้ายงานไป Sprint 3 เพื่อให้ตารางดูเสร็จโดยไม่มี approved revision
- Sprint 3 มี contract ครอบคลุม baseline ที่เหลือ และมี **อย่างน้อยหนึ่ง meaningful workflow/rule ที่ implement และ test จริง** ไม่ใช่หน้าเปล่าหรือ test ที่ไม่รัน
- Candidate บน main รวม Sprint 1 + Sprint 2 + ส่วน Sprint 3 ที่ทำแล้ว และ deploy ผ่าน pipeline Lab 5
- Auth, ownership, financial calculations และ behavior เก่ายังทำงาน; มี exact remaining-work list พร้อม owners/dependencies/actions/date ก่อน 13 ธันวาคม

## Rubric A–E

| Part | คะแนน | ต้องอยู่ใน PDF โดยตรง |
| --- | ---: | --- |
| A | 5 | Sprint 1 continuity, baseline change log และ Lab 5–7 finding/defect status |
| B | 25 | Sprint 2 contracts/AC/STS/DoD ทั้งหมด, complete feature table, running behavior/tests/reviewed release |
| C | 15 | Sprint 3 contractsทั้งหมด, implemented tested progress และ remaining-work plan |
| D | 10 | Complete current SRS, feature inventory, system SDS และ full traceability ถึง actual result/version |
| E | 15 | Integrated candidate demos, build/regression/CI/deploy output, readiness/setup และ completion plan |

เก็บ accepted Sprint 1 และ Sprint 2 releases เดิมให้ตรวจได้ แม้ candidate ล่าสุดรวม Sprint 3 แล้ว ใช้ [product assessment plan](https://github.com/Palapluem/pocket-ledger/blob/main/docs/assessment-plan.md) และ [release register](https://github.com/Palapluem/pocket-ledger/blob/main/docs/releases.md) เป็นจุดเชื่อมหลักฐาน

## หลักฐานที่ต้องเตรียม

- เลือก meaningful Sprint 2 features สองเรื่องและ Sprint 3 workflow/rule ที่ทำจริงอย่างน้อยหนึ่งเรื่อง พร้อม short Sprint 1 continuity demonstration
- แต่ละ demo มี feature/AC, role, preconditions, steps, expected/actual และ tested version; แสดง saved retrieval, rejection และ backend/API access restriction
- Actual commands/SHAs/readable output พร้อม passing/failing/skipped counts และ actual file/test names
- Actual test excerpts สั้นสองส่วน: domain/cross-feature rule และ access restriction พร้อม setup/assertion/result; มี meaningful red/green versions
- Issue/PR chains สองตัวอย่างที่มี substantive review, staging integration และ main release
- Traceability ครบ requirement → feature/responsibility → sprint → AC/target → planned test → actual file/name/measurement → result/version
- Defect/change register: source, affected IDs, triage/approved decision, fix/change release และ re-test; ไม่อ้างว่าจบจาก board status อย่างเดียว
- Dated remaining-work plan ครอบคลุม features/AC, defects, owners, dependencies, next action และการเสร็จก่อน 13 ธันวาคม ช่วงสอบปลายภาคคือ 1–11 ธันวาคม

## รายงานและ setup

ส่ง **self-contained PDF หนึ่งไฟล์ต่อทีม** พร้อม identities/theme/repo/immutable release/deployed URL+version และ navigation A–E ที่อ้าง page ranges/IDs จริง เอกสารเต็มต้องฝังใน PDF; ลิงก์เป็นทาง targeted verification ไม่ทดแทนเอกสาร

ใช้ [report outline](report-outline.md) เก็บรายละเอียดจริงและ appendices เฉพาะที่จำเป็นใน PDF เดียว ไม่ทำสำเนา traceability/เอกสารซ้ำหลายส่วน ไม่มี fixed page limit ตาม handout แต่ทุกอย่างต้องอ่านได้

README/setup ต้องมี dependencies/env examples/Docker/build/run/test/migrate/seed/deploy และ synthetic access ผ่าน private handoff คง repo/deployment ให้ตรวจจนจบ grading

## พร้อมส่งเมื่อ

- [ ] Sprint 2 ทุก feature complete และมี accepted release ที่ระบุได้
- [ ] Sprint 3 contractsครบและมี meaningful implemented/tested progress
- [ ] Whole-product documents/traceability ตรง candidate และเปิดเผย gaps/failures/skips
- [ ] Integrated main release ผ่าน build/regression และ deployตรง CI/version พร้อม post-deploy journey/persistence checks
- [ ] PDFมี complete documents, selected execution/history และ exact remaining-work plan
