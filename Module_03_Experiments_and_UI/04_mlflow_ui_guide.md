# Module 3.4: MLFlow UI Guide

## 🎯 How to Use the MLFlow UI Like a Pro

The MLFlow UI at **http://localhost:5000** is your visual dashboard for exploring experiments.

### Starting the UI

```bash
cd c:\Users\sujat\projects\MLFlow_Learn
mlflow ui
```

---

## 1. The Main Page — Experiments List

When you open the UI, you'll see:

- **Left sidebar**: List of all experiments
- **Main area**: Runs table for the selected experiment
- **Top bar**: Search/filter controls

### Quick Tips:
- Click an experiment name to see its runs
- The "Default" experiment (ID=0) catches runs not assigned to any experiment
- Deleted experiments can be viewed by toggling the filter

---

## 2. The Runs Table

| Column | Description |
|--------|-------------|
| **Run Name** | The name you set with `run_name=` |
| **Created** | When the run was started |
| **Duration** | How long the run took |
| **Status** | FINISHED, RUNNING, or FAILED |
| **Parameters** | Columns for each parameter |
| **Metrics** | Columns for each metric |

### Customizing Columns:
1. Click the **Columns** button (top right of table)
2. Check/uncheck parameters and metrics to show/hide
3. This makes it easy to compare specific values

### Sorting:
- Click any column header to sort ascending/descending
- Great for quickly finding the best run by a metric

---

## 3. Comparing Runs

This is one of the most powerful UI features:

1. **Select 2+ runs** using the checkboxes
2. Click the **Compare** button
3. You'll see:
   - **Parameters comparison table** — spot differences
   - **Metrics comparison table** — compare performance
   - **Scatter plots** — metric vs metric
   - **Parallel coordinates plot** — see parameter-metric relationships

### Parallel Coordinates Plot
This chart shows how different parameter combinations affect metrics:
- Each vertical axis is a parameter or metric
- Each line is a run
- Look for patterns: "higher n_estimators → higher accuracy"

---

## 4. Run Details Page

Click on any run name to see its full details:

### Overview Tab
- Run ID, status, start/end time, duration
- All parameters in a table
- All metrics in a table
- All tags

### Metrics Tab
- Click any metric to see its chart
- For step-based metrics (logged with `step=`), you'll see training curves
- Zoom, pan, and download charts

### Artifacts Tab
- Browse all logged artifacts (files, models, plots)
- **Preview** images directly in the browser
- **Download** any artifact
- View the **MLmodel** file for logged models

---

## 5. Chart View

The table view has a **Chart** toggle:

1. Click **Chart** (next to Table) in the runs view
2. Choose chart type: bar, scatter, contour
3. Select X/Y axes from your parameters and metrics
4. Visualize relationships like:
   - `n_estimators` vs `accuracy` (scatter)
   - `model_type` vs `accuracy` (bar)

---

## 6. Search Bar

The search bar at the top supports the same filter syntax as the API:

```
metrics.accuracy > 0.95
params.model_type = 'RandomForest'
tags.purpose = 'baseline'
metrics.accuracy > 0.9 AND params.model_type = 'RandomForest'
```

---

## 7. Pro Tips 🏆

1. **Name your runs** — `run_name="descriptive_name"` makes the UI 10x more useful
2. **Use tags liberally** — they show up as filterable columns
3. **Always log plots** — viewable directly in the artifact browser
4. **Compare early, compare often** — don't wait until the end to compare runs
5. **Bookmark the UI** — keep it open in a tab while working in notebooks
6. **Nested runs** — expand parent runs to see child runs grouped together

---

## ➡️ Next: `05_exercises.ipynb` — Practice Module 3 concepts
