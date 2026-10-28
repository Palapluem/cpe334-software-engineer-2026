# CPE334 Midterm Practice Set

These student-created materials are for study and timed practice. They are not actual or officially approved examinations and do not predict the real questions. Publication, committee and signature fields reproduce an exam-form layout; they do not record official permission or approval.

## Published files

| File | Format | Contents |
| --- | --- | --- |
| [Bilingual mock exam](midterm/output/pdf/CPE334_Midterm_Mock_TH_EN.pdf) | **33 A4 pages**; page 14 landscape, all other pages portrait | Thai cover; full question prose in English followed by Thai; given content in English-left/Thai-right tables; 3 parts, 12 questions, 100 marks, 3 hours |
| [Thai core solutions](midterm/output/pdf/CPE334_Midterm_Mock_Solutions.pdf) | 16 pages | Answers and marking guide for Questions 1-12, including the revised TokTickIT problems |
| [Thai solutions with supplementary answers](midterm/output/pdf/CPE334_Midterm_Mock_Solutions_With_Supplements.pdf) | 19 pages | The same core answers followed by S1-S3 |

ข้อสอบหลักมีไฟล์เดียว ไม่แยกฉบับไทย อังกฤษ หรือฉบับแนบแบบฝึกเสริม ส่วน S1-S3 ยังเก็บเป็น [source ไทย](midterm/supplements/questions-th.tex) และ [source อังกฤษ](midterm/supplements/questions-en.tex) พร้อมเฉลยไทยเพื่อใช้ฝึกแยก ไม่อยู่ในข้อสอบหลักและไม่นับรวม 100 คะแนนหรือเวลา 3 ชั่วโมง

## รูปแบบ

