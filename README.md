# PPH7092S Assignment 2 – Survival Analysis

This repository contains the analysis and code for Assignment 2 of **PPH7092S** at the University of Cape Town. The assignment uses **survival analysis** to look at how clinical characteristics and treatment relate to survival time in a cohort of patients with stage 3 or stage 4 cancer.

The analysis covers:

- Kaplan–Meier survival curves and a log-rank test
- Univariable Cox proportional hazards regression
- Multivariable Cox proportional hazards regression
- Checks of the proportional hazards assumption (Schoenfeld residuals)

All analyses were done in **Python using lifelines, pandas, numpy and statsmodels**.

---

# Repository Structure

```
.
├── analysis.ipynb                 # Main analysis notebook
├── analysis copy.ipynb            # Working copy (includes the full PH assumption check)
├── config.py                      # Paths and random seed
├── get_data.py                    # DataLoader: loads the data and draws the assignment sample
├── cox_ph_coefficient_plot.png    # Hazard ratio plot (multivariable model)
│
├── data/
│   ├── PPH7092S_Assign2.csv       # Dataset used in this assignment
│   └── PPH7092S_Assign1.csv       # Assignment 1 dataset (not used here)
│
└── output/
    ├── cox_univariable_results.csv
    └── cox_multivariable_results.csv
```

---

# Dataset

`data/PPH7092S_Assign2.csv` has 501 patients with these variables:

| Variable | Description |
|---|---|
| `id` | Patient identifier |
| `time` | Follow-up time (months) |
| `status` | 1 = death (event), 0 = censored |
| `hg` | Serum haemoglobin (g/100 mL) |
| `pap` | Prostatic acid phosphatase (ng/mL) |
| `cvd` | History of cardiovascular disease (yes / no) |
| `stage` | Cancer stage (stage3 / stage4) |
| `treat` | Treatment group (high-dose / low-dose / placebo) |

As the assignment requires, the analysis uses a **75% random sample** (`random_state` set in `config.py`), which gives 376 patients and 263 deaths.

---

# Statistical Methods

## Kaplan–Meier Curves
Survival curves were estimated by cancer stage and compared with a **log-rank test**.

## Cox Proportional Hazards Regression
- **Models 1–5:** a univariable Cox model for each covariate (`hg`, `pap`, `cvd`, `stage`, `treat`).
- **Model 6:** a multivariable Cox model with all five covariates.

Categorical variables were entered with `C()` in the formula. Models used robust (sandwich) standard errors. Hazard ratios and 95% confidence intervals are saved to `output/`.

## Proportional Hazards Assumption
Checked with **Schoenfeld residuals** plotted against time with LOWESS smoothing, and with lifelines' `check_assumptions` test.

---

# Key Results

- **Kaplan–Meier:** survival was worse for stage 4 than stage 3. Median survival was 28 months for stage 4 and 43 months for stage 3 (log-rank χ² = 7.24, p = 0.007).
- **Multivariable Cox model (Model 6):**

| Covariate | HR | 95% CI | p |
|---|---|---|---|
| Haemoglobin (per g/100 mL) | 0.88 | 0.82–0.94 | < 0.001 |
| Prostatic acid phosphatase | 1.00 | 1.00–1.00 | 0.88 |
| CVD history (yes vs no) | 1.50 | 1.17–1.94 | 0.002 |
| Stage 4 vs stage 3 | 1.32 | 1.01–1.72 | 0.039 |
| Low-dose vs high-dose | 1.21 | 0.90–1.62 | 0.22 |
| Placebo vs high-dose | 1.10 | 0.81–1.50 | 0.54 |

- Higher haemoglobin was linked to lower hazard of death. A history of cardiovascular disease and stage 4 disease were linked to higher hazard.
- The **low-dose treatment term failed the proportional hazards test** (p = 0.005), so its hazard ratio should be read with caution. Stratifying on treatment is one option.

---

# Requirements

Python packages used:

1. pandas
1. numpy
1. lifelines
1. statsmodels
1. matplotlib
1. seaborn
1. jupyter

Install them with:

```bash
pip install pandas numpy lifelines statsmodels matplotlib seaborn jupyter
```

---

# Running the Analysis

Open `analysis.ipynb` in Jupyter and run all cells. The results tables are written to `output/` and the hazard ratio plot to `cox_ph_coefficient_plot.png`.
