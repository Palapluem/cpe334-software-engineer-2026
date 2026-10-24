# CPE334 Midterm Practice Set

These student-created materials are for study and timed practice. They are not actual or officially approved examinations, and they do not predict the questions on the real exam. The cover reproduces institutional exam-paper fields; its publication checkbox and committee/signature lines are layout examples, not records of actual permission or approval. The set is published as a practice resource in this repository.

## Midterm

- [ข้อสอบภาษาไทย 100 คะแนน: 12 ข้อหลัก 17 หน้ารวมปก](midterm/output/pdf/CPE334_Midterm_Mock_Exam.pdf)
- [ข้อสอบภาษาอังกฤษ 100 คะแนน: 12 ข้อหลัก 17 หน้ารวมปก](midterm/output/pdf/CPE334_Midterm_Mock_Exam_EN.pdf)
- [เฉลยภาษาไทยฉบับเดียว: คำตอบกระชับและเกณฑ์ตรวจ 15 หน้า](midterm/output/pdf/CPE334_Midterm_Mock_Solutions.pdf)

ฉบับอังกฤษแปลหน้าปก คำชี้แจง เงื่อนไข โจทย์ และตารางครบทุกข้อจากฉบับไทย โดยคงคะแนน ข้อกำหนด R1-R11 สถานการณ์ ตัวเลข ลำดับข้อ และความสูงช่องตอบทุกช่อง ใช้ TH Sarabun New ที่สเกล ขนาดตัวอักษร ระยะบรรทัด และระยะขอบตรงกับฉบับไทย (เนื้อหาประมาณ 14 pt) ปรับถ้อยคำให้กระชับโดยไม่ตัดข้อกำหนด เพื่อให้ทั้งสองภาษามี 17 หน้าและมีข้อ/ข้อย่อยชุดเดียวกันในแต่ละหน้า ไม่แยกข้อ 2.2, ข้อ 4 หรือ RACI เป็นหน้าเพิ่ม แหล่งแก้ไขอยู่ใน `midterm/english/` และใช้เฉลยภาษาไทยอ้างอิงตามหมายเลขข้อเดิม

หน้าปกทั้งสองภาษาใช้ `midterm/frontmatter/cover-layout.tex` เป็นกริดพิกัดร่วมกัน ยึดตำแหน่งจากฉบับไทยสำหรับกรอบเผยแพร่ โลโก้ รหัส/ชื่อวิชา ช่องสอบ กล่องข้อมูลนักศึกษา หัวข้อคำชี้แจง/เงื่อนไข และกล่องลายเซ็น ความยาวถ้อยคำ/เส้นใต้เปลี่ยนตามภาษา แต่ไม่ปล่อยให้ความสูงข้อความเลื่อนส่วนถัดไป

เฉลยจัดทำเฉพาะภาษาไทย ไม่มีไฟล์เฉลยอังกฤษแยก ปรับคำตอบทั้ง 12 ข้อให้เป็นไทยธรรมชาติ คงคำเทคนิคที่ใช้ในข้อสอบ พร้อมอธิบายไทยเมื่อจำเป็น ข้อ 1.1-1.4 ยังตอบข้อย่อยละ 2 บรรทัดในรูป “เป็น... เพราะ...” โดยคงประเภท จุดประสงค์ คุณภาพ วิธีตรวจ ผลคาดหวัง และสิ่งที่ควรปรับ/ยืนยัน ข้อ 2.1 ครบ 8 ด้าน ส่วน 2.2 เป็นย่อหน้าต่อเนื่อง แยกคำตอบจากเกณฑ์ตรวจ คงตาราง ตัวเลข Gherkin คำสั่งและแผนภาพ ไม่ย่อจนเงื่อนไขหรือคำปฏิเสธเปลี่ยน

