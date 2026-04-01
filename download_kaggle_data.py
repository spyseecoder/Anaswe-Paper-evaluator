#!/usr/bin/env python3
"""
Script to download sample exam papers data from Kaggle
"""

import os
import sys
from pathlib import Path
import zipfile
import shutil

def download_from_kaggle():
    """Download handwritten exam papers dataset from Kaggle"""
    try:
        import kaggle
        print("Kaggle API found. Installing dataset...")
        
        # Create data directory
        data_dir = Path("sample_data")
        data_dir.mkdir(exist_ok=True)
        
        # Download a dataset - you may need to adjust the dataset name
        # Popular options: handwritten exam papers, document images, etc.
        try:
            print("Attempting to download MNIST dataset (handwritten digits)...")
            kaggle.api.dataset_download_files('hmnist_28_28', path=str(data_dir), unzip=True)
            print("Download successful!")
            return True
        except Exception as e:
            print(f"Dataset not found: {e}")
            print("Trying alternative dataset...")
            try:
                kaggle.api.dataset_download_files('jpmiller/documents', path=str(data_dir), unzip=True)
                print("Alternative dataset downloaded successfully!")
                return True
            except:
                print("Could not download from Kaggle. Please install kaggle API or configure credentials.")
                print("Install with: pip install -U kaggle")
                print("Configure credentials from: https://www.kaggle.com/account")
                return False
    except ImportError:
        print("Kaggle API not installed. Install with: pip install -U kaggle")
        return False

def create_sample_data():
    """Create sample marking scheme and answer papers for testing"""
    print("\nCreating sample data for testing...")
    
    sample_data_dir = Path("sample_data")
    sample_data_dir.mkdir(exist_ok=True)
    
    # Create sample marking scheme
    marking_scheme = """
    MATHEMATICS EXAM - MARKING SCHEME
    ================================
    
    Question 1: Algebra (20 marks)
    - Correct expansion: 10 marks
    - Solving equation: 10 marks
    
    Question 2: Geometry (20 marks)
    - Identifying angles: 5 marks
    - Calculating area: 10 marks
    - Using correct formula: 5 marks
    
    Question 3: Calculus (30 marks)
    - Finding derivative: 10 marks
    - Finding integral: 10 marks
    - Final answer: 10 marks
    
    Question 4: Statistics (30 marks)
    - Data interpretation: 10 marks
    - Calculation: 10 marks
    - Conclusion: 10 marks
    
    Total: 100 marks
    """
    
    marking_file = sample_data_dir / "marking_scheme.txt"
    with open(marking_file, "w") as f:
        f.write(marking_scheme)
    print(f"Created: {marking_file}")
    
    # Create sample answer paper
    answer_paper = """
    STUDENT ANSWER SHEET
    Student ID: STU001
    Date: 28/03/2026
    
    Question 1: Algebra
    (x + 5)² = x² + 10x + 25
    Solving x² + 10x + 25 = 0:
    (x + 5)² = 0
    x = -5
    
    Question 2: Geometry
    Triangle angles: 45°, 60°, 75°
    Area of triangle = 1/2 × base × height = 1/2 × 10 × 8 = 40 cm²
    
    Question 3: Calculus
    f(x) = 3x² + 2x + 1
    f'(x) = 6x + 2
    ∫f(x)dx = x³ + x² + x + C
    
    Question 4: Statistics
    Mean = 75, Std Dev = 8, Sample size = 100
    Conclusion: Data is normally distributed
    """
    
    answer_file = sample_data_dir / "sample_answer_paper.txt"
    with open(answer_file, "w") as f:
        f.write(answer_paper)
    print(f"Created: {answer_file}")
    
    return sample_data_dir

def main():
    print("=" * 60)
    print("Answer Paper Evaluation System - Data Setup")
    print("=" * 60)
    
    # Try to download from Kaggle
    kaggle_success = download_from_kaggle()
    
    # Always create sample data
    sample_dir = create_sample_data()
    
    if kaggle_success:
        print("\n✓ Kaggle data downloaded successfully")
    else:
        print("\n✓ Sample data created for testing")
        print("  You can manually download datasets from:")
        print("  https://www.kaggle.com/")
    
    print(f"\nSample data location: {sample_dir.absolute()}")
    print("\nNext steps:")
    print("1. Ensure MongoDB is running: docker ps | grep mongodb")
    print("2. Set GEMINI_API_KEY in .env file")
    print("3. Run backend: python backend/main.py")
    print("4. Run frontend: streamlit run frontend/app.py")
    
if __name__ == "__main__":
    main()
