# เตรียม Lab 5: Cloud Deployment and CI/CD on GCP

**Product:** PocketLedger · **งานกลุ่ม 2 คน:** Wisit + Natthawat · **หัวข้อ:** Personal Money and Expense Logging System · **จุดเริ่ม:** accepted Group Project Sprint 1 release · **ส่ง:** 15 พฤศจิกายน 2026 เวลา 23:59 · **คะแนน:** 100 (5% ของรายวิชา)

นี่เป็นเอกสารเตรียมงาน ยังไม่มีการอ้างว่ามี public URL, CI, cloud resources หรือผลตรวจผ่านแล้ว ต้องใช้แอปและ product repository ของกลุ่มเดียวกับ [Group Project](../../project/README.md) ไม่ใช่ย้าย Lab 5 กลับไปเพิ่มฟีเจอร์ใน TokTickIT รายบุคคล

## แหล่งข้อมูลและลำดับอ้างอิง

- [Lab 5 updated handout](01_SE_Lab_5_updated.pdf): อ่านครบ 11 หน้า; §4 R-01–R-12/required files, §8 checks, §12 rubric/report format หากขัดกับ guide/kit ให้ยึด handout (§6)
- [Student Guide V1.1](03_Student-Guide-GCP-Deployment-and%20CI%20CD-V1_1.pdf): 105 PDF pages; Episodes 0–10 เป็น walkthrough ใช้อ่าน episode ที่กำลังจะทำก่อนรันคำสั่ง
- [Starter kit README](toktickit-lab5-starter/README.md): รายการ 23 template files และส่วนที่ต้องแก้ตามแอป
- [Lecture 11](../../lectures/Week%2011/CPE334_Lecture11%20-%20Cloud%20Deployment%20and%20Delivery%20to%20Users.pdf): SDD หน้า 8, version chain หน้า 36, workflow นักศึกษา หน้า 37, deploy/smoke หน้า 40–41

## Starter kit ที่แตกแล้ว

ไฟล์จาก `02_lab5-starter-kit.zip` อยู่ใน [`toktickit-lab5-starter/`](toktickit-lab5-starter/) ครบ **23 ไฟล์ รวม 110,871 bytes** ตรวจ ZIP CRC แล้วเทียบข้อมูลทุกไฟล์ตรงกับ archive member ทุกไบต์เมื่อ 3 พฤศจิกายน 2026 ก่อนลบ ZIP เดิมตามคำอนุญาต

SHA-256 ของ ZIP ต้นฉบับ: `7797840c4d1ca256270e4f4efea93b5d471d24b1e988ad4b6b9bf7bea5d1713c`

โฟลเดอร์นี้เป็น reference ที่เก็บใน course repo ซึ่งอยู่แยกจาก product repo ตามแนวทาง guide อย่า execute deploy/teardown หรือคัดลอกทับแอปทั้งก้อน Starter ไม่มี application source และสมมติ Node.js 24 + React/Express + PostgreSQL/Prisma; ไม่ใช่ข้อบังคับให้เปลี่ยน stack ของทีม

| กลุ่มไฟล์ใน kit | หน้าที่ / ตอนนำไปใช้ |
| --- | --- |
| root `Dockerfile`, `.dockerignore`, `docker-compose.yml`, client/server Dockerfiles และ entrypoint/nginx | Episode 3: production image และ local app/database |
| `.github/workflows/ci-docker.yml` + **ทั้ง `deploy/` รวม tests** | Episode 4: CI ตรวจ app และ deployment scripts แบบ offline |
| `deploy/deploy.sh` | Episode 5: one-time initial cloud setup; ต้องอ่านและปรับก่อนใช้ |
| `.github/workflows/deploy.yml`, `deploy/release.sh`, `deploy/smoke_test.py` | Episode 7: reviewed main release → image/migrate/deploy/smoke |
| `.env.example` ของ UI/API | placeholder configuration; ต้องเพิ่มทุก variable ที่แอปจริงอ่าน |
| `docs/`, `.github/dependabot.yml` | คำอธิบาย reference และ action updates |
| `deploy/teardown.sh` | หลังสิ้นสุด grading และได้รับอนุญาต ไม่ใช้ตอนเก็บหลักฐาน |

**ช่องที่พบว่าต้องปรับแน่นอนก่อนใช้:** CI template ตั้ง `pull_request.branches: [main]` เท่านั้น ต้องเพิ่ม sprint staging จริงให้ครอบคลุม integration และ release PR ตาม Lecture 11 หน้า 37 อีกทั้งต้องตรวจว่า test commands ครอบคลุมชุดทดสอบของแอป รวม E2E ที่เกี่ยวข้อง ไม่ถือว่า kit รัน tests ของทีมครบโดยอัตโนมัติ

