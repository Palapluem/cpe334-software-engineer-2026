# CPE334 Midterm Practice Set

These student-created materials are for study and timed practice. They are not actual or officially approved examinations, and they do not predict the questions on the real exam. The cover reproduces institutional exam-paper fields; its publication checkbox and committee/signature lines are layout examples, not records of actual permission or approval. The set is published as a practice resource in this repository.

## Midterm editions

| Edition | Thai | English | Use |
| --- | --- | --- | --- |
| Core mock exam, 17 pages | [ข้อสอบชุดหลัก](midterm/output/pdf/CPE334_Midterm_Mock_Exam.pdf) | [Core mock exam](midterm/output/pdf/CPE334_Midterm_Mock_Exam_EN.pdf) | Questions 1-12 only: 3 parts, 100 marks, 3 hours |
| Full practice booklet, 21 pages | [ข้อสอบพร้อมแบบฝึกเสริม](midterm/output/pdf/CPE334_Midterm_Mock_Exam_With_Supplements.pdf) | [Full practice booklet](midterm/output/pdf/CPE334_Midterm_Mock_Exam_EN_With_Supplements.pdf) | The same core paper followed by S1-S3, which are outside the 100 marks and 3 hours |

| Answer key | Thai | Contents |
| --- | --- | --- |
| Core edition, 15 pages | [เฉลยชุดหลัก](midterm/output/pdf/CPE334_Midterm_Mock_Solutions.pdf) | Answers and marking guide for Questions 1-12 |
| Full practice booklet, 18 pages | [เฉลยพร้อมแบบฝึกเสริม](midterm/output/pdf/CPE334_Midterm_Mock_Solutions_With_Supplements.pdf) | Core answers followed by answers to S1-S3 |

เฉลยคงเป็นภาษาไทยตามที่กำหนดไว้ก่อนหน้า และไม่มีฉบับเฉลยอังกฤษ ฉบับอังกฤษของข้อสอบแปลหน้าปก คำชี้แจง เงื่อนไข โจทย์ และตารางครบทุกข้อจากฉบับไทย โดยคงคะแนน ข้อกำหนด R1-R11 สถานการณ์ ตัวเลข ลำดับข้อ และพื้นที่คำตอบ ใช้ TH Sarabun New ที่สเกล ขนาดตัวอักษร ระยะบรรทัด และระยะขอบตรงกับฉบับไทย (เนื้อหาประมาณ 14 pt)

**ความแตกต่างระหว่างไฟล์:** ไฟล์ชุดหลักหยุดหลังข้อ 12 และหน้าปกระบุ 17 หน้า ส่วนไฟล์ที่มีแบบฝึกเสริมเป็นข้อสอบชุดหลักเดิมตามด้วย S1-S3 และหน้าปกระบุ 21 หน้า ทั้งสองฉบับยังคงชุดหลัก 100 คะแนน/3 ชั่วโมงเหมือนกัน S1 ใช้ Grades Submission และมี requirements พร้อมตารางระบบภายนอกในหน้า 18 ก่อนพื้นที่วาดหน้า 19; S2 ใช้ Service Ticket ในหน้า 20; S3 ใช้ Git Explain graph พร้อมคำถามหกประเด็นในหน้า 21 ไม่มีการนำข้อเสริมไปคิดคะแนนหรือเพิ่มเวลาให้การสอบหลัก

เฉลยชุดหลักมี 15 หน้า ส่วนเฉลยฉบับเต็มมี 18 หน้า โดยคำตอบ S1-S3 อยู่หน้า 16-18 เฉลยทั้งสองไฟล์เป็นภาษาไทย ไม่มีฉบับเฉลยอังกฤษแยก

ผลตรวจรอบแยก edition: ชุดหลักไทย/อังกฤษ 17 หน้า; ฉบับมี S1-S3 ไทย/อังกฤษ 21 หน้า; เฉลยไทย 15 และ 18 หน้า ทุกไฟล์เป็น A4 แนวตั้ง ตรวจจำนวนหน้าและข้อความหน้าปกแยกตาม edition และตรวจ layout ของหน้าที่ถูกแยกกับหน้าฝึกเสริม เพื่อให้แน่ใจว่าฉบับชุดหลักไม่มีหน้าหรือข้อความ S1-S3 หลงเหลือ

