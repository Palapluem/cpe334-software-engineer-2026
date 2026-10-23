# CPE334 Midterm Cheat Sheet

[เปิด PDF สองหน้า](midterm/output/pdf/CPE334_Midterm_Cheat_Sheet.pdf) · [ต้นฉบับ LaTeX](midterm/cheat-sheet.tex)

โพยสำหรับ วิศิษฐ์ สุวรรณเนาว์ 67070501042 ใช้ A4 แนวตั้งสองหน้า หน้าละสี่คอลัมน์ ตามเรฟ [CPE241 Cheat Sheet M3](<ref/CPE241 Cheat Sheet M3.pdf>): หัวข้อพื้นพาสเทล เส้นแบ่งคอลัมน์บาง คำอธิบายไทยพร้อมศัพท์อังกฤษ ตารางเทียบ กฎสีแดง สูตร/คำสั่งสีน้ำเงิน และตัวอย่างสีเขียว ไดอะแกรมวาดด้วย TikZ จึงเป็นเวกเตอร์และแก้ต่อได้

ฉบับนี้ไม่มีหัวกระดาษ ไม่มีเลขหน้า/คำอธิบายสี/ข้อความอ้าง README ท้ายกระดาษ เหลือเฉพาะกรอบชื่อและรหัสที่มุมล่างขวาของทั้งสองหน้า ตัวอักษรประมาณ 11.5 pt โดยล็อกกรอบไว้เท่าฉบับก่อน (44.77 × 5.05 mm) และจัดข้อความกึ่งกลางทั้งสองแกน เพื่อให้มีช่องว่างรอบชื่อมากขึ้นตามคำขอ ใช้ชื่อ Lecture 1–7 เต็ม ณ จุดเปลี่ยนบท (Lecture 6 แยก Initiation กับ Planning) ใช้ขอบ 3 mm และความสูงคอลัมน์ 289.5 mm; คอลัมน์ขวาสุดกันพื้นที่ชื่อไว้ 8 mm จึงมี budget 281.5 mm ไม่ปล่อยให้เนื้อหาชนกรอบชื่อ

ตรวจภาษาใหม่ทั้งแปดคอลัมน์: เว้นวรรคระหว่างไทยกับอังกฤษ/ตัวเลข ปรับคำแปลและประโยคให้เป็นธรรมชาติ ลดการใช้คำอังกฤษต่อกันโดยไม่จำเป็น แต่รักษาชื่อคำสั่ง API identifiers และศัพท์สำคัญไว้ เช่น อธิบาย idempotency ว่าเรียกซ้ำแล้วมีผลต่อระบบเท่าเดิม พร้อมตัวอย่างไม่ตัดเงินซ้ำ รอบปรับความหนาแน่นเพิ่มตัวเนื้อหาจาก 7.6 เป็น 8 pt แต่ลดระยะบรรทัด/ช่องไฟตามเรฟ ไม่ได้ย่อทั้งหน้า

## ค่าที่วัดจากเรฟและฉบับปรับพื้นที่

วัดจาก text spans และตำแหน่ง baseline ใน PDF ไม่ได้กะจากภาพย่อ ตัวเลข font ใน PDF ต่างจากค่า TeX เล็กน้อยเพราะหน่วย pt/bp

| รายการ | เรฟ CPE241 หน้า 1 | ฉบับนี้ |
| --- | --- | --- |
| ฟอนต์เนื้อหาหลักใน PDF | 8.00 pt | 7.97 pt (ตั้งใน TeX 8 pt) |
| ระยะ baseline ที่พบมากในเนื้อหา | 7.34 pt | 7.32 pt (ตั้ง leading 7.35 pt) |
| ฟอนต์ชื่อ/รหัสใน PDF | 14.50 pt | 11.51 pt (ตั้งใน TeX 11.55 pt; กรอบขนาดเดิม) |
| ขอบซ้ายข้อความโดยประมาณ | 3 mm | 3 mm |

