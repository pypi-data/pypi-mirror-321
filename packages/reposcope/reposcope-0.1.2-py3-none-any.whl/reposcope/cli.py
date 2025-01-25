#!/usr/bin/env python3
import argparse
import logging
import sys
from reposcope.core import RepoScope

def setup_logging(verbose: bool):
    """Configure logging based on verbosity level."""
    level = logging.DEBUG if verbose else logging.WARNING
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    )

def main():
    parser = argparse.ArgumentParser(
        description="RepoScope - Generate repository context files for LLMs"
    )
    parser.add_argument(
        "--dir", 
        default=".",
        help="Root directory of the repository (default: current directory)"
    )
    parser.add_argument(
        "--output",
        default="context.txt",
        help="Output file path (default: context.txt)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output"
    )

    # Ignore-based selection options
    ignore_group = parser.add_argument_group('Ignore-based selection')
    ignore_group.add_argument(
        "--use-gitignore",
        action="store_true",
        help="Use patterns from .gitignore file"
    )
    ignore_group.add_argument(
        "--ignore-file",
        help="Use patterns from specified ignore file"
    )
    ignore_group.add_argument(
        "--ignore",
        nargs="*",
        help="Specify ignore patterns directly"
    )

    # Include-based selection options
    include_group = parser.add_argument_group('Include-based selection')
    include_group.add_argument(
        "--include-file",
        help="Use patterns from specified include file"
    )
    include_group.add_argument(
        "--include",
        nargs="*",
        help="Specify include patterns directly"
    )

    args = parser.parse_args()
    
    # Setup logging
    setup_logging(args.verbose)
    logger = logging.getLogger(__name__)

    # Check for mixing of modes
    has_include = bool(args.include_file or args.include)
    has_ignore = bool(args.use_gitignore or args.ignore_file or args.ignore)
    
    if has_include and has_ignore:
        logger.warning("Both ignore and include options specified. Include patterns will take precedence.")

    # Create RepoScope instance
    try:
        scope = RepoScope(args.dir)

        # Check if we're in include mode
        if has_include:
            if args.include_file:
                scope.use_include_file(args.include_file)
            if args.include:
                scope.use_include_patterns(args.include)
        else:
            # Ignore mode - apply specified ignore patterns
            if args.use_gitignore:
                scope.use_gitignore()
            if args.ignore_file:
                scope.use_ignore_file(args.ignore_file)
            if args.ignore:
                scope.use_ignore_patterns(args.ignore)

        scope.generate_context_file(args.output)
        print(f"Generated context file: {args.output}")
        
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()