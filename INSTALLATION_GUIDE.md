# Installation Script Setup Guide

## Quick Setup for Different Operating Systems

Choose your operating system below:

### Windows
```bash
# 1. Create virtual environment
python -m venv .venv

# 2. Activate virtual environment
.venv\Scripts\activate

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Verify setup
python verify_setup.py

# 5. Run the code
python milestone1_optimized.py
```

### macOS
```bash
# 1. Create virtual environment
python3 -m venv .venv

# 2. Activate virtual environment
source .venv/bin/activate

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Verify setup
python verify_setup.py

# 5. Run the code
python milestone1_optimized.py
```

### Linux (Ubuntu/Debian)
```bash
# 1. Install system dependencies (if needed)
sudo apt-get install python3-venv python3-dev

# 2. Create virtual environment
python3 -m venv .venv

# 3. Activate virtual environment
source .venv/bin/activate

# 4. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 5. Verify setup
python verify_setup.py

# 6. Run the code
python milestone1_optimized.py
```

### Linux (Fedora/RHEL)
```bash
# 1. Install system dependencies (if needed)
sudo dnf install python3-venv python3-devel

# 2. Create virtual environment
python3 -m venv .venv

# 3. Activate virtual environment
source .venv/bin/activate

# 4. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 5. Verify setup
python verify_setup.py

# 6. Run the code
python milestone1_optimized.py
```

---

## One-Line Installation (If You Already Have Virtual Environment Active)

```bash
pip install -r requirements.txt && python verify_setup.py && python milestone1_optimized.py
```

---

## Installation Troubleshooting

### Issue 1: Virtual environment activation fails

**Windows**:
```bash
# Try using full path
venv\Scripts\activate.bat
# Or
venv\Scripts\Activate.ps1
```

**macOS/Linux**:
```bash
# Make sure .venv/bin/activate is executable
chmod +x .venv/bin/activate
source .venv/bin/activate
```

### Issue 2: pip install fails

Try upgrading pip first:
```bash
python -m pip install --upgrade pip
```

### Issue 3: ModuleNotFoundError after installation

Make sure virtual environment is activated:
```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# Then verify
python -c "import pandas; print(pandas.__version__)"
```

### Issue 4: Permission denied (Linux/macOS)

Try with `--user` flag:
```bash
pip install --user -r requirements.txt
```

Or use `sudo` (not recommended):
```bash
sudo pip install -r requirements.txt
```

---

## Verifying Installation

After installation, run:
```bash
python verify_setup.py
```

Expected output:
```
✅ ALL CHECKS PASSED - Ready to run!
```

If any check fails, follow the printed instructions to fix it.

---

## Running the Code

### Quick Test (Optimized Version - Recommended)
```bash
python milestone1_optimized.py
```
Expected runtime: 4-5 minutes
Output: test_predictions.npy

### Full Version (All Labels)
```bash
python milestone1.py
```
Expected runtime: 30+ minutes (depending on system)
Warning: Requires 16+ GB RAM

---

## Deactivating Virtual Environment

When done, deactivate with:

**Windows/macOS/Linux**:
```bash
deactivate
```

This returns you to your system Python environment.

---

## Reinstalling Dependencies

If you need to reinstall with clean slate:

```bash
# Windows
.venv\Scripts\pip uninstall -r requirements.txt -y
.venv\Scripts\pip install -r requirements.txt

# macOS/Linux
source .venv/bin/activate
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

---

## Using Without Virtual Environment (Not Recommended)

If you want to install system-wide:

```bash
pip install --user -r requirements.txt
```

This installs to your user Python site-packages directory.

---

## Docker Installation (Optional Advanced)

If you prefer containerized environment:

```bash
# Create simple Dockerfile
cat > Dockerfile << EOF
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "milestone1_optimized.py"]
EOF

# Build and run
docker build -t binary-relevance .
docker run binary-relevance
```

---

## Next Steps After Installation

1. ✅ Install dependencies
2. ✅ Run `verify_setup.py`
3. ✅ Run `python milestone1_optimized.py`
4. ✅ Check `test_predictions.npy` output
5. Read `README.md` for usage details
6. Read `REPORT.md` for technical details

---

## Need Help?

- See `README.md` for troubleshooting
- See `REPORT.md` for detailed documentation
- See `GITHUB_SETUP_GUIDE.md` for GitHub setup
- Run `python verify_setup.py` to diagnose issues