นำกติกาภาษาและแหล่งข้อมูลจากรอบโพยมาใช้กับเฉลยเดิม ไม่เพิ่มบทสรุปหรือชุดคำถามใหม่: มีแหล่งรายข้อและชื่อไฟล์เต็มท้าย PDF ข้อเสนอที่เติมเองใช้ป้าย “คำอธิบายเสริม” เช่น ค่า NFR และแนวทดสอบ API ส่วน effort 15 คน-วันเดิมถูกนำออกเพราะไม่มีรายการงานรองรับ ใช้การระบุข้อมูลที่ยังขาดและเสนอให้ทีมประเมินก่อนรับกำหนดส่งแทน ไม่อ้างว่าคำนวณ effort จริงได้จากโจทย์

หัวลูกศรใช้สามเหลี่ยมทึบเรียบสำหรับ control flow/การเรียก และหัวเปิดบนเส้นประสำหรับ reply; notification เป็นเส้นทึบหัวเปิด เส้น Git ancestry ไม่มีหัว ปรับ Sequence Diagram ให้เส้นตอบกลับเป็น reply จริงตามคำอธิบาย มีหมายเลขและข้อความไทยครบทุก message ไม่เติมคำตอบลงใน diagram skeleton ของข้อสอบ และไม่แก้ shared style ที่ใช้กับข้อสอบไทย/อังกฤษ

ชุดฝึกนี้อิง blueprint ของ Lecture 10: Requirements/Security 25, Planning/Execution 25, UML/UI 30 และ Git 20 คะแนน ไม่ใช่ข้อสอบทางการหรือคำยืนยันว่าจะออกตรงชุดนี้ เลือก Sequence, Activity, List/Form UI และ Git แบบทำนาย graph กับเขียน commands/redraw เพื่อฝึกทั้งการออกแบบและ repository state ไม่มี Class Diagram ใน midterm; `final/` เป็นพื้นที่เตรียมไว้เท่านั้น

**ข้อมูลสำหรับจำลองการสอบ:** 26 ตุลาคม 2569 เวลา 13.00-16.00 (3 ชั่วโมง), ภาค 1/2569 ชื่อบนชุดฝึกคือ CPE334 Software Engineering และรองรับทั้งกลุ่มปกติและ International วันเวลาและเงื่อนไขนี้ใช้จัดรูปแบบการฝึก ไม่ใช่ประกาศสอบหรือข้อกำหนดจากผู้สอน

คำชี้แจงและเงื่อนไขปรับจากตัวอย่าง CPE241: ทำคำตอบในข้อสอบ เขียนชื่อและรหัสทุกหน้า ใช้ปากกาสีน้ำเงินหรือสีดำ ต่อคำตอบด้านหลังหน้าข้อเดียวกันเมื่อจำเป็น ตั้งสมมติฐานพร้อมให้เหตุผลเมื่อโจทย์ไม่ชัดเจน ไม่ใช้เครื่องคำนวณ และนำกระดาษ A4 1 แผ่นที่เขียนชื่อและรหัสแล้วมาส่งพร้อมข้อสอบ โดยหัก 5 คะแนนหากไม่ส่ง เงื่อนไขเหล่านี้ใช้จำลองการสอบตามคำขอของนักศึกษา ข้อความคณะกรรมการและกล่องลายเซ็นเป็นองค์ประกอบหน้าปกจากแม่แบบ CPE333 สำหรับจำลองรูปแบบข้อสอบ ไม่ได้บันทึกการอนุมัติจริงของชุดฝึกนี้

**การจับเวลา 180 นาที:** แนะนำส่วนที่ 1 จำนวน 45 นาที ส่วนที่ 2 จำนวน 40 นาที ส่วนที่ 3 จำนวน 85 นาที และตรวจคำตอบ 10 นาที เป็นงบเวลาสำหรับการฝึก โดยยังไม่ได้ทดลองจับเวลาผู้สอบจริง ส่วนที่ 3 คงรูปแบบคำสั่ง Sequence/Activity และ Git assumptions ตามแนวอาจารย์ เพิ่มคำอธิบายภาษาไทย และใช้ List/Form ตาม blueprint ของ Lecture 10; เลือก 3 ประเภทจากรายการที่อาจออก จึงไม่ได้ครอบคลุม Use Case และ State Diagram ในชุดเดียว

