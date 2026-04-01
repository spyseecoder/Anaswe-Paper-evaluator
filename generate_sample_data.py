#!/usr/bin/env python3
"""
Generate sample marking scheme and answer papers for testing the evaluation system
"""

import os
from pathlib import Path
from datetime import datetime, timedelta
import random

def create_marking_scheme():
    """Create a comprehensive marking scheme"""
    
    marking_scheme = """MATHEMATICS FINAL EXAMINATION
====================================
Course: Mathematics 101
Total Marks: 100
Duration: 3 hours
Date: March 28, 2026

MARKING SCHEME
==============

SECTION A: ALGEBRA (30 marks)
-----------------------------
Question 1: Solve the quadratic equation (10 marks)
- Correct identification of equation type: 2 marks
- Setting up correctly: 2 marks
- Using correct method (factoring/quadratic formula): 3 marks
- Correct calculation: 2 marks
- Correct final answer: 1 mark

Question 2: Simplify the algebraic expression (10 marks)
- Identifying like terms: 2 marks
- Correct expansion: 3 marks
- Combining terms correctly: 3 marks
- Final simplified form: 2 marks

Question 3: System of linear equations (10 marks)
- Correct method selection: 2 marks
- Setting up equations: 2 marks
- Solving first variable: 3 marks
- Solving second variable: 2 marks
- Verification: 1 mark

SECTION B: GEOMETRY (35 marks)
------------------------------
Question 4: Triangle properties (12 marks)
- Identifying triangle type: 2 marks
- Angle calculation: 4 marks
- Area calculation: 4 marks
- Using correct formula: 2 marks

Question 5: Circle theorems (12 marks)
- Understanding the theorem: 3 marks
- Angle identification: 3 marks
- Calculation of arc length: 3 marks
- Final answer with units: 3 marks

Question 6: 3D geometry (11 marks)
- Visualization: 2 marks
- Correct formula application: 3 marks
- Volume calculation: 3 marks
- Surface area calculation: 3 marks

SECTION C: CALCULUS (25 marks)
------------------------------
Question 7: Differentiation (12 marks)
- Power rule application: 2 marks
- Chain rule application: 3 marks
- Product rule application: 3 marks
- Correct final derivative: 2 marks
- Simplification: 2 marks

Question 8: Integration (13 marks)
- Recognizing integration type: 2 marks
- Correct formula: 3 marks
- Proper substitution: 3 marks
- Finding constant: 3 marks
- Final integral form: 2 marks

SECTION D: STATISTICS (10 marks)
--------------------------------
Question 9: Data analysis (10 marks)
- Data interpretation: 2 marks
- Mean calculation: 2 marks
- Standard deviation calculation: 3 marks
- Statistical conclusion: 3 marks

GRADING SCALE:
90-100: A (Excellent)
80-89: B (Very Good)
70-79: C (Good)
60-69: D (Satisfactory)
Below 60: F (Fail)

NOTES FOR EVALUATORS:
- Award partial credit for correct method even if final answer is wrong
- Deduct marks for missing units in answers
- Accept alternative correct methods
- Penalize for calculation errors but give credit for approach
"""
    
    return marking_scheme