ฉบับก่อนหน้ามี baseline ประมาณ 9.33 pt เพราะ spacing ของภาษาไทยซ้อนกับค่าที่กำหนด จึงแก้ line spread ที่ต้นเหตุ ลดช่องก่อนหัวข้อและ padding ของตาราง/แถบสี พร้อมคงขนาดตัวอักษรของคำสั่งและรูป ไม่ปล่อยให้สระ/วรรณยุกต์ชนกัน การอ่านบนกระดาษจริงยังควรทดสอบที่ 100% ก่อนพิมพ์ใช้งาน

รอบปรับความชัดมีแผนภาพรวม 17 ภาพ: เพิ่ม fork/join จากเดิม 16 ภาพ ขยายป้ายทั่วไปเป็นประมาณ 7.1 pt, Git commits/refs เป็น 7.3 pt และวันที่ใน Gantt เป็น 6.2 pt; ใช้เส้นลูกศรทั่วไป 0.35 pt และเน้น Critical Path สีแดง 0.5 pt กราฟ `B: 3` และ `Example B: 3-way` คงขนาดกรอบย่อในคอลัมน์ แต่ป้ายและเส้นชัดขึ้น ไม่ขยายช่องว่างตามสัดส่วนของตัวหนังสือ ส่วน lifelines, swimlanes และทางแยกยังเว้นระยะเท่าที่จำเป็นต่อการอ่าน เสริมพื้นขาวหลังข้อความ Sequence เพื่อไม่ให้เส้น lifeline พาดผ่านตัวอักษร หัว control flow/call เป็นสามเหลี่ยมทึบเรียบ ส่วน reply/dependency เป็นหัวเปิดบนเส้นประ ไม่ใช้หัวเว้า Stealth ปนกันทุกประเภท เพิ่ม merge node ขนาดเล็กให้เส้นวนกลับใน Activity มีช่วงปลายยาวพอและไม่ส่งหัวลูกศรชนกรอบซ้าย; actor association และ Git ancestry ยังคงไม่มีหัว

สูตรใช้ Latin Modern Math จากไฟล์ใน TeX distribution โดยตั้ง `Scale=MatchUppercase` ให้ความสูงอักษรใหญ่ตรงกับ TH Sarabun New เนื้อหา สูตรจึงมีขนาด nominal ประมาณ 5.55 pt ใน PDF เทียบกับ Sarabun 7.97 pt แต่ความสูงอักษรใหญ่ใกล้กัน ไม่ใช้เลข 8 pt เท่ากันแล้วปล่อยให้สูตรใหญ่กว่าข้อความ รูปเศษส่วน รากและผลรวมยังรักษาสัดส่วนทางคณิตศาสตร์; ชื่อปริมาณ เช่น SD, points และ capacity จัดเป็นข้อความ ไม่คูณตัวอักษรแยกกัน ฟอนต์เนื้อหา ตารางและโค้ดคงขนาดเดิม

## เนื้อหา

