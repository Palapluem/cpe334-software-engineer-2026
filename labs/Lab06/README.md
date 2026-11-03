# เตรียม Lab 6: Cross-team UAT and Defect Management

**PocketLedger · ทีม Wisit + Natthawat · กำหนดตาม master: 22 พฤศจิกายน 2026 เวลา 23:59 · 100 คะแนน (5%)**

โฟลเดอร์นี้ยังไม่มีใบ Lab 6 ฉบับละเอียดเมื่อจัดเตรียมวันที่ 3 พฤศจิกายน 2026 คู่มือนี้อิง [Group Work Specification §10](../../project/group_work_specs_v1.pdf#page=14) ต้องตรวจรูปแบบส่ง ชื่อไฟล์ และ rubric กับ handout/ประกาศจริงเมื่อได้รับ ไม่ใช้แม่แบบนี้แทนการยืนยันข้อกำหนดใหม่

## ต้องมีอะไรพร้อมก่อน

- Accepted release ของ PocketLedger ที่ deploy ผ่าน pipeline ของ Lab 5; ระบุ tag/full SHA, public URL และ served version
- **อีกหนึ่งทีม Project** สำหรับ independent UAT ไม่ใช่ Natthawat ซึ่งเป็นสมาชิกทีมเดียวกัน
- Synthetic test accounts/data และ private credential handoff; ห้ามใส่รหัสผ่านในรายงาน/public repo
- UAT cases อย่างน้อย 4 แบบ: normal journey, rule/boundary, role/ownership restriction และ state/history/persistence
- วิธีบันทึก defect, triage, fix/release และ independent re-test ของ version ใหม่

## Rubric จาก master

| ส่วน | คะแนน | หลักฐานที่ต้องเตรียม |
| --- | ---: | --- |
| UAT preparation and handoff | 20 | cases ที่ทำตามได้, safe accounts/data, access และ release/version |
| Independent execution | 25 | ผลทดสอบแอปทีมคู่ ระบุผู้ทดสอบ version, expected/actual, PASS/FAIL และ evidence |
| Defect reporting and triage | 20 | reproduction, expected/actual, severity และ accepted/duplicate/not-defect/enhancement พร้อมเหตุผล |
| Resolution and independent re-test | 35 | accepted defect → regression red → fix → reviewed PR/CI/deploy → partner re-test |

แต่ละทีมมีหน้าที่ทั้ง **tester ของทีมคู่** และ **developer ของแอปตัวเอง** ต้องเก็บสองฝั่ง ไม่สรุปว่าจบ Lab 6 จากการให้เพื่อนดูแอปของเราเพียงอย่างเดียว

## แผน UAT สำหรับ PocketLedger

แหล่ง record จริงอยู่ใน [product UAT record](https://github.com/Palapluem/pocket-ledger/blob/main/docs/labs/lab-06/uat.md) โดยเตรียม candidate cases 5 เรื่องเพื่อแยก privacy ของ User กับ Admin ให้ชัด:

1. opening balance → salary → split credit-card charge → repayment → persisted summary/history
2. allocation ไม่ตรง total ต้องถูกปฏิเสธและไม่เปลี่ยนยอดบางส่วน
3. User B เข้า financial records ของ User A ไม่ได้
4. Admin ทำงานดูแล platform access ได้ แต่เข้า financial records/summaries ไม่ได้
5. อ่านรายการเดิมและ state/history/persisted values กลับมาตาม version/เหตุการณ์ที่กำหนด

นี่เป็นแผนเสนอ ต้องเติม AC, preconditions, steps และ expected values จาก contract ที่อนุมัติแล้วก่อนส่งทีมคู่ ห้ามใส่ผล PASS ล่วงหน้า

## ลำดับทำงาน

| ขั้น | งาน | จบเมื่อ |
| --- | --- | --- |
| Handoff | ตกลงทีมคู่ version, test window, cases และส่ง credentials ส่วนตัว | อีกทีมเริ่มทำตามได้โดยไม่เดา |
| Execute | แต่ละคนในทีมทดสอบแอปคู่และเก็บ actual result | มี case/tester/date/version/evidence ครบ |
| Triage | ตรวจพบจริงเทียบ expected requirement และจัดประเภท | defect ที่ accepted มี reproduction/impact และ owner |
| Fix | เขียน regression ที่แดงก่อน, แก้บน bounded branch, ให้ teammate review/merge, CI/deploy | ระบุ red/fix/release versions ได้ |
| Re-test | ทีมคู่ทดสอบ version ที่แก้แล้วโดยอิสระ | expected/actual และ PASS/FAIL/reopened มีหลักฐาน |

ต้อง resolve และ independent re-test อย่างน้อยหนึ่ง legitimate accepted defect หากไม่พบจริง ให้ติดต่อ TA เพื่อ controlled defect exercise บน isolated version/branch ไม่สร้างเรื่อง ไม่ทำ live release เสีย และไม่ใช้ enhancement แทน defect

## ไฟล์และการส่งต่อ

- Product repo: UAT/triage/re-test records, defect Issues, regression tests, reviewed PR/CI/release evidence
- Course repo: ใบงานเมื่อได้รับ, คู่มือเตรียม, report outline และ PDF ฉบับส่ง
- Raw evidence/credentials: เก็บส่วนตัวที่ `_private/pocket-ledger/` เมื่อจำเป็น
- ใช้ [report outline](report-outline.md) เตรียมช่องข้อมูล; หัวข้อและชื่อ PDF ยังต้องยืนยันจากใบ Lab 6
- ผลและ defects ที่เกี่ยวข้องต้องต่อเข้า Deliverable 2 และ Final; final ยังต้อง re-test version ใหม่เมื่อ behavior ได้รับผลกระทบ

## พร้อมส่งเมื่อ

- [ ] handout ฉบับจริงถูกเทียบแล้ว
- [ ] มีอย่างน้อย 4 executable cases และหลักฐานรับส่ง safe access/version
- [ ] มี independent results สำหรับแอปคู่และผลที่รับกลับของ PocketLedger
- [ ] legitimate accepted defect หรือ TA-controlled exercise มี red/fix/CI/deploy และ independent re-test
- [ ] triage/known issues/version/contributions ตรงกัน ไม่มีผลหรือ finding ที่แต่งขึ้น
