#!/usr/bin/env python3
"""
Convert sample data text files to PDF format for upload
"""

from pathlib import Path
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import textwrap

def text_to_pdf(text_file, pdf_file, title=None):
    """Convert text file to PDF"""
    
    # Read text file
    with open(text_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create PDF document
    doc = SimpleDocTemplate(
        str(pdf_file),
        pagesize=letter,
        rightMargin=0.5*inch,
        leftMargin=0.5*inch,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch
    )
    
    # Container for PDF content
    elements = []
    
    # Create styles
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=14,
        textColor=colors.HexColor('#1f77d4'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=11,
        textColor=colors.HexColor('#2ca02c'),
        spaceAfter=6,
        spaceBefore=6,
        fontName='Helvetica-Bold'
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=9,
        alignment=TA_LEFT,
        fontName='Courier',
        spaceAfter=3
    )
    
    # Parse content
    lines = content.split('\n')
    
    for line in lines:
        line = line.rstrip()
        
        if not line:
            elements.append(Spacer(1, 0.05*inch))
        elif line.startswith('# '):
            # Main title
            elements.append(Paragraph(line[2:], title_style))
            elements.append(Spacer(1, 0.1*inch))
        elif line.startswith('## '):
            # Section heading
            elements.append(Spacer(1, 0.05*inch))
            elements.append(Paragraph(line[3:], heading_style))
            elements.append(Spacer(1, 0.05*inch))
        elif line.startswith('='):
            # Separator
            elements.append(Spacer(1, 0.08*inch))
        else:
            # Normal text
            # Handle long lines by wrapping
            if len(line) > 90:
                # Wrap long lines
                for wrapped_line in textwrap.wrap(line, width=90):
                    elements.append(Paragraph(wrapped_line, normal_style))
            else:
                elements.append(Paragraph(line, normal_style))
    
    # Build PDF
    doc.build(elements)
    print(f'✓ PDF created: {pdf_file}')

def convert_all_samples():
    """Convert all sample files to PDF"""
    
    sample_data_dir = Path('sample_data')
    
    # Convert marking scheme
    marking_txt = sample_data_dir / 'marking_scheme.txt'
    marking_pdf = sample_data_dir / 'marking_scheme.pdf'
    
    if marking_txt.exists():
        text_to_pdf(marking_txt, marking_pdf, 'Marking Scheme')
    
    # Convert answer papers
    papers_dir = sample_data_dir / 'answer_papers'
    pdf_dir = sample_data_dir / 'answer_papers_pdf'
    pdf_dir.mkdir(exist_ok=True)
    
    for txt_file in sorted(papers_dir.glob('*.txt')):
        pdf_file = pdf_dir / (txt_file.stem + '.pdf')
        text_to_pdf(txt_file, pdf_file)
    
    print(f'\n✓ Marking scheme PDF: {marking_pdf}')
    print(f'✓ Answer papers PDFs: {pdf_dir}/')
    
    return sample_data_dir

def main():
    print('=' * 70)
    print('CONVERTING SAMPLE DATA TO PDF FORMAT')
    print('=' * 70)
    print()
    
    convert_all_samples()
    
    print()
    print('=' * 70)
    print('CONVERSION COMPLETE')
    print('=' * 70)
    print()
    print('Files ready for upload:')
    print('  - Marking Scheme: sample_data/marking_scheme.pdf')
    print('  - Answer Papers: sample_data/answer_papers_pdf/*.pdf')
    print()
    print('Upload steps:')
    print('1. Go to Streamlit app interface')
    print('2. Upload marking scheme PDF')
    print('3. Upload all answer paper PDFs (10 files)')
    print('4. Click Evaluate')
    print()

if __name__ == '__main__':
    main()