| หน้า | คอลัมน์ | เนื้อหา |
| --- | --- | --- |
| 1 | 1: Lecture 1–2 | Product/SDLC, feasibility, process models, Agile values, DoD, AI delegation, vertical slice, Git basics, requirement levels/types/NFR, RE process, quality/validation, proposal/traceability, AC/DoR/MoSCoW; quality-defect/revision table, elicitation questions, BR-vs-FR and a worked AC |
| 1 | 2: Lecture 3–4 | SRS/SDS/STS, seven-field invoice contract, test-case row, score-boundary example, sync/async/idempotency, TDD/BDD, test levels/types, UML/UI, fork/join example, expanded POS/Hotel/Ticket/Grades case table and diagram checklist; Class notation retained only as a Lecture 4 reminder |
| 1 | 3: Lecture 5 + Lecture 6 | CIA, actors/assets/boundaries, AuthN/AuthZ, RBAC/ABAC/ACL, passwords/sessions/tokens, OAuth/OIDC/SSO, vulnerability-control-test table, direct API/owner/session/validation expected results, defense in depth; initiation, SMART/OKR/ROI, scope/change, Power/Interest and charter |
| 1 | 4: Lecture 6–7 | WBS/Gantt/CPM/PERT/buffers/RACI/risks, worked critical-path graph and ES/EF/LS/LF/Float table, Agile/MVP/pair/DevOps, Scrum, stories/INVEST/metadata, refinement/planning/capacity/velocity, board/WIP/review/retro, end-sprint, docs/organisation; four metrics with meanings and measurement caveats |
| 2 | 1 | Practice Midterm Part 1: requirements analysis, eight-element proposal evaluation and a revised proposal, complete RBAC table, upload scenario/controls/negative tests, XSS/CSRF/SSRF/SQLi diagrams, boundary questions and threat/vulnerability/attack/risk/control distinctions |
| 2 | 2 | Practice Midterm Part 2: PM/PO/SM perspectives, DormFix WBS tree, mock RACI notes, owners/durations/dates/Gantt/buffers/milestones, badminton story/details/Gherkin/metadata, clarification questions, ShuttleNow points/selections/Fibonacci; worked Lecture 6 PERT effort and Git remote reference |
| 2 | 3 | Practice Midterm Part 3: KU R1-R11 digest plus R1-R4 administrator scope, distinct Sequence/Activity initial states, full branch/loop/payment coverage, Ticket State (Lecture 4 p. 62), Grades submit-use-case/Ready gate; explicit warning not to mix case rules |
| 2 | 4 | Practice Midterm Part 4: Registration List/Form wireframes, Git pointers/FF/three-way, explicit staging/create-base/inspection/redraw checklist; Samples 2.6/2.7/2.8/2.9 covering remote-tracking vs local/tag, unpublished merge, a new feature based on the integrated tip, FF staging then merge diverged feature and push |

“บท 1-7 ในหนึ่งหน้า” หมายถึงสรุปสาระและหัวข้อหลักสำหรับทบทวน ไม่ใช่ถอดทุกสไลด์ลงหนึ่งหน้า รายละเอียด setup เฉพาะเครื่อง ภาพ UI ตัวอย่างซ้ำ และขั้นตอน vendor/budget แบบยาวไม่ได้คัดลงโพย ส่วน Git อยู่ในหน้าแนวสอบด้วยเพราะ Lecture 10 ระบุเป็น 20 คะแนน และมีพื้นฐานตั้งแต่ Lecture 1 ไม่ได้นำ architecture/containers ของ Week 8-9 มาเบียดหน้าสรุป

## แหล่งและจุดที่ตรวจเทียบ

เลขหน้าต่อไปนี้เป็นลำดับหน้า PDF ไม่ใช่เลขสไลด์ที่พิมพ์ไว้ในหน้า