เปลี่ยนชื่อ `toktickit`/resource/image, endpoint เช่น `/api/categories`, build paths, package manager/runtime, migration/seed และ secrets ให้ตรงกันทุกไฟล์ ห้ามปล่อยให้ smoke check ผ่านเพียงเพราะตรวจ endpoint ของตัวอย่างที่ไม่มี domain ของทีม

## สิ่งที่ต้องเตรียมก่อนเริ่ม cloud

- [ ] Team name/number/section, product repo URL, sprint staging และ accepted Sprint 1 SHA/tag ยืนยันแล้ว
- [ ] Repo เป็น public จนจบ grading; ทั้งสองคนเปิด code/Issues/PRs/Actions และ review กันได้
- [ ] Product baseline/contract/test history มาจาก Deliverable 1 และแอปรัน local ได้จริง
- [ ] เลือกสมาชิกหนึ่งคนที่มี personal Gmail ไม่เคยใช้ Free Trial สำหรับ GCP ตาม handout §4.4; ไม่ใช้ `@mail.kmutt.ac.th`
- [ ] เลือก GCP project เดียวใช้ Lab 5–7/Final และเตรียมเพิ่ม teammate เป็น IAM Editor ตาม handout โดยคนอ่าน/ดำเนินการขั้น billing/IAM/database
- [ ] จัด synthetic demo data และวิธีส่ง test credentials ส่วนตัว ไม่มี secrets ใน chat/repo/PDF/logs
- [ ] อ่านทุก command/console change ก่อนทำจริง; handout ห้ามจ่าย prepayment/กด Upgrade ถ้าพบให้เก็บภาพที่ไม่แสดงข้อมูลลับและแจ้ง TA

ตาม handout แนะนำ budget alerts ก่อนสร้าง paid resources; alert ไม่ใช่ spending cap รักษาบริการให้ตรวจได้จนผู้สอนประกาศจบ grading การ pause/teardown ต้องไม่ขัดช่วงตรวจ/demo/pipeline

เครื่อง Mac รอบตรวจ 3 พ.ย. มี Git, Node, npm, Docker engine, GitHub CLI และ Python แล้ว; `gcloud` ไม่อยู่บน PATH คู่มือรองรับ Cloud Shell จึงเลือกใช้ Cloud Shell หรือติดตั้ง local CLI เมื่อตกลงวิธีแล้ว Node local เป็น 26.7.0 แต่ kit ใช้ 24 ต้องกำหนด version ของทีมให้ตรงใน local/CI/container โดยไม่เปลี่ยน global runtime ของงานอื่นโดยไม่จำเป็น

## Required work: R-01–R-12

| ID | สิ่งที่ต้องทำ | หลักฐาน / check ที่เชื่อม |
| --- | --- | --- |
| R-01 | clean clone สร้าง Docker image และรันได้จริง | C-03, Dockerfile/build/run output |
| R-02 | ทุก setting จาก env, document ทุก app variable, ไม่มี real secrets | C-03, `.env.example`, env table |
| R-03 | public GCP URL และ domain UI → API → DB | C-04 |
| R-04 | persistent DB; record เดิมอยู่หลัง restart **และ** redeploy | C-05 |
| R-05 | ทุก relevant PR รัน build และ automated tests ที่มีความหมาย | C-01 |
| R-06 | required check ที่ล้มเหลวขวาง merge ได้จริง | C-02, failing temporary PR + blocked button |
| R-07 | accepted main releases deploy ด้วย repeatable pipeline; มี manual approval ใน pipeline ได้ | C-06 |
| R-08 | ระบุ release commit/tag และทำขั้นตอนซ้ำได้ | C-06, release procedure/version chain |
| R-09 | Issue/board, feature/fix → reviewed staging PR → integration → reviewed release PR → main | C-06, substantive teammate review; ไม่ self-approve |
| R-10 | label เช่น `lab5`, เก็บ commits/contracts/CI history; CI ยังบังคับหลัง Lab 5 | C-06 และ evidence links |
| R-11 | ทั้งสองคนมีส่วนร่วม requirements/testing/supervision/implementation/review/deploy; pair work ระบุทั้งคู่ | contribution table + Issues/PRs; ไม่กำหนด equal commits |
| R-12 | public repo จนจบ grading ให้ TA/partner team เปิดดูได้ | repo visibility/access |

## งาน 9 ชุดตาม guide

เลขในตารางเป็นลำดับงาน ไม่ใช่ GitHub Issue ID ที่สร้างแล้ว เมื่อเริ่ม implementation ใช้ Issue จริงของทีมและ label `lab5`

