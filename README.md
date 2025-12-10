# Prerequisites

TLDR for the impatient: Install these two packages
1. antlr4
2. uv (yes, this is required.)

antlr4 and a runtime for antlr needs to be installed. Refer to https://www.antlr.org/download.html for instructions on installing these. Alternatively, you can simply pull the docker image: https://hub.docker.com/r/petervaczi/antlr. This image has the required packages for using antlr4.

# Usage (The way I intended)

Simply run

```sh
bash scripts/run.sh
```

Then check the outputs in `output/`. The files are designated as follows-

- `output_pd<x>.log` contains the log for each pd aka **p**roject **d**eliverable sample python code (e.g. `output_pd1.log` contains log for `project_deliverable_1.py`)

- `run.log` contains the log for everything, which means
    - output for running the `antlr4 -Dlanguage ...` command
    - the contents of `output_pd<x>.log`

# Usage (if you want to do every step manually)

> Note: I highly recommend using [Usage (The way I intended)](#usage-the-way-i-intended). Because I've automated whatever you'd be running in this section :)

>Note: FOLLOW THIS EXACTLY. OTHERWISE THE PROJECT WON'T WORK


A grammar file is named <grammar_name>.g4, same as the name of the grammar. The most basic command to create a lexer and parser for the grammar is the following- 

```sh
antlr4 -Dlanguage=Python3 <.g4 file>
```

You can also use the docker image in https://hub.docker.com/r/petervaczi/antlr, follow the instructions there and run

```sh
docker-antlr -Dlanguage=Python3 <.g4 file>
```