| แหล่งหลัก | หน้าที่ใช้ตรวจ / หัวข้อ |
| --- | --- |
| [Lecture 1](<../../lectures/Week 1/CPE334_Lecture01 Introduction.pdf>) | pp. 3-30: SDLC/models/agent responsibility/DoD/vertical slice; pp. 31-46: Git, PR, staging/main, evidence |
| [Lecture 2](<../../lectures/Week 2/CPE334_Lecture02 Requirement Engineering.pdf>) | pp. 10-33: requirements/types/quality, elicitation, validation, scope/proposal, traceability; pp. 35-43: architecture/API/testing basics |
| [Lecture 3](<../../lectures/Week 3/CPE334_Lecture03 Specifications, SDD, Testing, TDD.pdf>) | pp. 28-43: layers, SRS/SDS/STS, feature contracts; pp. 54-57: testing/maintenance |
| [Lecture 4](<../../lectures/Week 4/CPE334_Lecture04 UML, SDS Features, STS Features.pdf>) | pp. 3-75: sync/async, UML/UI/cases; pp. 79-100, 133-139: contracts, engineering process, feature/sprint/release verification |
| [Lecture 5](<../../lectures/Week 5/CPE334_Lecture05 - Security in SE.pdf>) | pp. 5-24: landscape/CIA/authentication/authorization; pp. 26-40: OWASP topics, validation, vulnerabilities, configuration and tests |
| [Lecture 6](<../../lectures/Week 6/CPE334_Lecture06 - Project Management.pdf>) | pp. 5-63: initiation/goals/scope/ROI/charter; pp. 68-96: organisation/WBS/schedule/PERT/RACI; pp. 103-114: risks/kick-off |
| [Lecture 7](<../../lectures/Week 7/CPE334_Lecture07 - Project Execution.pdf>) | pp. 3-19: lifecycle/docs/tracking; pp. 21-72: Agile/Scrum/stories/points; pp. 94-170: grooming/planning/execution/review/retro/metrics/end-sprint |
| [Lecture 10: Midterm Prep](<../../lectures/Week 10/CPE334_Lecture10 - Midterm Exam Prep_Group Work Project.pdf>) | pp. 3-11: requirements/security; pp. 12-26: planning worked examples; pp. 27-31: UML/UI 30 + Git 20 blueprint and lecture case patterns |
| [Midterm Samples by Suthep](<../../lectures/Week 10/CPE334_Midterm Samples by Suthep.pdf>) | pp. 1-5: KU registration/scenarios/UI and Git assumptions; pp. 6-14: Git question types; pp. 18-26: Git model answers |

## สมมติฐานและการแยกตัวอย่างจากข้อเท็จจริง

