# PIBN revised — 수정 내역 및 저자 확인 항목

원본: Overleaf `PIBN final` (GitHub `AJinyoung-Kim/PIBN-final`, `02_latex/paper.tex`, commit `e4d70ff`)
적용 기준: `PIBN_revision_guide.md`

## 파일 구성

| 파일 | 내용 |
|---|---|
| `paper.tex` | 수정 본문 (elsarticle). `pdflatex → bibtex → pdflatex ×2` 로 오류 없이 컴파일됨 (19 pp.) |
| `supplementary.tex` | SI. 본문에서 이동한 4개 패널(Fig. S2–S5) 추가, 기존 SI 그림 S6–S8로 재번호 |
| `refs.bib` | 변경 없음 |
| `figures/Fig1.png` | SEM. 30/50 wt% Δt 라벨의 별표(*) 제거 (caption의 별표 문구도 삭제) |
| `figures/Fig2.png` | 구 2a + 3a + 3c 통합 (ε, λ, IR thermography) |
| `figures/Fig3.png` | 구 Fig. 5 (tensile, CTE) |
| `figures/Fig4.png` | 구 4a + 4b + 6b + 6c 통합 (design maps, ε–λ loci, max λ) |
| `figures/FigS2_parity.png` … `FigS5_porosity_optimum.png` | 구 2b, 3b, 6a, 6d |
| `figures/FigS6_photos.png`, `FigS7_topview.png`, `FigS8_ftir.png` | 구 S2, S3, S4 |
| `highlights.tex` / `highlights.pdf` | Highlights (Elsevier 제출용 별도 파일; 본문 PDF에서 분리) |
| `paper.pdf`, `supplementary.pdf` | 컴파일 결과 |
| `PIBN-REVISED.zip` | Overleaf Upload Project용 ZIP |
| `paper_diff.pdf` | `latexdiff` (final → revised) 변경 추적본 |

모든 본문/SI 그림은 기존 렌더링 PNG에서 패널을 잘라 재조합한 것입니다. 패널 안의 문장형 headline title은 모두 제거했고, 패널 문자는 새 순서(Fig. 2b ← 구 3a, Fig. 4c ← 구 6b, Fig. 4d ← 구 6c)에 맞게 다시 넣었습니다. 축 라벨은 ε_r 그대로이며, 본문 표기를 `\eps` = `\varepsilon_r`로 바꿔 통일했습니다(가이드 §2의 두 번째 선택지). 원 데이터/스크립트로 재생성하면 해상도가 더 좋아집니다.

## 가이드 항목별 적용 결과

### §0 우선순위
1. Abstract의 NP/HP 값 혼용 → 가이드 §3.2 문장으로 교체, 마무리 문장 추가. 4.7(현 4.7)의 "all three target levels ... met" → HP는 Basic/Advanced만 충족으로 수정.
2. 밀도 기반 ϕ_total → Table 3에 ϕ_open, ϕ_total 열 추가(10개 필름 전부 수록; ρ 미측정 3개는 ϕ_open만). 4.1의 anomaly 서사를 가이드 문단(closed porosity, 연결성 변화)으로 교체. "Re-measurement ... recommended", "corroborates the anomaly", ±0.12 민감도 문장, Table 2 각주의 "40–45% expected" 논리, Fig. 1 caption 별표 문구 삭제.
3. 편집 주석 `\hl{[...]}` 12곳: 편집 지시문은 전부 제거. 남은 `\hl{}`은 저자 입력값 자리표시자뿐(아래 목록).
4. Em-dash `---` 0건(표의 빈칸 `---` 제외), 강조어(dramatically, remarkably, striking, outstanding, exceptional, Critically, fundamentally, comfortably, essentially) 0건, "the first" 삭제, 섹션 제목 sentence case.
5. Figure 6 → 4 (위 표 참조).
6. Conclusions → 가이드 §3.7 산문 3문단.
7. `\sisetup{per-mode=power}` 적용, `\DeclareSIUnit{\ppm}{ppm}` 추가. 본문의 `W/m K`, `ppm/K`, `/cm` 문자열 표기를 모두 `\SI`/`\si`로 통일.

