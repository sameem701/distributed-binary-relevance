# Milestone 3 Run Instructions

This guide explains how to run `milestone3_updated.ipynb` on another PC.

## 1. Prerequisites: Milestones 1 and 2 Must Be Run First

Milestone 3 depends entirely on output files from both Milestone 1 and Milestone 2.
Before running `milestone3.ipynb`, you must have already run both previous notebooks
successfully and have the following files in your project folder:

From Milestone 1:

- `X_test_normalized.npz`
- `test_meta.csv`

From Milestone 2:

- `models_node_level/model_registry.csv`
- `models_node_level/node_training_summary.csv`
- `models_node_level/node_0/` to `models_node_level/node_3/` (one folder per worker node,
  each containing `label_*_model.pkl`, `label_*_coef.npy`, `label_*_intercept.npy` files)

If any of these are missing, run the earlier milestones first using their respective
run instructions.

## 2. Required Software

- Python 3.11+ (all machines — master and workers — **must run the same Python version**)
- VS Code with Jupyter extension (recommended) or Jupyter Notebook/Lab
- A running Dask cluster (scheduler + workers) — see Section 6 below

## 3. Required Python Libraries

Install the libraries below in your environment:

- pandas
- numpy
- scipy
- scikit-learn
- dask[distributed]
- matplotlib
- pyarrow (for Parquet output — optional but recommended)
- jupyter
- ipykernel

## 4. Setup Commands (Windows CMD)

From the project folder (you can reuse the same `venv` from Milestones 1 and 2 if it
still exists):

```bat
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install pandas numpy scipy scikit-learn "dask[distributed]" matplotlib pyarrow jupyter ipykernel
```

If you already have the Milestone 1/2 environment active, just add any missing libraries:

```bat
venv\Scripts\activate
pip install scipy pyarrow
```

## 5. File Layout Expected

Your folder should contain at least:

- `milestone3_updated.ipynb`
- `X_test_normalized.npz`
- `test_meta.csv`
- `models_node_level/` (folder produced by Milestone 2, with all node subfolders and
  their model files intact)

## 6. Starting the Dask Cluster (Multi-Machine)

Milestone 3 connects to a real multi-machine Dask cluster. All machines must be on
the same network (LAN or Wi-Fi) and have the project dependencies installed.

**On the scheduler machine**, run:

```bat
venv\Scripts\activate
dask scheduler
```

The scheduler will print its address, for example:

```
Scheduler at: tcp://192.168.0.103:8786
```

**On each worker machine**, run:

```bat
venv\Scripts\activate
dask worker tcp://<SCHEDULER_IP>:8786
```

Replace `<SCHEDULER_IP>` with the actual IP printed by the scheduler.

**Before running the notebook**, open `milestone3_updated.ipynb` and update the scheduler IP
in the connection cell:

```python
SCHEDULER_IP = "192.168.0.103"   # <-- set this to your scheduler machine's actual IP
```

Worker machines do not need to hold a copy of the model files — the master (notebook)
machine loads all model bytes locally and scatters only the test feature matrix to
workers over the network.

## 7. How To Run

1. Start the Dask scheduler and all worker machines as described in Section 6.
2. Open `milestone3_updated.ipynb`.
3. Update `SCHEDULER_IP` to your scheduler's IP address.
4. Select the Python kernel from your `venv`.
5. Run all cells from top to bottom in order.
6. Do not skip any cells — each cell depends on variables and objects defined in the
   ones before it.

## 8. What Gets Generated

After successful execution, the notebook generates:

- `milestone3_predictions.csv` — final multi-label predictions for all test rows
- `milestone3_predictions.parquet` — same predictions in Parquet format (if pyarrow is installed)
- `milestone3_benchmark.csv` — sequential vs distributed inference timing results
- `milestone3_speedup.png` — speedup plot across worker counts
- `milestone3_efficiency.png` — parallel efficiency plot across worker counts
- `milestone3_manifest.json` — summary of the full Milestone 3 run (timing, threshold,
  worker count, file paths)

## 9. Expected Runtime

- **Inference cell** (distributed prediction across all trained labels): a few minutes
  depending on the number of active workers and their CPU speed. The test feature matrix
  is scattered once to all workers and each worker processes its assigned label batch
  in parallel.
- **Benchmarking cell**: a few additional minutes. It reruns inference on a subset of
  300 labels sequentially and then in parallel across 1, 2, 4, and 8 workers to measure
  speedup. Worker counts that exceed the number of active workers are automatically
  skipped.
- All other cells complete in seconds.

## 10. Important Note About Distributed Execution

Milestone 3 uses a real multi-machine Dask cluster — not a LocalCluster simulation.

- The notebook machine acts as the master: it loads all trained model files, connects
  to the scheduler, and scatters the test feature matrix to workers.
- Each worker machine receives a batch of label models and runs inference on the full
  test set for its assigned labels.
- Aggregation (thresholding at 0.5, fallback to best-probability label) is performed
  on the master after all worker results are collected.

## 11. Typical Constraints On Other PCs

To run reliably on another machine:

- Have at least 4 GB of free RAM on the master machine (it holds all model files in
  memory before scattering inference tasks).
- Have at least 2 GB of free RAM on each worker machine (it receives the test feature
  matrix and runs inference for its label batch).
- Have at least 1 GB of free disk space for generated prediction and benchmark files.
- Keep all Milestone 1 and Milestone 2 output files in the same folder as `milestone3.ipynb`.
- Ensure all machines on the cluster have the required Python libraries installed.
- Ensure firewalls on all machines allow TCP traffic on port 8786 (scheduler) and
  8787 (Dask dashboard).
- Run cells in sequence without skipping dependencies.

## 12. Troubleshooting

- If `FileNotFoundError` appears for `X_test_normalized.npz`, `test_meta.csv`, or files
  inside `models_node_level/`, verify Milestones 1 and 2 were run successfully and all
  output files are present in the notebook folder.
- If `RuntimeError: No active workers` appears, make sure at least one `dask worker`
  process is running and has successfully registered with the scheduler before running
  the connection cell.
- If the connection cell hangs or times out, double-check that `SCHEDULER_IP` is set
  correctly and that port 8786 is not blocked by a firewall on the scheduler machine.
- If `ModuleNotFoundError` appears, reinstall missing packages in the same environment
  on the affected machine.
- If predictions appear empty or all rows fall back to a single label, verify that the
  `model_registry.csv` integrity column contains `OK` entries — this means Milestone 2
  completed its model collection step successfully.
- If the Parquet write is skipped, install pyarrow (`pip install pyarrow`) and re-run
  only the inference cell. The CSV output is always written regardless.
- If `SystemError: unknown opcode 128` appears on the inference cell, it means the master
  machine and worker machines are running different Python versions. The master is likely
  Python 3.11+ while one or more workers are on 3.10 or older. Fix: install the same
  Python version on all machines, then restart all worker processes with
  `dask worker tcp://<SCHEDULER_IP>:8786`.