| งาน | Guide (PDF pages) | Done when |
| --- | --- | --- |
| บัญชี/project/team access และ cost control | Ep. 1, 6–25 | account/project ใช้ได้และทั้งคู่เข้าถึง; ไม่มี payment/upgrade นอกคำสั่งรายวิชา |
| Cloud-ready app + initial deployment doc | Ep. 2, 26–29 | env ครบ, durable state, seed safe, production auth, PORT/listen และ readiness ตรวจได้ |
| Docker packaging | Ep. 3, 30–37 | clean build + running app/database |
| PR CI | Ep. 4, 38–43 | staging/main PR รัน checks และอ่านผล tests ได้ |
| First GCP deploy | Ep. 5, 44–55 | public URL login/domain workflow ได้ |
| GitHub–GCP connection และ gate | Ep. 6, 56–80 | main-only deployment identity/config; required CI blocks failure |
| Pipeline + reviewed visible change | Ep. 7, 81–91 | accepted change ผ่าน staging/main แล้ว URL/revision แสดง version ที่พิสูจน์ได้ |
| Persistence | Ep. 8, 92–95 | record เดิมอยู่หลัง restart และ redeploy; rollback/forward เป็น recommended exercise |
| deployment.md + final evidence index | handout §4.3/§12 | rubric ทุก Part มีหลักฐานชี้ตรงและผลจริง |

Ep. 9 (96–101) เป็นการ pause อย่างเหมาะสม; Ep. 10 (102–105) เป็น teardown หลังจบ access period อย่าใช้การ rollback ใน Ep. 8 แทนหลักฐาน restart โดยไม่แสดงว่าทดสอบ restart จริง

### Cloud-ready check ให้เข้ากับ Theme 7

Guide Ep. 2 ให้ตรวจ durable uploads ถ้ามี, production-safe rerunnable seed, ไม่มี identity bypass/default-password display, durable sessions ตาม auth design, `PORT` และ readiness ที่ตอบ failure เมื่อ DB ใช้ไม่ได้ สำหรับระบบการเงินต้องระวัง seed ไม่ reset opening balances/transactions ของผู้ใช้เดิม และข้อมูลสำคัญไม่อยู่เฉพาะ container memory/disk

### Required กับ recommended

Cloud Run, Artifact Registry, Cloud SQL PostgreSQL, Secret Manager, WIF, full-SHA image tag/digest, separate migration job, read-only post-deploy smoke, pinned Actions, budget controls และ rollback/forward เป็น reference/recommended practices ตาม handout §5 ไม่ใช่คะแนนเพิ่มแยก แต่ช่วยทำ required checks ให้พิสูจน์ได้ หากเลือกต่างให้บันทึกเหตุผลใน deployment.md

ไม่มี requirement ให้ทำ Kubernetes, infrastructure-as-code, cloud staging แยก, custom domain, load balancer, canary/blue-green, monitoring dashboard หรือ load testing ใน Lab 5

## Required product files และแม่แบบเตรียมไว้

| ไฟล์ใน product repo | ต้องมีอะไร |
| --- | --- |
| `Dockerfile`, `.dockerignore` | build/runtime files ของแอปจริง ไม่พึ่งไฟล์ที่ไม่ได้อยู่ใน clean clone |
| `docker-compose.yml` ถ้าใช้ app + DB local | services/ports/config ตาม stack จริง |
| `.env.example` หรือแยก UI/API | ทุก env variable ที่อ่านจริง, purpose และ placeholders |
| CI/deploy workflows เช่น `.github/workflows/ci-docker.yml`, `deploy.yml` | required checks และ main-only repeatable deploy |
| **`docs/labs/lab-05/deployment.md`** | stack/deviations, env, commands, GCP resources, release/identify-running-version |

ใช้ [deployment template](deployment-template.md) เป็นแม่แบบของ path สุดท้ายข้างต้น ปัจจุบันยังอยู่ใน course repo; อย่าคัดลอกคำสั่งหรือชื่อ resource ตัวอย่างโดยไม่ปรับ ระบบไม่ต้องมี database upload feature หาก product scope ไม่ต้องใช้

