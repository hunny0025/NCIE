#!/usr/bin/env python3
"""
Quick test to verify NCIE installation
"""
import sys
import os

print("🧪 Quick NCIE Test...")

# Add src to path
sys.path.append('src')

# Test 1: Check Python version
print(f"Python: {sys.version.split()[0]}")

# Test 2: Check imports
try:
    from config import Config
    print("✅ Config imported")
except ImportError as e:
    print(f"❌ Config import failed: {e}")
    sys.exit(1)

# Test 3: Check dependencies
dependencies = ['pandas', 'numpy', 'openai', 'pydantic', 'sentence_transformers']
for dep in dependencies:
    try:
        __import__(dep)
        print(f"✅ {dep}")
    except ImportError:
        print(f"❌ {dep} missing")

# Test 4: Create results directory
config = Config.validate()
if config.paths.results_dir.exists():
    print(f"✅ Results directory exists: {config.paths.results_dir}")
else:
    print(f"❌ Results directory not created")

print("\n🎉 Quick test complete!")
print("Run 'python run.py demo' to test the full system")