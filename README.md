# kmtools

A collection of utilities extending the functionality of [`km`](https://github.com/iric-soft/km), providing parallelisation, filtering, merging, and plotting of `km find_mutation` results.

`kmtools` is designed to streamline large-scale `km` workflows by allowing you to:

- Run `km find_mutation` across multiple threads via target sequence chunking
- Merge and filter results
- Generate summary plots for downstream analysis

---

## Installation

### Using pipx (recommended)

```bash
pipx install git+https://github.com/trentzz/kmtools
````

This tool may eventually be published to PyPI.
Using `pipx` is recommended to isolate `kmtools` from your system Python environment.

### Prerequisites

- Python ≥ 3.10
- [`km`](https://github.com/iric-soft/km) must be installed and accessible in your `PATH`.

To install `km` via `pipx`:

```bash
pipx install km-walk
```

Any of the installation methods listed in the `km` documentation will also work.

---

## Overview of Commands

| Command          | Description                                                                              |
| ---------------- | ---------------------------------------------------------------------------------------- |
| `kmtools chunk`  | Run multiple instances of `km find_mutation` in parallel using target sequence chunking. |
| `kmtools merge`  | Merge multiple `km` outputs into a combined result.                                      |
| `kmtools filter` | Filter `km` results based on a reference or other criteria.                              |
| `kmtools plot`   | Generate visualisations from filtered results.                                           |
| `kmtools runall` | Run the full pipeline (`chunk → merge → filter → plot`) automatically.                   |

---

## Usage

### `kmtools chunk`

Run `km find_mutation` concurrently across multiple threads by splitting target sequences.

```bash
kmtools chunk \
    --threads 8 \
    --km-find-mutation-options "--ratio 0.0001 targets_dir database.jf" \
    --merge \
    --verbose
```

### Arguments

| Argument                     | Description                                                                                 |
| ---------------------------- | ------------------------------------------------------------------------------------------- |
| `--threads`                  | Number of threads (parallel `km` processes).                                                |
| `--km-find-mutation-options` | Options passed directly to `km find_mutation`. Do **not** include output redirection (`>`). |
| `--merge`                    | Merge chunked results automatically after processing.                                       |
| `--verbose`                  | Enable detailed logging and timing information.                                             |

#### Process

1. Splits the list of target sequences into chunks (one per thread).
2. Runs `km find_mutation` on each chunk in parallel.
3. Optionally merges all results when complete.

---

### `kmtools merge`

Combine multiple chunk outputs into a single result file.

```bash
kmtools merge \
    chunk_*/results.txt \
    --output merged.txt \
    --verbose
```

### Arguments

| Argument    | Description                          |
| ----------- | ------------------------------------ |
| `inputs`    | Input files or directories to merge. |
| `--output`  | Output file for merged data.         |
| `--verbose` | Enable detailed logging.             |

This is typically used after chunking to combine partial `km` results.

---

### `kmtools filter`

Filter `km` output based on a reference sequence or other logic.

```bash
kmtools filter \
    --reference ref.fa \
    --km-output merged.txt \
    --output filtered.txt \
    --verbose
```

### Arguments

| Argument      | Description                       |
| ------------- | --------------------------------- |
| `--reference` | Reference FASTA file.             |
| `--km-output` | Input `km` output file to filter. |
| `--output`    | Output file for filtered results. |
| `--verbose`   | Enable detailed logging.          |

This step removes false positives or unwanted variants.

---

### `kmtools plot`

Generate plots and summary charts from filtered results.

```bash
kmtools plot \
    filtered.txt \
    --output-dir plots \
    --charts vaf,patient,sample \
    --verbose
```

### Arguments

| Argument       | Description                                                                                   |
| -------------- | --------------------------------------------------------------------------------------------- |
| `file`         | Filtered results file.                                                                        |
| `--output-dir` | Directory to save plots (default: current directory).                                         |
| `--charts`     | Comma-separated list of charts to generate (`vaf`, `patient`, `sample`, `overall`, or `all`). |
| `--verbose`    | Enable detailed logging.                                                                      |

Example outputs include:

- `vaf_distribution.png`
- `patient_summary.png`
- `sample_overview.png`

---

### `kmtools runall`

Run the full workflow — `chunk → merge → filter → plot` — in a single command.

```bash
kmtools runall \
    --threads 8 \
    --km-find-mutation-options "--ratio 0.0001 targets_dir database.jf" \
    --merge-inputs chunk_*/results.txt \
    --merge-output merged.txt \
    --reference ref.fa \
    --filtered-output filtered.txt \
    --output-dir plots \
    --charts all \
    --verbose
```

### Arguments

| Argument                     | Description                                     |
| ---------------------------- | ----------------------------------------------- |
| `--threads`                  | Number of threads for chunking.                 |
| `--km-find-mutation-options` | Options for `km find_mutation`.                 |
| `--merge-inputs`             | Files or directories to merge after chunking.   |
| `--merge-output`             | Output file for merged data.                    |
| `--reference`                | Reference file for filtering.                   |
| `--filtered-output`          | Output file for filtered results.               |
| `--output-dir`               | Directory for plots.                            |
| `--charts`                   | Charts to generate (default: `all`).            |
| `--verbose`                  | Enable detailed logging and timing information. |

### Workflow

1. Splits and runs `km find_mutation` in parallel.
2. Merges chunk results.
3. Filters merged results using the provided reference.
4. Generates plots and summaries.

---

## Notes and Best Practices

- Always test your `--km-find-mutation-options` with a single `km find_mutation` run before using `kmtools chunk` or `runall`.
- Use `--working-dir` (if supported) to isolate intermediate outputs.
- Maintain a consistent output naming scheme to simplify automated merging.
- Use `--verbose` for debugging and benchmarking; it reports timing and process details.

---

## Example Full Workflow

```bash
kmtools runall \
  --threads 8 \
  --km-find-mutation-options "--ratio 0.0001 targets_dir database.jf" \
  --merge-inputs chunk_*/results.txt \
  --merge-output merged.txt \
  --reference ref.fa \
  --filtered-output filtered.txt \
  --output-dir plots \
  --charts all \
  --verbose
```

---

## Project Structure

```text
kmtools/
├── __init__.py
├── cli.py           # Entry point for all subcommands
├── chunk.py         # Handles kmtools chunk
├── merge.py         # Handles kmtools merge
├── filter.py        # Handles kmtools filter
├── plot.py          # Handles kmtools plot
└── utils.py         # Shared utilities (logging, validation, etc.)
```

---

## Future Plans

- Automatic detection of chunk outputs in `runall`
- Multiprocessing backend for chunking
- Extended filtering and visualisation modules
- Support for JSON and TSV output formats