def generate_answer_papers():
    """Generate 10 sample answer papers with varying quality"""
    
    papers = []
    
    # Paper 1: Excellent (95 marks)
    papers.append({
        'student_id': 'STU001',
        'name': 'Alice Johnson',
        'score': 95,
        'content': """STUDENT ANSWER SHEET
Student ID: STU001
Name: Alice Johnson
Date: March 28, 2026
Roll Number: 001

SECTION A: ALGEBRA

Q1: Solve the quadratic equation 2x² - 8x + 6 = 0
Solution:
2x² - 8x + 6 = 0
Dividing by 2: x² - 4x + 3 = 0
Factoring: (x - 1)(x - 3) = 0
Therefore: x = 1 or x = 3
Verification: 2(1)² - 8(1) + 6 = 2 - 8 + 6 = 0 ✓
             2(3)² - 8(3) + 6 = 18 - 24 + 6 = 0 ✓
Answer: x = 1, x = 3

Q2: Simplify 3x² + 5y - 2x² + 3y - 4
Solution:
Grouping like terms:
= (3x² - 2x²) + (5y + 3y) - 4
= x² + 8y - 4
Answer: x² + 8y - 4

Q3: Solve the system:
2x + 3y = 11
x - y = 0

Solution:
From second equation: x = y
Substituting in first: 2y + 3y = 11
5y = 11
y = 2.2
Therefore: x = 2.2

Verification:
2(2.2) + 3(2.2) = 4.4 + 6.6 = 11 ✓
2.2 - 2.2 = 0 ✓
Answer: x = 2.2, y = 2.2

SECTION B: GEOMETRY

Q4: Triangle with sides 3, 4, 5 cm
This is a right-angled triangle (Pythagorean triple)
Angles: 90°, 53.13°, 36.87°
Area = ½ × base × height = ½ × 3 × 4 = 6 cm²
Perimeter = 3 + 4 + 5 = 12 cm

Q5: Circle with radius 5 cm
Arc length subtending 60°:
Arc length = (θ/360°) × 2πr
= (60/360) × 2π × 5
= (1/6) × 10π
= 5π/3 ≈ 5.24 cm

Q6: Cube with side 4 cm
Volume = side³ = 4³ = 64 cm³
Surface Area = 6 × side² = 6 × 16 = 96 cm²

SECTION C: CALCULUS

Q7: Find dy/dx for y = 3x⁴ - 2x² + 5x - 7
Solution:
dy/dx = 12x³ - 4x + 5

Q8: Find ∫(3x² + 2x + 1)dx
Solution:
∫(3x² + 2x + 1)dx = x³ + x² + x + C

SECTION D: STATISTICS

Q9: Data set: {85, 90, 88, 92, 87, 91, 86, 89, 90, 88}
Mean = (85+90+88+92+87+91+86+89+90+88)/10 = 886/10 = 88.6
Variance = 4.84
Standard Deviation ≈ 2.2
Conclusion: The data shows consistent performance with most scores near the mean.
"""
    })
    
    # Paper 2: Very Good (87 marks)
    papers.append({
        'student_id': 'STU002',
        'name': 'Bob Smith',
        'score': 87,
        'content': """STUDENT ANSWER SHEET
Student ID: STU002
Name: Bob Smith
Date: March 28, 2026
Roll Number: 002

SECTION A: ALGEBRA

Q1: 2x² - 8x + 6 = 0
Using quadratic formula: x = (-b ± √(b²-4ac))/2a
a=2, b=-8, c=6
x = (8 ± √(64-48))/4 = (8 ± √16)/4 = (8 ± 4)/4
x = 3 or x = 1
Answer: x = 1, x = 3

Q2: 3x² + 5y - 2x² + 3y - 4
= (3-2)x² + (5+3)y - 4
= x² + 8y - 4

Q3: 2x + 3y = 11, x - y = 0
From eq 2: x = y
Sub: 2y + 3y = 11, so y = 2.2, x = 2.2

SECTION B: GEOMETRY

Q4: Triangle 3-4-5
Right angle triangle
Area = 6 cm²

Q5: Circle radius 5, arc 60°
Arc = (60/360) × 2π(5) ≈ 5.24 cm

Q6: Cube side 4
Volume = 64 cm³
Surface area = 96 cm²

SECTION C: CALCULUS

Q7: y = 3x⁴ - 2x² + 5x - 7
dy/dx = 12x³ - 4x + 5

Q8: ∫(3x² + 2x + 1)dx = x³ + x² + x + C

SECTION D: STATISTICS

Q9: Data: {85, 90, 88, 92, 87, 91, 86, 89, 90, 88}
Mean = 88.6
Standard Dev ≈ 2.2
Most scores are close to mean, showing average consistency.
"""
    })
    
    # Paper 3: Good (78 marks)
    papers.append({
        'student_id': 'STU003',
        'name': 'Carol Davis',
        'score': 78,
        'content': """STUDENT ANSWER SHEET
Student ID: STU003
Name: Carol Davis
Date: March 28, 2026
Roll Number: 003

SECTION A: ALGEBRA

Q1: 2x² - 8x + 6 = 0
Factoring: (2x - 6)(x - 1) = 0
x = 3, x = 1

Q2: 3x² + 5y - 2x² + 3y - 4 = x² + 8y - 4

Q3: 2x + 3y = 11, x - y = 0
x = 2.2, y = 2.2

SECTION B: GEOMETRY

Q4: 3-4-5 triangle
Area = 6 cm²

Q5: Arc length ≈ 5 cm

Q6: Cube volume = 64 cm³

SECTION C: CALCULUS

Q7: dy/dx = 12x³ - 4x + 5

Q8: ∫(3x² + 2x + 1)dx = x³ + x² + x + C

SECTION D: STATISTICS

Q9: Mean = 88.6, Standard dev = 2.2
"""
    })
    
    # Paper 4: Satisfactory (68 marks)
    papers.append({
        'student_id': 'STU004',
        'name': 'David Wilson',
        'score': 68,
        'content': """STUDENT ANSWER SHEET
Student ID: STU004
Name: David Wilson
Date: March 28, 2026

SECTION A: ALGEBRA

Q1: 2x² - 8x + 6 = 0
x = 3, x = 1

Q2: x² + 8y - 4

Q3: x = 2.2, y = 2.2

SECTION B: GEOMETRY

Q4: Area = 6

Q5: Arc = 5

SECTION C: CALCULUS

Q7: dy/dx = 12x³ - 4x + 5

Q8: x³ + x² + x + C

SECTION D: STATISTICS

Q9: Mean = 88.6
"""
    })
    
    # Paper 5: Below Average (55 marks)
    papers.append({
        'student_id': 'STU005',
        'name': 'Emma Brown',
        'score': 55,
        'content': """STUDENT ANSWER SHEET
Student ID: STU005
Name: Emma Brown
Date: March 28, 2026

SECTION A: ALGEBRA

Q1: x = 3, 1

Q2: x² + 8y - 4

Q3: x = 2, y = 2

SECTION B: GEOMETRY

Q4: Area = 5

Q5: Arc = 4

SECTION C: CALCULUS

Q7: dy/dx = 12x³ - 4x (missing +5)

Q8: x³ + x² + x
"""
    })
    
    # Papers 6-10: Additional papers with varying scores
    remaining_scores = [82, 72, 91, 64, 76]
    
    for i, score in enumerate(remaining_scores, start=6):
        papers.append({
            'student_id': f'STU{i:03d}',
            'name': f'Student {chr(70+i)}',
            'score': score,
            'content': f"""STUDENT ANSWER SHEET
Student ID: STU{i:03d}
Name: Student {chr(70+i)}
Date: March 28, 2026
Score (Expected): {score}/100

SECTION A: ALGEBRA
Q1: x = 1, 3
Q2: x² + 8y - 4
Q3: x = 2.2, y = 2.2

SECTION B: GEOMETRY
Q4: Area = 6 cm²
Q5: Arc ≈ 5.2 cm
Q6: Volume = 64 cm³

SECTION C: CALCULUS
Q7: dy/dx = 12x³ - 4x + 5
Q8: x³ + x² + x + C

SECTION D: STATISTICS
Q9: Mean = 88.6, Std Dev ≈ 2.2

Note: This is sample answer paper {i} with expected score of {score}/100
"""
        })
    
    return papers

