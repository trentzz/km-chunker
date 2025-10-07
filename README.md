# km-chunker

A chunker that allows you to run `km find_mutation` with multiple threads in parallel and combines the results.

## Install

```bash
pipx install git+https://github.com/trentzz/km-chunker
```

This may graduate to a pypi repo eventually.

### Prerequisites

- [km](https://github.com/iric-soft/km)
- python >=3.10


This tool calls `km find_mutation` so we need to have [km](https://github.com/iric-soft/km) installed as well.

I would recommend using pipx:

```bash
pipx install km-walk
```

But any of the installation methods should work alright. Keep in mind that this tool requires python 3.10 and above so the python environment should abide by that.

## Usage

Simply pass through the same options you would normally use for `km find_mutation` into `--km-find-mutation-options` and specify the number of threads with `--threads`. `km-chunker` will then:

1. Split the list of targets into however many threads specified
2. Run several instances of km
3. Recombine the km text outputs

> [!IMPORTANT]
> Do not include the normal `> output.txt` at the end of the `km find_mutation` options. Instead specify it with `--output <outputfile>`.

You can also use:

- `--keep` to keep the intermediate outputs for km
- `--working-dir` to specify where the intermediate outputs should be stored, otherwise it will use the current directory. This is recommended to set.

### Examples

```bash
km-chunker \
    --threads 8 \
    --working-dir ./km_outputs \
    --keep \
    --km-find-mutation-options "--ratio 0.0001 --etc etc targets_directory database.jf"
    --output "output.txt"
```
