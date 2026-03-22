# Dataset Downloads

This file contains the download links for the EURLex-4K dataset files required to run the Binary Relevance classification project.

## Training Data
**File**: `eurlex.csv`  
**Size**: ~308 MB  
**Samples**: 15,377 training samples with 5,000 features + multi-label targets  
**Download**: https://drive.google.com/file/d/1jTIYiGGs5fHLe_NRd8HiK7ADvxyLlSMU/view?usp=drive_link

## Test Data
**File**: `eurlex_test.csv`  
**Size**: ~79 MB  
**Samples**: 3,971 test samples with 5,000 features  
**Download**: https://drive.google.com/file/d/1SOmvcq2f04VNJkkBtN3ERqK52zJlrsuD/view?usp=drive_link

---

## Setup Instructions

1. Click on the download links above
2. Download both CSV files to your local machine
3. Place them in the project directory:
   ```
   distributed-binary-relevance/
   ├── eurlex.csv
   ├── eurlex_test.csv
   ├── milestone1_optimized.py
   └── ... (other files)
   ```

4. Verify setup with:
   ```bash
   python verify_setup.py
   ```

5. Run the code:
   ```bash
   python milestone1_optimized.py
   ```

---

## Alternative: Direct Google Drive Access

If the links above don't work, you can access the files through:
- Navigate to Google Drive
- Search for the file IDs:
  - Training: `1jTIYiGGs5fHLe_NRd8HiK7ADvxyLlSMU`
  - Test: `1SOmvcq2f04VNJkkBtN3ERqK52zJlrsuD`

---

## Dataset Information

**Dataset Name**: EURLex-4K  
**Description**: European legal documents multi-label classification  
**Source**: [Dataset Lab](http://www.datasciencelab.org/multilabel-learning/)  
**Total Labels**: 3,806  
**Feature Type**: TF-IDF term frequencies (sparse)  
**Format**: CSV with row_id, features (f0-f4999), and labels (sparse format: "idx:value")

---

## Verification

After downloading, verify file sizes:
- `eurlex.csv`: ~307 MB
- `eurlex_test.csv`: ~79 MB

Run `python verify_setup.py` to confirm files are in the correct location and readable.

---

**Last Updated**: March 22, 2026