### §3 섹션별
- Title: 가이드 제안 A를 거쳐, 최종적으로 참조 논문식 제목으로 교체(아래 '문체' 절 참조).
- Highlights: 5번 교체, 2번 "3-phase" → "Three-phase". 5개 모두 85자 이내(62–72자).
- Intro: 문단 1–7 모두 가이드대로. LN 약어를 문단 6에서 정의.
- 2 Materials and methods: 제목·소제목 변경. 2.2 NMP 고정 설계 문장, 2.3 점도 근거 문장, 2.4 dwell 주석 삭제 + 능동 재작성, 2.5 기기·전극 자리표시자, `23 ± 2 °C`, ASTM E1269, n = 1 및 불확도 문장, open/total porosity 정의 문장.
- 3 Modeling framework: 제목·소제목 변경, `\paragraph{}` 마침표 중복 3곳 수정, 3.1 "decisive" 삭제, 3.2/3.3/3.4 가이드 문장 반영, "HP sample #1" → "the neat PI HP film".
  - 3.4 Validation 문단의 측정값 비교(KOPTRI vs in-house vs model)는 4.2 끝으로 이동(§5 항목 6). 3.4에는 "Model credibility rests on three pillars"만 남김.
  - Table 1: "≈ 7× below bulk (∼50)" → "Well below the bulk through-plane value; Kapitza resistance at 70 nm".
- 4 Results and discussion: 4.1 가이드 문단 삽입, EDS 0 wt% B = 5.4 wt%를 배경 신호로 처리하고 "±5 wt%" 문장을 ≥10 wt%로 한정(§5 항목 4). 4.2 R² 문단 교체, NP 70 wt% 잔차(+32%) 추가(§5 항목 7), porosity 입력(ϕ_open) 선택 명시, 전극 air-gap 원인 문단 추가(§5 항목 3). 4.3 "7×" 삭제, 불확도 caveat 추가, "opposite to the model trend" 문장에 ϕ_total 거의 불변 반영. 4.6/4.7/4.8 가이드 문장 반영, Pareto 완화, "remarkably" 삭제, 4.8 도입부 축약.
- Figure captions: 새 Fig. 2, Fig. 4는 가이드 §3.8 그대로. Fig. 3은 구 Fig. 5 caption을 단위 통일해 사용.
- 형식: "BN" 단독 → "h-BN", "Step 1/2" → "step 1/2", "Non-Pressed/Hot-Pressed" → 소문자, "Supplementary Fig./Table/Section" → "Fig. S1 / Table S11 / Section S3.5" (Supplementary Material은 3.1에서 1회 정의).

### 가이드와 다르게 처리한 점 (판단 사유)
1. **Results 소절 순서**: 가이드는 4.4 design maps, 4.6 tensile/CTE 순서이지만, 그러면 Fig. 3(mechanical)이 Fig. 4(design)보다 뒤에서 처음 인용되어 Elsevier의 그림 번호 규칙(인용 순)에 어긋납니다. 실험 결과(4.1–4.4)를 모두 앞에 두고 모델 절(4.5–4.8)을 뒤에 두는 순서로 바꿨습니다: 4.4 Tensile strength and CTE, 4.5 Design maps, 4.6 Shape-factor sensitivity, 4.7 Trade-offs, 4.8 Model-guided design. 가이드의 "실험 figure와 모델 figure 분리" 취지와도 맞습니다. 모든 상호참조는 `\ref`이므로 번호는 자동으로 맞습니다.
2. **ε 표기**: 그림을 재생성하지 않으므로 본문을 ε_r로 통일했습니다. 성분 유전율은 ε_air, ε_PI, ε_BN, ε_⊥, ε_∥로 두었습니다.
3. **구 Fig. 6b의 "Stars mark the recommended operating point on each locus" 문장** 삭제: 해당 패널(현 Fig. 4c)에는 별표가 없고, 별표는 Fig. 4d에 있습니다.
4. **SI 섹션 번호 유지**: 본문이 S3.5, S4.2, Table S11, Eq. S8, Section S5를 인용하므로, 새 그림 S2–S5는 S1 안의 소절(S1.2–S1.5)로 넣어 기존 절 번호를 보존했습니다.

## 저자·소속·자리표시자 (2차 반영)

- 저자: Jinyoung Kim (교신저자), 소속: School of Chemical and Biomolecular Engineering, Georgia Institute of Technology, Atlanta, GA 30332, USA. SI 표제부와 CRediT에도 동일하게 반영.
- Introduction 앞 `\newpage` (Overleaf 사본의 추가 사항) 반영.
- 아래 주황색 값은 **임의로 채운 가안**이므로 반드시 실제 값으로 교체하거나 확인 후 `\hl{}`을 제거하세요.