- Target “p95 ≤ 2 s ที่ 100 concurrent users” เป็นตัวอย่าง rewrite ที่เสนอเพิ่ม จึงระบุชัดว่ารอยืนยัน client ไม่ใช่ตัวเลขที่โจทย์ให้
- WBS มีสาม milestones เท่านั้น ตาม worked example ใน Lecture 10 p. 16 ช่อง 1.4 เว้นว่าง ไม่สร้างงานเพิ่มให้เต็มช่อง
- DormFix เริ่ม 4 January 2027; ทำงานจันทร์-ศุกร์; buffer หลัง B/F/H อย่างละหนึ่งวัน; project buffer 28-29 January; milestones 8/15/29 January ตรง Lecture 10 pp. 18-21 กฎ buffer นี้ใช้กับเงื่อนไขตัวอย่าง ไม่ใช่กฎว่าทุกโครงการต้องมี buffer หลังทุก approval
- RACI สี่แถวเป็นตัวอย่างจาก meeting notes ที่เขียนในชุดฝึก CPE334 12 ข้อ ไม่อ้างว่าเป็นตารางคำตอบตายตัวของข้อสอบจริง
- ShuttleNow: points 8, 3, 5, 3, 5, 2; เลือก stories 1/3/4 รวม 16 ตรง Lecture 10 p. 26
- Sequence ใช้ scenario ที่มี Draft เดิมสอง offerings แล้วเพิ่มอีกหนึ่ง ต่างจาก Activity ซึ่งเริ่มครั้งแรกของภาคด้วย blank form ภาพทั้งสองจึงไม่ได้ใช้ initial state เดียวกัน
- UI wireframes เป็นแบบวาดย่อเพื่ออธิบายการตอบโจทย์ ไม่ใช่ screenshot แอปจริง ค่า sample ในตารางใช้ประกอบเท่านั้น `/////` แทน diagonal hatching ของ read-only fields
- Use Case ของ Grades เป็น architectural slice ของการ Submit เท่านั้น: Instructor ใช้งาน Submit grades ซึ่ง include การ update transcript และ send email ไม่ได้อ้างว่าเป็น Use Case diagram ครบระบบ ต้องเพิ่ม goal และ external actors ตามคำถามจริง
- Ticket State วาดใหม่ตาม Lecture 4 p. 62 โดยย่อ Programmer เป็น P ตาม legend: มี Requested, Approved, In Progress, Closed by CCE และ Closed by Programmer พร้อม self-loop และจุดจบ; ไม่ใช้สถานะ/สิทธิ์ของแอป TokTickIT มาแทน case ใน lecture
- Critical-path graph เป็นตัวอย่างที่สร้างเพื่ออธิบายสูตร ไม่ใช่คำตอบ DormFix: A=2, B=3, C=1, D=2 วัน; A→B→D ใช้ 7 วัน, A→C→D ใช้ 5 วัน และ C มี float 2 วัน ภายใต้ dependency ในรูปและไม่มีข้อจำกัดทรัพยากรเพิ่มเติม
- ตารางใต้กราฟใช้เวลาเริ่ม 0 และเส้นตาย 7: A=(ES 0, EF 2, LS 0, LF 2), B=(2,5,2,5), C=(2,3,4,5), D=(5,7,5,7); Float เท่ากับ LS-ES จึงมีเฉพาะ C ที่เลื่อนได้ 2 วัน
- PERT worked example มาจาก Lecture 6 pp. 90-92: T1 มี O=2, M=3, P=6 ชั่วโมง จึง E=3.33 และ SD=0.67 ชั่วโมง; หกงานรวม E=35.6667 และ SD=3.2318 ชั่วโมงเมื่อ estimates อิสระ แสดงเป็น 35.7 ± 3.2 ชั่วโมงตามสไลด์ นี่คือ effort รวม ไม่ใช่กำหนดส่งเมื่อทำงานขนาน
- ภาพโจมตีเป็น conceptual flows ไม่ใช่ screenshot หรือ request log; แยกให้เห็น XSS รันที่ browser, CSRF อาศัย browser/cookie, SSRF ให้ server เรียกปลายทาง และ SQLi เปลี่ยน query ที่ไม่ปลอดภัย
- Git example A แสดงผลหลัง fast-forward, สร้าง F บน staging แล้ว switch main; example B ขยายเฉพาะ fork ที่ D ไม่ได้แสดงบรรพบุรุษทั้งหมด ยังคงเตือนให้วาดทุก branch/origin/HEAD ในคำตอบจริง
- คำสั่ง commit ที่ยาวใน example A ใช้ shell continuation (`\` ท้ายบรรทัด) อย่างชัดเจน จึงไม่ตัดคำใน commit message จนกลายเป็นคำสั่งคนละอัน
- ตัวอย่าง Explain state แยกจาก A/B: Samples 2.6 ใช้ main=B, origin/main=H, tag v1.0=H; Samples 2.7 ใช้ H เป็น unpublished merge ที่มี parents E/G ไม่ใช่ commit G ของ example B
- Sample 2.8 เริ่มจาก FF staging C→E ก่อนใช้ `branch` และ `switch` สร้าง `feature/grade_distribution` ที่ E; commit F เลื่อนเฉพาะ feature ใหม่ ส่วน staging และ `feature/pass_rate` ยัง E และ `origin/staging` ยัง C
- Sample 2.9 เป็นกรณีเริ่มใหม่: local staging=D, remote-tracking=G, feature=F; FF D→G ก่อน merge feature จึงได้ H ที่มี parents G/F; ไม่ใช้ FF กับ feature ที่แยกสาย และ main/feature ไม่เลื่อนตาม staging
- Revised proposal เก็บข้อเท็จจริงเรื่องปัญหา ผู้ใช้และขอบเขตจาก Practice Midterm / Lecture 10; metric, risk/control, effort-planning และ evidence/sign-off เป็นข้อเสนอที่ติดป้าย ไม่ใส่ตัวเลขหรือผู้อนุมัติที่โจทย์ไม่ยืนยัน
- Mean Lead Time ใช้จุดเริ่ม “idea” ถึง “production” ตาม Lecture 7 p. 159 ในวิชานี้ ไม่สลับไปนิยามที่เริ่มจาก commit โดยไม่แจ้ง
- การทดสอบ rejection ตรวจว่า business data/side effects ที่ห้ามไม่เปลี่ยน ไม่ได้ห้ามระบบบันทึก audit log ของความพยายามที่ถูกปฏิเสธ
- สูตร ES/EF/LS/LF ใช้เวลาเริ่มศูนย์ ส่วนวันที่ใน Gantt ใช้วันทำงานแบบ inclusive จึงแยก convention ไม่บวกหรือลบวันปนกัน สูตร SD รวมใช้เมื่อ estimates เป็นอิสระต่อกัน
- Scrum formal events ห้ารายการนับ Sprint ด้วย; backlog refinement เป็นกิจกรรมต่อเนื่อง ใน Lecture 7 บางหน้าใช้ตารางหัวข้อ “meetings” ซึ่งนับ refinement แทน Sprint จึงจัดคำให้แยกกันชัด
- Lecture 7 pp. 163-164 กล่าวถึงการแบ่งเครดิตงาน unfinished ตามนโยบายในสไลด์ โพยแยกประเด็นนี้จาก DoD: partial work ไม่ได้แปลว่า increment ผ่าน DoD ส่วนที่เหลือต้องเป็น story ใหม่ ไม่ใช้คำว่า Done แบบกำกวม
- Blueprint หลัก Lecture 10 p. 29 เลือก 30 คะแนนจาก Sequence/Activity/UI/Use Case/State; หน้า 30 กล่าวถึง Class ในรายการตัวอย่าง lecture แต่ Midterm Samples p. 6 ระบุชัดว่า Class Diagrams จะอยู่ใน Final จึงเก็บเฉพาะ notation สั้น ๆ ไม่เพิ่ม worked Class exercise ลงหน้าแนวกลางภาค

## ไฟล์และการ build บน Mac

`midterm/cheat-sheet.tex` กำหนดกระดาษ ฟอนต์ สี คอลัมน์และ macro; `theory-1.tex` ถึง `theory-4.tex` เป็นหน้าแรก; `practice-1.tex` ถึง `practice-4.tex` เป็นหน้าที่สอง เนื้อหาทั้งหมดแก้ได้โดยไม่ต้องแก้ PDF โดยตรง ใช้ฟอนต์ TH Sarabun New ที่มีอยู่แล้วใน `preparation/mock-exam/midterm/fonts/` และ Menlo บน Mac เพื่อไม่สร้างสำเนาฟอนต์ซ้ำ ต้องมีแพ็กเกจ `unicode-math` และ `latinmodern-math.otf` ใน TeX distribution; โหลดด้วยชื่อไฟล์เพื่อไม่พึ่งการลงทะเบียนฟอนต์ใน macOS

จาก `preparation/cheat-sheet/midterm/`:

```bash
sheet_build_dir=$(mktemp -d /private/tmp/cpe334-cheatsheet-build.XXXXXX)
xelatex -interaction=nonstopmode -halt-on-error -output-directory="$sheet_build_dir" cheat-sheet.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory="$sheet_build_dir" cheat-sheet.tex
mkdir -p output/pdf
cp "$sheet_build_dir/cheat-sheet.pdf" output/pdf/CPE334_Midterm_Cheat_Sheet.pdf
trash "$sheet_build_dir"
```

แต่ละคอลัมน์พิมพ์ความสูงลง log และเตือนถ้าเกิน budget อย่าใช้ผล build ที่มี `Column ... exceeds its page budget`, `Overfull`, หรือ `Missing character` ต้องตรวจภาพเรนเดอร์และจำนวนสองหน้าอีกครั้งหลังเปลี่ยนเนื้อหา

## การพิมพ์ / การนำไปทำ Canva ต่อ

- A4 แนวตั้ง ขนาดจริง 100% ไม่ใช้ booklet หรือหลายหน้าต่อแผ่น ขอบกระดาษ 3 mm; ตรวจว่าเครื่องพิมพ์พิมพ์ถึงขอบนี้ได้ หากไม่ได้ต้องปรับ layout ใหม่ ไม่กด Fit โดยไม่ตรวจขนาดตัวอักษร
- ถ้าพิมพ์สองหน้าลงกระดาษหนึ่งแผ่น ให้เลือก duplex / flip on long edge
- ตัวเนื้อหา TH Sarabun New 8 pt/leading 7.35 pt, ตาราง 7.1 pt/leading 7.2 pt (ตาราง CP 7 pt/leading 6.9 pt), โค้ด Menlo 5.7 pt/leading 6 pt, diagram labels ประมาณ 6-7.3 pt ส่วนใหญ่ 7.1 pt; ชื่อ/รหัส 11.55 pt แบบหนาในกรอบสีเหลืองขนาดคงที่ 44.77 × 5.05 mm
- ยังไม่ได้สร้าง Canva design ในรอบนี้ ต้นฉบับแยกคอลัมน์และกราฟิกเวกเตอร์ไว้แล้ว จึงใช้ PDF นี้เป็นเรฟ/import หรือจัดใหม่เป็น text boxes ได้ภายหลัง โดยตรวจฟอนต์และ line breaks ใหม่เมื่อแปลง
- เก็บเฉพาะ source, README, reference เดิม และ PDF สองหน้า ไฟล์ render/aux/log ที่ใช้ตรวจอยู่ใน temporary directory และล้างหลังตรวจ ไม่แตะ repository ของ TokTickIT

## การตรวจฉบับนี้

- PDF สองหน้า A4 แนวตั้ง ตรวจภาพเรนเดอร์ครบทั้งสองหน้าและขยายดูไดอะแกรม/ตัวพิมพ์เล็ก
- ไม่มีหัวกระดาษหรือ legend/เลขหน้า/แหล่งอ้างอิงท้ายหน้า; ชื่อ/รหัสประมาณ 11.5 pt มีครบทั้งสองหน้าและไม่ชนเนื้อหาคอลัมน์ขวาสุด กรอบมีขนาด/ตำแหน่งเดิม แต่ชื่ออยู่กึ่งกลางและมีระยะห่างจากเส้นกรอบมากขึ้น
- ความสูงทั้งแปดคอลัมน์อยู่ใน budget; log ไม่มี `Overfull`, `Missing character` หรือคำเตือนว่าคอลัมน์เกินหน้า
- ตรวจต้นฉบับทุกคอลัมน์แล้วไม่พบตัวอักษรไทยติดกับอังกฤษ/ตัวเลขโดยไม่เว้นวรรค; ชื่อเฉพาะและ identifiers ในรูปยังคงรูปเดิม
- ขยายตรวจไดอะแกรมครบทั้ง 17 ภาพและภาพรวมสองหน้า หลังปรับระยะไม่พบป้าย/กล่อง/ลูกศรชนกัน; ไม่ลดฟอนต์เนื้อหาหรือคำสั่งเพื่อบีบพื้นที่
- ตรวจหัวข้อและกรณีเดิมร่วมกับส่วนเพิ่ม: fork/join, CP forward/backward pass, PERT จาก Lecture 6, คำศัพท์ security และ Sample 2.8; ส่วนเพิ่มใช้พื้นที่ที่เหลือโดยคงจำนวนสองหน้า
- ฟอนต์ทุกตัวฝังใน PDF ไม่มีภาพ raster ที่อาจแตกเมื่อซูม และไม่พบข้อความออกนอกขอบปลอดภัย
- ตรวจคำหลักของบท 1-7 บนหน้าแรกครบ; ตรวจวันทำงานและ duration ของ Gantt, milestones 8/15/29 January และผลรวม Sprint 16/16 points ซ้ำด้วยการคำนวณ
- ตัวอย่างและการเติมข้อมูลที่ไม่ได้มาจากโจทย์ถูกแยกไว้ในหัวข้อสมมติฐานด้านบน ไม่ได้อ้างว่าเป็นเงื่อนไขข้อสอบจริง
- ตรวจ coverage กับ Practice Midterm Part 1 (4 activities), Part 2 (WBS/RACI/Gantt/grooming/planning) และ Parts 3-4 (UML/UI 30 + Git 20); การย่อเป็นโพยไม่ใช่การรับรองว่าทุกคำถามในข้อสอบจริงจะเหมือนตัวอย่าง
