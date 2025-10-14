#!/usr/bin/env python3
"""
kmtools: A toolkit for running, filtering, merging, and plotting km find_mutation results.
"""

import argparse
from kmtools.chunk import Chunk
from kmtools.filter import Filter
from kmtools.merge import Merge
from kmtools.plot import Plot
from kmtools.utils import Utils


# === Subcommand Functions ===


def run_chunk(args):
    Utils.log(f"Running chunk with args: {args}", args.verbose)
    Chunk(
        threads=args.threads,
        km_find_mutation_options=args.km_find_mutation_options,
        merge=args.merge,
        verbose=args.verbose,
    ).run()


def run_filter(args):
    Utils.log(f"Running filter with args: {args}", args.verbose)
    Filter(
        reference=args.reference,
        km_output=args.km_output,
        output=args.output,
        verbose=args.verbose,
    ).run()


def run_merge(args):
    Utils.log(f"Running merge with args: {args}", args.verbose)
    Merge(inputs=args.inputs, output=args.output, verbose=args.verbose).run()


def run_plot(args):
    Utils.log(f"Running plot with args: {args}", args.verbose)
    Plot(
        file=args.file,
        output_dir=args.output_dir,
        charts=args.charts,
        verbose=args.verbose,
    ).run()


def run_all(args):
    """
    Runs the entire workflow:
    1. chunk
    2. merge
    3. filter
    4. plot
    """
    Utils.log(
        "Running full kmtools pipeline (chunk -> merge -> filter -> plot)", args.verbose
    )

    # --- Step 1: Chunk ---
    chunk = Chunk(
        threads=args.threads,
        km_find_mutation_options=args.km_find_mutation_options,
        merge=True,  # runall always merges
        verbose=args.verbose,
    )
    chunk.run()

    # --- Step 2: Merge ---
    merge = Merge(
        inputs=args.merge_inputs, output=args.merge_output, verbose=args.verbose
    )
    merge.run()

    # --- Step 3: Filter ---
    filter_step = Filter(
        reference=args.reference,
        km_output=args.merge_output,
        output=args.filtered_output,
        verbose=args.verbose,
    )
    filter_step.run()

    # --- Step 4: Plot ---
    plot = Plot(
        file=args.filtered_output,
        output_dir=args.output_dir,
        charts=args.charts,
        verbose=args.verbose,
    )
    plot.run()

    Utils.log("Pipeline complete.", args.verbose)


# === CLI Setup ===


def main():
    parser = argparse.ArgumentParser(
        prog="kmtools",
        description="kmtools: run, filter, merge, and plot km find_mutation results.",
    )

    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    subparsers = parser.add_subparsers(
        title="subcommands", dest="command", required=True
    )

    # --- chunk ---
    chunk_parser = subparsers.add_parser("chunk", help="Chunk input data")
    chunk_parser.add_argument(
        "--threads", type=int, required=True, help="Number of threads to use"
    )
    chunk_parser.add_argument(
        "--km-find-mutation-options",
        type=str,
        required=True,
        help="Options for km-find-mutation",
    )
    chunk_parser.add_argument(
        "--merge", action="store_true", help="Merge chunks after processing"
    )
    chunk_parser.set_defaults(func=run_chunk)

    # --- merge ---
    merge_parser = subparsers.add_parser("merge", help="Merge data")
    merge_parser.add_argument(
        "inputs", nargs="+", type=str, help="Input files or directories to merge"
    )
    merge_parser.add_argument(
        "--output", type=str, required=True, help="Merged output file"
    )
    merge_parser.set_defaults(func=run_merge)

    # --- filter ---
    filter_parser = subparsers.add_parser("filter", help="Filter data")
    filter_parser.add_argument(
        "--reference", type=str, required=True, help="Reference file"
    )
    filter_parser.add_argument(
        "--km-output", type=str, required=True, help="KM output file"
    )
    filter_parser.add_argument(
        "--output", type=str, required=True, help="Filtered output file"
    )
    filter_parser.set_defaults(func=run_filter)

    # --- plot ---
    plot_parser = subparsers.add_parser("plot", help="Plot results")
    plot_parser.add_argument("file", type=str, help="Filtered result file to plot")
    plot_parser.add_argument(
        "--output-dir", type=str, default=".", help="Directory to save plots"
    )
    plot_parser.add_argument(
        "--charts",
        type=str,
        default="all",
        help='Comma-separated list of charts to generate (default: "all")',
    )
    plot_parser.set_defaults(func=run_plot)

    # --- runall ---
    runall_parser = subparsers.add_parser(
        "runall", help="Run full pipeline: chunk -> merge -> filter -> plot"
    )
    runall_parser.add_argument(
        "--threads", type=int, required=True, help="Number of threads for chunking"
    )
    runall_parser.add_argument(
        "--km-find-mutation-options",
        type=str,
        required=True,
        help="Options for km-find-mutation",
    )

    # Merge step
    runall_parser.add_argument(
        "--merge-inputs",
        nargs="+",
        required=True,
        help="Files or directories to merge after chunking",
    )
    runall_parser.add_argument(
        "--merge-output", type=str, required=True, help="Output file for merged data"
    )

    # Filter step
    runall_parser.add_argument(
        "--reference", type=str, required=True, help="Reference FASTA file"
    )
    runall_parser.add_argument(
        "--filtered-output",
        type=str,
        required=True,
        help="Output file for filtered results",
    )

    # Plot step
    runall_parser.add_argument(
        "--output-dir", type=str, default=".", help="Directory to save plots"
    )
    runall_parser.add_argument(
        "--charts",
        type=str,
        default="all",
        help='Comma-separated list of charts to generate (default: "all")',
    )

    runall_parser.set_defaults(func=run_all)

    # --- parse and dispatch ---
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