ทั้งข้อสอบและเฉลยเป็น A4 แนวตั้งทั้งหมด ข้อสอบไทยและอังกฤษอย่างละ 17 หน้ารวมปก คงศัพท์เทคนิคและชื่อระบบที่ใช้ในแนว ตัวโจทย์และเฉลยใช้ TH Sarabun New ประมาณ 14 pt ช่องวาด Sequence ยาว 14 ซม.; Activity สูง 21 ซม.; List View และ Form View แยกคนละหน้า มีกรอบสูง 14 และ 21.5 ซม. ตามลำดับ หน้า List เพิ่มตัวอย่าง Invoice แบบเวกเตอร์สูง 5.1 ซม. เพื่อสาธิต notation ตาม Samples หน้า 5 โดยเว้นพื้นที่ให้ออกแบบ Registration เอง ข้อความใน participant, lane header และ action boxes จัดกึ่งกลางพร้อม padding รอบข้อความ ชื่อ participants, guards, identifiers และ UI wireframes คงภาษาอังกฤษตามแนว; ข้อความอธิบายและเกณฑ์ตรวจใช้ภาษาไทย โดย Sequence Diagram ในเฉลยมีป้ายข้อความภาษาไทยครบทุก message แผนภาพ Activity ขยายเต็มความกว้างเขตพิมพ์ ใช้ฟอนต์ภายใน 9 pt และคง 7 lanes โดยเว้นระยะจาก footer และขอบกระดาษอย่างปลอดภัย

**อ่านโจทย์ UI ให้ตรงคำสั่ง:** Samples หน้า 5 ใช้คำว่า “Design” และให้ Invoice เป็นตัวอย่างสัญลักษณ์ ไม่ใช่ Registration Form ที่เติมคำตอบลงช่องเดิม ส่วน Sequence/Activity ใช้ “Complete” พร้อมโครงภาพให้เติม ชุดฝึกจึงเพิ่มตัวอย่าง Invoice หนึ่งครั้งในข้อ 10 ของทั้งสองภาษา และยังให้วาด List/Form จาก R5-R11; `ui-reference.tex` เก็บภาพตัวอย่างและตัวช่วยวาด textbox/ช่องขีดเฉียงที่ใช้ร่วมกัน เฉลยข้อ 10 วาด List/Form จริงพร้อมช่องอ่านอย่างเดียว, LoV, line items และสถานะ ไม่ใช้เพียงคำว่า RO แทน notation ฉบับอังกฤษใช้ปี ค.ศ. 2026 ที่วันที่และท้ายกระดาษ ส่วนมกราคม 2027 เป็นวันในโจทย์โครงการ

ตรวจรอบ UI วันที่ 24 October 2026: build ไทย/อังกฤษ 17 หน้า และเฉลยไทย 15 หน้า คะแนนยังเป็น 25+25+50 รวม 100 ตรวจภาพหน้าที่เปลี่ยนครบ ส่วนหน้าอื่นเทียบภาพ render กับฉบับก่อนแล้วเหมือนกันทุกพิกเซลที่ 144 dpi หน้าที่เปลี่ยนคือข้อสอบหน้า 8 (กฎการถือ booking) และ 13 (ตัวอย่าง UI); เฉลยหน้า 6 (กฎเดียวกัน) และ 11-12 (UI wireframes) ไม่มี `Overfull` หรือ `Missing character` ใน build รอบสุดท้าย

ตารางข้อ 7.1 จัดข้อความกึ่งกลางทั้งแนวนอนและแนวตั้ง ส่วนตารางคำตอบและช่องเขียนในข้อ 2.1-2.2, 5.1-5.2, 6.4 และ 7.1-7.3 ขยายเท่าที่พื้นที่ของหน้าเอื้อ โดยเว้นระยะจาก footer และขอบกระดาษอย่างปลอดภัย หน้าที่มีตารางหลายชุดหรือเนื้อหาแน่นคงขนาดแถวเดิมเพื่อไม่ให้ล้นหน้า ตารางข้อมูลอ้างอิงและ Gantt ซึ่งใช้พื้นที่หน้าอยู่แล้วคงขนาดเดิม จำนวนหน้าเป็นพื้นที่ของชุดฝึก ไม่ใช่จำนวนหน้าข้อสอบจริงที่ผู้สอนประกาศ ตาราง Gantt แบ่งช่วงวันเพื่อคงขนาดตัวอักษรและช่อง No./Task/Owner/Start/Due

