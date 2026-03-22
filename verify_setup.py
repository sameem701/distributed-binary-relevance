#!/usr/bin/env python
"""
Quick verification script for Binary Relevance project setup
Run this to verify your environment is ready to execute milestone1_optimized.py
"""

import sys
import subprocess
from pathlib import Path

def print_header(text):
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)

def check_python_version():
    """Check if Python version is 3.8 or higher"""
    print("\n1. Checking Python version...")
    version = sys.version_info
    version_str = f"{version.major}.{version.minor}.{version.micro}"
    print(f"   Python version: {version_str}")
    
    if version.major >= 3 and version.minor >= 8:
        print("   ✅ Python version OK (3.8+)")
        return True
    else:
        print("   ❌ Python version TOO OLD (need 3.8+)")
        return False

def check_required_packages():
    """Check if all required packages are installed"""
    print("\n2. Checking required packages...")
    
    packages = ['pandas', 'numpy', 'sklearn', 'scipy']
    all_ok = True
    
    for package in packages:
        try:
            if package == 'sklearn':
                import sklearn
                version = sklearn.__version__
            else:
                mod = __import__(package)
                version = mod.__version__
            print(f"   ✅ {package.upper()} version: {version}")
        except ImportError:
            print(f"   ❌ {package.upper()} NOT INSTALLED")
            all_ok = False
    
    if not all_ok:
        print("\n   Fix: Run: pip install -r requirements.txt")
    
    return all_ok

def check_data_files():
    """Check if data files exist"""
    print("\n3. Checking data files...")
    
    files_to_check = [
        ('eurlex.csv', 'Training data'),
        ('eurlex_test.csv', 'Test data'),
    ]
    
    all_ok = True
    for filename, description in files_to_check:
        filepath = Path(filename)
        if filepath.exists():
            size_mb = filepath.stat().st_size / (1024 * 1024)
            print(f"   ✅ {filename}: {size_mb:.1f} MB ({description})")
        else:
            print(f"   ❌ {filename}: NOT FOUND ({description})")
            all_ok = False
    
    return all_ok

def check_output_structure():
    """Check project structure"""
    print("\n4. Checking project structure...")
    
    files_to_check = [
        'README.md',
        'REPORT.md',
        'milestone1_optimized.py',
        'milestone1.py',
        'requirements.txt',
    ]
    
    all_ok = True
    for filename in files_to_check:
        filepath = Path(filename)
        if filepath.exists():
            size_kb = filepath.stat().st_size / 1024
            print(f"   ✅ {filename}: {size_kb:.1f} KB")
        else:
            print(f"   ❌ {filename}: NOT FOUND")
            all_ok = False
    
    return all_ok

def check_disk_space():
    """Check available disk space"""
    print("\n5. Checking disk space...")
    
    try:
        import shutil
        stat = shutil.disk_usage('.')
        total_gb = stat.total / (1024 ** 3)
        free_gb = stat.free / (1024 ** 3)
        
        print(f"   Total disk space: {total_gb:.1f} GB")
        print(f"   Free disk space: {free_gb:.1f} GB")
        
        if free_gb >= 2:
            print("   ✅ Sufficient disk space (need ~3 GB)") 
            return True
        else:
            print("   ⚠️  Limited disk space (need ~3 GB)")
            return False
    except Exception as e:
        print(f"   ⚠️  Could not check disk space: {e}")
        return True  # Don't fail on this check

def print_summary(results):
    """Print verification summary"""
    print_header("VERIFICATION SUMMARY")
    
    checks = [
        ("Python Version", results[0]),
        ("Required Packages", results[1]),
        ("Data Files", results[2]),
        ("Project Structure", results[3]),
        ("Disk Space", results[4]),
    ]
    
    all_ok = all(results)
    
    for check_name, passed in checks:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{check_name:.<35} {status}")
    
    print()
    if all_ok:
        print("✅ ALL CHECKS PASSED - Ready to run!")
        print("\nRun the code with:")
        print("   python milestone1_optimized.py")
        return True
    else:
        print("❌ SOME CHECKS FAILED - Fix issues above")
        print("\nTo install dependencies:")
        print("   pip install -r requirements.txt")
        return False

def main():
    print_header("BINARY RELEVANCE PROJECT - ENVIRONMENT VERIFICATION")
    
    print("\nChecking project setup and dependencies...")
    
    results = [
        check_python_version(),
        check_required_packages(),
        check_data_files(),
        check_output_structure(),
        check_disk_space(),
    ]
    
    success = print_summary(results)
    
    if success:
        print("\n📊 Next Steps:")
        print("1. Run: python milestone1_optimized.py")
        print("2. Expected runtime: 4-5 minutes")
        print("3. Results saved to: test_predictions.npy")
        print("4. Optionally run full version: python milestone1.py")
        sys.exit(0)
    else:
        print("\n❌ Please fix the issues above and rerun this script")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error during verification: {e}")
        sys.exit(1)
