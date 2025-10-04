#!/usr/bin/env python3
"""
Command-line interface for CSV to QLab

This module provides a CLI for sending CSV files to QLab without the GUI.
"""

import sys
import argparse
import json
import io
from pathlib import Path

from .csv_parser import send_csv
from .error_success_handler import ErrorHandler


class FileStorageAdapter:
    """Adapter to make a file object compatible with Flask's FileStorage interface"""

    def __init__(self, file_path):
        self.file_path = Path(file_path)
        with open(self.file_path, 'rb') as f:
            self.stream = io.BytesIO(f.read())


def format_human_readable(error_handler):
    """Format errors and successes in human-readable format"""
    output = []

    errors = error_handler.get_errors()
    successes = error_handler.get_success()

    if successes:
        output.append(f"✓ Successfully processed {len(successes)} cue(s)")

    if errors:
        output.append(f"\n✗ Encountered {len(errors)} error(s):")
        for error in errors:
            output.append(f"  - {error['status']}: {error['message']}")

    return "\n".join(output) if output else "No cues processed"


def format_json(error_handler):
    """Format errors and successes as JSON"""
    return json.dumps({
        "success": error_handler.get_success(),
        "errors": error_handler.get_errors(),
        "has_errors": error_handler.has_errors()
    }, indent=2)


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Send CSV files to QLab via OSC",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage
  csv-to-qlab show.csv 127.0.0.1 5

  # With passcode
  csv-to-qlab show.csv 192.168.1.100 5 --passcode 1234

  # Quiet output (errors only)
  csv-to-qlab show.csv 127.0.0.1 5 --quiet

  # JSON output for scripting
  csv-to-qlab show.csv 127.0.0.1 5 --json
        """
    )

    parser.add_argument(
        'csv_file',
        type=str,
        help='Path to CSV file containing cue data'
    )

    parser.add_argument(
        'ip',
        type=str,
        help='IP address of QLab machine (e.g., 127.0.0.1)'
    )

    parser.add_argument(
        'qlab_version',
        type=int,
        choices=[4, 5],
        help='QLab version (4 or 5)'
    )

    parser.add_argument(
        '-p', '--passcode',
        type=str,
        default='',
        help='QLab workspace passcode (optional)'
    )

    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )

    parser.add_argument(
        '-q', '--quiet',
        action='store_true',
        help='Suppress success messages, only show errors'
    )

    parser.add_argument(
        '-j', '--json',
        action='store_true',
        help='Output results in JSON format'
    )

    args = parser.parse_args()

    # Validate CSV file exists
    csv_path = Path(args.csv_file)
    if not csv_path.exists():
        print(f"Error: CSV file not found: {args.csv_file}", file=sys.stderr)
        return 1

    if not csv_path.is_file():
        print(f"Error: Path is not a file: {args.csv_file}", file=sys.stderr)
        return 1

    # Create error handler
    error_handler = ErrorHandler()

    # Suppress print statements in error handler for quiet/json mode
    if args.quiet or args.json:
        error_handler.handle_errors = lambda status, message: error_handler.errors.append({
            "status": status,
            "message": message
        })

    try:
        # Create file adapter
        document = FileStorageAdapter(args.csv_file)

        if args.verbose and not args.json:
            print(f"Sending CSV file: {args.csv_file}")
            print(f"QLab IP: {args.ip}")
            print(f"QLab version: {args.qlab_version}")
            if args.passcode:
                print(f"Using passcode: {'*' * len(args.passcode)}")
            print()

        # Send CSV to QLab
        send_csv(
            ip=args.ip,
            document=document,
            qlab_version=args.qlab_version,
            passcode=args.passcode,
            error_handler=error_handler
        )

        # Output results
        if args.json:
            print(format_json(error_handler))
        elif not args.quiet:
            output = format_human_readable(error_handler)
            if output:
                print(output)

        # Return exit code based on errors
        return 1 if error_handler.has_errors() else 0

    except FileNotFoundError as e:
        error_msg = f"Error: File not found: {e}"
        if args.json:
            print(json.dumps({"error": error_msg, "success": [], "errors": []}))
        else:
            print(error_msg, file=sys.stderr)
        return 1

    except Exception as e:
        error_msg = f"Error: {str(e)}"
        if args.json:
            print(json.dumps({"error": error_msg, "success": [], "errors": []}))
        else:
            print(error_msg, file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