**สถานะการเผยแพร่:** ชุดฝึกและเฉลยนี้เผยแพร่ใน repository นี้ตามคำสั่งของผู้จัดทำ ฟิลด์การเผยแพร่และข้อความรับรอง/ลายเซ็นบนปกเป็นองค์ประกอบจากแม่แบบเพื่อฝึกจัดรูปแบบ ไม่ใช่การอ้างว่าหน่วยงานรับรองหรืออนุญาตข้อสอบชุดนี้อย่างเป็นทางการ

## แหล่งและการดัดแปลง

เลขหน้าต่อไปนี้คือลำดับหน้า PDF เริ่มจาก 1

| ข้อ | แหล่งหลัก | ลักษณะชุดฝึก |
| --- | --- | --- |
| 1-4 | [Lecture 10](../../lectures/Week%2010/CPE334_Lecture10%20-%20Midterm%20Exam%20Prep_Group%20Work%20Project.pdf), หน้า 4-11 | เรียบเรียง/แปล scenario เดิม เพิ่มคำสั่งและพื้นที่ตอบให้ชัด; คะแนน 8/7/4/6 และ rubric เป็นของชุดฝึก |
| 5 | Lecture 10 หน้า 14-21 | คง tasks, durations, owners และวันที่ scenario; เพิ่มบันทึกประชุม RACI และระบุเงื่อนไขการจัดตารางให้ตอบได้ครบ |
| 6-7 | Lecture 10 หน้า 22-26 | คง client facts, goal, anchor และ velocity; แยกงานตอบ/คะแนน และระบุ metadata ที่ทีมยังไม่ตกลง |
| 8-10 | [Midterm Samples by Suthep](../../lectures/Week%2010/CPE334_Midterm%20Samples%20by%20Suthep.pdf), หน้า 1-5 | ใช้ KU Course Registration ฉบับไทยเทียบกับอังกฤษ; Sequence/Activity มี skeleton ให้เติม ส่วน UI ให้ตัวอย่าง Invoice เพื่อดู notation แล้วออกแบบ Registration; เพิ่ม List ตาม blueprint |
| 11-12 | Samples, ข้อ 2.5 และ 2.3 | แปลคำสั่งเป็นไทย คง ExamScore, commits, branches, filenames และลำดับงาน; วาด graph ใหม่เป็น vector |

### แหล่งตรวจเฉลยรายข้อ

ตัวเลขคือหน้า PDF ไม่ใช่เลขสไลด์ ชื่อ Lecture ที่ใช้ในเฉลยหมายถึงไฟล์เต็มตามลิงก์นี้

