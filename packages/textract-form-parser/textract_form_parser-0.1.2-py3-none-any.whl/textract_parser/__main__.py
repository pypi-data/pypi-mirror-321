"""
Command-line interface for Textract Form Parser
"""

import argparse
import json
import os
import sys
from datetime import datetime

from textract_parser import (
    analyze_document,
    create_concise_results,
    generate_html_report,
    setup_textract_logger,
)


def create_parser():
    parser = argparse.ArgumentParser(
        description="Parse AWS Textract form output and generate reports"
    )
    parser.add_argument(
        "input_file",
        help="Input JSON file containing Textract output",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        default="output",
        help="Output directory for reports (default: output)",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose logging",
    )
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    try:
        # Create output directory
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = os.path.join(args.output_dir, timestamp)
        os.makedirs(output_dir, exist_ok=True)

        # Setup logger
        logger = setup_textract_logger(verbose=args.verbose, log_dir=output_dir)

        # Load and analyze document
        with open(args.input_file, "r") as f:
            textract_json = json.load(f)
        analysis_results = analyze_document(textract_json)

        # Generate outputs
        report_file = os.path.join(output_dir, "textract_report.html")
        verbose_json = os.path.join(output_dir, "analysis_results_verbose.json")
        concise_json = os.path.join(output_dir, "analysis_results_concise.json")

        # Generate HTML report
        generate_html_report(analysis_results, report_file)

        # Save verbose JSON
        with open(verbose_json, "w") as f:
            json.dump(analysis_results, f, indent=2)

        # Create and save concise results
        concise_results = create_concise_results(analysis_results)
        with open(concise_json, "w") as f:
            json.dump(concise_results, f, indent=2)

        logger.info(f"Analysis complete. Check the reports in: {output_dir}")
        return 0

    except Exception as e:
        logger.error(f"Error processing document: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
