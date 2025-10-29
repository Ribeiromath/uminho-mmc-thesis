# GaitRec - Gait Recognition Using Machine Learning

Research project focused on applying machine learning techniques to classify gait patterns from biomechanical ground reaction force (GRF) data.

## Overview

This project evaluates the performance of multiple ML algorithms (RandomForest, SVM, MLP, CatBoost) in identifying different types of orthopedic fractures through gait analysis. The study investigates how model performance varies with different dataset sizes (10%-100%), providing insights into the data efficiency of each approach.

## Context and Motivation

Gait analysis through force platforms is a valuable tool for medical diagnosis. This project uses the **GaitRec** dataset, a large-scale database containing biomechanical signals from patients with different orthopedic conditions and healthy controls.

**Main objectives:**
- Evaluate the ability of different ML models to distinguish pathological gait patterns
- Analyze learning curves to understand data volume requirements
- Identify which disease classes are most distinguishable through gait analysis
- Compare model robustness with limited datasets

## Dataset

### GaitRec Dataset
- **Total subjects:** 2,295
- **Source:** Figshare (11 articles with biomechanical signals)
- **Composition:**
  - Calcaneus Fracture (C_F): 380 subjects
  - Knee Fracture (K_F): 285 subjects
  - Ankle Fracture (A_F): 338 subjects
  - Healthy Controls (HC): 211 subjects

### Biomechanical Signals (5 features)
1. **F_V** - Vertical force
2. **F_AP** - Anterior-posterior force
3. **F_ML** - Medial-lateral force
4. **COP_AP** - Center of pressure (anterior-posterior)
5. **COP_ML** - Center of pressure (medial-lateral)

## Methodology

### Evaluated Models
1. **Random Forest** - 100 estimators, balanced classes
2. **SVM** - Linear kernel with standardization
3. **MLP** - Neural network (50 hidden units)
4. **CatBoost** - Gradient boosting (100 iterations, depth=6)

### Evaluation Protocol
- **Stratified K-Fold cross-validation** (5 folds)
- **10 dataset fractions tested:** 10%, 20%, 30%...90%, 100%
- **4 performance metrics:** Accuracy, AUC, Specificity, Sensitivity
- **Binary classification:** Each fracture type vs. healthy controls

### Processing Pipeline
1. Load signal CSVs from database
2. Transform to long format
3. Merge all 5 signals per subject
4. Filter by affected side (left foot for patients)
5. Combine with healthy controls
6. Create feature matrices with padding

## Project Structure

```
uminho-mmc-gaitrec/
├── init.py                          # Dataset download script
├── README.md                        # This file
├── .gitignore                       # Git exclusions
├── database/                        # Downloaded GaitRec dataset
└── src/
    ├── assets/
    │   ├── pdf/                     # Reference papers
    │   └── views/
    │       └── binary/              # Visualizations and results
    └── analysis/
        ├── binary/
        │   ├── index.ipynb          # Main analysis notebook
        │   ├── selected_data/       # Processed data
        │   └── catboost_info/       # CatBoost logs
        └── insights/
            ├── subjects_by_age.ipynb    # Age distribution analysis
            └── subjects_by_sex.ipynb    # Sex distribution analysis
```

## How to Use

### 1. Download the Dataset

Run the initialization script to download data from Figshare:

```bash
python init.py
```

This will create the `database/` directory with 11 articles containing GRF signals.

### 2. Exploratory Analysis

Explore the demographic characteristics of the dataset:

```bash
jupyter notebook src/analysis/insights/subjects_by_age.ipynb
jupyter notebook src/analysis/insights/subjects_by_sex.ipynb
```

### 3. Main Analysis

Run the main notebook to train models and generate results:

```bash
jupyter notebook src/analysis/binary/index.ipynb
```

## Main Results

### Best Performance by Class (100% Dataset)

| Fracture Type | Best Model | AUC | Accuracy |
|--------------|------------|-----|----------|
| Calcaneus | Random Forest | 0.968 ± 0.018 | 91.5% |
| Knee | CatBoost | 0.927 ± 0.037 | - |
| Ankle | MLP | 0.933 ± 0.026 | - |

### Generated Visualizations

All results are saved to `src/assets/views/binary/`:

1. **Comparative ROC Curves** - AUC for all classes
2. **Metrics Bar Charts** - Side-by-side comparison
3. **Performance Heatmaps** - Matrix view (models vs diseases)
4. **Confusion Matrices** - Classification details per model
5. **Learning Curves (Detailed)** - 4 images (one per metric)
6. **Learning Curves (Condensed)** - 2x2 grid showing dataset size effects
7. **Comprehensive Results Table** - CSV with all analysis

## Technologies Used

### Machine Learning
- **scikit-learn** - Classical models, preprocessing, validation
- **CatBoost** - Gradient boosting
- **pandas** - Data manipulation
- **numpy** - Numerical computing

### Visualization
- **matplotlib** - Plotting
- **seaborn** - Statistical visualization

### Utilities
- **requests** - Dataset download via Figshare API
- **glob** - File pattern matching

## Demographic Insights

- **Age range:** 9-80 years (median: 43 years)
- **Sex distribution:** Analysis available in `subjects_by_sex.ipynb`

## References

Reference papers available in `src/assets/pdf/`:
- GaitRec dataset technical documentation
- Related studies in biomechanical analysis

## Contributions

This is an academic research project from the University of Minho for the MMC (Mathematics and Computation Master) course.

## License

Academic project - University of Minho

---

**Developed in:** 2025
**Institution:** University of Minho
**Course:** MMC - Master Degree in Mathematics and Computation
