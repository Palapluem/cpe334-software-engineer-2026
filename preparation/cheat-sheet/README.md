# CPE334 Midterm Cheat Sheet

[เปิดโพย PDF สองหน้า](midterm/output/pdf/CPE334_Midterm_Cheat_Sheet.pdf) · [ต้นฉบับ LaTeX](midterm/cheat-sheet.tex) · [ชุดฝึกและเฉลย](../mock-exam/README.md)

สื่อทบทวนของ วิศิษฐ์ สุวรรณเนาว์ 67070501042 สำหรับ CPE334 Software Engineering: หน้าแรกสรุป Lecture 1-7 หน้าที่สองเป็น Practice Midterm ตาม Lecture 10 และ Midterm Samples ไม่ใช่การรับรองว่าข้อสอบจริงจะตรงกับตัวอย่าง

ฉบับปรับ 27 October 2026 เตรียม UML/UI **ครบทั้ง 5 ประเภท** ตาม Lecture 10 หน้า 29 (ข้อสอบเลือก 3 จาก 5 แบบละ 10 คะแนน) ไม่เลือกอ่านเองเพียง 3 ประเภท: มีตารางวิธีเริ่มทำแต่ละแบบ, Sequence/Activity/UI ของ KU Registration, Use Case ของ Grades Submission ที่เพิ่มเป้าหมายและ external actors ทั้งระบบ และ State ของ Ticket พร้อมเงื่อนไขเปรียบเทียบกับ Registration/Grades ภาพประยุกต์เหล่านี้ใช้ฝึกวิเคราะห์ requirements ไม่ใช่ภาพเฉลยทางการ

หน้าแนวสอบยังมี Part 1-2 ครบกลุ่มโจทย์ เพิ่มบริบทสี่ระบบที่อาจารย์ให้เตรียม และสรุปกรณี Git A-I พร้อมแม่แบบคำสั่งและชุดไฟล์/ข้อความ commit ตามรูปแบบข้อสอบที่กำหนด ได้แก่ ทำนาย graph, อธิบาย graph และเขียน commands พร้อมวาด graph กราฟ Git ในโพยเป็นภาพย่อเฉพาะช่วงที่เปลี่ยน ต้องใช้ผลและตัวชี้ในตารางประกอบ ไม่ใช่การคัดโจทย์และกราฟทุกหน้าไว้ครบ

ฉบับนี้ปรับภาษาไทยให้เป็นธรรมชาติ คงศัพท์เทคนิค สูตร เงื่อนไขและคำปฏิเสธ ใช้คำว่า **“เพิ่มเติม”** กำกับตัวอย่างที่ขยายจากเนื้อหาหลัก ภาพวาดย่อเป็นสื่อช่วยจำ ไม่ใช่ screenshot แอป ผลทดลองหรือภาพเฉลยทางการ

Use Case แสดงทิศทางแยกครบทั้ง `<<include>>` (base → งานบังคับ), `<<extend>>` (ส่วนเสริม → base พร้อมเงื่อนไข) และ generalization (child → parent; สามเหลี่ยมโปร่งชี้ parent) โดยอ้างตัวอย่าง Cashier/Manager → User จาก Lecture 4 หน้า 7 ส่วนโจทย์ Grades Submission ใช้ include/extend ตาม requirement และไม่ฝืนวาด generalization เพราะโจทย์ไม่ได้กำหนด actor หรือ use case แบบ parent-child

ยังเป็น **A4 แนวตั้ง 2 หน้า หน้าละ 4 คอลัมน์** ตาม [เรฟ CPE241](<ref/CPE241 Cheat Sheet M3.pdf>) ไม่มีหัวกระดาษ เลขหน้าหรือ legend ท้ายหน้า มีเพียงกรอบชื่อ/รหัส แหล่งอ้างอิง ตารางศัพท์และคำถามฝึกจึงอยู่ใน README นี้ ไม่เพิ่มหน้าให้โพย

รอบเพิ่มบริบทโจทย์: Part 2 มีชื่อและความหมายของงาน DormFix A-I ครบ พร้อมผู้ทำ จำนวนวัน และวันที่ทำ/เผื่อในตารางสามคอลัมน์ ไม่ใช้ช่องวันที่กว้างจนรายละเอียดงานหาย เพิ่มบทบาททีม/ผู้อนุมัติ, anchor ของ ShuttleNow, ข้อมูล bug variant และ O/M/P ของงาน PERT ทั้งหกก่อนแสดงผลรวม ส่วน UML ระบุ Req IDs/ข้อมูล master และความหมายตัวย่อในภาพ; Form แสดง profile ทั้งห้าช่องแยกกันด้วยกรอบขีดเฉียงจริง มี semester/status/total ในแถวเดียว และตัวเลือก card/KBank หรือ transfer/BBL หลังตรวจที่นั่งผ่าน; Git เติมไฟล์ที่แก้/สร้าง ขั้น inspect และข้อความ commit ที่ใช้ในตัวอย่าง

รอบตรวจ UI: แยกคำสั่ง Complete ที่ให้เติมโครง ออกจาก Design ที่ต้องออกแบบจาก requirements; Invoice ใน Samples หน้า 5 เป็นตัวอย่าง notation เพิ่มลำดับคิดจาก req ไป header/line items, label/textbox, required/edit/read-only/LoV และ controls ตาม role/state/error พร้อมอธิบายว่า offering รวม course/semester/section และค่าที่ prefill อาจยังเป็น read-only ได้ Activity ย้าย merge เหนือ Select / edit ให้มีช่วงลูกศรชัด แบ่งข้อความ Select/Warn/Done เป็นสองบรรทัด และนำ diamond ที่มีทางเข้า/ออกอย่างละหนึ่งเส้นออกเพื่อไม่สื่อว่าเป็น merge ของหลายทาง โดยไม่ลดฟอนต์

ชื่องาน A-I ใช้ภาษาอังกฤษตามคำหลักใน Lecture 10 pp. 14-16 เพื่อฝึกอ่านโจทย์และเชื่อมกับ WBS/RACI/Gantt โดยย่อถ้อยคำ ไม่อ้างว่าเป็นการคัดโจทย์เต็ม คงเงื่อนไข C/G ใช้ approved requirements, A/I ใช้ approved designs, D ทดสอบสองส่วนร่วมกัน และ H ส่งระบบที่ทดสอบแล้วให้ตรวจรับ แยกผู้อนุมัติ B/F/H ไว้ในบริบท และใช้ชื่อ milestone `Requirements approved`, `Designs approved`, `System accepted` ใน WBS ส่วนวิธีคิดและคำอธิบายยังเป็นไทย

ใช้พื้นที่จากการลดข้อความซ้ำ จัดหัวข้อข้อกำหนดให้กระชับ รวมคำสั่งที่สั้นพอ และลดช่องไฟแนวตั้งของ Sequence/Activity เล็กน้อยโดยไม่ลดตัวอักษรในภาพ คำสั่ง/ชื่อไฟล์ใช้ Sarabun ตัวหนาสีน้ำเงินแทน Menlo แต่คง `--`, `_` และเครื่องหมายคำพูดตรงตามคำสั่งจริง

## แหล่งหลักและวิธีอ่านเลขหน้า

เลขหน้าทั้งหมดเป็น **ลำดับหน้า PDF เริ่มที่ 1** ไม่ใช่เลขสไลด์บนหน้า โดยเฉพาะ Lecture 6-7 ที่เลขสองแบบไม่ตรงกัน ชื่อย่อในหัวข้อถัดไปอ้างชื่อไฟล์เต็มในตารางนี้