| ข้อเฉลย | ไฟล์และหน้า | สิ่งที่ใช้ตรวจ |
| --- | --- | --- |
| 1 | [CPE334_Lecture10 - Midterm Exam Prep_Group Work Project.pdf](<../../lectures/Week 10/CPE334_Lecture10 - Midterm Exam Prep_Group Work Project.pdf>) pp. 5-6; [CPE334_Lecture02 Requirement Engineering.pdf](<../../lectures/Week 2/CPE334_Lecture02 Requirement Engineering.pdf>) pp. 14-26 | ชนิด จุดประสงค์ คุณภาพ วิธีตรวจและการปรับข้อกำหนด |
| 2 | Lecture 10 pp. 7-8; Lecture 2 pp. 28-29 | องค์ประกอบ 8 ด้าน ข้อเท็จจริงเดิมกับข้อเสนอเพิ่ม; deadline ไม่ใช่ effort |
| 3 | Lecture 10 p. 9; [CPE334_Lecture05 - Security in SE.pdf](<../../lectures/Week 5/CPE334_Lecture05 - Security in SE.pdf>) pp. 8, 19-23, 34 | AuthN/AuthZ, RBAC/default deny และรหัสตอบกลับตัวอย่าง |
| 4 | Lecture 10 pp. 10-11; Lecture 5 pp. 5-8, 28-38 | จุดโจมตี ขอบเขตความเชื่อถือ CIA และมาตรการ/การทดสอบที่เสนอ |
| 5 | Lecture 10 pp. 14-21; [CPE334_Lecture06 - Project Management.pdf](<../../lectures/Week 6/CPE334_Lecture06 - Project Management.pdf>) pp. 71-96 | WBS, Gantt, milestone, buffer และความหมาย RACI; ค่าตาราง RACI อิง notes ข้อ 5.2 ที่ชุดฝึกเพิ่ม |
| 6 | Lecture 10 pp. 22-23; [CPE334_Lecture07 - Project Execution.pdf](<../../lectures/Week 7/CPE334_Lecture07 - Project Execution.pdf>) pp. 60-64, 94-104 | User story, Gherkin, refinement และ metadata |
| 7 | Lecture 10 pp. 25-26; Lecture 7 pp. 67-72, 114-118 | Anchor/Fibonacci, sprint goal, points และ capacity |
| 8 | [CPE334_Midterm Samples by Suthep.pdf](<../../lectures/Week 10/CPE334_Midterm Samples by Suthep.pdf>) pp. 1-3; [CPE334_Lecture04 UML, SDS Features, STS Features.pdf](<../../lectures/Week 4/CPE334_Lecture04 UML, SDS Features, STS Features.pdf>) p. 13 | R1/R5-R11 และ scenario Draft เดิม/section เต็ม/จ่าย BBL |
| 9 | Samples pp. 1-2, 4; Lecture 4 pp. 13, 16 | ฟอร์มว่างของครั้งแรก workflow, branches, guards และ loops |
| 10 | Samples pp. 1-2, 5; Lecture 4 pp. 111-117 | R5-R11, ช่องอ่านอย่างเดียว/แก้ได้/บังคับ และ line items; List View เพิ่มตามโจทย์ชุดฝึก |
| 11 | Samples pp. 6, 12, 21 | สมมติฐาน Git, ข้อ 2.5 และ model answer |
| 12 | Samples pp. 6, 10-11, 20-21 | สมมติฐาน Git, ข้อ 2.3 และ model answer |

รอบปรับภาษาตรวจโจทย์ชุดฝึกและเฉลยครบทุกข้อ อ่านซ้ำข้อความแนว Lecture 10 pp. 4-26 และ Samples pp. 1-6, 18-21 ร่วมกับผลตรวจหลักการ Lectures 2/4/5/6/7 จากรอบโพย ไม่ได้ตรวจภาพเฉลยต้นฉบับทุกภาพหรือเอกสารในลิงก์ภายนอก แผนภาพในเฉลยเป็นแบบวาดของชุดฝึก ไม่อ้างว่าเป็นภาพเฉลยทางการ [StudyNotes](../../lectures/CPE334_SE_Midterm_StudyNotes.pdf) ใช้ทบทวนเพิ่มได้ แต่ไม่แทนเอกสารหลัก

ข้อที่ต้องแยกบริบท: ข้อ 6 และเฉลยใช้กฎ “ถือการจองได้ไม่เกินหนึ่งรายการต่อวัน” ตรงกับ Lecture 10 หน้า 22-23 ไม่เปลี่ยนเป็นโควตาจำนวนครั้งที่กดทำรายการ และยังต้องยืนยันการนับหลังยกเลิก ตัวเลข NFR, HTTP 403 และรายละเอียด UI เป็นข้อเสนอ/แบบจำลองที่ติดป้าย ไม่ใช่ contract ที่โจทย์กำหนดไว้ทั้งหมด ไม่นำ Group Project/Labs 5-7 ช่วงหลังของ Lecture 10 มารวมเป็นขอบเขตข้อสอบ