หน้าปกทั้งสองภาษาใช้ `midterm/frontmatter/cover-layout.tex` เป็นกริดพิกัดร่วมกัน ยึดตำแหน่งจากฉบับไทยสำหรับกรอบเผยแพร่ โลโก้ รหัส/ชื่อวิชา ช่องสอบ กล่องข้อมูลนักศึกษา หัวข้อคำชี้แจง/เงื่อนไข และกล่องลายเซ็น ความยาวถ้อยคำ/เส้นใต้เปลี่ยนตามภาษา แต่ไม่ปล่อยให้ความสูงข้อความเลื่อนส่วนถัดไป

เฉลยจัดทำเฉพาะภาษาไทย ไม่มีไฟล์เฉลยอังกฤษแยก คำตอบทั้ง 12 ข้อหลักและ S1-S3 ใช้ไทยธรรมชาติ คงคำเทคนิคที่ใช้ในข้อสอบ พร้อมอธิบายไทยเมื่อจำเป็น ข้อ 1.1-1.4 ยังตอบข้อย่อยละ 2 บรรทัดในรูป “เป็น... เพราะ...” โดยคงประเภท จุดประสงค์ คุณภาพ วิธีตรวจ ผลคาดหวัง และสิ่งที่ควรปรับ/ยืนยัน ข้อ 2.1 ครบ 8 ด้าน ส่วน 2.2 เป็นย่อหน้าต่อเนื่อง แยกคำตอบจากเกณฑ์ตรวจ คงตาราง ตัวเลข Gherkin คำสั่งและแผนภาพ ไม่ย่อจนเงื่อนไขหรือคำปฏิเสธเปลี่ยน S1/S2 มีแผนภาพเวกเตอร์และรายการตรวจตนเอง; S3 มีเหตุผลครบหกข้อและตาราง pointers โดยไม่มีคะแนนเพิ่ม

นำกติกาภาษาและแหล่งข้อมูลจากรอบโพยมาใช้กับเฉลย: มีแหล่งรายข้อและชื่อไฟล์เต็มท้ายเฉลยชุดหลัก ข้อเสนอที่เติมเองใช้ป้าย “คำอธิบายเสริม” เช่น ค่า NFR และแนวทดสอบ API ส่วน effort 15 คน-วันเดิมถูกนำออกเพราะไม่มีรายการงานรองรับ ใช้การระบุข้อมูลที่ยังขาดและเสนอให้ทีมประเมินก่อนรับกำหนดส่งแทน ไม่อ้างว่าคำนวณ effort จริงได้จากโจทย์ แบบฝึกเสริมมีแหล่งและข้อจำกัดของแบบจำลองระบุแยกในแต่ละข้อ

หัวลูกศรใช้สามเหลี่ยมทึบเรียบสำหรับ control flow/การเรียก และหัวเปิดบนเส้นประสำหรับ reply; notification เป็นเส้นทึบหัวเปิด เส้น Git ancestry ไม่มีหัว ปรับ Sequence Diagram ให้เส้นตอบกลับเป็น reply จริงตามคำอธิบาย มีหมายเลขและข้อความไทยครบทุก message ไม่เติมคำตอบลงใน diagram skeleton ของข้อสอบ และไม่แก้ shared style ที่ใช้กับข้อสอบไทย/อังกฤษ

ชุดฝึกนี้อิง blueprint ของ Lecture 10: Requirements/Security 25, Planning/Execution 25, UML/UI 30 และ Git 20 คะแนน ไม่ใช่ข้อสอบทางการหรือคำยืนยันว่าจะออกตรงชุดนี้ เลือก Sequence, Activity, List/Form UI และ Git แบบทำนาย graph กับเขียน commands/redraw เพื่อฝึกทั้งการออกแบบและ repository state ไม่มี Class Diagram ใน midterm; `final/` เป็นพื้นที่เตรียมไว้เท่านั้น

**ข้อมูลสำหรับจำลองการสอบ:** 27 ตุลาคม 2569 เวลา 13.00-16.00 (3 ชั่วโมง), ภาค 1/2569 ชื่อบนชุดฝึกคือ CPE334 Software Engineering และรองรับทั้งกลุ่มปกติและ International วันเวลาและเงื่อนไขนี้ใช้จัดรูปแบบการฝึก ไม่ใช่ประกาศสอบหรือข้อกำหนดจากผู้สอน

