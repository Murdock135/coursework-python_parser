# Prerequisites

1. antlr4 (or docker-antlr from https://hub.docker.com/r/petervaczi/antlr)
2. [uv](https://docs.astral.sh/uv/)
3. [graphviz](https://github.com/graphp/graphviz?tab=readme-ov-file#install) 


# Usage (The way I intended)

This project will create a grammar and the corresponding ANTLR parser code and finally test the grammar against sample python code in `test_code/`. Some files already exist in the directory. When you run the project, only those will be used to test the grammar. If you wish to use other sample code to test the grammar against, read [Usage (if you want to do every step manually)](#usage-if-you-want-to-do-every-step-manually)

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
> I highly recommend using [Usage (The way I intended)](#usage-the-way-i-intended) if you only want to test the grammar against the existing sample code. Otherwise, read on. You can also read the scripts in `scripts/` and skip reading below. The scripts are very simple.

>[!NOTE]
> The below commands are simply my opinionated suggestions. I believe running the below commands is more convenient than running their baser counterparts manually.

> [!CAUTION]
> The scripts have only been tested with bash. If you're using a different shell, results may vary. 


## Generating parser



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

The sample code is kept in `test_code/`. If you want to add more sample code files, you can store the additional code files in this directory.

Before testing, create and initialize a virtual environment with `uv`.

```sh
uv sync && source .venv/bin/activate
```

To test the generated grammar against any sample in `test_code/`, the command is

```sh
uv run -m src.main "<path_to_sample_code>"
```
It may be better to store the output somewhere. To do so, create the output directory first.

```sh
mkdir output
```

Then test.

```sh
# Test grammar against <path_to_sample_code> and save the output in output/<output_file.log>
uv run -m src.main "<path_to_sample_code" 2>&1 | tee "output/<output_file>.log"
```

This will save results in `output/<output_file>.log`