def save_data(marking_scheme, papers):
    """Save marking scheme and papers to files"""
    
    # Create sample_data directory
    data_dir = Path('sample_data')
    data_dir.mkdir(exist_ok=True)
    
    # Save marking scheme
    scheme_file = data_dir / 'marking_scheme.txt'
    with open(scheme_file, 'w', encoding='utf-8') as f:
        f.write(marking_scheme)
    print(f'✓ Marking scheme saved: {scheme_file}')
    
    # Save answer papers
    papers_dir = data_dir / 'answer_papers'
    papers_dir.mkdir(exist_ok=True)
    
    for i, paper in enumerate(papers, 1):
        paper_file = papers_dir / f'paper_{i:02d}_{paper["student_id"]}.txt'
        with open(paper_file, 'w', encoding='utf-8') as f:
            f.write(paper['content'])
        print(f'✓ Paper {i}: {paper_file} (Expected Score: {paper["score"]}/100)')
    
    # Create a summary file
    summary_file = data_dir / 'PAPERS_SUMMARY.txt'
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write('SAMPLE DATA SUMMARY\n')
        f.write('=' * 60 + '\n\n')
        f.write('Marking Scheme: marking_scheme.txt\n\n')
        f.write('Answer Papers (10 total):\n')
        f.write('-' * 60 + '\n')
        for i, paper in enumerate(papers, 1):
            f.write(f'{i:2d}. {paper["name"]:20s} (ID: {paper["student_id"]}) - {paper["score"]:3d}/100\n')
        f.write('\n' + '-' * 60 + '\n')
        f.write('Grade Distribution:\n')
        f.write(f'  A (90-100): {sum(1 for p in papers if p["score"] >= 90)} papers\n')
        f.write(f'  B (80-89):  {sum(1 for p in papers if 80 <= p["score"] < 90)} papers\n')
        f.write(f'  C (70-79):  {sum(1 for p in papers if 70 <= p["score"] < 80)} papers\n')
        f.write(f'  D (60-69):  {sum(1 for p in papers if 60 <= p["score"] < 70)} papers\n')
        f.write(f'  F (<60):    {sum(1 for p in papers if p["score"] < 60)} papers\n')
    
    print(f'✓ Summary saved: {summary_file}')
    
    return data_dir

def main():
    print('=' * 70)
    print('SAMPLE DATA GENERATION FOR ANSWER PAPER EVALUATION SYSTEM')
    print('=' * 70)
    print()
    
    print('Generating marking scheme...')
    marking_scheme = create_marking_scheme()
    
    print('Generating 10 sample answer papers...')
    papers = generate_answer_papers()
    
    print()
    print('Saving files...')
    data_dir = save_data(marking_scheme, papers)
    
    print()
    print('=' * 70)
    print('SUMMARY')
    print('=' * 70)
    print(f'Data saved to: {data_dir.absolute()}')
    print()
    print('Files created:')
    print(f'  - Marking scheme: {data_dir}/marking_scheme.txt')
    print(f'  - Answer papers: {data_dir}/answer_papers/ (10 files)')
    print(f'  - Summary: {data_dir}/PAPERS_SUMMARY.txt')
    print()
    print('Next steps:')
    print('1. Start MongoDB: docker run -d -p 27017:27017 --name mongodb mongo:latest')
    print('2. Install backend packages: cd backend && pip install -r requirements.txt')
    print('3. Install frontend packages: cd frontend && pip install -r requirements.txt')
    print('4. Run backend: python backend/main.py')
    print('5. Run frontend: streamlit run frontend/app.py')
    print('6. Upload marking scheme and answer papers through the web interface')
    print()

if __name__ == '__main__':
    main()