คำชี้แจงและเงื่อนไขปรับจากตัวอย่าง CPE241: ทำคำตอบในข้อสอบ เขียนชื่อและรหัสทุกหน้า ใช้ปากกาสีน้ำเงินหรือสีดำ ต่อคำตอบด้านหลังหน้าข้อเดียวกันเมื่อจำเป็น ตั้งสมมติฐานพร้อมให้เหตุผลเมื่อโจทย์ไม่ชัดเจน ไม่ใช้เครื่องคำนวณ และนำกระดาษ A4 1 แผ่นที่เขียนชื่อและรหัสแล้วมาส่งพร้อมข้อสอบ โดยหัก 5 คะแนนหากไม่ส่ง เงื่อนไขเหล่านี้ใช้จำลองการสอบตามคำขอของนักศึกษา ข้อความคณะกรรมการและกล่องลายเซ็นเป็นองค์ประกอบหน้าปกจากแม่แบบ CPE333 สำหรับจำลองรูปแบบข้อสอบ ไม่ได้บันทึกการอนุมัติจริงของชุดฝึกนี้

**การจับเวลา 180 นาที:** แนะนำส่วนที่ 1 จำนวน 45 นาที ส่วนที่ 2 จำนวน 40 นาที ส่วนที่ 3 จำนวน 85 นาที และตรวจคำตอบ 10 นาที เป็นงบเวลาสำหรับการฝึก โดยยังไม่ได้ทดลองจับเวลาผู้สอบจริง ส่วนที่ 3 ของชุดหลักเลือก Sequence/Activity/List+Form ตาม blueprint; Use Case และ State อยู่ในแบบฝึกเสริมท้ายไฟล์ ไม่จับเวลารวมกับชุดหลัก

ทั้งข้อสอบและเฉลยเป็น A4 แนวตั้งทั้งหมด ข้อสอบชุดหลักไทยและอังกฤษอย่างละ 17 หน้า; ฉบับที่มี S1-S3 อย่างละ 21 หน้า คงศัพท์เทคนิคและชื่อระบบที่ใช้ในแนว ตัวโจทย์และเฉลยใช้ TH Sarabun New ประมาณ 14 pt ช่องวาด Sequence ยาว 14 ซม.; Activity สูง 21 ซม.; List View และ Form View แยกคนละหน้า มีกรอบสูง 14 และ 21.5 ซม. ตามลำดับ หน้า List เพิ่มตัวอย่าง Invoice แบบเวกเตอร์สูง 5.1 ซม. เพื่อสาธิต notation ตาม Samples หน้า 5 โดยเว้นพื้นที่ให้ออกแบบ Registration เอง ข้อความใน participant, lane header และ action boxes จัดกึ่งกลางพร้อม padding รอบข้อความ ชื่อ participants, guards, identifiers และ UI wireframes คงภาษาอังกฤษตามแนว; ข้อความอธิบายและเกณฑ์ตรวจใช้ภาษาไทย โดย Sequence Diagram ในเฉลยมีป้ายข้อความภาษาไทยครบทุก message แผนภาพ Activity ขยายเต็มความกว้างเขตพิมพ์ ใช้ฟอนต์ภายใน 9 pt และคง 7 lanes โดยเว้นระยะจาก footer และขอบกระดาษอย่างปลอดภัย

**อ่านโจทย์ UI ให้ตรงคำสั่ง:** Samples หน้า 5 ใช้คำว่า “Design” และให้ Invoice เป็นตัวอย่างสัญลักษณ์ ไม่ใช่ Registration Form ที่เติมคำตอบลงช่องเดิม ส่วน Sequence/Activity ใช้ “Complete” พร้อมโครงภาพให้เติม ชุดฝึกจึงเพิ่มตัวอย่าง Invoice หนึ่งครั้งในข้อ 10 ของทั้งสองภาษา และยังให้วาด List/Form จาก R5-R11; `ui-reference.tex` เก็บภาพตัวอย่างและตัวช่วยวาด textbox/ช่องขีดเฉียงที่ใช้ร่วมกัน เฉลยข้อ 10 วาด List/Form จริงพร้อมช่องอ่านอย่างเดียว, LoV, line items และสถานะ ไม่ใช้เพียงคำว่า RO แทน notation ฉบับอังกฤษใช้ปี ค.ศ. 2026 ที่วันที่และท้ายกระดาษ ส่วนมกราคม 2027 เป็นวันในโจทย์โครงการ