| ชื่อย่อ | ไฟล์หลัก | ขอบเขตที่อ่าน |
| --- | --- | --- |
| Lecture 1 | [CPE334_Lecture01 Introduction.pdf](<../../lectures/Week 1/CPE334_Lecture01 Introduction.pdf>) | ข้อความ pp. 1-46 |
| Lecture 2 | [CPE334_Lecture02 Requirement Engineering.pdf](<../../lectures/Week 2/CPE334_Lecture02 Requirement Engineering.pdf>) | ข้อความ pp. 1-43 |
| Lecture 3 | [CPE334_Lecture03 Specifications, SDD, Testing, TDD.pdf](<../../lectures/Week 3/CPE334_Lecture03 Specifications, SDD, Testing, TDD.pdf>) | ข้อความ pp. 1-59 |
| Lecture 4 | [CPE334_Lecture04 UML, SDS Features, STS Features.pdf](<../../lectures/Week 4/CPE334_Lecture04 UML, SDS Features, STS Features.pdf>) | ข้อความ pp. 1-161; ไม่ได้ตรวจรายละเอียดภาพทุกสไลด์ |
| Lecture 5 | [CPE334_Lecture05 - Security in SE.pdf](<../../lectures/Week 5/CPE334_Lecture05 - Security in SE.pdf>) | ข้อความ pp. 1-40 |
| Lecture 6 | [CPE334_Lecture06 - Project Management.pdf](<../../lectures/Week 6/CPE334_Lecture06 - Project Management.pdf>) | ข้อความ pp. 1-116 |
| Lecture 7 | [CPE334_Lecture07 - Project Execution.pdf](<../../lectures/Week 7/CPE334_Lecture07 - Project Execution.pdf>) | ข้อความ pp. 1-171 |
| Lecture 10 | [CPE334_Lecture10 - Midterm Exam Prep_Group Work Project.pdf](<../../lectures/Week 10/CPE334_Lecture10 - Midterm Exam Prep_Group Work Project.pdf>) | pp. 1-31 เฉพาะ Midterm Review |
| Samples | [CPE334_Midterm Samples by Suthep.pdf](<../../lectures/Week 10/CPE334_Midterm Samples by Suthep.pdf>) | ข้อความ pp. 1-26; ตรวจภาพโจทย์ Sequence/Activity และตัวอย่าง notation UI pp. 3-5 เพิ่ม |

ตรวจภาพต้นฉบับเพิ่มเติมที่ Invoice UI ใน Samples p. 5, Ticket State ใน Lecture 4 p. 62 และ Gantt worked example ใน Lecture 10 p. 20 เพื่อไม่อาศัย text extraction อย่างเดียว **ไม่ได้ตรวจภาพ UI/เฉลยทุกภาพในสไลด์ หรือเอกสารที่ลิงก์ออกนอกไฟล์** จึงไม่อ้างว่าอ่านรายละเอียดภายในภาพทุกหน้าครบแล้ว

## A. ภาพรวม: แต่ละบทต่อกันอย่างไร

เริ่มจากปัญหาและคุณค่าที่ต้องส่งมอบ (Lecture 1) เปลี่ยนความต้องการให้เป็นข้อกำหนดที่ตรวจได้ (Lecture 2) แล้วออกแบบระบบ สัญญาพฤติกรรมและการทดสอบ (Lecture 3-4) โดยตรวจความปลอดภัยตลอดทาง ไม่ใช่รอทำงานเสร็จ (Lecture 5)

ด้านบริหาร ให้ตกลงเป้าหมาย ขอบเขต ผู้เกี่ยวข้องและทรัพยากร ก่อนแบ่งงาน วางเวลาและความรับผิดชอบ (Lecture 6) แล้วใช้ backlog, sprint, board และ feedback คุมการส่งมอบจริง (Lecture 7) ทุกส่วนควรตอบได้ว่า **ทำเพราะข้อกำหนดใด และมีหลักฐานใดว่าใช้ได้**

คำอธิบายเสริม: ปัญหาอาจไม่ได้เริ่มจากโค้ดผิด แต่อาจเริ่มจากขอบเขตไม่ตรงกัน ไม่รู้ว่าจะตรวจอะไร หรือรับงานโดยไม่มีหลักฐาน จึงควรอ่าน requirements, design และ tests เป็นเส้นเดียวกัน ไม่ท่องแยกเป็นชื่อเอกสาร

## B. สรุปไทยสำหรับทำความเข้าใจ

### 1. SDLC และความรับผิดชอบของคน

SDLC คือวงจรพัฒนาตั้งแต่เข้าใจปัญหาจนส่งมอบและดูแล ช่วยแยก “โค้ดรันได้” จาก “ระบบแก้ปัญหาและใช้งานได้จริง” เริ่มจากข้อกำหนด/AC แบ่ง vertical slice ที่ใช้ได้ครบเส้นทาง แล้วทดสอบ ทบทวนและรวมงาน Coding agent ช่วยลงมือ แต่คนยังรับผิดชอบการตัดสินใจและการยอมรับ

จุดสับสน: Incremental เพิ่มส่วนที่ใช้ได้ ส่วน iterative ปรับสิ่งเดิมจาก feedback ทั้งสองใช้ร่วมกันได้ Agile ไม่ใช่การไม่วางแผนหรือไม่เขียนเอกสาร

แหล่ง: Lecture 1 pp. 6-25, 29-30; Lecture 4 pp. 77-89.

### 2. Requirement Engineering: เขียนให้ตรวจได้

FR บอกว่าระบบทำอะไร NFR บอกระดับคุณภาพ BR/domain rule บอกกฎธุรกิจ ให้หาผู้เกี่ยวข้อง/เป้าหมาย สอบถาม สังเกต บันทึก วิเคราะห์ ยืนยันและจัดลำดับ เช่น “ถือการสมัครไม่เกินสามรายการต่อภาค” เป็นกฎ ส่วนการปฏิเสธครั้งที่สี่เป็นพฤติกรรมที่บังคับกฎนั้น

ข้อจำกัด: ชนิด FR/NFR/BR ไม่ใช่ระดับ user/system; “เร็ว” ยังใช้รับงานไม่ได้จนกว่าจะตกลงตัวชี้วัด/เงื่อนไข ต้องแยก fact/assumption/question แบบจำลองช่วยลดความซับซ้อนแต่ไม่ใช่ระบบจริง และ rationale ต้องบอกด้วยว่าทำไมจึงตัดสินใจเช่นนั้น

แหล่ง: Lecture 2 pp. 4-5, 12-31; Lecture 7 pp. 4-6; Lecture 10 pp. 5-8.

### 3. SDD/TDD: เชื่อมข้อกำหนดกับหลักฐาน

SRS บอกสิ่งที่ต้องการ SDS บอกการออกแบบ STS บอกวิธีพิสูจน์ Contract ระบุ input, validation, behavior, persistence, side effects, errors และ output เช่น สร้าง invoice ต้องตรวจลูกค้า/จำนวน/ราคา แล้วบันทึกหัวกับรายการใน transaction เดียว ข้อมูลผิดต้องไม่เหลือชุดครึ่งหนึ่ง TDD เริ่ม test ที่ล้มเหลวตามเหตุผลที่ตั้งใจ ทำให้ผ่าน แล้วปรับโครงสร้างโดยยังผ่าน

จุดสับสน: Coverage สูงหรือ test ผ่านมากไม่ได้ยืนยันว่าจับข้อผิดพลาดสำคัญได้ Regression ใช้ได้หลายระดับ ไม่ใช่ระดับถัดจาก UAT; UAT ให้ผู้เกี่ยวข้องตัดสินว่าตรงความต้องการธุรกิจ

แหล่ง: Lecture 3 pp. 33-43, 54-57; Lecture 4 pp. 79, 88-100, 133-139; Lecture 7 pp. 35-36.

### 4. UML/UI: เลือกภาพให้ตรงคำถาม

Use Case แสดงเป้าหมายของ actor; Activity แสดง workflow ที่มีทางเลือก/วงวน; Sequence แสดงเหตุการณ์ตามลำดับใน scenario หนึ่ง; State แสดงการเปลี่ยนสถานะของ object เดียว เช่น KU Sequence เริ่ม Draft เดิม แต่ Activity เริ่มครั้งแรกด้วยฟอร์มว่าง UI แยกช่องแก้ได้ อ่านอย่างเดียว บังคับกรอก และรายการย่อย

ข้อจำกัด: อย่าเพิ่มสถานะ สิทธิ์หรือช่องชำระที่โจทย์ไม่ให้ อย่าย้ายสถานะระหว่าง Ticket กับ Registration; Class เก็บ notation ย่อไว้ แต่ Samples p. 6 ระบุอยู่ Final

แหล่ง: Lecture 4 pp. 5-16, 28-75, 111-117; Samples pp. 1-6; Lecture 10 pp. 29-31.

### 5. ความปลอดภัย: ตรวจที่ขอบเขตความเชื่อถือ

ระบุผู้กระทำ ทรัพย์สิน จุดโจมตีและ trust boundary แล้วดูผลต่อ CIA; AuthN ยืนยันตัวตน ส่วน AuthZ ตรวจสิทธิ์ต่อการกระทำ/ทรัพยากร กรณีสคริปต์ปลอม PDF ข้าม browser check ได้ server จึงต้องตรวจไฟล์ และแม้ตรวจพลาด ที่เก็บก็ควรรันสคริปต์ไม่ได้พร้อมตรวจสิทธิ์ดาวน์โหลด

