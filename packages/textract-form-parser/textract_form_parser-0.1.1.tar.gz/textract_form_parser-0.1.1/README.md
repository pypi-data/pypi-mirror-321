# Textract Form Parser

A Python library for parsing and analyzing AWS Textract output from forms, with a focus on structured data extraction and report generation.

## Features

- Extract form fields, tables, and key-value pairs from AWS Textract JSON output
- Generate HTML reports with detailed analysis
- Create both verbose and concise JSON outputs
- Organize outputs in timestamped directories
- Comprehensive logging system
- Support for various form elements:
  - Text fields
  - Checkboxes
  - Tables
  - Key-value pairs
  - Selection elements

## Installation

```bash
pip install textract-form-parser
```

## Quick Start

```python
from textract_parser import analyze_document, generate_html_report

# Load your Textract JSON output
with open('textract_output.json', 'r') as f:
    textract_json = json.load(f)

# Analyze the document
analysis_results = analyze_document(textract_json)

# Generate HTML report
generate_html_report(analysis_results, 'output_report.html')
```

## Detailed Usage

### 1. Document Analysis

```python
from textract_parser import analyze_document

analysis_results = analyze_document(textract_json)
```

The analyzer extracts:
- Form fields and their values
- Tables and their contents
- Key-value pairs
- Geometric relationships between elements
- Confidence scores for each extraction

### 2. Report Generation

```python
from textract_parser import generate_html_report, create_concise_results

# Generate detailed HTML report
generate_html_report(analysis_results, 'report.html')

# Create concise version of results
concise_results = create_concise_results(analysis_results)
```

### 3. Organized Output Structure

The library automatically creates timestamped directories for outputs:
```
logs/
└── Jan_19_2025_1000/
    ├── textract_report.html
    ├── analysis_results_verbose.json
    ├── analysis_results_concise.json
    └── textract.log
```

## Data Structures

### Form Fields
```python
{
    "key": "Field Name",
    "value": "Field Value",
    "confidence": 99.5,
    "geometry": {
        "key_bbox": {...},
        "value_bbox": {...}
    }
}
```

### Tables
```python
{
    "data": [
        [{"text": "Cell Value", "confidence": 99.5}, ...],
        ...
    ],
    "summary": {
        "rows": 5,
        "columns": 3,
        "merged_cells": 2
    }
}
```

## Configuration

### Logging Setup
```python
from textract_parser import setup_textract_logger

logger = setup_textract_logger(
    verbose=False,  # Set to True for debug logging
    log_dir='custom/log/path'
)
```

## Complete Example

```python
from textract_parser import (
    analyze_document,
    generate_html_report,
    setup_textract_logger,
    create_concise_results
)
import json
import os
from datetime import datetime

def create_timestamped_dir():
    """Create a timestamped directory for logs"""
    timestamp = datetime.now().strftime("%b_%d_%Y_%H%M")
    log_dir = os.path.join('logs', timestamp)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    return log_dir

def main():
    try:
        # Create timestamped directory for this run
        log_dir = create_timestamped_dir()
        
        # Set up logger
        logger = setup_textract_logger(verbose=False, log_dir=log_dir)
        
        # Load and analyze document
        with open('notebook.json', 'r') as f:
            textract_json = json.load(f)
        analysis_results = analyze_document(textract_json)
        
        # Generate reports
        report_file = os.path.join(log_dir, 'textract_report.html')
        verbose_json = os.path.join(log_dir, 'analysis_results_verbose.json')
        concise_json = os.path.join(log_dir, 'analysis_results_concise.json')
        
        # Generate outputs
        generate_html_report(analysis_results, report_file)
        
        with open(verbose_json, 'w') as f:
            json.dump(analysis_results, f, indent=2)
        
        concise_results = create_concise_results(analysis_results)
        with open(concise_json, 'w') as f:
            json.dump(concise_results, f, indent=2)

        logger.info(f"Analysis complete. Check the reports in: {log_dir}")

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
```

## Key Components

1. **Document Analyzer**
   - Processes raw Textract JSON
   - Extracts structured data
   - Calculates confidence scores
   - Handles geometric relationships

2. **Report Generator**
   - Creates HTML reports
   - Formats data in tables
   - Includes confidence scores
   - Shows geometric relationships

3. **Data Processors**
   - Key-value pair extraction
   - Table structure analysis
   - Form field identification
   - Selection element detection

## Error Handling

The library includes comprehensive error handling:
```python
try:
    analysis_results = analyze_document(textract_json)
except FileNotFoundError:
    logger.error("JSON file not found")
except json.JSONDecodeError:
    logger.error("Invalid JSON format")
except Exception as e:
    logger.error(f"Unexpected error: {str(e)}")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