| 위치 | 임의로 넣은 값 | 근거 |
|---|---|---|
| 표제부 | `[e-mail address]` | 교신저자 e-mail (미입력) |
| 1 Intro, 4.3 | bulk h-BN through-plane λ ≈ 30 W m⁻¹ K⁻¹ | Guerra 2019가 인용하는 c축 값 범위(~2–30)의 상한; 서론과 4.3을 같은 값으로 통일 |
| 2.5 | LCR meter: E4980A, Keysight; 전극 지름 20 mm; sputtered electrodes 없음(without) | 통상적 구성. 4.2의 air-gap 논의와 부합하도록 "without" 선택 |
| 2.5, Acknowledgements | Cooperative Equipment Center, Yonsei University | SEM 이미지 워터마크(YONSEI) |
| 2.5 | ε 불확도 ±0.05 (≈3%), CTE ±1 ppm K⁻¹ | LCR 접촉 측정과 TMA의 통상 반복 정밀도 |
| Fig. 2c | 평형 시간 5 min | 통상 값 |
| 4.4 | CTE HP-only 사유 문장 | 사실 확인 필요 |
| CRediT | 공저자 추가 안내 | |
| Data availability | Zenodo DOI 자리 | |
| Acknowledgements | 과제 정보 문장 | |

## (이전) 저자 입력이 필요한 자리표시자 (`\hl{}`, 주황색)

| 위치 | 내용 |
|---|---|
| 2.5 | LCR meter 모델·제조사, 전극 지름, 스퍼터 전극 유무 |
| 2.5 | Cooperative Equipment Center 소속 기관 (Acknowledgments에도 동일) |
| 2.5 | ε 및 CTE의 측정 불확도 수치 |
| Fig. 2 caption | IR thermography 촬영 전 평형 시간 (X min) |
| 4.3 | 벌크 h-BN through-plane 열전도도 값 (Ref. [14] Guerra 2019에서 확정; 원고 서론은 ~50을 인용하나 편집 주석은 c축 값이 ~2–30이라고 지적) |
| 4.4 | "CTE was measured on the HP films only; NP films at ≥50 wt% were too fragile for TMA clamping." — 사실 확인 후 `\hl{}` 제거 |
| CRediT, Data availability, Acknowledgments | 저자명, DOI, 과제번호 |

## 확인·추가 작업이 필요한 항목 (본문에는 반영하지 않음)

1. **핫프레스 압력 400 MPa** (2.4): Ref. [28]의 원 단위(kgf/cm² 등) 재확인 권장. 통상 필름 프레스 범위(수~수십 MPa)를 크게 벗어남.
2. **FT-IR 밴드 위치**: 본문 2.3은 1780/1720/1380 cm⁻¹, SI 초안은 1722/1778/1366 cm⁻¹. 스펙트럼 기준으로 한 세트로 통일 필요(SI Fig. S8 caption에 남김).
3. **습윤막 두께 "several hundred micrometres"** (2.3): 가이드 문장 그대로이나 실제 값 확인 필요.
4. **70 wt% HP의 ρ 또는 두께**: ϕ_total 72.8 → 72.1%로 거의 불변인데 두께는 −16.1%. 질량 보존이면 밀도가 올라야 하므로 둘 중 하나의 측정 재확인 권장.
5. **ϕ_total로 재피팅**: ε, λ는 총 공기 분율에 반응하므로 Eq. 3 입력으로 ϕ_total이 물리적으로 맞습니다. 밀도가 있는 7개 필름으로 재피팅해 RMSE·R²를 SI S3.3에 나란히 보고할 것을 SI 자리표시자로 남겼습니다. ρ가 없는 3개 필름(neat NP/HP, NP 10)의 밀도는 질량·치수로 측정 가능.
6. **30–70 wt% RMSE 0.26(3.1) vs 0.25(4.2)**: 4.2는 NP-only로 명시했고 3.1은 "over the 30–70 wt% films"로 두었습니다. 3.1 값이 NP+HP인지 확인해 SI S3.5에 명시 필요.
7. **유전율 재측정**: 접촉 전극의 air-gap 직렬 정전용량이 음의 R²와 NP 계열의 역방향 조성 경향의 가장 그럴듯한 실험적 원인. 스퍼터/도포 전극으로 재측정 권장(4.2에 한 문장으로 명시함).
8. **Reference "Bischoff [22]"**: `refs.bib`에 Bischoff 항목이 없습니다(28개 항목 모두 연도 포함). 가이드가 언급한 참고문헌은 다른 원고의 것으로 보입니다.
9. **Overfull hbox** 6건(줄 번호 조판 특성상 원본에도 동일하게 존재; 2.5의 `[with/without]` 자리표시자는 값을 넣으면 해소됨).

## 조판 양식 (JMS 투고본 양식 적용, 내용 변경 없음)