ตรวจรอบ UI วันที่ 24 October 2026: build ไทย/อังกฤษ 17 หน้า และเฉลยไทย 15 หน้า คะแนนยังเป็น 25+25+50 รวม 100 ตรวจภาพหน้าที่เปลี่ยนครบ ส่วนหน้าอื่นเทียบภาพ render กับฉบับก่อนแล้วเหมือนกันทุกพิกเซลที่ 144 dpi หน้าที่เปลี่ยนคือข้อสอบหน้า 8 (กฎการถือ booking) และ 13 (ตัวอย่าง UI); เฉลยหน้า 6 (กฎเดียวกัน) และ 11-12 (UI wireframes) ไม่มี `Overfull` หรือ `Missing character` ใน build รอบสุดท้าย

รอบเทียบโครงภาพ 27 October 2026: ข้อ 5.1 เปลี่ยนจากตารางเป็นต้นไม้ DormFix มีช่อง milestone 1.1-1.4 และช่องงาน 1.1.1-1.4.4 ตาม Lecture 10 pp. 15-16; เฉลยใช้ต้นไม้เดียวกันและเว้นช่องที่ไม่ใช้จริง ข้อ 9 ใช้โครง Activity ร่วมกันทั้งสองภาษา แยก Launch app และ Select Login พร้อม active semester และ profile ทั้งห้าค่า เฉลยเทียบกับ Samples p. 16 แล้วเพิ่มการตรวจผลชำระ/วนกลับเมื่อไม่สำเร็จ และจบที่ Student รับ confirmation ตัวอย่าง UI ยังคงเป็น Invoice สำหรับดู notation ไม่เติมคำตอบ Registration ลงในข้อสอบ

ผลตรวจก่อนเพิ่มแบบฝึกเสริม: ไทย 17 หน้า อังกฤษ 17 หน้า เฉลยไทย 15 หน้า เป็น A4 แนวตั้งทั้งหมด ไม่มีหน้าว่างหรือข้อความล้นขอบหน้า และไม่พบ `Overfull`/`Missing character` ใน build เรนเดอร์ครบ 49 หน้าและตรวจหน้าที่เปลี่ยนโดยละเอียด เทียบภาพที่ 108 dpi กับฉบับก่อน: ไทย/อังกฤษเปลี่ยนเฉพาะหน้า 6 และ 12; เฉลยเปลี่ยนหน้า 4, 5, 9 และ 10 หน้าอื่นเหมือนเดิมทุกพิกเซล ความถูกต้องของการเลือกโจทย์และข้อจำกัดความครอบคลุมดูตารางด้านล่าง ไม่ใช่การรับรองข้อสอบจริง

ตารางข้อ 7.1 จัดข้อความกึ่งกลางทั้งแนวนอนและแนวตั้ง ส่วนตารางคำตอบและช่องเขียนในข้อ 2.1-2.2, 5.2, 6.4 และ 7.1-7.3 ขยายเท่าที่พื้นที่ของหน้าเอื้อ โดยเว้นระยะจาก footer และขอบกระดาษอย่างปลอดภัย ข้อ 5.1 ใช้ต้นไม้ WBS แทนตาราง หน้าที่มีตารางหลายชุดหรือเนื้อหาแน่นคงขนาดแถวเดิมเพื่อไม่ให้ล้นหน้า ตารางข้อมูลอ้างอิงและ Gantt ซึ่งใช้พื้นที่หน้าอยู่แล้วคงขนาดเดิม จำนวนหน้าเป็นพื้นที่ของชุดฝึก ไม่ใช่จำนวนหน้าข้อสอบจริงที่ผู้สอนประกาศ ตาราง Gantt แบ่งช่วงวันเพื่อคงขนาดตัวอักษรและช่อง No./Task/Owner/Start/Due

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
| S1 | Lecture 4 pp. 5-8, 64-65 | โจทย์ Use Case ที่ประยุกต์จาก Grades Submission; ให้ข้อมูลครบก่อนวาด ไม่อ้างว่าเป็นโจทย์ Midterm Samples |
| S2 | Lecture 4 pp. 45-46, 61-62 | ฝึก State ของ Service Ticket โดยระบุให้ยึดเส้นทางเริ่มงานก่อนปิดตามภาพ p. 62 |
| S3 | Samples ข้อ 2.2 pp. 8-9, 19 | คง ancestry/pointers และประเด็นคำถามหกข้อ อธิบายความต่างระหว่าง snapshot กับ remote ปัจจุบัน |

### ขอบเขตชุดหลักและแบบฝึกเสริม

