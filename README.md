# Binary Relevance Multi-Label Classification with Parallel & Distributed Computing

A distributed computing project implementing **Binary Relevance** approach for multi-label classification on the EURLex-4K dataset, with parallel training and inference using Python's concurrent.futures.

## Project Overview

This project implements multi-label classification using binary relevance decomposition, where a complex multi-label problem is solved by training independent binary classifiers for each label. The implementation emphasizes parallel and distributed computing techniques to efficiently handle large-scale multi-label datasets.

### Key Features
- **Binary Relevance Decomposition**: Converts multi-label problem into independent binary classification tasks
- **Parallel Training**: Uses ThreadPoolExecutor to train multiple binary classifiers concurrently
- **Parallel Inference**: Makes predictions across all labels in parallel
- **Scalable Design**: Handles large feature sets (5,000+) and large label sets (3,000+)
- **High Performance**: Achieves ~84% exact match accuracy on EURLex-4K test set

## Dataset

**EURLex-4K** - European legal document classification
- **Training samples**: 15,377
- **Test samples**: 3,971
- **Features**: 5,000
- **Labels**: 3,806 unique (project focuses on top 50 for efficiency)
- **Format**: CSV with sparse multi-label representation

### 📥 Download Dataset Files

The dataset files must be downloaded separately and placed in the project directory:

📄 **See [DATASET_DOWNLOADS.md](DATASET_DOWNLOADS.md)** for download links and instructions

