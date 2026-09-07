"""Build PIBN_Figure_Data.xlsx: plot-ready data for Figures 2, 3, 4 of the revised manuscript.

Measured values (blue) are taken from Tables 2-4 of the manuscript; model values (black) are live
Lewis-Nielsen formulas that reference the yellow parameter cells on the Parameters sheet.
"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.utils import get_column_letter as L
from openpyxl.comments import Comment

OUT = "/home/user/PIBN/PIBN_revised/data/PIBN_Figure_Data.xlsx"
ARIAL = "Arial"
BLUE = Font(name=ARIAL, size=10, color="0000FF")
BLACK = Font(name=ARIAL, size=10)
BOLD = Font(name=ARIAL, size=10, bold=True)
TITLE = Font(name=ARIAL, size=12, bold=True)
GREY = Font(name=ARIAL, size=9, italic=True, color="666666")
YELLOW = PatternFill("solid", fgColor="FFFF00")
HEAD = PatternFill("solid", fgColor="DDEBF7")
thin = Side(style="thin", color="999999")

wb = Workbook()

def header(ws, row, labels, col0=1):
    for j, lab in enumerate(labels):
        c = ws.cell(row=row, column=col0 + j, value=lab)
        c.font = BOLD; c.fill = HEAD; c.alignment = Alignment(horizontal="center", wrap_text=True)

def setw(ws, widths):
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[L(i)].width = w

# ------------------------------------------------------------------ README
ws = wb.active; ws.title = "README"
lines = [
 ("PIBN revised manuscript: plot-ready data for Figures 2, 3, 4", TITLE),
 ("", BLACK),
 ("Legend", BOLD),
 ("  Blue text  = measured values transcribed from the manuscript (Tables 2-4, Section 4.1 thickness data, Fig. 2c thermography).", BLUE),
 ("  Black text = three-phase Lewis-Nielsen model, computed by live formulas from the Parameters sheet.", BLACK),
 ("  Yellow fill = editable inputs (Parameters sheet). Change a parameter and every model series recalculates.", BLACK),
 ("", BLACK),
 ("Sheet -> figure panel", BOLD),
 ("  Parameters      constants of the model (eps_PI, eps_BN, A_BN, A_pore, lam_BN_eff, ...)", BLACK),
 ("  Samples         all ten films: composition, porosity (open/total), density, Cp, alpha, lambda, eps, tensile, CTE + model columns", BLACK),
 ("  Fig2a_Dielectric   eps (100 kHz) vs h-BN wt%: NP/HP measured, LN model at each film's open porosity, KOPTRI point", BLACK),
 ("  Fig2b_Thermal      lambda vs h-BN wt%: measured (laser flash), LN model at each film's open porosity; blanks = not measured (fragile)", BLACK),
 ("  Fig2c_IR           spot temperatures read from the infrared images (200 C stage), for the annotation of panel (c)", BLACK),
 ("  Fig3a_Tensile      tensile strength NP/HP and NP->HP change (%)", BLACK),
 ("  Fig3b_CTE          CTE of HP films with Turner (lower) and rule-of-mixtures (upper) bounds; PCB window 3-17 ppm/K", BLACK),
 ("  Fig4a_EpsMap       eps grid: rows = porosity (%), columns = h-BN wt%  (contour/heat map) + measured NP/HP overlay for arrows", BLACK),
 ("  Fig4b_LamMap       lambda grid, same layout as Fig4a", BLACK),
 ("  Fig4c_Loci         eps-lambda loci: porosity swept 20-95 % for 0/10/30/50/70 wt%; measured 70 wt% points", BLACK),
 ("  Fig4d_MaxLambda    maximum lambda under an eps ceiling (porosity optimised), per loading; stars = 70 wt% at eps <= 1.6 and 1.8", BLACK),
 ("", BLACK),
 ("Notes", BOLD),
 ("  1. lambda measured values are alpha*rho*Cp from Table 3 (0.063, 0.091, 0.305 NP; 0.114, 0.051, 0.088, 0.279 HP). The earlier workbook", BLACK),
 ("     used values digitised from the old figure (0.06, 0.09, 0.047, 0.084, 0.11); the Table 3 values are the ones to plot.", BLACK),
 ("  2. The model uses the OPEN (mercury intrusion) porosity as the pore input, as in the manuscript. Total porosity is listed for reference.", BLACK),
 ("  3. Panel (d) uses INDEX/MATCH on the Fig4c_Loci sheet (porosity step 0.5 %); resolution of the reported optimum is +/-0.25 % porosity.", BLACK),
 ("  4. Model constants reproduce Table 2 of the manuscript to +/-0.002 and the thermal RMSE of 0.027/0.030 W m-1 K-1.", BLACK),
]
for i, (t, f) in enumerate(lines, 1):
    c = ws.cell(row=i, column=1, value=t); c.font = f
ws.column_dimensions["A"].width = 130

# ------------------------------------------------------------------ Parameters
wp = wb.create_sheet("Parameters")
wp["A1"] = "Three-phase Lewis-Nielsen model parameters (edit yellow cells only)"; wp["A1"].font = TITLE
header(wp, 3, ["Name", "Value", "Unit", "Meaning / source"])
params = [
 ("eps_PI", 3.5, "-", "Dielectric constant of dense PMDA-ODA PI (manuscript Section 3.1)"),
 ("eps_BN", 6.0, "-", "Dielectric constant of h-BN (manuscript Section 1)"),
 ("eps_air", 1.0, "-", "Dielectric constant of air"),
 ("A_BN_eps", 0.68, "-", "h-BN shape factor, dielectric model (fitted, weakly determined; Table 1)"),
 ("phimax_BN_eps", 0.99, "-", "h-BN max. packing, dielectric model (boundary; Table 1)"),
 ("A_pore", 0.08, "-", "Pore shape factor (fitted; Table 1)"),
 ("phimax_pore", 0.99, "-", "Pore max. packing (boundary; Table 1)"),
 ("lam_PI", 0.12, "W m-1 K-1", "Thermal conductivity of dense PI"),
 ("lam_BN_eff", 6.81, "W m-1 K-1", "Effective h-BN conductivity (fitted, single parameter; Table 1)"),
 ("lam_air", 0.026, "W m-1 K-1", "Thermal conductivity of air"),
 ("A_BN_lam", 5.5, "-", "h-BN shape factor, thermal model (fixed, literature; Table 1)"),
 ("phimax_BN_lam", 0.60, "-", "h-BN max. packing, thermal model (fixed, literature; Table 1)"),
 ("rho_PI", 1.42, "g cm-3", "Density of PI (Section 3.1)"),
 ("rho_BN", 2.29, "g cm-3", "Density of h-BN (Section 3.1)"),
]
for i, (n, v, u, m) in enumerate(params, 4):
    wp.cell(row=i, column=1, value=n).font = BOLD
    c = wp.cell(row=i, column=2, value=v); c.font = BLUE; c.fill = YELLOW
    wp.cell(row=i, column=3, value=u).font = BLACK
    wp.cell(row=i, column=4, value=m).font = GREY
    wb.defined_names[n] = DefinedName(n, attr_text=f"Parameters!$B${i}")
setw(wp, [16, 10, 12, 80])

# LN helper formula strings ----------------------------------------------------
def phiBN(wcell):   # wt% cell -> solid-phase volume fraction
    return f"IF({wcell}=0,0,({wcell}/100/rho_BN)/(({wcell}/100/rho_BN)+((1-{wcell}/100)/rho_PI)))"
def eps_dense(phi):  # phi = cell with phi_BN
    return f"eps_PI*(1+A_BN_eps*((eps_BN/eps_PI-1)/(eps_BN/eps_PI+A_BN_eps))*{phi})/(1-((eps_BN/eps_PI-1)/(eps_BN/eps_PI+A_BN_eps))*(1+((1-phimax_BN_eps)/phimax_BN_eps^2)*{phi})*{phi})"
def lam_dense(phi):
    return f"lam_PI*(1+A_BN_lam*((lam_BN_eff/lam_PI-1)/(lam_BN_eff/lam_PI+A_BN_lam))*{phi})/(1-((lam_BN_eff/lam_PI-1)/(lam_BN_eff/lam_PI+A_BN_lam))*(1+((1-phimax_BN_lam)/phimax_BN_lam^2)*{phi})*{phi})"
def pore_step(kd, kair, p):  # kd = dense-property cell, p = porosity fraction cell/expr
    Bp = f"(({kair}/{kd}-1)/({kair}/{kd}+A_pore))"
    return f"{kd}*(1+A_pore*{Bp}*{p})/(1-{Bp}*(1+((1-phimax_pore)/phimax_pore^2)*{p})*{p})"

# ------------------------------------------------------------------ Samples
wsm = wb.create_sheet("Samples")
wsm["A1"] = "All ten films: measured data (blue) and model columns (formulas)"; wsm["A1"].font = TITLE
cols = ["h-BN (wt%)", "State", "phi_open (%)  Hg intrusion", "phi_total (%)  1-rho/rho_solid", "rho (g cm-3)", "Cp (J g-1 K-1)",
        "alpha (mm2 s-1)", "lambda_exp (W m-1 K-1)", "eps_exp (100 kHz)", "Tensile (MPa)", "CTE_exp HP (ppm K-1)",
        "CTE_Turner (ppm K-1)", "CTE_ROM (ppm K-1)", "Thickness SEM (um)", "Delta t (%)",
        "phi_BN (solid vol frac)", "rho_solid (g cm-3)", "eps_dense (model)", "eps_LN (model)", "Delta_eps (%)",
        "lam_dense (model)", "lam_LN (model)", "Delta_lam (%)", "Notes"]
header(wsm, 3, cols)
# measured rows (manuscript Tables 2-4; thickness from Fig. 1 labels)
rows = [
 # wt, state, phi_open, rho, Cp, alpha, lam, eps, tensile, CTE, Turner, ROM, thick, dt, note
 (0,  "NP", 75.4, None,  None,  None,  None,  1.757, 20.85, None,  None,  None,  167,  None, ""),
 (10, "NP", 91.4, None,  None,  None,  None,  1.740, 14.86, None,  None,  None,  184,  None, "lambda not measured (film fragility)"),
 (30, "NP", 48.8, 0.323, 0.853, 0.230, 0.063, 1.659, 25.43, None,  None,  None,  91.5, None, ""),
 (50, "NP", 58.1, 0.515, 0.875, 0.202, 0.091, 1.407, 12.47, None,  None,  None,  84.1, None, ""),
 (70, "NP", 54.2, 0.526, 0.838, 0.693, 0.305, 1.278, None,  None,  None,  None,  137,  None, "tensile not tested (brittle)"),
 (0,  "HP", 43.4, None,  None,  None,  None,  2.178, 37.02, 41.92, 41.92, 41.92, 113,  -32.3, "lambda not measured (film fragility)"),
 (10, "HP", 29.8, 0.879, 0.903, 0.143, 0.114, 1.924, 17.74, 24.96, 9.69,  39.31, 134,  -27.2, ""),
 (30, "HP", 67.2, 0.455, 0.863, 0.131, 0.051, 1.864, 38.15, 16.49, 4.00,  33.43, 57.2, -7.0,  "KOPTRI cross-check eps = 1.610 (ASTM D150)"),
 (50, "HP", 64.6, 0.678, 0.885, 0.147, 0.088, 1.829, 24.28, 13.06, 2.61,  26.45, 84.8, +0.8,  ""),
 (70, "HP", 48.8, 0.539, 0.846, 0.613, 0.279, 1.622, None,  10.11, 1.98,  18.02, 115,  -16.1, "tensile not tested (brittle)"),
]
for i, r in enumerate(rows, 4):
    wt, st, po, rho, cp, al, lam, eps, ten, cte, tur, rom, th, dt, note = r
    vals = [wt, st, po, None, rho, cp, al, lam, eps, ten, cte, tur, rom, th, dt]
    for j, v in enumerate(vals, 1):
        c = wsm.cell(row=i, column=j, value=v); c.font = BLUE
    # phi_total from density
    wsm.cell(row=i, column=4, value=f'=IF(E{i}="","",100*(1-E{i}/Q{i}))').font = BLACK
    wsm.cell(row=i, column=16, value="=" + phiBN(f"A{i}")).font = BLACK
    wsm.cell(row=i, column=17, value=f"=1/((A{i}/100/rho_BN)+((1-A{i}/100)/rho_PI))").font = BLACK
    wsm.cell(row=i, column=18, value="=" + eps_dense(f"P{i}")).font = BLACK
    wsm.cell(row=i, column=19, value="=" + pore_step(f"R{i}", "eps_air", f"(C{i}/100)")).font = BLACK
    wsm.cell(row=i, column=20, value=f"=100*(S{i}-I{i})/I{i}").font = BLACK
    wsm.cell(row=i, column=21, value="=" + lam_dense(f"P{i}")).font = BLACK
    wsm.cell(row=i, column=22, value="=" + pore_step(f"U{i}", "lam_air", f"(C{i}/100)")).font = BLACK
    wsm.cell(row=i, column=23, value=f'=IF(H{i}="","",100*(V{i}-H{i})/H{i})').font = BLACK
    wsm.cell(row=i, column=24, value=note).font = GREY
wsm["A15"] = "Sources: phi_open, rho, Cp, alpha, lambda = Table 3; eps = Table 2; tensile, CTE, Turner, ROM = Table 4; thickness = Fig. 1 SEM labels; Delta t = Section 4.1."
wsm["A15"].font = GREY
wsm["A16"] = "RMSE check:"; wsm["A16"].font = BOLD
wsm["B16"] = "eps NP"; wsm["C16"] = "=SQRT(SUMPRODUCT((S4:S8-I4:I8)^2)/5)"
wsm["D16"] = "eps HP"; wsm["E16"] = "=SQRT(SUMPRODUCT((S9:S13-I9:I13)^2)/5)"
wsm["F16"] = "lam NP"; wsm["G16"] = "=SQRT(SUMPRODUCT((V6:V8-H6:H8)^2)/3)"
wsm["H16"] = "lam HP"; wsm["I16"] = "=SQRT(SUMPRODUCT((V10:V13-H10:H13)^2)/4)"
for a in ("B16", "D16", "F16", "H16"): wsm[a].font = BOLD
for a in ("C16", "E16", "G16", "I16"): wsm[a].font = BLACK; wsm[a].number_format = "0.000"
wsm.freeze_panes = "C4"
setw(wsm, [10, 7, 13, 14, 10, 11, 11, 13, 12, 11, 12, 12, 12, 12, 9, 12, 11, 11, 11, 10, 11, 11, 10, 40])
for rr in range(4, 14):
    for cc in (16, 17, 18, 19, 21, 22): wsm.cell(row=rr, column=cc).number_format = "0.000"
    wsm.cell(row=rr, column=4).number_format = "0.0"; wsm.cell(row=rr, column=20).number_format = "0.0"; wsm.cell(row=rr, column=23).number_format = "0.0"

# ------------------------------------------------------------------ Fig2a
w2a = wb.create_sheet("Fig2a_Dielectric")
w2a["A1"] = "Figure 2a: dielectric constant (100 kHz) vs h-BN content"; w2a["A1"].font = TITLE
header(w2a, 3, ["h-BN (wt%)", "eps_NP_exp", "eps_HP_exp", "eps_LN_NP (model at NP open porosity)", "eps_LN_HP (model at HP open porosity)", "KOPTRI HP 30 wt% (not fitted)", "eps_air (reference line)"])
for k, wt in enumerate([0, 10, 30, 50, 70]):
    r = 4 + k; np_row = 4 + k; hp_row = 9 + k
    w2a.cell(row=r, column=1, value=wt).font = BLUE
    w2a.cell(row=r, column=2, value=f"=Samples!I{np_row}").font = BLUE
    w2a.cell(row=r, column=3, value=f"=Samples!I{hp_row}").font = BLUE
    w2a.cell(row=r, column=4, value=f"=Samples!S{np_row}").font = BLACK
    w2a.cell(row=r, column=5, value=f"=Samples!S{hp_row}").font = BLACK
    w2a.cell(row=r, column=7, value="=eps_air").font = BLACK
    for cc in range(2, 8): w2a.cell(row=r, column=cc).number_format = "0.000"
w2a["F6"] = 1.610; w2a["F6"].font = BLUE
w2a["A10"] = "Plot: filled circles/squares = measured NP/HP (solid lines); open symbols + dashed lines = model; black diamond = KOPTRI; dotted line at eps = 1 (air)."; w2a["A10"].font = GREY
setw(w2a, [11, 12, 12, 20, 20, 18, 14])

# ------------------------------------------------------------------ Fig2b
w2b = wb.create_sheet("Fig2b_Thermal")
w2b["A1"] = "Figure 2b: thermal conductivity vs h-BN content (W m-1 K-1)"; w2b["A1"].font = TITLE
header(w2b, 3, ["h-BN (wt%)", "lam_NP_exp", "lam_HP_exp", "lam_LN_NP (model at NP open porosity)", "lam_LN_HP (model at HP open porosity)", "NP measured?", "HP measured?"])
for k, wt in enumerate([0, 10, 30, 50, 70]):
    r = 4 + k; np_row = 4 + k; hp_row = 9 + k
    w2b.cell(row=r, column=1, value=wt).font = BLUE
    w2b.cell(row=r, column=2, value=f'=IF(Samples!H{np_row}="","",Samples!H{np_row})').font = BLUE
    w2b.cell(row=r, column=3, value=f'=IF(Samples!H{hp_row}="","",Samples!H{hp_row})').font = BLUE
    w2b.cell(row=r, column=4, value=f"=Samples!V{np_row}").font = BLACK
    w2b.cell(row=r, column=5, value=f"=Samples!V{hp_row}").font = BLACK
    w2b.cell(row=r, column=6, value=f'=IF(B{r}="","no (fragile)","yes")').font = BLACK
    w2b.cell(row=r, column=7, value=f'=IF(C{r}="","no (fragile)","yes")').font = BLACK
    for cc in range(2, 6): w2b.cell(row=r, column=cc).number_format = "0.000"
w2b["A10"] = "Plot: filled symbols = measured; open symbols = model at each film's own porosity, joined by a vertical tie-line; crosses at compositions marked 'no'."; w2b["A10"].font = GREY
setw(w2b, [11, 12, 12, 20, 20, 13, 13])

# ------------------------------------------------------------------ Fig2c
w2c = wb.create_sheet("Fig2c_IR")
w2c["A1"] = "Figure 2c: infrared thermography spot temperatures (200 C stage; uncorrected radiometric values)"; w2c["A1"].font = TITLE
header(w2c, 3, ["h-BN (wt%)", "T_spot NP (C)", "T_spot HP (C)", "Label NP", "Label HP"])
ir = [(0, 79.9, 76.4), (10, 144.3, 154.9), (30, 169.0, 196.1), (50, 179.8, 182.7), (70, 183.8, 192.2)]
for k, (wt, tn, th) in enumerate(ir):
    r = 4 + k
    for j, v in enumerate([wt, tn, th], 1): w2c.cell(row=r, column=j, value=v).font = BLUE
    w2c.cell(row=r, column=4, value=f'=TEXT(ROUND(B{r},0),"0")&" C"').font = BLACK
    w2c.cell(row=r, column=5, value=f'=TEXT(ROUND(C{r},0),"0")&" C"').font = BLACK
w2c["A10"] = "Values read from the Sp1 annotation of each FLIR frame (Fig. 2c). Comparative only: emissivity not corrected. Equilibration time before imaging: [5] min (to be confirmed)."; w2c["A10"].font = GREY
setw(w2c, [11, 14, 14, 10, 10])

# ------------------------------------------------------------------ Fig3a
w3a = wb.create_sheet("Fig3a_Tensile")
w3a["A1"] = "Figure 3a: tensile strength (MPa), n = 1 per bar"; w3a["A1"].font = TITLE
header(w3a, 3, ["h-BN (wt%)", "NP (MPa)", "HP (MPa)", "NP->HP change (%)", "Label"])
for k, wt in enumerate([0, 10, 30, 50, 70]):
    r = 4 + k; np_row = 4 + k; hp_row = 9 + k
    w3a.cell(row=r, column=1, value=wt).font = BLUE
    w3a.cell(row=r, column=2, value=f'=IF(Samples!J{np_row}="","",Samples!J{np_row})').font = BLUE
    w3a.cell(row=r, column=3, value=f'=IF(Samples!J{hp_row}="","",Samples!J{hp_row})').font = BLUE
    w3a.cell(row=r, column=4, value=f'=IF(OR(B{r}="",C{r}=""),"",100*(C{r}-B{r})/B{r})').font = BLACK
    w3a.cell(row=r, column=5, value=f'=IF(D{r}="","not tested (too brittle)","+"&TEXT(D{r},"0")&"%")').font = BLACK
    w3a.cell(row=r, column=4).number_format = "0.0"
w3a["A10"] = "70 wt%: draw a small baseline stub (not zero) and label 'not tested (too brittle)'."; w3a["A10"].font = GREY
setw(w3a, [11, 11, 11, 16, 22])

# ------------------------------------------------------------------ Fig3b
w3b = wb.create_sheet("Fig3b_CTE")
w3b["A1"] = "Figure 3b: CTE of HP films (ppm K-1) with Turner and rule-of-mixtures bounds"; w3b["A1"].font = TITLE
header(w3b, 3, ["h-BN (wt%)", "CTE_exp HP", "Turner (lower bound)", "ROM (upper bound)", "PCB window low", "PCB window high"])
for k, wt in enumerate([0, 10, 30, 50, 70]):
    r = 4 + k; hp_row = 9 + k
    w3b.cell(row=r, column=1, value=wt).font = BLUE
    w3b.cell(row=r, column=2, value=f"=Samples!K{hp_row}").font = BLUE
    w3b.cell(row=r, column=3, value=f"=Samples!L{hp_row}").font = BLUE
    w3b.cell(row=r, column=4, value=f"=Samples!M{hp_row}").font = BLUE
    w3b.cell(row=r, column=5, value=3).font = BLUE
    w3b.cell(row=r, column=6, value=17).font = BLUE
w3b["A10"] = "Turner and ROM computed with alpha_PI = 41.92 ppm/K (measured, neat HP), E_PI = 3.5 GPa, E_BN = 200 GPa, alpha_BN = 1.5 ppm/K (Table 4). Shade 3-17 ppm/K as the PCB target zone; annotate 10.1 ppm/K at 70 wt%."; w3b["A10"].font = GREY
setw(w3b, [11, 12, 18, 16, 14, 14])

# ------------------------------------------------------------------ Fig4a / Fig4b design maps
def design_map(name, title, kind):
    w = wb.create_sheet(name)
    w["A1"] = title; w["A1"].font = TITLE
    w["A2"] = "helper rows: 3 = h-BN wt%, 4 = phi_BN, 5 = dense-composite property, 6 = B_pore. Grid from row 8: rows = porosity (%), columns = wt%."; w["A2"].font = GREY
    wts = list(range(0, 71, 2)); pors = list(range(0, 96, 1))
    w.cell(row=3, column=1, value="wt% ->").font = BOLD
    w.cell(row=4, column=1, value="phi_BN").font = BOLD
    w.cell(row=5, column=1, value="dense property").font = BOLD
    w.cell(row=6, column=1, value="B_pore").font = BOLD
    w.cell(row=8, column=1, value="porosity (%) \\ wt%").font = BOLD; w.cell(row=8, column=1).fill = HEAD
    for j, wt in enumerate(wts):
        col = 2 + j; cl = L(col)
        c = w.cell(row=3, column=col, value=wt); c.font = BLUE; c.fill = HEAD
        w.cell(row=4, column=col, value="=" + phiBN(f"{cl}$3")).font = BLACK
        w.cell(row=5, column=col, value="=" + (eps_dense(f"{cl}$4") if kind == "eps" else lam_dense(f"{cl}$4"))).font = BLACK
        kair = "eps_air" if kind == "eps" else "lam_air"
        w.cell(row=6, column=col, value=f"=({kair}/{cl}$5-1)/({kair}/{cl}$5+A_pore)").font = BLACK
        w.cell(row=8, column=col, value=f"={cl}$3").font = BOLD
        w.cell(row=8, column=col).fill = HEAD
        for i, p in enumerate(pors):
            r = 9 + i
            if j == 0:
                w.cell(row=r, column=1, value=p).font = BLUE
            f = f"={cl}$5*(1+A_pore*{cl}$6*($A{r}/100))/(1-{cl}$6*(1+((1-phimax_pore)/phimax_pore^2)*($A{r}/100))*($A{r}/100))"
            c = w.cell(row=r, column=col, value=f); c.font = BLACK; c.number_format = "0.000"
        for rr in (4, 5, 6): w.cell(row=rr, column=col).number_format = "0.0000"
    # overlay of measured states
    oc = 2 + len(wts) + 2
    w.cell(row=8, column=oc, value="Measured overlay (for symbols and NP->HP arrows)").font = BOLD
    header(w, 9, ["h-BN (wt%)", "phi_open NP (%)", "phi_open HP (%)", "arrow dx", "arrow dy"], col0=oc)
    for k, wt in enumerate([0, 10, 30, 50, 70]):
        r = 10 + k
        w.cell(row=r, column=oc, value=wt).font = BLUE
        w.cell(row=r, column=oc + 1, value=f"=Samples!C{4 + k}").font = BLUE
        w.cell(row=r, column=oc + 2, value=f"=Samples!C{9 + k}").font = BLUE
        w.cell(row=r, column=oc + 3, value=0).font = BLACK
        w.cell(row=r, column=oc + 4, value=f"={L(oc+2)}{r}-{L(oc+1)}{r}").font = BLACK
    w.cell(row=16, column=oc, value="Faded bands in the figure: porosity > 91 % and < 30 % (outside the measured range).").font = GREY
    w.cell(row=17, column=oc, value="Suggested contour levels: eps 1.5, 1.8, 2.0; lambda 0.05, 0.12, 0.20 W m-1 K-1.").font = GREY
    w.freeze_panes = "B9"
    w.column_dimensions["A"].width = 16
    for j in range(len(wts)): w.column_dimensions[L(2 + j)].width = 8
    return w
design_map("Fig4a_EpsMap", "Figure 4a: eps design map (three-phase LN model)", "eps")
design_map("Fig4b_LamMap", "Figure 4b: lambda design map, W m-1 K-1 (three-phase LN model)", "lam")

# ------------------------------------------------------------------ Fig4c loci
w4c = wb.create_sheet("Fig4c_Loci")
w4c["A1"] = "Figure 4c: eps-lambda loci, porosity swept along each curve (x = eps, y = lambda)"; w4c["A1"].font = TITLE
loci_wts = [0, 10, 30, 50, 70]
w4c["A3"] = "wt% ->"; w4c["A4"] = "phi_BN"; w4c["A5"] = "eps_dense"; w4c["A6"] = "B_pore_eps"; w4c["A7"] = "lam_dense"; w4c["A8"] = "B_pore_lam"
for a in ("A3", "A4", "A5", "A6", "A7", "A8"): w4c[a].font = BOLD
header(w4c, 10, ["porosity (%)"])
for k, wt in enumerate(loci_wts):
    ce = 2 + 2 * k; cl_ = L(ce); cl2 = L(ce + 1)   # eps column, lam column
    c = w4c.cell(row=3, column=ce, value=wt); c.font = BLUE; c.fill = HEAD
    w4c.cell(row=4, column=ce, value="=" + phiBN(f"{cl_}$3")).font = BLACK
    w4c.cell(row=5, column=ce, value="=" + eps_dense(f"{cl_}$4")).font = BLACK
    w4c.cell(row=6, column=ce, value=f"=(eps_air/{cl_}$5-1)/(eps_air/{cl_}$5+A_pore)").font = BLACK
    w4c.cell(row=7, column=ce, value="=" + lam_dense(f"{cl_}$4")).font = BLACK
    w4c.cell(row=8, column=ce, value=f"=(lam_air/{cl_}$7-1)/(lam_air/{cl_}$7+A_pore)").font = BLACK
    header(w4c, 10, [f"eps_{wt}wt", f"lam_{wt}wt"], col0=ce)
    for rr in range(4, 9): w4c.cell(row=rr, column=ce).number_format = "0.0000"
pors = [20 + 0.5 * i for i in range(151)]
for i, p in enumerate(pors):
    r = 11 + i
    w4c.cell(row=r, column=1, value=p).font = BLUE
    for k, wt in enumerate(loci_wts):
        ce = 2 + 2 * k; cl_ = L(ce)
        fe = f"={cl_}$5*(1+A_pore*{cl_}$6*($A{r}/100))/(1-{cl_}$6*(1+((1-phimax_pore)/phimax_pore^2)*($A{r}/100))*($A{r}/100))"
        fl = f"={cl_}$7*(1+A_pore*{cl_}$8*($A{r}/100))/(1-{cl_}$8*(1+((1-phimax_pore)/phimax_pore^2)*($A{r}/100))*($A{r}/100))"
        a = w4c.cell(row=r, column=ce, value=fe); a.font = BLACK; a.number_format = "0.0000"
        b = w4c.cell(row=r, column=ce + 1, value=fl); b.font = BLACK; b.number_format = "0.0000"
# measured 70 wt% overlay + target zone
w4c["N10"] = "Measured 70 wt% films (overlay)"; w4c["N10"].font = BOLD
header(w4c, 11, ["State", "eps_exp", "lam_exp", "phi_open (%)"], col0=14)
w4c["N12"] = "NP"; w4c["O12"] = "=Samples!I8"; w4c["P12"] = "=Samples!H8"; w4c["Q12"] = "=Samples!C8"
w4c["N13"] = "HP"; w4c["O13"] = "=Samples!I13"; w4c["P13"] = "=Samples!H13"; w4c["Q13"] = "=Samples!C13"
for a in ("N12", "O12", "P12", "Q12", "N13", "O13", "P13", "Q13"): w4c[a].font = BLUE
w4c["N15"] = "Target zone shading: eps <= 1.8 (vertical band). Plot each wt% as a line with eps on x and lambda on y; highlight 70 wt%."; w4c["N15"].font = GREY
w4c["N16"] = "The 50 wt% columns (H:I) are also the porosity-sensitivity curves of Figure S3."; w4c["N16"].font = GREY
w4c.freeze_panes = "B11"
setw(w4c, [12] + [10] * 10 + [4, 4, 8, 10, 10, 12])

# ------------------------------------------------------------------ Fig4d max lambda under eps ceiling
w4d = wb.create_sheet("Fig4d_MaxLambda")
w4d["A1"] = "Figure 4d: maximum lambda under an eps ceiling (porosity optimised), from the loci of Fig4c (porosity step 0.5 %)"; w4d["A1"].font = TITLE
labels = ["eps ceiling"]
for wt in loci_wts: labels += [f"max lam_{wt}wt", f"porosity*_{wt}wt (%)"]
header(w4d, 3, labels)
ceils = [round(1.10 + 0.02 * i, 2) for i in range(66)]   # 1.10 .. 2.40
n_last = 11 + len(pors) - 1
for i, cv in enumerate(ceils):
    r = 4 + i
    w4d.cell(row=r, column=1, value=cv).font = BLUE
    for k, wt in enumerate(loci_wts):
        ce = 2 + 2 * k; cl_ = L(ce); cl2 = L(ce + 1)
        eps_rng = f"Fig4c_Loci!${cl_}$11:${cl_}${n_last}"; lam_rng = f"Fig4c_Loci!${cl2}$11:${cl2}${n_last}"; por_rng = f"Fig4c_Loci!$A$11:$A${n_last}"
        # eps decreases with porosity (descending array): MATCH(...,-1) gives the smallest eps >= ceiling; the next row is the max lambda with eps <= ceiling
        pos = f"IFERROR(MATCH($A{r},{eps_rng},-1)+1,1)"
        w4d.cell(row=r, column=2 + 2 * k, value=f"=IFERROR(INDEX({lam_rng},{pos}),NA())").font = BLACK
        w4d.cell(row=r, column=3 + 2 * k, value=f"=IFERROR(INDEX({por_rng},{pos}),NA())").font = BLACK
        w4d.cell(row=r, column=2 + 2 * k).number_format = "0.0000"
        w4d.cell(row=r, column=3 + 2 * k).number_format = "0.0"
r0 = 4 + len(ceils) + 1
w4d.cell(row=r0, column=1, value="Stars (70 wt%)").font = BOLD
header(w4d, r0 + 1, ["eps ceiling", "max lam_70wt", "porosity* (%)"])
for k, cv in enumerate([1.6, 1.8]):
    r = r0 + 2 + k
    w4d.cell(row=r, column=1, value=cv).font = BLUE
    w4d.cell(row=r, column=2, value=f"=INDEX($J$4:$J${3+len(ceils)},MATCH(A{r},$A$4:$A${3+len(ceils)},0))").font = BLACK
    w4d.cell(row=r, column=3, value=f"=INDEX($K$4:$K${3+len(ceils)},MATCH(A{r},$A$4:$A${3+len(ceils)},0))").font = BLACK
    w4d.cell(row=r, column=2).number_format = "0.000"; w4d.cell(row=r, column=3).number_format = "0.0"
w4d.cell(row=r0 + 5, column=1, value="A cell showing N/A means the ceiling lies below the lowest eps reachable at 95 % porosity for that loading (outside the plotted range). Plot x = eps ceiling, y = max lambda, one line per loading.").font = GREY
w4d.freeze_panes = "B4"
setw(w4d, [12] + [13, 15] * 5)

import os; os.makedirs(os.path.dirname(OUT), exist_ok=True)
wb.save(OUT); print("saved", OUT)
