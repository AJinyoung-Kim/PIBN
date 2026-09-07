"""Three-phase Lewis-Nielsen (LN) model for porous PI/h-BN films.

Reproduces the calibration, benchmarks and sensitivity analyses of the
Supplementary Material (Sections S3-S4).  Requires numpy and scipy.
"""
import numpy as np
from scipy.optimize import minimize

# ------------------------------------------------------------------ data
w = np.array([0, 10, 30, 50, 70]) / 100.0            # h-BN weight fraction of solids
RHO_PI, RHO_BN = 1.42, 2.29                           # g cm^-3
phi_BN = (w / RHO_BN) / (w / RHO_BN + (1 - w) / RHO_PI)   # solid-phase volume fraction
rho_solid = 1 / (w / RHO_BN + (1 - w) / RHO_PI)
eps_meas = {"NP": np.array([1.757, 1.740, 1.659, 1.407, 1.278]),
            "HP": np.array([2.178, 1.924, 1.864, 1.829, 1.622])}
lam_meas = {"NP": np.array([np.nan, np.nan, 0.063, 0.091, 0.305]),
            "HP": np.array([np.nan, 0.114, 0.051, 0.088, 0.279])}
phi_open = {"NP": np.array([75.4, 91.4, 48.8, 58.1, 54.2]) / 100,
            "HP": np.array([43.4, 29.8, 67.2, 64.6, 48.8]) / 100}
rho_bulk = {"NP": np.array([np.nan, np.nan, 0.323, 0.515, 0.526]),
            "HP": np.array([np.nan, 0.879, 0.455, 0.678, 0.539])}
phi_total = {s: 1 - rho_bulk[s] / rho_solid for s in rho_bulk}
EPS_PI, EPS_BN, EPS_AIR = 3.5, 6.0, 1.0
LAM_PI, LAM_AIR = 0.12, 0.026                         # W m^-1 K^-1

# ------------------------------------------------------------------ model
def ln(k_m, k_f, phi, A, phi_max):
    """Two-phase Lewis-Nielsen expression (Eqs. S1-S3)."""
    B = (k_f / k_m - 1) / (k_f / k_m + A)
    psi = 1 + (1 - phi_max) / phi_max**2 * phi
    return k_m * (1 + A * B * phi) / (1 - B * psi * phi)

def ln3(k_m, k_f, k_pore, phi_f, phi_p, A_f, pmax_f, A_p, pmax_p):
    """Sequential three-phase model: step 1 (filler), step 2 (pores)."""
    k_dense = ln(k_m, k_f, phi_f, A_f, pmax_f)
    return ln(k_dense, k_pore, phi_p, A_p, pmax_p)

def eps_model(p, phi_in=phi_open):
    A_BN, pmax_BN, A_p, pmax_p = p
    return {s: ln3(EPS_PI, EPS_BN, EPS_AIR, phi_BN, phi_in[s],
                   A_BN, pmax_BN, A_p, pmax_p) for s in ("NP", "HP")}

def lam_model(lam_BN, A=5.5, pmax=0.60, A_p=0.08, pmax_p=0.99):
    return {s: ln3(LAM_PI, lam_BN, LAM_AIR, phi_BN, phi_open[s],
                   A, pmax, A_p, pmax_p) for s in ("NP", "HP")}

def rmse(meas, pred):
    m = ~np.isnan(meas) & ~np.isnan(pred)
    return np.sqrt(np.mean((meas[m] - pred[m])**2))

def r2(meas, pred):
    m = ~np.isnan(meas) & ~np.isnan(pred)
    return 1 - np.sum((meas[m] - pred[m])**2) / np.sum((meas[m] - meas[m].mean())**2)

# ------------------------------------------------------------------ objective (Eq. S8)
BOUNDS = [(0.05, 20), (0.30, 0.99), (0.01, 20), (0.30, 0.99)]

def objective(p, phi_in=phi_open):
    if any(not (lo <= v <= hi) for v, (lo, hi) in zip(p, BOUNDS)):
        return 1e6
    pred = eps_model(p, phi_in)
    res = np.concatenate([(pred[s] - eps_meas[s])[~np.isnan(phi_in[s])] for s in ("NP", "HP")])
    return np.mean(res**2)

def multistart(fun, sampler, n=16, seed=0):
    rng = np.random.default_rng(seed)
    best = None
    for _ in range(n):
        r = minimize(fun, sampler(rng), method="Nelder-Mead",
                     options={"xatol": 1e-6, "fatol": 1e-9, "maxiter": 4000})
        if best is None or r.fun < best.fun:
            best = r
    return best

if __name__ == "__main__":
    # dielectric calibration with open porosity (Section S4.1)
    samp = lambda g: [g.uniform(0.3, 6), g.uniform(0.5, 0.99), g.uniform(0.02, 2), g.uniform(0.5, 0.99)]
    fit = multistart(objective, samp)
    print("dielectric fit (open porosity):", fit.x.round(3), "RMSE", np.sqrt(fit.fun).round(3))
    # published parameter set
    pub = (0.68, 0.99, 0.08, 0.99)
    pred = eps_model(pub)
    for s in ("NP", "HP"):
        print(s, pred[s].round(3), "RMSE", rmse(eps_meas[s], pred[s]).round(3), "R2", r2(eps_meas[s], pred[s]).round(2))
    # re-fit with total porosity (Section S3.3)
    fit_t = multistart(lambda p: objective(p, phi_total), samp)
    print("dielectric fit (total porosity):", fit_t.x.round(3), "RMSE", np.sqrt(fit_t.fun).round(3))
    # thermal single-parameter fit (Section S4.2)
    def obj_l(x, A=5.5, pmax=0.60):
        if x[0] <= 0 or not (0.05 < pmax < 0.99):
            return 1e6
        pr = lam_model(x[0], A, pmax)
        res = np.concatenate([(pr[s] - lam_meas[s])[~np.isnan(lam_meas[s])] for s in ("NP", "HP")])
        return np.mean(res**2)
    r = minimize(obj_l, [5.0], method="Nelder-Mead")
    pl = lam_model(r.x[0])
    print("lam_BN,eff =", r.x[0].round(3), {s: rmse(lam_meas[s], pl[s]).round(4) for s in ("NP", "HP")})
    # unconstrained three-parameter thermal fit
    fit_3 = multistart(lambda x: obj_l([x[0]], A=x[1], pmax=x[2]) if 0.05 < x[1] < 2000 else 1e6,
                       lambda g: [g.uniform(1, 50), g.uniform(0.5, 50), g.uniform(0.2, 0.95)], n=20)
    print("unconstrained thermal fit:", fit_3.x.round(3), "RMSE", np.sqrt(fit_3.fun).round(4))