Working draft ของ PocketLedger อยู่ที่ [product deployment.md](https://github.com/Palapluem/pocket-ledger/blob/main/docs/labs/lab-05/deployment.md) แล้ว ให้เติม environment/commands/resources/results จริงที่ product draft นี้ โดย course template คงเป็นแม่แบบ ไม่มี completed deployment ในรอบ bootstrap

## Check/evidence matrix

| Check | สิ่งที่ต้องแสดง | แผนสำหรับ Theme 7 | ผลจริง / ลิงก์ / tested SHA |
| --- | --- | --- | --- |
| C-01 | normal PR build + automated tests pass | domain, auth/access, persistence และ UI checks ตามชุดจริงของทีม | |
| C-02 | failed required test blocks merge | temporary branch/normal PR ตาม guide; เก็บ required-check status และ disabled merge, **ไม่ merge** | |
| C-03 | fresh clone build/run จาก documented env | setup DB/migrate/seed, production image, sign in/read sample data | |
| C-04 | public URL login + main business action + rejection/access restriction | salary/split charge/repayment ที่เลือก และ validation หรือ cross-user/role denial | |
| C-05 | record เดิมอยู่หลัง restart และ redeploy | record ID + details/history/balances ก่อนและหลัง; restart กับ redeploy แยกเหตุการณ์ชัด | |
| C-06 | reviewed staging → main → deploy; running revision ตรง commit | Issue/feature PR/review/release PR/CI/deploy/image/revision | |

ผลในคอลัมน์สุดท้ายเว้นไว้สำหรับการรันจริง ห้ามนำตัวเลขจาก TokTickIT หรือ starter example มาใส่เป็นผลของแอปกลุ่ม

## Release workflow และไม่สร้าง PR วน

```text
bounded Issue + contract
  → feature/fix branch from current sprint staging
  → relevant tests + teammate-reviewed PR to staging
  → integration/system checks
  → teammate-reviewed release PR to main
  → CI → image → migration → deploy → smoke
```

CI ต้องครอบคลุม integration/release PR ทั้งคู่และ required checks ต้องขวาง normal release path ได้ C-02 เป็น failure-proof PR แยกที่ไม่ merge ไม่ใช่เหตุผลให้ bypass rules หรือทำให้ main เสีย เก็บ PR/commit/run evidence ตาม R-10

อาจต้องมี reviewed bootstrap release เพื่อให้ workflow/config อยู่บน main ก่อน setup บางตอน จัดตาม dependency ที่มีจริง ไม่รับปากว่าใช้ PR เดียวจบทั้ง Lab และไม่เปิด docs PR เพียงเพื่อบันทึก merge ของ PR ก่อนหน้าอีกชั้น เก็บ release SHA/tag ที่แน่นอน แล้วอ้าง pipeline/image/revision นั้นใน report

Version chain ที่ต้องตรวจได้: **Git commit SHA → Docker image digest → GCP running revision** การ rollback image ไม่ได้ย้อน database schema จึงต้องวาง compatibility/migrations ก่อนลอง rollback

## Rubric และรายงานที่ต้องส่ง

| Heading | คะแนน | หลักฐาน |
| --- | ---: | --- |
| Answer Part 0: Team and Evidence Index | บังคับ ไม่คิดแยก | ทีม/IDs/GitHub, public repo, submitted release, URL/served commit, contributions, evidence index |
| Answer Part 1: CI and Quality Gate | 30 | workflow, passing PR/tests, main required-check setting, failed temporary PR + blocked merge |
| Answer Part 2: Docker and Reproducible Configuration | 20 | Docker files, C-03 commands/output, running app+DB, env examples/table |
| Answer Part 3: GCP Deployment and Persistence | 35 | live URL/domain workflow/UIAPI DB, service/database, before/after restart/redeploy |
| Answer Part 4: Repeatable Release Pipeline | 15 | labelled Issue/PR/review/release/run/revision/commit และ procedure |

ใช้ [report outline](report-outline.md), ส่ง PDF หนึ่งไฟล์ต่อทีมทาง LEB2 ชื่อ **`lab5_sec<section>_<group name>.pdf`** (ยังไม่ตั้งชื่อจริงเพราะ section/ชื่อกลุ่มยังไม่ยืนยัน) รายงานเป็น **concise evidence index**: direct links + คำอธิบายสั้น 1–2 ประโยค ใช้ภาพเฉพาะสิ่งที่ลิงก์แสดงเองไม่ได้ เช่น blocked merge, console setting และ before/after persistence ทุกภาพ numbered caption ระบุ check/R ID และ commit/run/URL อ่านได้ที่ 100% และไม่มี secret

ไม่แคป source/Markdown ทั้งไฟล์ซ้ำกับลิงก์ทุกหน้า ไม่แนบ full prompt transcripts และไม่ทำ Appendix ยาวเพื่อเพิ่มจำนวนหน้า เก็บ complete raw evidence ที่ปลอดภัยแยกไว้ใช้ตรวจ โดยสรุป actual commands/results/versions ให้ครบใน report

## Final readiness

- [ ] C-01–C-06 มีผลจริงและ link/version ครบ ไม่มี required failure ถูกซ่อน
- [ ] clean clone + env + image + DB ใช้งานได้
- [ ] public URL แสดง accepted main release และตรวจ running commit ได้
- [ ] persistence ผ่านทั้ง restart และ redeploy
- [ ] repo public, required gate บังคับจริง และทั้งสองคนมี substantive participation
- [ ] deployment.md และ report index ตรงกับ release ที่ส่ง; จำกัดภาพให้จำเป็น/อ่านได้
- [ ] ไม่มี secret ใน repository/image/logs/PDF; service เปิดให้ตรวจจนประกาศจบ grading