ชุดหลักเป็นการเลือกข้อสำหรับจำลอง 100 คะแนนใน 3 ชั่วโมง ไม่ใช่คลังโจทย์ทุกแบบที่อาจออก จำนวนส่วนและคะแนนตรง blueprint แต่ไม่ควรใช้ชุดนี้แทนการเตรียมทุกทางเลือก

| กลุ่มตามแนว | ในชุดหลัก | สิ่งที่ต้องทบทวนเพิ่ม |
| --- | --- | --- |
| Part 1: requirement, proposal, RBAC, upload security | ข้อ 1-4 ครบทั้งสี่กลุ่ม รวม 25 คะแนน | หลักการ Lecture 1-7 และการเปลี่ยน scenario; คะแนนย่อยของชุดฝึกไม่ใช่คะแนนย่อยที่อาจารย์รับรอง |
| Part 2: WBS 3 / RACI 2 / Gantt 5 / grooming 10 / sprint 5 | ข้อ 5-7 รวม 25 คะแนน | Bug-grooming Issue #15 ใน Lecture 10 p. 24 ต่างจาก enhancement Issue #12 ที่ใช้ในข้อ 6 |
| Part 3: UML/UI เลือก 3 จาก 5 ประเภท | ข้อ 8 Sequence, ข้อ 9 Activity, ข้อ 10 List/Form รวม 30 คะแนน | ท้ายเล่มเพิ่ม **S1 Use Case และ S2 State** จึงมีแบบฝึกทั้งห้าประเภท; [โพยหน้า 2](../cheat-sheet/midterm/output/pdf/CPE334_Midterm_Cheat_Sheet.pdf) ใช้ทบทวนเพิ่ม; Class ใน Samples p. 6 ระบุ Final |
| Git เลือกจาก Predict / Explain / Commands + redraw | ข้อ 11 Predict และข้อ 12 Commands + redraw รวม 20 คะแนน | ท้ายเล่มเพิ่ม **S3 Explain graph**; ยังควรฝึกกรณี Samples 2.1-2.9 ซึ่งสรุปไว้ในโพยหน้า 2 เพราะประเภทเดียวกันเปลี่ยน ancestry/refs ได้ |
| Requirements ภาษาอังกฤษของระบบที่เรียนมาก่อน | ชุดหลักใช้ KU Registration; ท้ายเล่มเพิ่ม Grades และ Ticket พร้อมฉบับอังกฤษ | Lecture 10 p. 31 ยังให้เตรียม POS และ All-in Hotel ด้วย; ไม่ควรจำเฉพาะเคสที่เลือกในชุดนี้ |

การวาดที่ผู้สอบต้องทำต่างกัน: WBS เติมชื่อ milestone/ตัวอักษรงานในต้นไม้, RACI เติมตัวอักษรในตาราง, Gantt ลงงาน/วันที่/เครื่องหมาย/เส้นเชื่อม, Sequence เติม messages บน lifelines, Activity ต่อ workflow จาก prefix ที่ให้ ส่วน UI อ่าน Invoice เพื่อใช้ notation แล้ว **ออกแบบ List/Form เอง** จาก R5-R11 โครงและแผนภาพวาดใหม่สำหรับ A4 แนวตั้ง จึงคงหน้าที่ของแบบฝึกแต่ไม่อ้างว่าเป็นสำเนาภาพต้นฉบับทุกตำแหน่ง

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

แก้โจทย์ไทยที่ `midterm/chapters/questions.tex`, ฉบับอังกฤษที่ `midterm/english/questions.tex` และเฉลยที่ `midterm/solutions/answers.tex` ใช้ XeLaTeX, `exam`, `polyglossia`, `tikz`, `pdfpages`, `geometry`, `lastpage`, `tabularx` และฟอนต์ TH Sarabun New ที่แนบมา หน้าปกสอง edition ใช้กริดเดียวกัน; core cover ไม่กล่าวถึงแบบฝึกเสริมและนับ 17 หน้า ส่วน cover ของฉบับเต็มแจ้ง S1-S3 และนับ 21 หน้า

จาก root ของ repository ใช้คำสั่งต่อไปนี้ (ไม่ต้องใช้ shell escape หรือดาวน์โหลดฟอนต์):

