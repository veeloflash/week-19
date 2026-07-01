# Week 19: AI Learning Analytics Dashboard

## Project Overview
This is the Week 19 learning project. It includes a text classification pipeline based on KNN and TF-IDF, model evaluation, and generation of dashboard-ready data for visualization.

## Directory Structure

- `data/`
  - `questions.json`: question text and categories
  - `labels.json`: ground truth labels
  - `predictions.json`: model predictions
  - `confusion_matrix.json`: confusion matrix counts
- `model/`
  - `features.py`: TF-IDF feature extraction
  - `knn_model.py`: KNN classifier wrapper
  - `predictor.py`: unified prediction interface
- `evaluation/`
  - `confusion.py`: manual TP/TN/FP/FN computation
  - `metrics.py`: Accuracy / Precision / Recall / F1 calculations
  - `imbalance_experiment.py`: class imbalance experiment script
- `analytics/`
  - `statistics.py`: question statistics and error analysis
  - `generate_dashboard_data.py`: create dashboard JSON data
- `security/`
  - `input_guard.py`: input boundary checks
- `dashboard/`
  - `index.html`: dashboard page
  - `style.css`: page styles
  - `app.js`: dynamic show/hide and reload functionality
- `main.py`: entry point to run the model, evaluate, and generate dashboard data

## Usage

1. Install dependencies:

```powershell
pip install -r requirements.txt
```

2. Run the main program:

```powershell
python main.py
```

3. Open the dashboard:

- Open `dashboard/index.html` in a browser
- Click `Load Data` to load results
- Click `Hide Results` / `Show Results` to toggle visibility

## Dependencies

- Python 3.8+
- scikit-learn

## Notes

- `main.py` reads `data/questions.json` and `data/labels.json`, trains the model, and generates predictions.
- `dashboard/dashboard_data.json` is written by `main.py`, and the front-end loads it with `app.js`.
- The `evaluation/` folder contains confusion matrix and metric calculation utilities for analysis.

## Suggestions for Improvement

- Add more question data to improve model robustness
- Extend `analytics/generate_dashboard_data.py` with additional metrics
- Serve the dashboard from a static server to support `fetch` requests