ข้อควรระวังจากต้นฉบับ: blueprint หน้า 29 ให้เลือก UML/UI เพียง 3 ประเภท; sample หน้า 6 ขีดฆ่า Class Diagram และย้ายไป Final แม้หน้าอื่นกล่าวถึงหัวข้อนี้; เลข Solution 1.2/1.3 ใน sample ไม่ตรงชนิดโจทย์ จึงจับคู่จากเนื้อหา ไม่คัด requirement เรื่องกรอกเกรดที่ปนในตัวอย่าง UI มาใช้ Lecture 10 หน้า 31 ระบุว่าบางเคสจริงใช้ requirements ภาษาอังกฤษเท่านั้น ชุดฝึกนี้ใช้ไทยตามคำขอนักศึกษา จึงควรอ่าน requirements อังกฤษในเอกสารต้นฉบับประกอบ

## แก้ไขและคอมไพล์

แก้โจทย์โดยตรงที่ `midterm/chapters/questions.tex` และเฉลยที่ `midterm/solutions/answers.tex` ใช้ XeLaTeX พร้อม `exam`, `polyglossia`, `tikz`, `pdfpages`, `geometry`, `lastpage`, `tabularx` และฟอนต์ TH Sarabun New ที่แนบมา ใช้โครงหน้าปกสองคอลัมน์ กล่องข้อมูลนักศึกษา และช่องลายเซ็นว่างตามแม่แบบ CPE333 หน้าปกไม่มีท้ายกระดาษชื่อวิชา; หน้าเนื้อหามีชื่อวิชาและเลขหน้าเป็นตัวเอียง class/font/margins ของเนื้อหาคงตามแม่แบบ โลโก้ PDF ใช้ในการ build ส่วน SVG เก็บเป็นต้นฉบับแก้ไข

จากโฟลเดอร์ `midterm/` ใช้คำสั่งต่อไปนี้ (ไม่ต้องใช้ shell escape หรือดาวน์โหลดฟอนต์):

```bash
mock_build_dir=$(mktemp -d /private/tmp/cpe334-mock-build.XXXXXX)
mkdir -p "$mock_build_dir"/{exam,cover,solutions,main}
(cd chapters && xelatex -halt-on-error -output-directory="$mock_build_dir/exam" exam.tex && xelatex -halt-on-error -output-directory="$mock_build_dir/exam" exam.tex)
cp "$mock_build_dir/exam/exam.pdf" chapters/exam.pdf
(cd frontmatter && xelatex -halt-on-error -output-directory="$mock_build_dir/cover" cover.tex && xelatex -halt-on-error -output-directory="$mock_build_dir/cover" cover.tex)
cp "$mock_build_dir/cover/cover.pdf" frontmatter/cover.pdf
(cd solutions && xelatex -halt-on-error -output-directory="$mock_build_dir/solutions" solutions.tex && xelatex -halt-on-error -output-directory="$mock_build_dir/solutions" solutions.tex)
xelatex -halt-on-error -output-directory="$mock_build_dir/main" main.tex
cp "$mock_build_dir/main/main.pdf" output/pdf/CPE334_Midterm_Mock_Exam.pdf
cp "$mock_build_dir/solutions/solutions.pdf" output/pdf/CPE334_Midterm_Mock_Solutions.pdf
mkdir -p "$mock_build_dir/english"
(cd english && xelatex -halt-on-error -output-directory="$mock_build_dir/english" exam.tex && xelatex -halt-on-error -output-directory="$mock_build_dir/english" exam.tex)
cp "$mock_build_dir/english/exam.pdf" output/pdf/CPE334_Midterm_Mock_Exam_EN.pdf
```

`main.tex` รวม cover PDF และ chapter PDF ทีละหน้าเป็น A4 แนวตั้ง จำนวนหน้าปกอ่านจาก chapter PDF ส่วน footer ใช้ LastPage หลัง build ให้ render ตรวจทุกหน้าก่อนใช้งาน แล้วล้างเฉพาะ temporary directory ที่คำสั่งสร้างไว้ เก็บ `frontmatter/cover.pdf` และ `chapters/exam.pdf` เพราะ wrapper ใช้จริง ไม่เก็บ aux/log หรือ QA scripts ใน repo พิมพ์ที่ขนาดจริง 100% เพื่อรักษาขนาดตัวอักษรและพื้นที่ตอบ