- หน้าปกยึดฉบับแรกที่เก็บไว้ในประวัติ 24 October 2026: คืนถ้อยคำคำชี้แจงฉบับเต็ม ชื่อส่วน Requirements/Security, Project Planning/Execution และ UML/UI/Git Workflow พร้อมกริด ฟอนต์ ตัวหนา เส้นใต้และระยะบรรทัดเดิม คำชี้แจงเป็นภาษาไทยและใช้ศัพท์เนื้อหารายวิชาตามต้นแบบ ช่องชุดข้อสอบคงความหมาย optional ด้วยคำไทย “ถ้ามี” และกลุ่มนานาชาติใช้ป้ายภาษาไทย
- เงื่อนไขกระดาษสรุปแก้ตามที่นักศึกษายืนยันหลังสอบ: อนุญาต A4 1 แผ่นและ **ไม่ต้องส่งพร้อมข้อสอบ** นำข้อบังคับให้ส่ง ข้อหัก 5 คะแนน และข้อบังคับเขียนชื่อบนกระดาษสรุปที่ยกมาจากเรฟ CPE241 ออก ไม่ใช้กติกาของวิชาอื่นแทนข้อสอบ CPE334
- คำถามและคำสั่งเขียนเป็นย่อหน้าเต็ม **อังกฤษก่อน แล้วตามด้วยภาษาไทยบรรทัดถัดไป** ส่วนข้อมูลที่โจทย์ให้ เช่น สถานการณ์ ข้อความความต้องการ ข้อเสนอ บันทึกประชุม และเงื่อนไข ใช้ตารางสองคอลัมน์ **อังกฤษฝั่งซ้าย ไทยฝั่งขวา** จับคู่เนื้อหาในแถวเดียวกัน ตารางข้อความไม่มีเส้นกรอบตามตัวอย่างอาจารย์ ส่วนตารางงาน สิทธิ์ และ backlog แยกคอลัมน์ข้อความอังกฤษกับไทยให้ตรงกัน
- คง Sarabun และขนาดโจทย์ประมาณ 14 pt; หัว/ท้ายกระดาษเล็กกว่าโจทย์ ไม่ลดฟอนต์เพื่อบีบจำนวนหน้า พื้นที่ตอบใช้ร่วมกันเต็มความกว้าง ไม่แบ่งคำตอบเป็นสองภาษา
- หน้า Gantt เป็นแนวนอนเพียงหน้าเดียว ครบ 20 วันทำงาน มี 14 แถวสำหรับ tasks/milestones/buffer และคอลัมน์ No., Task, Owner, Start, Due; หน้าถัดไปกลับเป็นแนวตั้ง
- ข้อ 8 ให้ actors, use cases และ boundary มาแล้ว ผู้ทำเติมเส้น association, include, extend และ generalization; ข้อ 9 ให้ states มาแล้ว ผู้ทำเติม transitions/events/guards; ข้อ 10 ให้กรอบ List/Form พร้อมตัวอย่าง notation แล้วเติมข้อมูลและ controls
- กราฟ Git ใช้รูปแบบส่วน 2 ของ Samples: แผงสีเทาอ่อนมีกรอบ, monospace `A---B`, ชื่อ refs ใน `[main, origin/main]` ต่อท้าย commit, `[HEAD -> branch]`, เส้น `\`/`/` แยกสายและรวมประวัติ และ `ref -> commit` ใต้กราฟเมื่อวางในบรรทัดไม่พอ คำสั่งอยู่ในแผงแบบเดียวกันและมี `>` นำหน้าเป็น prompt รับคำตอบทั้ง ASCII และภาพวาดหาก ancestry/refs ถูกต้อง ไม่ใช้ผัง `+--` หรือ caret เป็นตัวชี้แทนรูปแบบนี้
- ภาพคนกับวงรีงานและเส้น include/extend/generalization เป็น **Use Case Diagram** ส่วน **State Diagram** แสดง states กับ transitions แยกเป็นคนละข้อ เพื่อไม่ใช้สัญลักษณ์ผิดประเภท

## แผนหน้าและคะแนน

| ส่วน | หน้า | ข้อและคะแนน |
| --- | --- | --- |
| หน้าปก | 1 | 27 ตุลาคม 2569, 13.00-16.00, 3 ชั่วโมง, ภาค 1/2569 |
| Requirements / Security | 2-9 | 1: 8; 2: 7; 3: 4; 4: 6 รวม **25** |
| Planning / Execution | 10-18 | 5: 10; 6: 10; 7: 5 รวม **25**; Gantt หน้า 14 แนวนอน |
| TokTickIT shared requirements | 19-20 | R1-R12 ใช้ร่วมกันในข้อ 8-10 |
| Use Case Diagram | 21-22 | 8: **10** |
| State Diagram | 23 | 9: **10** |
| Role dashboards, Queue and Detail | 24-27 | 10: **10**; dashboard frames are on p.25 |
| Git context | 28 | ข้อสมมติร่วม แต่ข้อ 11/12 เริ่มจาก graph ของตนเอง |
| Git: integrate a feature into `sprint_1` | 29-30 | 11: **10** |
| Git: commands and redraw | 31-33 | 12: **10** |
| **รวม** | **33** | **100 คะแนน** |

ข้อ 1 วิเคราะห์ประเภท จุดประสงค์ คุณภาพ วิธีตรวจ ผลคาดหวังและการปรับข้อความ ข้อ 2 ครบองค์ประกอบข้อเสนอ 8 ด้าน ข้อ 3 ใช้ default deny และไม่มี role inheritance ในระบบ WorkshopHub ข้อ 4 ยึดเหตุการณ์ script รันบน server ไม่เปลี่ยนเป็น XSS ฝั่ง browser

ข้อ 5 คงงาน A-I, owners, durations, วันที่และ buffers ตามแนวเดิม ข้อ 6 คงกฎถือการจองได้ไม่เกินหนึ่งรายการต่อวัน ข้อ 7 คง velocity 16, anchor 3 และ Fibonacci scale

พาร์ท 50 คะแนนใช้ข้อกำหนด TokTickIT แบบย่อในข้อ 8-10 และสถานการณ์ Git ในข้อ 11-12 ทั้งหมดเป็นโจทย์ฝึกที่เรียบเรียงจากเนื้อหารายวิชาและบริบทที่นักศึกษาเล่า ไม่ใช่การถอดข้อสอบจริงหรือการคัดกฎจากแลปมาทั้งหมด ใน R1 กำหนดให้ Administrator เป็นชนิดย่อยของ IT Staff **เฉพาะในแบบจำลองของโจทย์นี้** เพื่อฝึก generalization ไม่ได้หมายความว่า RBAC ทุกระบบต้องจัดบทบาทแบบเดียวกัน ข้อ 8 ให้เติมความสัมพันธ์ระหว่าง node ที่แสดงไว้แล้ว ส่วนข้อ 9 ใช้เฉพาะ state transitions ที่ระบุใน R8-R10

ข้อ 11 คงจุดเริ่มตามที่นักศึกษาจำได้จากข้อสอบจริง คือ `main` ชี้ไป C และ `sprint_1` ชี้ไป D ซึ่งแยกจาก B ส่วนโจทย์ฝึกเพิ่ม branch `feature/load_scores` ที่ E และใช้สถานการณ์ ExamScore สำหรับฝึก merge รายละเอียดและเหตุการณ์ที่เหลือเป็นโจทย์ฝึก ไม่ใช่ข้อความจากข้อสอบจริง ให้ stage เฉพาะ `score_data.py` แล้วบันทึกการแก้เป็น F จากนั้น merge feature เข้า `sprint_1` ให้เกิด G และสลับกลับ `main` โดยไม่ push ข้อ 12 เป็นอีกสถานการณ์หนึ่ง: D และ E อยู่บน feature branch เดียวกัน จึงฝึก fast-forward และสร้าง F หลัง stage สามไฟล์ตาม commit message ที่กำหนด หากโจทย์ไม่ได้สั่ง fetch หรือ push ให้คง remote-tracking refs ไว้ และห้ามใช้ `git add .`

## ความครอบคลุมและแหล่งข้อมูล

Lecture 10 ให้ฝึก UML/UI ห้าประเภท (Use Case, Activity, Sequence, State, List/Form) และเลือกรูปแบบ Git สองจากสาม ชุดหลักนี้เลือก Use Case, State, List/Form และ Git Predict/Commands; **Activity และ Sequence ยังเป็นขอบเขตที่ต้องทบทวน** ไม่ได้ตัดออกจากเนื้อหาวิชาเพราะไม่อยู่ในชุดฝึกฉบับนี้ Class ใน Samples p. 6 ระบุว่าเป็น Final

| ข้อ | แหล่งหลัก | การดัดแปลง |
| --- | --- | --- |
| 1-4 | [Lecture 10](<../../lectures/Week 10/CPE334_Lecture10 - Midterm Exam Prep_Group Work Project.pdf>) pp. 4-11 | WorkshopHub, proposal, RBAC และ upload incident; เพิ่มคำชี้แจง/พื้นที่ตอบและคะแนนย่อยของชุดฝึก |
| 5 | Lecture 10 pp. 14-21 | คง tasks, owners, durations, วันที่และ buffers; meeting notes ของ RACI เพิ่มเพื่อให้กรอกครบ |
| 6-7 | Lecture 10 pp. 22-26 | คง client facts, sprint goal, anchor และ velocity |
| 8-10 | [Lecture 4](<../../lectures/Week 4/CPE334_Lecture04 UML, SDS Features, STS Features.pdf>) pp. 5-8, 45-46, 111-117; บริบท TokTickIT จากคำบอกเล่านักศึกษา | แต่ง R1-R12 ให้ตอบได้ในตัวเอง; ไม่ใช่ R1-R11 ของ KU Registration ใน Samples |
| 11 | [Midterm Samples](<../../lectures/Week 10/CPE334_Midterm Samples by Suthep.pdf>) pp. 6, 12, 21; ความทรงจำหลังสอบของนักศึกษา | คงจุดเริ่มที่จำได้ว่า main อยู่ C และ `sprint_1` อยู่ D จาก B; เพิ่ม feature branch และส่วนที่เหลือเป็นโจทย์ฝึก ไม่ใช่การคัด graph หรือเนื้อหาข้อสอบจริง |
| 12 | Samples pp. 6, 10-11, 20-21 | คง 2.3: ancestry, refs, filenames และ commit message; ใช้กราฟเรียงบรรทัด/วงเล็บและแผงคำสั่งตามรูปแบบต้นฉบับ |
| S1 | Lecture 4 pp. 5-8, 64-65 | Grades Submission Use Case; ฝึกแยกจาก TokTickIT |
| S2 | Lecture 4 pp. 45-46, 61-62 | Service Ticket State ตามตัวอย่างใน Lecture ไม่ใช่ state rules ของข้อ 9 ใหม่ |
| S3 | Samples pp. 8-9, 19 | Explain graph ตาม 2.2 ครบหกคำถาม |

รูปแบบคำถามอังกฤษก่อนและภาษาไทยบรรทัดถัดไปเทียบกับ Samples pp. 1-2 ส่วนหน้าปกเทียบ source และ PDF ฉบับแรกใน commit `86647f0` โดยคงวันสอบเป็น 27 ตุลาคม 2569 ข้อสอบฉบับนี้มี 33 หน้า และปรับเฉพาะกติกากระดาษสรุปตามข้อมูลสอบจริงที่นักศึกษายืนยัน เลขหน้าแหล่งข้อมูลนับจากหน้าแรกของ PDF ไม่ใช่หมายเลขสไลด์

หลักการตรวจเฉลยยังอิง Lecture 2 pp. 14-29 (requirements/proposal), Lecture 5 pp. 5-8, 19-23, 28-38 (security), Lecture 6 pp. 71-96 (WBS/Gantt/RACI) และ Lecture 7 pp. 60-72, 94-104, 114-118 (grooming/planning) รับคำตอบอื่นที่ตรงข้อกำหนดและมีเหตุผล เกณฑ์คะแนนและตัวอย่างคำตอบเป็นของชุดฝึก ไม่ใช่เฉลยทางการ

## แก้ไขและคอมไพล์

- `midterm/main.tex`: จุดเริ่มต้นข้อสอบ
- `midterm/bilingual/questions.tex`: ข้อความคู่ภาษา โดย source รับ argument ไทยก่อน/อังกฤษหลัง แต่ macro แสดงอังกฤษก่อนและไทยบรรทัดถัดไป
- `midterm/bilingual/exam.tex`: layout, table macros, answer spaces และ Gantt
- `midterm/bilingual/ticket-diagrams.tex`: actors/use cases/states และ blank UI scaffolds; ภาพโจทย์ไม่มีเส้นคำตอบ
- `midterm/bilingual/cover.tex`, `frontmatter/cover-layout.tex`, `exam-info.tex`: ข้อความปก กริดและข้อมูลสอบ
- `midterm/solutions/answers.tex`: เฉลยไทยและเกณฑ์ตรวจ
- `midterm/style.tex`: รูปแบบร่วม รวม `gitpanel` สำหรับกราฟ/คำสั่ง; `midterm/git-explain-graph.tex` เป็น snapshot S3 ที่ใช้ร่วมกันในโจทย์และเฉลย

จาก root ของ repository:

```bash
python3 preparation/mock-exam/midterm/build.py
```

ใช้ XeLaTeX สองรอบกับฟอนต์ที่แนบมา ไม่ดาวน์โหลดฟอนต์และไม่ใช้ shell escape สคริปต์ปฏิเสธข้อความล้น อักษรหายและ references ที่ยังไม่ resolve แล้วลบ aux/log ของรอบนั้นอัตโนมัติ ใช้ `--output-dir <folder>` สร้าง candidate เพื่อตรวจ render ก่อนแทนไฟล์เผยแพร่

เฉลยคอมไพล์ `midterm/solutions/solutions.tex` สองรอบจากโฟลเดอร์ `solutions` โดยส่ง `-output-directory` ไป build directory ชั่วคราว ปกติรวม S1-S3; นิยาม `MockExamCoreOnly` ก่อน input เพื่อสร้างเฉพาะข้อ 1-12 ไม่สร้าง component PDFs ค้างใน source

## ตรวจฉบับ 28 October 2026

ตรวจ PDF ทั้ง 33 หน้า รวมถึงเลขหน้า เนื้อหาข้อ 1-12, R1-R12, คะแนนรวม 25+25+50 และตำแหน่ง Git refs ข้อมูลโจทย์จับคู่ในตารางอังกฤษซ้าย-ไทยขวา ส่วนคำถามและคำสั่งยังเป็นย่อหน้าเต็ม ตรวจเทียบข้อความก่อนและหลังจัดตารางแล้วไม่มีคำถามหรือข้อมูลถูกตัดออก ไม่พบหน้าว่าง แถวคู่ภาษาถูกแยกข้ามหน้า หรือกล่องคำตอบหลุดไปอีกหน้า หน้า 14 เป็นแนวนอนเพียงหน้าเดียว แผนภาพเป็น vector และไม่มีเส้นเฉลยในโจทย์ ตรวจทิศ include/extend/generalization และ state transitions เทียบกับเฉลยแล้ว สำหรับข้อ 11 ตรวจว่า C อยู่บน `main` และ D อยู่บน `sprint_1` ซึ่งแยกจาก B ส่วน feature branch และเหตุการณ์หลังจากนั้นระบุไว้ชัดว่าเป็นรายละเอียดสำหรับโจทย์ฝึก

ข้อสอบเก่า `TH_EN.pdf` ถูกแทนด้วยชื่อเต็มที่ลิงก์ไว้ด้านบน เฉลยยังเป็นไทยสองไฟล์ตามเดิม พิมพ์ที่ 100% และตั้งตามขนาด/ทิศทางหน้า PDF เพื่อรักษา Gantt แนวนอน
