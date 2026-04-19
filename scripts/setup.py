#!/usr/bin/env python
"""
Setup script for workshop_pixel_a_cuantificacion.

This script:
1. Installs the assistant environment
2. Detects CUDA availability
3. Installs cellpose (GPU) or cellpose-cpu (CPU) accordingly
4. Downloads data files
"""

import subprocess
import sys
from pathlib import Path


def detect_cuda():
    """
    Detect if CUDA is available on the system.
    
    Returns:
        bool: True if CUDA is detected, False otherwise
    """
    print("🔍 Detecting CUDA availability...")
    
    # Try nvidia-smi first
    try:
        result = subprocess.run(
            ["nvidia-smi"],
            capture_output=True,
            timeout=5,
            check=False
        )
        if result.returncode == 0:
            print("✅ CUDA detected (nvidia-smi found)")
            return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    
    # Try Python torch detection
    try:
        import torch
        if torch.cuda.is_available():
            print("✅ CUDA detected (PyTorch CUDA available)")
            return True
    except ImportError:
        pass
    
    print("❌ CUDA not detected - will use CPU version")
    return False


def run_command(cmd, description):
    """
    Run a shell command and handle errors.
    
    Args:
        cmd (list): Command to run as a list
        description (str): Description of what the command does
    """
    print(f"\n📦 {description}...")
    try:
        result = subprocess.run(cmd, check=True)
        if result.returncode == 0:
            print(f"✅ {description} completed successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}: {e}")
        sys.exit(1)


def check_data_files():
    """
    Check if data files are already downloaded.
    
    Returns:
        bool: True if all data files exist, False otherwise
    """
    data_dir = Path("data")
    required_files = [
        data_dir / "Lund.tif",
        data_dir / "lund1051_resampled.tif"
    ]
    
    all_exist = all(file.exists() for file in required_files)
    
    if all_exist:
        print("✅ Data files already downloaded")
        return True
    
    missing = [file for file in required_files if not file.exists()]
    print(f"📥 Missing data files: {', '.join(file.name for file in missing)}")
    return False


def main():
    """Main setup function."""
    print("=" * 60)
    print("🚀 Workshop Setup")
    print("=" * 60)
    
    # Step 1: Install assistant environment
    run_command(
        ["pixi", "install", "--feature", "assistant"],
        "Installing assistant environment"
    )
    
    # Step 2: Detect CUDA and install appropriate cellpose
    cuda_available = detect_cuda()
    cellpose_feature = "cellpose" if cuda_available else "cellpose-cpu"
    
    run_command(
        ["pixi", "install", "--feature", cellpose_feature],
        f"Installing cellpose environment ({cellpose_feature})"
    )
    
    # Step 3: Check if data needs to be downloaded
    print("\n📁 Checking data files...")
    if not check_data_files():
        run_command(
            ["pixi", "run", "download-data"],
            "Downloading data files"
        )
    
    print("\n" + "=" * 60)
    print("✅ Setup completed successfully!")
    print("=" * 60)
    print("\n🎯 Next steps:")
    print(f"   Assistant environment: pixi run --environment assistant napari")
    print(f"   Cellpose environment: pixi run --environment {cellpose_feature} cellpose")


if __name__ == "__main__":
    main()