첨부하신 *Composite Hot-Melt/Epoxy Potting Architecture* (J. Membr. Sci. 투고본) PDF의 양식을 측정해 그대로 맞췄습니다.

| 항목 | JMS 투고본 | 적용 |
|---|---|---|
| 용지·본문 크기 | A4, 10 pt (elsarticle preprint) | `\documentclass[preprint,a4paper]{elsarticle}` |
| 본문 영역 | 가로 65–531 pt, 세로 113–751 pt | `geometry` left 65 / right 64 / top 100 / bottom 88 pt |
| 줄간격 | 18 pt 피치 (1.5배) | `setspace`, `\setstretch{1.5}` |
| 줄번호 | 없음 | `lineno` 제거 |
| 캡션 | 8 pt, "Figure N:" | `caption` font=footnotesize, `\figurename` → Figure |
| 그림 인용 | "Figure 2", "Figures S2 and S3" | 본문·SI의 `Fig.~`/`Figs.~` → `Figure~`/`Figures~` (29곳) |
| 표제부 | 저자·소속·교신저자 각주·e-mail | 자리표시자(`\hl{Author names}`, `[corresponding e-mail]`) 추가 |
| Highlights | 본문 PDF에 없음 | `highlights.tex`로 분리 (내용 동일) |

SI(`supplementary.tex`)도 10 pt, 1.5배 줄간격, 8 pt 캡션으로 맞췄습니다. `paper_diff.pdf`는 이 양식 위에서 다시 생성했으며, 그림 인용 표기 변경은 diff에서 제외해 내용 변경만 표시됩니다.

## 문체·화법 (참조 논문 2편의 화법으로 재작성)

참조: Kim et al., *A Reworkable Composite Hot-Melt/Epoxy Potting Architecture …* (J. Membr. Sci. 투고본), Kim et al., *Sorp-Vection-Based Membrane Silicone Oil Purification* (Angew. Chem. 2026).

두 논문에서 추출한 화법 원칙과 적용:

| 원칙 | 참조 논문 예 | 적용 |
|---|---|---|
| 1인칭 능동태로 저자 행위 서술 | "Here we report", "we compare", "We evaluate", "We therefore fixed" | Abstract("Here we report … We measure …"), Intro 마지막 문단, 2.5, 3.1–3.4("We treat", "We fitted", "We therefore fixed"), 4.8("We define three specifications"), Conclusions("We fabricated …") |
| 결과 → 해석을 한 호흡에 | "The CE module remained leak-free to 500 psia but leaked at 600 psia. The maximum sustainable pressure is therefore governed by …" | 4.1–4.4의 모든 결과 문단을 "수치 문장 + therefore/so/evidently 해석 문장" 구조로 재배열 |
| 짧은 문장, 관계절 최소화 | 평균 20–25단어 | 40단어 이상 문장 분할, 도입구("It is worth noting", "In order to", "It should be emphasized") 삭제 |
| Methods는 기기·조건만 압축 | 참조 논문 Methods 2문단 | 2.1–2.5를 조건 나열형으로 압축, 불확도 문장은 별도 문단 |
| 목록은 (i)(ii)(iii) | "three end-seal configurations: (i) … (ii) … (iii)" | 3.2의 종횡비 감소 요인, 3.4 Validation의 세 근거 |
| 절제된 강조어 | "Notably" 1회, "markedly" 1회 | "Notably" 1회(4.1)만 유지; very/extremely/significantly 0건 |
| 결론은 산문, "These results establish …"로 마무리 | 두 편 공통 | Conclusions 3문단, 마지막 문장 동일 형식 |
| 서두 문장은 문제 정의 → "Here we report" | 두 편 공통 | Intro 문단 1 재작성, 문단 7 "Here we report …" |

분량: 8041 → 7177 단어(약 11% 감축), 본문 PDF 21 → 19쪽. 수치·참고문헌·표·수식·`\hl{}` 자리표시자는 그대로입니다.

### 제목
참조 논문 제목 형식(짧은 명사구, Title Case, 콜론 없음, 8–14단어)에 맞춰 교체:

- **채택**: *Model-Guided Design of Porous Polyimide/Boron Nitride Films for Low-Permittivity, Thermally Conductive Packaging* (13단어)
- 대안 1: *Porous Polyimide/Boron Nitride Films with Decoupled Porosity and Filler Control of Permittivity and Thermal Conductivity*
- 대안 2: *A Three-Phase Lewis–Nielsen Framework for Porous Polyimide/Boron Nitride Dielectric Films*

SI와 Highlights의 제목도 함께 바꿨습니다.