จุดสับสน: โจทย์ยืนยันว่าอ่านรายงานผู้อื่นได้ จึงละเมิด C แล้ว ส่วน I/A เป็นสิ่งที่อาจตามมา ไม่อ้างว่าเกิดแล้ว Base64 ไม่ใช่ encryption; JWT ที่ลงลายเซ็นไม่ได้ปิดบังเนื้อหาโดยอัตโนมัติ

แหล่ง: Lecture 5 pp. 5-24, 26-40; Lecture 10 pp. 9-11.

### 6. วางแผน: แยกผลสำเร็จ งาน เวลาและแรงงาน

Goal คือผลที่อยากได้ deliverable คือสิ่งส่งมอบ success criteria คือหลักฐานตัดสิน WBS แบ่งงาน Gantt วางเวลา RACI วางความรับผิดชอบ milestone เป็นจุดสำเร็จไม่ใช่งานกินเวลา ตัวอย่าง DormFix ให้ B/F/H เผื่อหนึ่งวันเพราะรอคนนอก แล้วมี project buffer สองวันท้าย

ข้อจำกัด: Effort ไม่เท่ากับ duration เมื่อทำขนาน PERT เป็นประมาณการไม่ใช่คำรับประกัน และ RACI ต้องอิง notes ไม่เดาจากตำแหน่งงานหรือ dependency

แหล่ง: Lecture 6 pp. 7-65, 71-96, 103-114; Lecture 10 pp. 13-21.

### 7. ดำเนินงาน: จัดลำดับ เรียนรู้และปรับแผน

PO ดูคุณค่า/ลำดับ backlog; SM อำนวยความสะดวกและแก้อุปสรรค; ทีมเลือกวิธีทำและประเมินกำลัง Story ระบุใคร ต้องการอะไร เพื่ออะไร พร้อมรายละเอียดและ AC; grooming ทำให้งานพร้อม planning เลือกงานตาม goal/capacity; review ตรวจผลผลิต ส่วน retro ปรับวิธีทำงาน

จุดสับสน: Story point ไม่ใช่ชั่วโมง ไม่เทียบข้ามทีม Burndown วัดงานคงเหลือ ไม่ใช่คนที่เริ่มงาน และเครดิต unfinished ตามสไลด์ไม่ใช่การผ่าน DoD

แหล่ง: Lecture 7 pp. 24-72, 94-170; Lecture 10 pp. 22-26.

## C. ตารางศัพท์