```bash
repo_root=$PWD
mkdir -p "$repo_root/tmp/pdfs"
mock_build_dir=$(mktemp -d "$repo_root/tmp/pdfs/cpe334-mock.XXXXXX")
cd "$repo_root/preparation/mock-exam/midterm"
mkdir -p "$mock_build_dir"/{chapter-full,chapter-core,cover-full,cover-core,main-core,main-full,english-full,english-core,solutions-full,solutions-core}
(cd chapters && xelatex -halt-on-error -output-directory="$mock_build_dir/chapter-full" exam.tex && xelatex -halt-on-error -output-directory="$mock_build_dir/chapter-full" exam.tex)
cp "$mock_build_dir/chapter-full/exam.pdf" chapters/exam.pdf
(cd chapters && xelatex -halt-on-error -jobname=exam-core -output-directory="$mock_build_dir/chapter-core" '\def\MockExamCoreOnly{1}\input{exam.tex}' && xelatex -halt-on-error -jobname=exam-core -output-directory="$mock_build_dir/chapter-core" '\def\MockExamCoreOnly{1}\input{exam.tex}')
cp "$mock_build_dir/chapter-core/exam-core.pdf" chapters/exam-core.pdf
(cd frontmatter && xelatex -halt-on-error -output-directory="$mock_build_dir/cover-full" cover.tex && xelatex -halt-on-error -output-directory="$mock_build_dir/cover-full" cover.tex)
cp "$mock_build_dir/cover-full/cover.pdf" frontmatter/cover-with-supplements.pdf
(cd frontmatter && xelatex -halt-on-error -jobname=cover-core -output-directory="$mock_build_dir/cover-core" '\def\MockExamCoreOnly{1}\input{cover.tex}' && xelatex -halt-on-error -jobname=cover-core -output-directory="$mock_build_dir/cover-core" '\def\MockExamCoreOnly{1}\input{cover.tex}')
cp "$mock_build_dir/cover-core/cover-core.pdf" frontmatter/cover.pdf
(cd solutions && xelatex -halt-on-error -output-directory="$mock_build_dir/solutions-full" solutions.tex && xelatex -halt-on-error -output-directory="$mock_build_dir/solutions-full" solutions.tex)
(cd solutions && xelatex -halt-on-error -jobname=solutions-core -output-directory="$mock_build_dir/solutions-core" '\def\MockExamCoreOnly{1}\input{solutions.tex}' && xelatex -halt-on-error -jobname=solutions-core -output-directory="$mock_build_dir/solutions-core" '\def\MockExamCoreOnly{1}\input{solutions.tex}')
(cd english && xelatex -halt-on-error -output-directory="$mock_build_dir/english-full" exam.tex && xelatex -halt-on-error -output-directory="$mock_build_dir/english-full" exam.tex)
(cd english && xelatex -halt-on-error -jobname=exam-core -output-directory="$mock_build_dir/english-core" '\def\MockExamCoreOnly{1}\input{exam.tex}' && xelatex -halt-on-error -jobname=exam-core -output-directory="$mock_build_dir/english-core" '\def\MockExamCoreOnly{1}\input{exam.tex}')
xelatex -halt-on-error -output-directory="$mock_build_dir/main-core" main.tex
xelatex -halt-on-error -output-directory="$mock_build_dir/main-full" main-with-supplements.tex
cp "$mock_build_dir/main-core/main.pdf" output/pdf/CPE334_Midterm_Mock_Exam.pdf
cp "$mock_build_dir/main-full/main-with-supplements.pdf" output/pdf/CPE334_Midterm_Mock_Exam_With_Supplements.pdf
cp "$mock_build_dir/english-core/exam-core.pdf" output/pdf/CPE334_Midterm_Mock_Exam_EN.pdf
cp "$mock_build_dir/english-full/exam.pdf" output/pdf/CPE334_Midterm_Mock_Exam_EN_With_Supplements.pdf
cp "$mock_build_dir/solutions-core/solutions-core.pdf" output/pdf/CPE334_Midterm_Mock_Solutions.pdf
cp "$mock_build_dir/solutions-full/solutions.pdf" output/pdf/CPE334_Midterm_Mock_Solutions_With_Supplements.pdf
```

`MockExamCoreOnly` omits S1-S3 from the question, cover and answer sources; the default build retains them. `main.tex` combines the core cover with `exam-core.pdf`; `main-with-supplements.tex` combines the extended cover with `exam.pdf`. The persistent component PDFs are build inputs; keep them in the repository. Keep aux/log files only in the temporary build directory, render and inspect all six deliverables, then remove only the temporary directory created for this build. Print at 100% to preserve type size and answer space.
