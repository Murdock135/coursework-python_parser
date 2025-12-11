# Prerequisites

1. antlr4 (or docker-antlr from https://hub.docker.com/r/petervaczi/antlr)
2. [uv](https://docs.astral.sh/uv/)


# Usage (The way I intended)

Create a virtual environment with `uv`.

```sh
uv sync && source .venv/bin/activate
```

Then simply run

```sh
bash scripts/run.sh
```

Then check the outputs in `output/`. The files are designated as follows-

- `output_pd<x>.log` contains the log for each pd aka **p**roject **d**eliverable sample python code (e.g. `output_pd1.log` contains log for `project_deliverable_1.py`)

- `run.log` contains the log for everything, which means
    - output for running the `antlr4 -Dlanguage ...` command
    - the contents of `output_pd<x>.log`

# Usage (if you want to do every step manually)

> [!NOTE] 
> I highly recommend using [Usage (The way I intended)](#usage-the-way-i-intended). Because I've automated whatever you'd be running in this section. You can also read the scripts in `scripts/` and skip reading below. The scripts are very simple.

> [!CAUTION]
> The scripts have only been tested with bash. If you're using a different shell, results may vary. 

> [!WARNING]
> FOLLOW THIS EXACTLY. OTHERWISE THE PROJECT WON'T WORK

## Generating parser

First create a directory to store output logs.

```sh
mkdir output
```

Generate the parser and associated files.

```sh
# Generate parser and store the generated parser into generated/ folder
antlr4 -Dlanguage=Python3 -o generated <.g4 file> 2>&1 | tee "output/parser_generation.log
```

You can also use the docker image in https://hub.docker.com/r/petervaczi/antlr, follow the instructions there and run

```sh
docker-antlr4 -Dlanguage=Python3 -o generated <.g4 file> 2>&1 | tee "output/parser_generation.log
```

The above command should create the `generated/` directory for you. If it doesn't, make the directory and run the command again. 

At this point, you will have generated the parser and the associated code. Read on to test code against this grammar.

## Testing against sample code

The sample code is kept in `test_code/`. If you want to add more sample code files, store the additional code files in this directory.

To test the generated grammar against any sample in `test_code/`, the command is (DO NOT USE THIS. READ BEYOND.)

```sh
uv run -m src.main "<path_to_sample_code>"
```
But in this project, you have to use

```sh
# Test grammar against <path_to_sample_code> and save the output in output/<output_file.log>
uv run -m src.main "<path_to_sample_code" 2>&1 | tee "output/<output_file>.log"
```

This will save results in `output/<output_file>.log`


