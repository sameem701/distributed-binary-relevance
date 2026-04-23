# Milestone 1 Run Instructions

This guide explains how to run `milestone1.ipynb` on another PC.

## 1. What To Download First

Before running the notebook, download these two required dataset files:

- `eurlex.csv`:
  https://drive.google.com/file/d/1jTIYiGGs5fHLe_NRd8HiK7ADvxyLlSMU/view?usp=sharing
- `eurlex_test.csv`:
  https://drive.google.com/file/d/1SOmvcq2f04VNJkkBtN3ERqK52zJlrsuD/view?usp=drive_link

After downloading, place both files in the same folder as `milestone1.ipynb`.

## 2. Required Software

- Python 3.10+ (recommended)
- VS Code with Jupyter extension (recommended) or Jupyter Notebook/Lab

## 3. Required Python Libraries

Install the libraries below in your environment:

- pandas
- numpy
- dask[distributed]
- jupyter
- ipykernel

## 4. Setup Commands (Windows CMD)

From the project folder:

```bat
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install pandas numpy "dask[distributed]" jupyter ipykernel
```

## 5. File Layout Expected

Your folder should contain at least:

- `milestone1.ipynb`
- `eurlex.csv`
- `eurlex_test.csv`

The notebook will generate the rest of the outputs (normalized files, partitions, metadata, and distributed config).

## 6. How To Run

1. Open `milestone1.ipynb`.
2. Select the Python kernel from your `venv`.
3. Run all cells from top to bottom in order.

## 7. What Gets Generated

After successful execution, the notebook generates:

- `eurlex_normalized.csv`
- `eurlex_test_normalized.csv`
- `normalization_params.pkl`
- `partitions/partition_0.csv` to `partitions/partition_3.csv`
- `partition_metadata.pkl`
- `distributed_config.json`

## 8. Important Note About Distributed Execution

Current implementation uses a Dask `LocalCluster`.

- It runs multiple Dask workers in parallel on a single PC.
- It is a local simulation of distributed processing.
- It is not a true multi-machine cluster in the current state.

## 9. Typical Constraints On Other PCs

To run reliably on another machine:

- Have enough free disk space for generated CSV files.
- Have enough RAM for loading and partitioning wide data.
- Keep the same file names (`eurlex.csv`, `eurlex_test.csv`).
- Run cells in sequence without skipping dependencies.

## 10. Troubleshooting

- If `ModuleNotFoundError` appears, reinstall missing packages in the same environment.
- If Dask worker startup fails, close old Python/Jupyter processes and run again.
- If file-not-found errors appear, verify both input CSV files are in the notebook folder.

## 11. Future Multi-Machine Upgrade Note

This project will later be upgraded from LocalCluster to a multi-machine Dask cluster (as it requires seperate machines to be on the same wifi, which currently wasn't feasible), this run guide will need to be updated.

Probable changes:

- A scheduler process would run on one machine and workers would run on other machines.
- All machines would need network reachability (same LAN/Wi-Fi, VPN, or other reachable network).
- Firewalls and ports would need to allow scheduler/worker communication.
- Data paths would need to be shared or synchronized across machines.
- Cluster startup commands would be different from local-only startup.

Current notebook is configured for single-machine execution using LocalCluster, so these distributed infrastructure steps are not required right now.
