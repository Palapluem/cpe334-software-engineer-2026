# เตรียม Final Project Delivery: PocketLedger

**Complete integrated and verified product release · ส่ง 13 ธันวาคม 2026 เวลา 23:59 · 100 คะแนน (10%)**

อิง [Final handout 6 หน้า](project_final_delivery_v1.pdf) ที่อ่านครบ ใช้ทีม หัวข้อ และ repo เดิมพร้อม approved changes งานนี้ต้องพิสูจน์ **ทั้งผลิตภัณฑ์บน final version** ผลผ่านเก่าของแต่ละ Lab ใช้แสดงประวัติได้ แต่ไม่ยืนยันว่าฉบับสุดท้ายยังทำงานถูกต้อง

## Rubric ฉบับ Final handout

| Part | คะแนน | ต้องพิสูจน์ |
| --- | ---: | --- |
| A Final working product | 35 | Required workflows/rules ครบสาม sprints, calculations/transitions/persistence/access และ failure handling |
| B Process and team evidence | 15 | Contractก่อนcode, Issues/branches/tests/reviews/integration/releases และ meaningful participation ทั้งคู่ |
| C Final traceability | 20 | Complete final SRS/features/system SDS/all feature contracts/AC/STS และ verification/result/final version ครบ baseline |
| D Final QA and DoD | 20 | Final build/regression/CI, independent UAT/re-tests, defect/debt/DoD, reproducible deployment |
| E Demonstration video | 10 | Actual deployed product ที่ทั้งสองคน present ร่วมกัน พร้อม version, journeys, rule และ rejected/failure case |

Master rubric แบ่ง video/release-summary points ต่างจาก handout นี้; อย่านำคะแนนสองฉบับมาบวกกัน

## จุดขัดแย้งเรื่องวิดีโอ

Final handout §2 ระบุไม่เกิน **10 นาที** แต่ §3.5 ซึ่งเป็น scored Part E ระบุ maximum **4 นาที** ต้องถามอาจารย์/TA และบันทึกคำตอบก่อน final recording การเตรียม demo ให้กระชับไม่ใช่หลักฐานว่าข้อขัดแย้งถูกตัดสินแล้ว

| สิ่งที่ต้องยืนยัน | คำตอบ/วันที่/แหล่ง |
| --- | --- |
| ระยะเวลาวิดีโอที่ใช้ตรวจจริง | |
| หากมี rubric ฉบับแก้ไข ให้เก็บ reference | |

วิดีโอต้องแสดงแอปที่รันจริง โดยทั้งสองคน present ร่วมกันตาม handout ไม่แยกทำผ่าน video conference call ใส่ YouTube link ที่ผู้มีลิงก์เปิดดูได้ พร้อม timestamp index และ assessed release ใน PDF Part E

## Final evidence ที่ต้องมี

- Completion table ครบทุก baseline requirement/feature/approved change; financial flows, correct balances, ownership และ Admin privacy boundary อยู่ครบ
- Final SRS, feature inventory, System-Level SDS และ feature contracts/AC/STS ตรงกับ behavior, data, access และ deployment design ที่ release แล้ว
- Final verification matrix ระบุ actual file/test/measurement, result และ final SHA; ผล NFR ต้องเทียบกับ target ที่กำหนดไว้จริง ไม่แต่ง benchmark ที่ SRS ไม่ได้ขอ
- Final build, meaningful automated regression, integration และ acceptance รันบน final commit โดยไม่ปิด required tests หรือทำให้ assertions อ่อนลง
- Latest relevant independent UAT/re-tests จาก Lab 6 และ affected fixes/changes ระบุ tester, expected/actual และ version
- Defect register ระบุ severity, affected behavior, fix/re-test version และ blockers; technical debt ไม่ใช้แทน required feature ที่ไม่เสร็จ
- Reviewed final main release → CI/deploy → public URL/running version พร้อมตรวจ persisted data หลัง restart/redeploy ที่เกี่ยวข้อง
- Reproducible Docker/env/migrate/seed/run/build/test/deploy และ synthetic access ที่ส่งส่วนตัว โดยคง repo/service ให้ตรวจได้จนจบ grading
- Two selected Issue/PR history chains **จากคนละ sprint**, actual test excerpts สองส่วน (domain/cross-feature และ access), meaningful red/green และ versions

## รูปแบบส่ง

ส่ง self-contained PDF หนึ่งไฟล์ พร้อมข้อมูลทีม หัวข้อ repo, immutable release, public URL/served version และ navigation A–E ตามหน้าจริง ใช้ [report outline](report-outline.md)

ใส่ complete final engineering documents ใน PDF เดียว ตาม §3.3 ใช้ appendices และ internal page references เพื่อลดเนื้อหาซ้ำ ไม่เพิ่มสำเนาไฟล์เดิมทุก Part ใส่ contributions, brief AI-use และ known limitations ครั้งเดียว แล้วชี้กลับไปหน้าที่เกี่ยวข้อง

ส่ง actual video แยกเป็น YouTube link ตาม §4.1 โดยภาพและข้อความใน PDF ยังต้องเพียงพอให้ตรวจงานวิศวกรรมได้ ส่วนวิดีโอต้องแสดง running product แทนการใช้ slides เพียงอย่างเดียว

## ลำดับปิดงาน

1. ก่อน 29 พ.ย.: ให้ผลิตภัณฑ์ substantially complete และมี bounded remaining-work plan สำหรับช่วงสอบ 1–11 ธ.ค.
2. ปิด accepted critical defects และ remaining required work พร้อม affected independent re-tests
3. สรุป scope/final contracts, integrate และ release; รัน final checks บน assessed version และ deploy ให้ตรงกัน
4. ประกอบ PDF จาก canonical documents กับ selected final evidence แล้วตรวจตาม rubric
5. ยืนยันข้อกำหนด video บันทึกแอป version เดียวกัน ตรวจสิทธิ์เปิด link แล้ว final print/check ก่อนส่ง

ยังไม่มี accepted final release, final test results หรือ video ในรอบเตรียมงานนี้ ดู [product assessment plan](https://github.com/Palapluem/pocket-ledger/blob/main/docs/assessment-plan.md) และ [release record](https://github.com/Palapluem/pocket-ledger/blob/main/docs/releases.md) สำหรับงานจริงต่อไป
