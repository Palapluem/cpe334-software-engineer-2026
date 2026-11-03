# เตรียม Lab 7: Maintenance, Metrics and Release Readiness

**PocketLedger · ทีม Wisit + Natthawat · กำหนดตาม master: 29 พฤศจิกายน 2026 เวลา 23:59 · 100 คะแนน (5%)**

โฟลเดอร์นี้ยังไม่มีใบ Lab 7 ฉบับละเอียดเมื่อจัดเตรียมวันที่ 3 พฤศจิกายน 2026 คู่มือนี้อิง [Group Work Specification §10](../../project/group_work_specs_v1.pdf#page=14) รูปแบบส่ง/ชื่อไฟล์/ข้อกำหนดเพิ่มเติมต้องเทียบ handout จริงเมื่อได้รับ

## งานนี้ต้องเป็นการเปลี่ยนอะไร

เลือกหนึ่ง **behavior หรือ business rule ที่ implement แล้ว** และขอ instructor/TA approval ก่อนเปลี่ยน ฟีเจอร์ที่อยู่ใน baseline แต่ยังทำไม่เสร็จไม่ถือเป็น maintenance exercise โดยตัวมันเอง

ยังไม่กำหนด change ของ PocketLedger แทนทีม ต้องระบุ old behavior/version, proposed behavior, เหตุผล, ขอบเขต และหลักฐานการอนุมัติก่อนเริ่ม

## Rubric จาก master

| ส่วน | คะแนน | สิ่งที่ต้องพิสูจน์ |
| --- | ---: | --- |
| Impact analysis and updated contract | 25 | change request → affected requirement/feature/SDS/AC/tests/code พร้อม reviewed revision |
| Implementation and regression-safe delivery | 50 | changed-behavior test แดงก่อน → implementation → pass/regression → review/CI/deployment |
| Objective engineering metrics | 15 | metrics 5 ตัวพร้อมวันเวลา ช่วงข้อมูล และแหล่ง; interpretation ไม่เกิน 100 คำ |
| Readiness and short retrospective | 10 | defect/test/debt/config/docs/release checks และคำตอบสั้น helped/hurt/change next |

## ลำดับทำงาน

1. บันทึก approved change และ impact analysis รวม data/migration/compatibility และ cross-feature/access effects
2. แก้ contract/AC/STS ผ่าน review ก่อน implementation โดยคงประวัติกติกาเดิม
3. เขียน changed-behavior test ให้ล้มเพราะ behavior ใหม่ยังไม่ถูกทำ ไม่ใช่เพราะ setup เสีย
4. implement ให้ผ่าน ตรวจ regression ของ behavior เก่า และไม่ลด assertions เพื่อให้เขียว
5. teammate review/merge เข้า staging, integration, reviewed main release, CI/deploy และ affected UAT re-test ตามจำเป็น
6. เก็บ metrics/readiness/retrospective และส่งต่อ status ไป Deliverable 2/Final

ใช้ [product change-and-metrics record](https://github.com/Palapluem/pocket-ledger/blob/main/docs/labs/lab-07/change-and-metrics.md) เป็นที่เก็บข้อมูลจริง และ [report outline](report-outline.md) เป็นโครงเตรียมรายงาน

## Metrics ที่เตรียมไว้

| ตัววัด | แหล่งที่ควรใช้ |
| --- | --- |
| Completed Issues | Issue close dates/state ในช่วงที่ระบุ |
| Merged PRs | PR merge dates/state ในช่วงเดียวกัน |
| Passing tests | actual regression output ของ tested SHA ที่ระบุ |
| UAT defects opened/resolved | defect register/Issues และ independent re-test status |
| Successful/failed CI runs | Actions history ที่เก็บต่อจาก Lab 5 |

อย่าเอา cumulative counts คนละช่วงมาเทียบกันโดยไม่บอกขอบเขต จำนวนมากไม่ได้แปลว่าคุณภาพดี การตีความไม่เกิน 100 คำต้องนำไปสู่การกระทำ เช่น defect/re-test ที่ควรรีบปิด ไม่ใช่อวดตัวเลข

Technical debt คือข้อประนีประนอมด้าน design/implementation ที่ทำให้งานอนาคตยากขึ้น อย่าใช้คำนี้แทน required feature ที่ยังไม่เสร็จ

## พร้อมส่งเมื่อ

- [ ] เทียบ handout จริงและมี instructor/TA approval ที่ตรวจได้
- [ ] old/new rule, impact, revised contract และ affected AC/tests ชัดเจน
- [ ] intended red, implementation green, regression, review/CI/deploy มี versions/results จริง
- [ ] metrics 5 ตัวมีเวลา/ช่วง/แหล่ง และ interpretation ไม่เกิน 100 คำ
- [ ] readiness และ retrospective 3 ข้อตอบจากหลักฐานจริง; remaining required work/defects/debt แยกชัด
