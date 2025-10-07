import argparse

def cli():
    parser = argparse.ArgumentParser(
        description="KM Chunker CLI Tool"
    )
    parser.add_argument(
        "--threads", type=int, required=True,
        help="Number of threads to use"
    )
    parser.add_argument(
        "--km-find-mutation-options", type=str, required=True,
        help="Options for km-find-mutation"
    )
    args = parser.parse_args()

    # Your main logic here
    print(f"Input file: {args.input}")
    print(f"Output file: {args.output}")

if __name__ == "__main__":
    cli()