- `eurlex.csv` (308 MB) - [Download](https://drive.google.com/file/d/1jTIYiGGs5fHLe_NRd8HiK7ADvxyLlSMU/view?usp=drive_link)
- `eurlex_test.csv` (79 MB) - [Download](https://drive.google.com/file/d/1SOmvcq2f04VNJkkBtN3ERqK52zJlrsuD/view?usp=drive_link)

## Project Structure

```
distributed-binary-relevance/
├── eurlex.csv                 # Training data (CSV format, ~323 MB)
├── eurlex_test.csv           # Test data (CSV format, ~83 MB)
├── milestone1.py             # Full implementation (all labels)
├── milestone1_optimized.py   # Optimized version (top 50 labels)
├── test_predictions.npy      # Model predictions output
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Prerequisites

- **Python**: 3.8 or higher
- **Operating System**: Windows, macOS, or Linux
- **Memory**: Minimum 8 GB RAM (16 GB recommended)
- **Disk Space**: ~500 MB for dependencies + ~400 MB for data files

## Installation

### 1. Clone or Download the Repository

```bash
git clone <repository-url>
cd distributed-binary-relevance
```

### 2. Create Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This will install:
- `pandas` - Data manipulation
- `numpy` - Numerical computing
- `scikit-learn` - Machine learning models
- `scipy` - Scientific computing (dependency)

## Running the Code

### Option 1: Quick Start (Optimized Version - Recommended)

```bash
# Run binary relevance on top 50 most frequent labels
python milestone1_optimized.py
```

**Expected Runtime**: ~4-5 minutes
**Memory Usage**: ~2-3 GB

**Output**:
- Trained 50 binary classifiers in parallel
- Test predictions saved to `test_predictions.npy`
- Console output showing metrics and timing

### Option 2: Full Implementation (All Labels)

```bash
# Run with all 3,806 labels - WARNING: Computationally expensive
python milestone1.py
```

**Expected Runtime**: 30+ minutes (depends on system)
**Memory Usage**: 8+ GB

## Output Interpretation

### Console Output Example

```
============================================================
Binary Relevance Classification with Parallel Training
============================================================
Loading data...
Train shape: (15377, 5000)
Test shape: (3971, 5000)
Number of samples: 15377
Total unique labels: 3806
Top 50 labels cover 19104 label occurrences

Focusing on 50 most frequent labels
Training binary matrix shape: (15377, 50)

Training 50 binary classifiers in parallel with 4 workers...
Training completed in 235.94s
Classifiers trained: 50/50
Average train accuracy: 0.9985
Average validation accuracy: 0.9752

Evaluation Metrics:
==================================================
Hamming Loss: 0.0061
Exact Match Accuracy: 0.8325
F1 Score (Micro): 0.8743
F1 Score (Macro): 0.8728
Label Accuracy - Min: 0.9794, Max: 0.9977, Mean: 0.9939

Performance Summary:
============================================================
Training time (parallel): 235.94s
Prediction time (parallel): 1.06s
Number of workers: 4
Test set predictions saved to: test_predictions.npy

============================================================
Milestone 1 Completed Successfully!
============================================================
```

### Loading and Using Predictions

```python
import numpy as np

# Load predictions (numpy array: shape (3971, 50))
predictions = np.load('test_predictions.npy')

# predictions[i, j] = 1 if label j is predicted for sample i, 0 otherwise
print(predictions.shape)  # (3971, 50)
print(predictions[0])     # Predictions for first test sample
```

## Performance Metrics Explanation

| Metric | Description | Value |
|--------|-------------|-------|
| **Exact Match Accuracy** | Percentage of samples with all labels correctly predicted | 83.25% |
| **Hamming Loss** | Average fraction of labels incorrectly predicted | 0.61% |
| **F1 Score (Micro)** | Unweighted mean F1 across all labels | 0.8743 |
| **F1 Score (Macro)** | Weighted mean F1 across all labels | 0.8728 |
| **Label Accuracy** | Per-label accuracy (min, max, mean) | 97.94%-99.77% |

## Parallel Computing Details

### Architecture
- **Executor**: ThreadPoolExecutor (4 workers by default)
- **Training Parallelism**: Each worker trains one binary classifier independently
- **Inference Parallelism**: Each worker makes predictions for one label across all samples
- **Synchronization**: join() at completion of all workers

### Configuration
You can adjust parallelism parameters in the script:

```python
NUM_WORKERS = 4          # Number of parallel workers
TEST_SIZE = 0.2          # Validation split ratio
TOP_LABELS = 50          # Number of labels to focus on (optimized version)
```

### Timing Breakdown (Optimized Version)
- **Data Loading**: ~10 seconds
- **Feature Scaling**: ~5 seconds
- **Parallel Training**: ~236 seconds (4 workers)
- **Parallel Inference**: ~1 second (test set)
- **Evaluation**: ~3 seconds

## Troubleshooting

### Issue: Memory Error
**Solution**: Reduce `NUM_WORKERS` or `TOP_LABELS` in the script:
```python
NUM_WORKERS = 2          # Reduce from 4 to 2
TOP_LABELS = 25          # Reduce from 50 to 25
```

### Issue: CSV Files Larger Than Expected Size
The original CSV files are large:
- `eurlex.csv`: ~323 MB
- `eurlex_test.csv`: ~83 MB

These are normal for the EURLex-4K dataset. Ensure you have sufficient disk space.

### Issue: Script Hangs
This is normal during training phase. The script prints progress messages. For status:
- Check system task manager (Windows) or `top` (Linux/macOS)
- Look for Python process using 100% CPU (training phase) or lower CPU (prediction)

### Issue: Import Errors
Ensure all dependencies are installed:
```bash
pip install --upgrade pandas numpy scikit-learn scipy
```

## Extending the Code

### Training on All Labels
Edit `milestone1_optimized.py` and modify:
```python
TOP_LABELS = None  # Remove limit to use all labels
```

### Using Different Classifiers
Replace LogisticRegression with other scikit-learn classifiers:
```python
# In train_binary_classifier function
clf = SVC(kernel='rbf')  # Support Vector Machine
# or
clf = RandomForestClassifier(n_estimators=100)  # Random Forest
```

### Implementing Distributed Computing
For true distributed training across multiple machines, consider:
- **PySpark**: For resource scheduling and distributed data processing
- **Dask**: For distributed computing with familiar pandas API
- **Ray**: For distributed ML with parallel training

## References

### Papers/Resources
- [Binary Relevance for Multi-Label Learning](https://arxiv.org/abs/1309.2329)
- [Multi-Label Classification: An Overview](https://arxiv.org/abs/1406.6339)
- [EURLex-4K Dataset](http://www.datasciencelab.org/multilabel-learning/)

### Related Work
- Multi-label to Binary transformation techniques
- Classifier chain approaches
- Label powerset methods

## License

This project is provided as-is for educational purposes.

## Contact & Support

For issues or questions regarding the implementation, refer to the REPORT.md for project status and remaining tasks.

## Version History

- **Milestone 1** (Current): Binary Relevance Implementation with Parallel Training
  - ✅ Completed: Binary relevance decomposition
  - ✅ Completed: Parallel training of binary classifiers
  - ✅ Completed: Parallel inference
  - ⏳ Future: Distributed computing across multiple nodes

---

**Last Updated**: March 22, 2026
