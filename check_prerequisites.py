#!/usr/bin/env python3
"""
Check all system prerequisites for the Answer Paper Evaluation System
"""

import subprocess
import sys
from pathlib import Path

def check_command(cmd, name):
    """Check if a command exists"""
    try:
        subprocess.run([cmd, "--version"], capture_output=True, check=True)
        print(f"✓ {name} is installed")
        return True
    except:
        print(f"✗ {name} is NOT installed")
        return False

def check_python_packages():
    """Check required Python packages"""
    required_packages = {
        'fastapi': 'FastAPI',
        'streamlit': 'Streamlit',
        'langchain': 'LangChain',
        'google.generativeai': 'Google Generative AI',
        'pymongo': 'PyMongo',
        'chromadb': 'ChromaDB',
        'easyocr': 'EasyOCR',
        'pdfplumber': 'PDFPlumber'
    }
    
    all_installed = True
    for package, name in required_packages.items():
        try:
            __import__(package)
            print(f"✓ {name} is installed")
        except ImportError:
            print(f"✗ {name} is NOT installed")
            all_installed = False
    
    return all_installed

def check_mongodb():
    """Check if MongoDB is running"""
    try:
        from pymongo import MongoClient
        client = MongoClient('mongodb://localhost:27017', serverSelectionTimeoutMS=2000)
        client.server_info()
        print("✓ MongoDB is running at localhost:27017")
        return True
    except Exception as e:
        print(f"✗ MongoDB is NOT running: {e}")
        return False

def check_env_file():
    """Check if .env file exists and has required keys"""
    env_file = Path(".env")
    if not env_file.exists():
        print("✗ .env file not found")
        return False
    
    with open(env_file, "r") as f:
        content = f.read()
    
    required_keys = ['GEMINI_API_KEY', 'MONGODB_URL', 'DATABASE_NAME']
    all_present = True
    
    for key in required_keys:
        if key in content:
            print(f"✓ {key} is configured")
        else:
            print(f"✗ {key} is NOT configured")
            all_present = False
    
    return all_present

def main():
    print("=" * 60)
    print("System Prerequisites Check")
    print("=" * 60)
    
    print("\n1. Checking System Commands:")
    check_command("python3", "Python 3")
    check_command("docker", "Docker")
    
    print("\n2. Checking Python Packages:")
    packages_ok = check_python_packages()
    
    print("\n3. Checking MongoDB:")
    db_ok = check_mongodb()
    
    print("\n4. Checking Configuration:")
    env_ok = check_env_file()
    
    print("\n" + "=" * 60)
    
    if not packages_ok:
        print("\nInstall missing packages:")
        print("  cd backend && pip install -r requirements.txt")
        print("  cd ../frontend && pip install -r requirements.txt")
    
    if not db_ok:
        print("\nStart MongoDB (if using Docker):")
        print("  docker run -d -p 27017:27017 --name mongodb mongo:latest")
    
    if not env_ok:
        print("\nSetup .env file:")
        print("  cp .env.example .env")
        print("  Edit .env and add your GEMINI_API_KEY")
    
    if packages_ok and db_ok and env_ok:
        print("\n✓ All prerequisites are met! Ready to run the application.")
        print("\nStart the application:")
        print("  Terminal 1: python backend/main.py")
        print("  Terminal 2: streamlit run frontend/app.py")
    
    return 0 if (packages_ok and db_ok and env_ok) else 1

if __name__ == "__main__":
    sys.exit(main())