| English | คำไทยที่ใช้ | ความหมายในวิชานี้ |
| --- | --- | --- |
| Software Development Life Cycle (SDLC) | วงจรพัฒนาซอฟต์แวร์ | ตั้งแต่ทำความเข้าใจความต้องการจนส่งมอบและดูแล |
| Feasibility | ความเป็นไปได้ | ประเมินเทคนิค ความคุ้มค่า การใช้งาน เวลาและทรัพยากร |
| Requirement | ข้อกำหนด | พฤติกรรม คุณสมบัติหรือข้อจำกัดที่ต้องมี |
| Functional / non-functional requirement (FR/NFR) | ข้อกำหนดหน้าที่ / คุณภาพ | ระบบทำอะไร / ทำได้ดีระดับใดภายใต้เงื่อนไขใด |
| Business rule (BR) | กฎธุรกิจ | กฎที่พฤติกรรมของระบบต้องรักษา |
| Stakeholder / rationale | ผู้เกี่ยวข้อง / เหตุผลของการตัดสินใจ | ใครมีส่วนได้เสีย / ทำไมจึงเลือกข้อกำหนดหรือแบบนั้น |
| Acceptance criteria (AC) | เกณฑ์ยอมรับ | เงื่อนไขตรวจรับเฉพาะงาน |
| Definition of Done (DoD) | เกณฑ์เสร็จร่วม | มาตรฐานที่งานต้องผ่านก่อนถือว่าเสร็จ |
| Definition of Ready (DoR) | เกณฑ์พร้อมเริ่ม | ข้อมูลพอให้เริ่ม ไม่ใช่ผ่านการตรวจรับ |
| Traceability | การเชื่อมโยงย้อนรอย | ข้อกำหนดไป design/code/test/release และย้อนกลับ |
| Engineering contract | สัญญาพฤติกรรมซอฟต์แวร์ | input/state นี้ต้องให้ผลและผลข้างเคียง/ข้อผิดพลาดใด |
| SRS / SDS / STS | ข้อกำหนดซอฟต์แวร์ / การออกแบบ / การทดสอบ | Software Requirements / Design / Test Specification: ต้องการอะไร สร้างอย่างไร พิสูจน์อย่างไร |
| Spec-Driven / Test-Driven Development (SDD/TDD) | พัฒนาโดยใช้ข้อกำหนด / การทดสอบนำ | ให้ contract ชี้ทิศทางและใช้ tests ขับการออกแบบ/ตรวจผล |
| Persistence / side effect | การบันทึกให้คงอยู่ / ผลข้างเคียง | ข้อมูลถาวร / ผลนอกค่าที่คืน เช่น email หรือ stock |
| Idempotency | เรียกซ้ำไม่เกิดผลซ้ำเกินที่ตกลง | ดูผลต่อระบบ ไม่จำเป็นต้องได้ response เหมือนกันทุก byte |
| Reconciliation / outbox | ตรวจสถานะให้ตรง / รายการงานรอส่งถาวร | เช่น ตรวจผล PSP / บันทึกพร้อมธุรกรรมแล้วส่งภายหลัง |
| Workflow / scenario | กระบวนงาน / เหตุการณ์เฉพาะเส้นทาง | Activity ครอบคลุมทางเลือก; Sequence เน้น scenario |
| Guard | เงื่อนไขกำกับทางเลือก/transition | เช่น [full] หรือ [all available] |
| List of Values (LoV) | รายการให้เลือกค่า | เลือกข้อมูลอ้างอิง เช่น course offering แทนการเดา foreign key |
| Authentication / authorization | ยืนยันตัวตน / ตรวจสิทธิ์ | “เป็นใคร” ไม่เท่ากับ “ทำอะไรได้” |
| Trust boundary | ขอบเขตความเชื่อถือ | จุดเปลี่ยนบริบทที่ต้องตรวจข้อมูล |
| Threat / vulnerability / attack | ภัยที่อาจเกิด / จุดอ่อน / การโจมตี | ไม่ใช้สามคำนี้แทนกัน |
| Risk / control | ความเสี่ยง / มาตรการควบคุม | พิจารณาโอกาสและผลกระทบ แล้วลดด้วยมาตรการ |
| Goal / deliverable | เป้าหมาย / สิ่งส่งมอบ | ผลที่ต้องการต่างจากชิ้นงานที่ใช้ทำให้เกิดผล |
| Milestone / task | จุดสำเร็จ / งาน | milestone ใช้เวลา 0; task มีเวลา/เจ้าของ |
| Effort / duration | ปริมาณแรงงาน / ระยะเวลา | person-hours ไม่เท่ากับชั่วโมงตามปฏิทินเสมอไป |
| Float / critical path | เวลาเลื่อนได้ / เส้นทางวิกฤต | ขึ้นกับ dependency และวันจบที่ใช้คำนวณ |
| Predecessor / successor (pred/succ) | งานก่อนหน้า / งานถัดไปที่พึ่งกัน | ใช้หาค่า max/min ใน forward/backward pass |
| RACI | ลงมือ / รับผิดชอบผล / ให้คำปรึกษา / รับแจ้ง | Responsible, Accountable, Consulted, Informed ตามบทบาทในงาน |
| Project Manager (PM) | ผู้จัดการโครงการ | ดูแผน เวลา ทรัพยากรและการประสานงาน |
| Product Owner (PO) | เจ้าของผลิตภัณฑ์ | ดูคุณค่า ลำดับ backlog และการยอมรับผลตามบทเรียน |
| Scrum Master (SM) | ผู้อำนวยความสะดวก Scrum | ดูกระบวนการ/timebox และช่วยแก้อุปสรรค ไม่ใช่ผู้สั่งแบ่งงาน |
| Minimum Viable Product (MVP) | ผลิตภัณฑ์ขั้นต่ำที่ใช้ทดสอบคุณค่า | สร้างเพื่อเรียนรู้ว่าจะเปลี่ยนทิศทางหรือพัฒนาต่อ |
| Epic | งานระดับใหญ่ที่ต้องแยก | ใหญ่เกินจะส่งมอบใน sprint เดียวหรือยังประมาณการตรง ๆ ไม่ได้ |
| Story points / velocity | ขนาดงานสัมพัทธ์ / points เสร็จต่อ sprint | ใช้บริบทและประวัติของทีม ไม่ใช่ชั่วโมงตายตัว |
| Backlog refinement (grooming) | ปรับ backlog ให้พร้อม | จัดลำดับ แยกและชี้แจงก่อนเลือกเข้า sprint |
| Remote-tracking reference | ตัวชี้สถานะ remote ที่เครื่องทราบ | origin/* ไม่ใช่ภาพสดของ GitHub |
| 95th percentile (p95) | เปอร์เซ็นไทล์ที่ 95 | ค่าระยะเวลาที่อย่างน้อย 95% ของคำขอใช้ไม่เกินค่านี้ ภายใต้ชุดข้อมูล/วิธีวัดที่ระบุ |

อ้างอิงกลุ่มหัวข้อ/หน้าในตารางถัดไป คำอธิบายเสริม: นิยาม idempotency ขยายเพื่อไม่ให้เข้าใจว่าต้องได้ response เดิมทุก byte หรือ retry แล้วเก็บเงินซ้ำได้

## D. Coverage ของโพยและแหล่งรายหัวข้อ

ชื่อ Lecture/Samples อ้างชื่อไฟล์เต็มที่ลิงก์ข้างต้น เพื่อให้ตรวจที่มาได้โดยไม่เบียดพื้นที่หน้าพิมพ์

| ตำแหน่ง | หัวข้อ | ไฟล์และหน้า PDF |
| --- | --- | --- |
| หน้า 1 คอลัมน์ 1 | SDLC/models/Agile/vertical slice/DoD | Lecture 1 pp. 8-25, 29-30 |
| หน้า 1 คอลัมน์ 1 | Agent/ความรับผิดชอบ | Lecture 1 pp. 3, 6-7, 12, 16-17; Lecture 4 pp. 77-83 |
| หน้า 1 คอลัมน์ 1 | Architecture/Git/Issue/PR/staging/main | Lecture 1 pp. 27-28, 31-46; Lecture 2 pp. 35-43 |
| หน้า 1 คอลัมน์ 1 | ระดับ/ชนิดข้อกำหนด, quality, RE/validation | Lecture 2 pp. 11-27; Lecture 7 pp. 4-6 |
| หน้า 1 คอลัมน์ 1 | Proposal/traceability/AC/DoR/MoSCoW | Lecture 2 pp. 23-31; Lecture 7 pp. 4-6, 102 |
| หน้า 1 คอลัมน์ 2 | SRS/SDS/STS, process, contract/invoice | Lecture 3 pp. 33-43; Lecture 4 pp. 79, 88-100, 133 |
| หน้า 1 คอลัมน์ 2 | AAA/TDD/BDD/tests/verification | Lecture 2 p. 43; Lecture 3 pp. 54-57; Lecture 4 pp. 136-139; Lecture 7 pp. 8-10, 35-36 |
| หน้า 1 คอลัมน์ 2 | Sync/async, payment recovery/outbox | Lecture 3 pp. 46-48; Lecture 4 pp. 3, 95-96 |
| หน้า 1 คอลัมน์ 2 | UML notation/workflow/scenario | Lecture 4 pp. 5-16, 61-62; Samples p. 6 เรื่อง Class |
| หน้า 1 คอลัมน์ 2 | Generic UI/List/Form/LoV/design system | Lecture 4 pp. 30-31, 47-48, 66-67, 101, 111-117 |
| หน้า 1 คอลัมน์ 2 | POS/Hotel/Ticket/Grades | Lecture 3 pp. 12-15; Lecture 4 pp. 14-15, 24, 28-29, 38, 41, 45-46, 64-65 |
| หน้า 1 คอลัมน์ 3 | Landscape/CIA/AuthN/AuthZ/RBAC/ABAC/ACL | Lecture 5 pp. 5-8, 19-23 |
| หน้า 1 คอลัมน์ 3 | Password/Basic/Digest/session/JWT/OAuth/OIDC/SSO | Lecture 5 pp. 10-17, 24 |
| หน้า 1 คอลัมน์ 3 | Vulnerabilities/status/config/secrets/tests | Lecture 5 pp. 26-40; Lecture 10 pp. 10-11 |
| หน้า 1 คอลัมน์ 3 | Initiation/SMART/OKR/ROI/criteria | Lecture 6 pp. 5-33, 59-65 |
| หน้า 1 คอลัมน์ 3 | Scope/creep/trade-off/stakeholders/charter | Lecture 6 pp. 35-57, 62-65 |
| หน้า 1 คอลัมน์ 4 | WBS/Gantt/CP/float/effort/PERT/buffers/RACI | Lecture 6 pp. 71-96; Lecture 7 pp. 15-19 |
| หน้า 1 คอลัมน์ 4 | Risk/kick-off/organisation/Conway | Lecture 6 pp. 68-70, 103-114 |
| หน้า 1 คอลัมน์ 4 | MVP/pair/DevOps/Scrum | Lecture 7 pp. 24-58 |
| หน้า 1 คอลัมน์ 4 | Stories/INVEST/points/refinement/planning | Lecture 7 pp. 60-72, 94-126 |
| หน้า 1 คอลัมน์ 4 | Board/WIP/Daily/Review/Retro/metrics/end sprint | Lecture 7 pp. 77, 129-170; docs/maintenance pp. 12-13 |
| หน้า 2 คอลัมน์ 1 | Part 1: requirements/proposal/RBAC/security | Lecture 10 pp. 3-11; Lecture 2 pp. 28-29; Lecture 5 pp. 19-40 |
| หน้า 2 คอลัมน์ 2 | Part 2: บริบท DormFix, งาน A-I/ผู้ทำ/วันทำและวันเผื่อ, WBS/RACI/Gantt | Lecture 10 pp. 13-21; p. 17 ให้รูปแบบ RACI แต่ไม่ให้ notes/เฉลยตายตัว |
| หน้า 2 คอลัมน์ 2 | Badminton story/Gherkin/metadata/bug และข้อเท็จจริงการยกเลิกใน DB | Lecture 10 pp. 22-24; คง “Booked”/“Free” ตามโจทย์ |
| หน้า 2 คอลัมน์ 2 | ShuttleNow: anchor ดูรายการเส้นทาง 3 points, priority/goal/16 points | Lecture 10 pp. 25-26; Lecture 7 pp. 67-72, 118 |
| หน้า 2 คอลัมน์ 1 ท้ายคอลัมน์ | สี่ระบบ: actors, workflow, constraints และผลข้างเคียงของ POS/Hotel/Ticket/Grades | Lecture 3 pp. 13-14; Lecture 4 pp. 28-29, 45-46, 64-65; Lecture 10 p. 31 |
| หน้า 2 คอลัมน์ 2 | PERT: O/M/P ของ T1-T6 และผลรวม | Lecture 6 pp. 90-92 |
| หน้า 2 คอลัมน์ 2 ท้ายคอลัมน์ | ตารางเตรียม UML/UI ครบทั้ง 5 ประเภท ไม่เลือกเตรียมเพียง 3 | Lecture 10 p. 29 |
| หน้า 2 คอลัมน์ 3 | KU R1-R11, master fields, ชื่อเต็มของ lifelines/lanes, Sequence/Activity | Samples pp. 1-4 |
| หน้า 2 คอลัมน์ 3 | Registration List/Form | Samples pp. 1-2, 5; รูปแบบทั่วไป Lecture 4 pp. 111-117 |
| หน้า 2 คอลัมน์ 4 | Use Case: Grades ทุกกลุ่มเป้าหมายและระบบภายนอกทั้งห้า; ทิศ include | Lecture 4 pp. 5-8, 64-65 |
| หน้า 2 คอลัมน์ 4 | State: Ticket และข้อแตกต่างจาก Registration/Grades | Lecture 4 pp. 45-46, 61-65; Samples pp. 1-2 |
| หน้า 2 คอลัมน์ 4 | Git 20 คะแนน: กรณี A-I, HEAD/FF/3-way/remote/tag และแม่แบบคำสั่ง | Lecture 10 p. 29; Samples pp. 6-14, 18-26 |

### เตรียม UML/UI ครบห้าแบบอย่างไร

| แบบ | ตัวอย่างในหน้าที่สอง | สิ่งที่ต้องตรวจเมื่อเปลี่ยนโจทย์ |
| --- | --- | --- |
| Sequence | KU Registration: Draft เดิมสอง offerings เพิ่มหนึ่ง เต็ม แก้ ส่งซ้ำ และจ่าย BBL | participants, ลำดับ request/reply, error ที่กำหนด, Done/lock/email; ไม่ยก workflow ทุกแขนงมาใส่ scenario เดียว |
| Activity | KU Registration: ฟอร์มว่าง, swimlanes, ตรวจที่นั่ง/กลับแก้, ทางเลือก KBank/BBL, ยืนยันและจบ | actions อยู่ lane ของผู้รับผิดชอบ, guards, decision/merge, loop และ start/end |
| UI | Course Offering List และ Student Registration Form | fields ตาม R5-R7, profile ห้าช่อง, required/editable/read-only/LoV, controls และ state; Complete ต่างจาก Design |
| Use Case | Grades Submission: login, courses/sections, students, edit/print sheet, submit, transcript และ email | human/external actors นอก boundary, goals ในกรอบ, association ไม่มีหัว, include ชี้ขั้นบังคับ; extend/generalization ตาม notation หน้าแรก |
| State | Ticket: Requested, Approved, In Progress, Closed by CCE, Closed by Programmer | object เดียว, event/actor/guard/effect, initial/final, self-loop, closed ห้ามเพิ่ม action; ไม่ย้าย Done ของ Registration ไป Grades |

### ครบในระดับใด และส่วนใดย่อออก

ครบ **กลุ่มหัวข้อหลักของ Lecture 1-7 และกลุ่มโจทย์ Midterm ที่ตรวจ** ไม่ใช่ทุกประโยคหรือทุกภาพ รายละเอียด career ladder, setup เฉพาะเครื่อง, code snippets ทุกตัว, UI ตัวอย่างซ้ำ, POS features A-R แบบเต็ม และขั้นตอน budget/procurement/communication แบบยาวไม่ได้คัดทั้งหมดลงโพย ให้เปิดหน้าที่อ้างเมื่อยังอธิบายหรือทำโจทย์เองไม่ได้

ไม่ได้ขยาย Component/Package จาก Lecture 4 p. 74 เพราะ blueprint เฉพาะ Midterm ใน Lecture 10 p. 29 ไม่เลือกสองแบบนี้ ไม่ได้รวม group project หลัง Lecture 10 p. 31 หรือ Week 8-9 และไม่ได้เปิด Google Docs ภายนอกที่สไลด์ลิงก์ไว้ จึงไม่รับรองเนื้อหาในลิงก์เหล่านั้น

### ตัวอย่างที่เติมเองและเงื่อนไขคำนวณ

- **คำอธิบายเสริม:** p95 ≤ 2 s ที่ 100 concurrent users เป็นค่าที่เสนอ ไม่ใช่ที่ coordinator ระบุ ต้องยืนยันจุดวัด เครือข่าย ชุดข้อมูลและกรณีผิดพลาด
- **คำอธิบายเสริม:** Proposal revision เพิ่ม metric, risk/control, effort planning และ evidence/sign-off โดยคงปัญหา ผู้ใช้และขอบเขตจากโจทย์ ห้ามอ้างว่าข้อเสนอเพิ่มได้รับอนุมัติแล้ว
- **คำอธิบายเสริม:** RACI สี่แถวตรงกับ meeting notes ใน [mock exam ข้อ 5.2](../mock-exam/midterm/chapters/questions.tex) ไม่ใช่เฉลย Lecture 10 p. 17
- **คำอธิบายเสริม:** กราฟ A=2, B=3, C=1, D=2 และตาราง ES/EF/LS/LF ใช้ finish-to-start ไม่มี lag/ข้อจำกัดคน เริ่ม 0 จบ 7; A-B-D=7 วัน, A-C-D=5 วัน, C float=2 ไม่ใช่กราฟ DormFix
- **คำอธิบายเสริม:** สูตร forward/backward pass ขยาย Lecture 6 pp. 82-85 อย่าปนเวลาเริ่มศูนย์กับวันที่ inclusive ใน Gantt
- **คำอธิบายเสริม:** SD รวมใช้รากของผลรวม variance เมื่อประมาณการอิสระ หกงาน Lecture 6 pp. 91-92 ให้ E=35.6667 h, SD=3.2318 h เป็น effort ไม่ใช่ duration เมื่อทำขนาน และหนึ่ง SD ไม่ใช่ช่วงรับประกัน
- DormFix ตาม Lecture 10 pp. 18-21: เริ่ม 4 Jan 2027 ทำ จ.-ศ.; buffer หลัง B/F/H อย่างละวัน, project buffer 28-29 Jan; milestones 8/15/29 Jan ใช้เวลา 0; WBS 1.4 ว่าง
- ShuttleNow ตาม p. 26: points 8,3,5,3,5,2; เลือก 1/3/4 รวม 16 ไม่เลือก QR fare เพราะไม่ตรง sprint goal
- **คำอธิบายเสริม:** Negative tests, score-boundary cases, attack flows, UI wireframes และ Use Case ของ Grades เป็นการประยุกต์ การปฏิเสธไม่ควรเปลี่ยน business data แต่ audit log ยังเกิดได้ตาม contract
- **คำอธิบายเสริม:** KU Sequence/Activity วาดย่อจากโจทย์ ไม่ใช่เฉลยภาพของอาจารย์ Sequence แสดง Student จ่าย BBL และ email PDF ถึง Student; Activity ในโพยย่อเส้นทางชำระสำเร็จ ส่วน Samples หน้า 16 และเฉลย Mock Exam แสดงผลชำระไม่สำเร็จแล้วกลับไปเลือกวิธีชำระด้วย จึงควรดูภาพเต็มเมื่อฝึกโจทย์ที่ขอทุกแขนง
- **คำอธิบายเสริม:** UI ไม่ถือ Registration No./Total Credits เป็นข้อบังคับจาก R5-R11 จึงไม่ใส่ แม้ภาพเฉลยตัวอย่างมีช่องเสริม รายละเอียด R7 แสดงผ่านตาราง/พื้นที่รายละเอียดได้
- **คำอธิบายเสริม:** ภาพ Git ใน PDF ย่อเฉพาะส่วนที่ใช้เทียบ fast-forward กับ three-way merge; รายละเอียดของแต่ละกรณีอยู่ในตาราง A-I และแต่ละกรณีเริ่มจากกราฟของตน ไม่ย้ายชื่อ commit หรือ remote-tracking refs ข้ามตัวอย่าง

### อธิบายคำสั่ง Git ที่ใช้ในโพยและโจทย์ 20 คะแนน

**คำอธิบายเสริม:** หน้านี้ขยายคำอธิบายสั้นใน PDF โดยยึดเงื่อนไข Samples หน้า 6-14 และเฉลยหน้า 18-26: เริ่มจาก working tree ที่ clean, คำสั่งสำเร็จ และไม่มี conflict เว้นแต่โจทย์ระบุ ชื่อ `<b>`, `<ref>`, `<files>` และ `<msg>` เป็นช่องให้แทนด้วยชื่อจริง ไม่พิมพ์วงเล็บแหลมลงในคำตอบ `;` ใช้แยกคำสั่งที่ทำตามลำดับ

ก่อนอ่านคำสั่ง ให้แยก working tree (ไฟล์ที่กำลังแก้), index/staging area (เวอร์ชันที่เลือกไว้ให้ commit), local repository (commits/branches ในเครื่อง) และ remote repository ออกจากกัน HEAD ในโจทย์ชี้ผ่าน current branch ไปยัง commit ส่วน `origin/main` เป็น ref ในเครื่องที่บันทึกสถานะ remote ล่าสุดที่รู้ ไม่ใช่การอ่าน GitHub สด

| คำสั่ง | ทำอะไร และกระทบส่วนใด |
| --- | --- |
| `git status` | แสดง current branch และแยก staged, unstaged, untracked เพื่อเลือกขั้นตอนต่อไป ไม่เปลี่ยนเนื้อหาไฟล์ ไม่สร้าง commit และไม่เลื่อน refs |
| `git diff` | เปรียบเทียบ working tree กับ index จึงเห็นสิ่งที่แก้หลังการ stage ครั้งล่าสุดของ tracked files ไม่แสดงไฟล์ใหม่ที่ยัง untracked; ใช้ `status` หาไฟล์เหล่านั้น |
| `git diff --cached` | เปรียบเทียบ index กับ HEAD จึงเห็นชุด staged changes ที่ commit ถัดไปจะบันทึก ต่างจาก `diff` ที่ดูสิ่งซึ่งยังไม่ stage |
| `git add <files>` | เก็บเวอร์ชันปัจจุบันของไฟล์ที่ระบุเข้า index รวมไฟล์ใหม่หรือการเปลี่ยนแปลงที่เลือก ยังไม่สร้าง commit ไม่เลื่อน branch และไม่ส่ง remote ถ้าแก้ไฟล์หลัง add ต้อง add อีกครั้งหากต้องการรวมเวอร์ชันใหม่ |
| `git commit -m "<msg>"` | สร้าง commit จาก snapshot ใน index โดยมี HEAD เดิมเป็น parent ในขั้น commit ปกติของโจทย์ แล้วเลื่อน current branch/HEAD ไป commit ใหม่ ไม่รวม unstaged/untracked โดยอัตโนมัติ และยังไม่ push; `-m` กำหนดข้อความ commit |
| `git branch <b>` | สร้าง local branch ชื่อ b ที่ commit ของ HEAD ปัจจุบัน แต่ยังอยู่ branch เดิม ไม่เปลี่ยนไฟล์และไม่สร้าง commit จึงต้องใช้ `switch` หากต้องการย้ายไป branch ใหม่ |
| `git switch <b>` | ให้ HEAD ชี้ branch b และเมื่อเริ่ม clean ให้ index/working tree แสดง snapshot ของ b ไม่มี branch tip ใดเลื่อนจากการ switch เพียงอย่างเดียว เช่น switch main ที่ B ไม่ทำให้ main ตาม origin/main ไป H |
| `git merge <ref>` | รวม ref ที่ระบุเข้ากับ current branch: ถ้า current เป็น ancestor ของ ref จะ fast-forward โดยเลื่อน current/HEAD และไม่สร้าง commit; ถ้าแยกสายจะสร้าง merge commit ที่มีสอง parents เมื่อสำเร็จ โดย source ref ไม่เลื่อน ถ้า source เป็น ancestor อยู่แล้วอาจไม่มีการเปลี่ยนแปลง; graph อย่างเดียวไม่พิสูจน์ว่าจะเกิด file conflict |
| `git merge --ff-only origin/<b>` | อัปเดต current branch ไปยัง ref ที่รู้แล้วเฉพาะกรณี fast-forward ได้ ถ้าแยกสายจะปฏิเสธแทนการสร้าง merge commit ต้อง switch branch เป้าหมายให้ถูกก่อน; คำสั่งนี้ไม่ fetch สถานะใหม่จาก server |
| `git fetch origin` | ติดต่อ remote เพื่อรับ commits/objects และอัปเดต refs อย่าง `origin/*` ตามการตั้งค่าของ repository ไม่รวมงานเข้า local branch ไม่เลื่อน HEAD และไม่เปลี่ยน working tree/index ให้ตาม remote โดยอัตโนมัติ |
| `git push origin <b>` | ส่งประวัติของ local branch b ที่ระบุไปอัปเดต branch นั้นบน remote เมื่อสำเร็จ matching remote-tracking ref เช่น origin/b จะตามสถานะที่ส่งภายใต้การแมปปกติของโจทย์ HEAD/working tree และ local branch tip ไม่เลื่อนเพราะ push การ push feature ที่ G ไม่เผยแพร่ merge H ซึ่งอยู่เฉพาะ staging |
| `git log --oneline --graph --decorate --all` | แสดงประวัติและ ancestry จาก refs ที่เครื่องมีโดยไม่แก้ข้อมูล: `--oneline` ย่อเป็น SHA สั้นกับหัวเรื่องต่อ commit, `--graph` วาดเส้นเชื่อมประวัติ, `--decorate` แสดงชื่อ branches/tags/refs, `--all` รวมประวัติที่เข้าถึงได้จาก refs ทั้งหมดในเครื่อง ไม่ติดต่อ GitHub หรือ fetch ข้อมูลใหม่ |

วิธีไล่กราฟให้ได้ครบประเด็น: จด HEAD/current branch และ tips ทุกตัวก่อน จากนั้นทำทีละคำสั่งว่าเปลี่ยนไฟล์/index, local refs หรือ remote-tracking refs ส่วนใด ถ้า merge ให้ตรวจ ancestry และระบุ parents ก่อนเลื่อน current branch; source branch และ refs ที่คำสั่งไม่แตะต้องอยู่เดิม สุดท้ายวาดทุก commit/parent, local branch, origin/*, tag และ HEAD ตามที่โจทย์ให้

ในตาราง PDF ใช้ `s` แทน staging, `f` แทน feature และ `os` แทน origin/staging เพื่อประหยัดพื้นที่ ตัวเล็กเหล่านี้เป็นชื่อย่อของ refs ไม่ใช่ commit ตัวใหญ่ A-H และต้องแทนด้วยชื่อจริงของแต่ละข้อเมื่อเขียนคำสั่ง ห้ามใช้ `git add .` ในโจทย์นี้: ระบุสามชื่อไฟล์ให้ตรงและตรวจ `diff --cached` ก่อน commit

## E. คำถามทบทวน 10 ข้อ

คำอธิบายเสริม: ชุดนี้สร้างเพื่อฝึก ไม่ใช่ข้อสอบจริง ให้ตอบก่อนอ่านเฉลยท้ายหัวข้อนี้

1. SRS/SDS/STS ต่างกันอย่างไร และควรเชื่อมด้วยอะไร? (Lecture 3 pp. 33-42; Lecture 4 pp. 88-100)
2. “สมัครได้เร็ว” กับ “ถือการสมัครไม่เกินสามรายการต่อภาค” เป็นชนิดใด ต้องรู้อะไรเพิ่มก่อนเขียน test? (Lecture 2 pp. 14-26; Lecture 10 pp. 5-6)
3. WorkshopHub รุ่นแรกเฉพาะ workshop ฟรี ข้อมูลใดยังขาดก่อนประเมินและรับงาน? (Lecture 10 pp. 7-8)
4. Coordinator สร้าง workshop ได้ จึงสมัครได้ด้วยไหม ตรวจที่ไหนและพิสูจน์อย่างไร? (Lecture 10 p. 9)
5. สคริปต์ปลอม PDF รันแล้วอ่านรายงานผู้อื่น: CIA ใดเกิดขึ้นแล้ว ใดแค่เสี่ยง และป้องกันสองชั้นอย่างไร? (Lecture 10 p. 10; Lecture 5 pp. 5-8, 28-38)
6. KU Sequence/Activity เริ่มจาก form เดียวกันไหม หลังจ่ายสำเร็จต้องเกิดอะไร? (Samples pp. 1-4)
7. A=2 วัน ก่อน B=3 และ C=1 ที่ทำขนาน แล้ว D=2 รอทั้งคู่ หากไม่มีข้อจำกัดคนและกำหนดจบเร็วสุด CP/float ของ C เท่าใด? (ประยุกต์ Lecture 6 pp. 82-85)
8. PERT O=2, M=3, P=6 h ให้ E/SD เท่าใด บวก effort ทุกงานเป็นวันจบได้เลยไหม? (Lecture 6 pp. 86, 90-92)
9. ShuttleNow anchor=3, velocity=16 เลือก stories ใด ทำไมไม่เอา QR fare และ points เป็นชั่วโมงไหม? (Lecture 10 pp. 25-26; Lecture 7 pp. 67-72)
10. main=B แต่ origin/main=H ซึ่ง H เป็นลูก B: switch main ถึง H เลยไหม อัปเดตอย่างไร และ branch อื่นเลื่อนตามไหม? (Samples pp. 12, 21-22)

### เฉลยย่อ

1. SRS บอกสิ่งที่ต้องการ SDS บอกแบบที่จะสร้าง STS บอกวิธีพิสูจน์ เชื่อม Req/AC IDs กับ design/code/tests/ไฟล์/ผลจริง ไม่เก็บเอกสารแยกขาดกัน
2. “เร็ว” เป็น NFR กำกวม ต้องตกลงตัวชี้วัด ภาระงาน จุดวัดและเกณฑ์ผ่าน; “ไม่เกินสาม” เป็น BR/domain rule ถามการยกเลิก/ข้ามภาคก่อนทดสอบขอบเขต 2/3/4
3. ยังขาดตัววัดคุณค่า/ค่าตั้งต้น ความเสี่ยง effort และหลักฐานรับงาน; “ก่อนภาคหน้า” เป็น deadline ไม่ใช่ effort ต้องติดป้ายสิ่งที่เสนอเพิ่ม
4. ไม่ได้ เพราะไม่มี grant สมัครและไม่สืบทอด role; ตรวจ backend ทุก request คำอธิบายเสริม: เรียก API สมัครด้วย Coordinator ต้องถูกปฏิเสธ/ไม่เพิ่มข้อมูล
5. C ถูกละเมิดแล้วจากการอ่านรายงานคนอื่น; I/A อาจตามมาแต่โจทย์ไม่ยืนยัน; ตรวจเนื้อหา/ชนิด/ขนาดบน server และเก็บแบบรันไม่ได้พร้อมตรวจสิทธิ์ดาวน์โหลด
6. Sequence มี Draft เดิมสอง offerings ก่อนเพิ่มหนึ่ง; Activity เริ่มฟอร์มว่าง; จ่ายสำเร็จเป็น Done แก้ไม่ได้ และส่ง PDF ผ่าน KU Email
7. A-B-D=7 วันเป็น CP; A-C-D=5 วัน; C float=2: ES=2, EF=3, LS=4, LF=5 ภายใต้เงื่อนไขที่ระบุ
8. E=(2+4×3+6)/6=3.33 h; SD=(6-2)/6=0.67 h ไม่รับประกันช่วงเวลา วันจบขึ้นกับ dependency งานขนาน คนและปฏิทิน
9. เลือก 1/3/4 ได้ 8+5+3=16 ตรง goal ติดตามรถ/เวลาถึง; QR fare ไม่ตรง goal; points เป็นขนาดสัมพัทธ์ไม่ใช่ชั่วโมง
10. switch ให้ HEAD อยู่ main ที่ B ไม่เลื่อน main; บน main ใช้ `git merge --ff-only origin/main` เพื่อเลื่อนไป H เมื่อไม่แยกสาย feature/staging ไม่เลื่อนตาม

## F. จุดต่างของเอกสารและสิ่งที่ควรถาม

| ประเด็น | เอกสารระบุอย่างไร | การใช้ในฉบับนี้ / ข้อควรถาม |
| --- | --- | --- |
| UML ในขอบเขตสอบ | Lecture 4 p. 74 รวม Component/Package/Class; Lecture 10 p. 30 ยังมี Class แต่ blueprint p. 29 เลือก Sequence/Activity/UI/Use Case/State; Samples p. 6 ระบุ Class อยู่ Final | โพยสรุป Class Diagram notation/checklist ไว้ใน Lecture 4 แต่ไม่ใส่เป็นแบบที่ 6 ของกลางภาค เพราะ blueprint มี 5 แบบ; ทบทวนขอบเขตอีกครั้งหากมีประกาศสอบใหม่ |
| Scrum events/meetings | Lecture 7 p. 40 นับ Sprint ใน 5 events แต่ p. 47 ตาราง meetings ใส่ refinement แทน | แยกชื่อหมวด ไม่อ้างว่ารายการเหมือนกัน; ถ้าถามสไลด์เฉพาะหน้าให้อธิบายบริบท |
| Unfinished/DoD | Lecture 7 pp. 163-164 ปรับ story/points ติด unfinished แยกส่วนเหลือ; pp. 146/169 กล่าวถึง AC/Done increment | เครดิตตามสไลด์ไม่เท่ากับผ่าน DoD; ควรถามก่อนคำนวณ velocity หากโจทย์มีกรณีนี้ |
| AuthN/AuthZ | Lecture 5 p. 13 หัวข้อ “Common authorization methods” แต่ยก Basic/Digest/API key/session | จัดใต้ AuthN ตามบริบท p. 8 แยก AuthZ ตาม pp. 19-23 ไม่แปลหัวข้อผิดตามไปด้วย |
| RACI/Gantt | Lecture 10 p. 17 ให้รูปแบบแต่ไม่มี notes/เฉลย RACI; pp. 18-21 ให้กฎและเฉลย Gantt | ไม่อ้าง RACI mock เป็นคำตอบทางการ และไม่เติมบทบาทเอง |
| ช่อง UI เสริม | Samples pp. 1-2, 5 ให้ข้อกำหนด/คำถาม; ภาพเฉลย pp. 15-16 มีช่องเสริมและป้าย Solution ชวนสับสน | ยึดข้อความ/Req IDs ไม่คัดทุกช่องเป็นข้อบังคับ ไม่อ้างว่าได้ตรวจภาพเฉลยทุกภาพ |
| Git staging | Lecture 1 pp. 36/43 มี `git add .`; Samples p. 6 ห้ามในโจทย์ | ใช้ชื่อไฟล์ตามกฎข้อสอบ ไม่ใช่ความขัดแย้งของ Git เอง |
| สิ่งที่โจทย์ไม่ให้ | “quick” ไม่มี threshold; cancellation ไม่บอกการนับ; proposal ไม่มี effort; API ไม่กำหนด | เสนอ/ถามและติดป้าย ไม่แต่งเป็นข้อเท็จจริง |

ไม่มีสมการสำคัญที่เลือกใช้ต้องเดาค่าที่อ่านไม่ออก แต่ยังไม่ได้ตรวจรายละเอียดภาพทุกสไลด์หรือเอกสารในลิงก์ภายนอก รายการ coverage จึงไม่ใช่คำรับรองว่าแทนต้นฉบับได้ทุกหน้า

คำอธิบายเสริม: ก่อนนำเข้าห้องสอบต้องยืนยันประกาศจริงว่าอนุญาตกี่หน้า/กี่ด้านและเงื่อนไขใด การมีโพยสองหน้าไม่ได้ยืนยันสิทธิ์นำเข้าสอบ

## รูปแบบ การ build และการตรวจฉบับพิมพ์

`midterm/cheat-sheet.tex` กำหนด layout; `theory-1.tex` ถึง `theory-4.tex` เป็นหน้าแรก และ `practice-1.tex` ถึง `practice-4.tex` เป็นหน้าที่สอง ใช้ TH Sarabun New ใน `preparation/mock-exam/midterm/fonts/` และ Latin Modern Math ไม่สร้างสำเนาฟอนต์เพิ่ม คำสั่งใช้ Sarabun ตัวหนาและปิด TeX ligatures เฉพาะ font family นี้ เพื่อไม่ให้ `--` หรือเครื่องหมายคำพูดกลายรูป

คงขนาดเนื้อหา 8 pt / leading 7.35 pt และตาราง 7.1 pt / 7.2 pt; คำสั่งเป็น Sarabun ตัวหนา 8 pt / 7.35 pt จึงมีสเกลเดียวกับข้อความรอบข้างแทนการเทียบขนาด pt กับ Menlo โดยตรง ป้ายภาพส่วนใหญ่ 7.1 pt; กรอบชื่อ 44.77 × 5.05 mm ตัวอักษร 11.55 pt สูตรใช้ `Scale=MatchUppercase` ให้ความสูงเข้ากับ Sarabun

ขอบ 3 mm ความสูงคอลัมน์ 289.5 mm; คอลัมน์ขวาสุดกันชื่อ 8 mm เหลือ 281.5 mm ภาพเป็นเวกเตอร์: flow/call ใช้หัวทึบ reply เส้นประหัวเปิด email delivery เส้นทึบหัวเปิด ส่วน actor association/Git ancestry ไม่มีหัว

จาก `preparation/cheat-sheet/midterm/`:

```bash
sheet_build_dir=$(mktemp -d /private/tmp/cpe334-cheatsheet-build.XXXXXX)
xelatex -interaction=nonstopmode -halt-on-error -output-directory="$sheet_build_dir" cheat-sheet.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory="$sheet_build_dir" cheat-sheet.tex
# ตรวจ log, จำนวนสองหน้า และภาพเรนเดอร์ก่อนแทนไฟล์ส่งออก
cp "$sheet_build_dir/cheat-sheet.pdf" output/pdf/CPE334_Midterm_Cheat_Sheet.pdf
trash "$sheet_build_dir"
```

ต้องไม่มี `Column ... exceeds its page budget`, `Overfull` หรือ `Missing character`; ตรวจภาพทั้งสองหน้าและซูมทุกคอลัมน์ โดยเฉพาะ Sequence/Activity, Gantt และสูตร ไม่ใช้เพียง text extraction ยืนยันว่าไม่มี clipping

พิมพ์ A4 แนวตั้ง 100% ไม่ใช้ Fit โดยไม่ตรวจ หากเครื่องพิมพ์พิมพ์ขอบ 3 mm ไม่ได้ต้องปรับ layout ก่อน ใช้ duplex/flip on long edge เฉพาะเมื่ออนุญาตสองด้าน และลองพิมพ์หนึ่งแผ่นเพราะจอไม่ยืนยันความคมของเครื่องพิมพ์

เก็บเฉพาะ source, reference, README และ PDF ตัวจริง aux/log/render ใช้ใน temporary directory แล้วล้างหลังตรวจ งานนี้เฉพาะ course repo ไม่แตะ TokTickIT หรือ Google Docs

### ผลตรวจฉบับ 24 October 2026

- PDF 2 หน้า A4 แนวตั้ง คงขนาดตัวอักษรเนื้อหา/ตารางเดิม คำสั่งเปลี่ยนเป็น Sarabun ตัวหนา 8 pt ตรวจภาพรวมทั้งสองหน้าและขยายอ่านครบแปดคอลัมน์ รวมทั้งหัวข้อข้อกำหนด รายละเอียด A-I เส้น/ป้ายภาพ และคำสั่งจริงหลังเปลี่ยนฟอนต์
- รอบ UI ตรวจภาพทั้งสองหน้าและขยาย Activity/ช่อง UI อีกครั้ง: diamond เหนือ Select / edit แยกจากหัวลูกศรและขอบกล่อง, เส้นเตือนกลับเข้า merge ชัด, read-only ใช้กรอบขีดเฉียงจริง เปรียบเทียบเนื้อหาห้าคอลัมน์ที่ไม่ได้แก้กับฉบับก่อนด้วยการ render ได้ภาพเหมือนกัน ส่วนคอลัมน์ T2/P3/P4 เพิ่มวิธีตอบ UI และปรับภาพตามรายละเอียดข้างต้น
- ความสูงทั้งแปดคอลัมน์อยู่ใน budget; build ไม่มี `Overfull`, `Missing character` หรือคำเตือนคอลัมน์เกินหน้า ข้อความทุก span อยู่ในขอบปลอดภัย ฟอนต์ทุกตัวฝังในไฟล์ ภาพเป็นเวกเตอร์
- ตรวจการเว้นวรรคไทย/อังกฤษ/ตัวเลขในต้นฉบับ ไม่พบการเขียนติดกันแบบ `idempotencyตามcontract` ตรวจชื่อไฟล์/ลิงก์ใน README ว่ามีจริง
- คำนวณ PERT ซ้ำได้ E=35.6667 h, SD=3.2318 h; ตรวจ milestones 8/15/29 Jan 2027, capacity 16 points และคะแนนแนวสอบ 25+25+30+20=100
- README มีแหล่งรายหัวข้อ ตารางศัพท์ คำถาม 10 ข้อและเฉลยแยก รวมทั้งข้อจำกัดการอ่านภาพ/แหล่งภายนอกข้างต้น ไม่รับรองว่าทุกเนื้อหาในข้อสอบจริงจะเหมือนแนว และยังไม่ได้ทดสอบความคมด้วยเครื่องพิมพ์จริง

### ผลตรวจฉบับ 27 October 2026: เตรียม UML/UI ครบห้าแบบ

- PDF ยังคงเป็น A4 แนวตั้ง 2 หน้า ไม่ลดขนาดฟอนต์หลัก/ตาราง และไม่มี `Overfull`, `Missing character` หรือคอลัมน์เกิน budget ทั้งแปดคอลัมน์ รอบขยาย UML/UI คงหน้าสรุปเดิม; รอบคำสั่ง Git เพิ่มความหมายของ log flags ในคอลัมน์แรกของหน้าแรก
- หน้าแนวสอบเรียงตัวอย่าง 1/5 Sequence, 2/5 Activity, 3/5 UI, 4/5 Use Case, 5/5 State ครบอย่างละหนึ่งชุด ตรวจภาพทั้งหน้าและขยายอ่านแต่ละแบบ ไม่ใช้เพียงการค้นหัวข้อในข้อความ
- Use Case ของ Grades มีเป้าหมาย login, courses/sections, load students, edit/print, submit, update transcript และ email พร้อมระบบภายนอก KU SSO, KU Registration, KU Transcript, KU Email, KU Student Info กล่อง `<<actor>>` อยู่นอก boundary และป้าย `<<include>>` อ่านแนวนอนโดยไม่ทับวงรี
- State ใช้สถานะและ transition ของ Ticket ตาม Lecture 4 หน้า 61-62 พร้อม actor, self-loop และข้อห้ามหลังปิด แยก Draft/Done ของ Registration จาก Draft/Ready/Submitted ของ Grades
- คง requirements R1-R11 และเส้นทางสำคัญของ KU Registration, profile ห้าช่อง, read-only/LoV และ notation UI เดิม เพิ่มตารางบริบทสี่ระบบและตารางเริ่มทำทั้งห้าแบบ
- Git มีแถวสรุปกรณี A-I ครบ พร้อมแม่แบบคำสั่ง ไฟล์/ข้อความ commit ที่ต้องใช้ และภาพ ancestry ย่อ ไม่อ้างว่าเป็นกราฟเต็มทุกข้อ แก้ถ้อยคำตรวจรับให้ Student ทดลองสมัคร/ยกเลิก และ Coordinator ตรวจรายชื่อ/รับรองผล สอดคล้องกับการแยกบทบาท
- ฟอนต์ที่ใช้ฝังครบ: TH Sarabun New, TH Sarabun New Bold และ Latin Modern Math ไม่พบข้อความอยู่นอกขอบหน้า การตรวจนี้เป็นการตรวจไฟล์/ภาพ render ยังไม่ได้พิมพ์ทดสอบกับเครื่องพิมพ์จริง
- รอบคำอธิบาย Git: PDF มีความหมายของ 12 รายการ ได้แก่ status, diff, diff --cached, add, commit -m, branch, switch, merge, merge --ff-only, fetch, push และ log พร้อม flags --oneline/--graph/--decorate/--all แยกผลต่อ working tree/index/HEAD/local refs/remote และมีคำอธิบายฉบับเต็มด้านบน
- หลังเพิ่มคำอธิบายยังเป็น PDF สองหน้าและไม่มีคำเตือน build หรือข้อความนอกขอบ เปรียบเทียบที่ 144 dpi แล้ว Parts 1-2, ตัวอย่าง UML/UI ทั้งห้า และคอลัมน์ทฤษฎี 2-4 ของหน้าแรกเหมือนก่อนรอบ Git ทุกพิกเซล ขนาดฟอนต์หลัก/ตาราง/คำสั่งยังเดิม สรุปกรณี Git A-I ใช้ชื่อย่อ s/f/os ที่อธิบายไว้ครบ
- ตรวจขอบเขตโจทย์กับ Lecture 10 อีกครั้ง: Part 1 มี requirement analysis, proposal, RBAC และ security; Part 2 มี DormFix WBS/RACI/Gantt, Badminton backlog grooming และ ShuttleNow sprint planning; Part 3 มี UML/UI ห้าแบบกับ Git สามรูปแบบ และกรณี Git A-I ครบตาม Samples 2.1-2.9
- เติม checklist Class Diagram ตามโจทย์ตัวอย่าง: ชื่อคลาส/attributes, ไม่ใส่ methods, associations/multiplicity, inheritance, composition, aggregation, external calls และจำกัด links ของ Header/Line Item ไว้ชั้นแรก โพยเก็บส่วนนี้ในสรุป Lecture 4 ไม่เพิ่มเป็นแบบที่ 6 ของกลางภาค เพราะ blueprint ให้เลือก 3 จาก 5 และ Sample ระบุ Class ว่าเป็น Final
- PDF build ล่าสุดยังเป็น A4 สองหน้า; T2 สูง 816.67 pt จาก budget 823.99 pt ไม่มีคำเตือนคอลัมน์เกินหน้า/อักขระหาย ตรวจภาพเรนเดอร์ทั้งสองหน้าแล้ว ไม่ได้ทดสอบกับเครื่องพิมพ์จริง
