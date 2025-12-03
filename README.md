# Prerequisites

antlr4 and a runtime for antlr needs to be installed. Refer to https://www.antlr.org/download.html for instructions on installing these. Alternatively, you can simply pull the docker image: https://hub.docker.com/r/petervaczi/antlr. This image has the required packages for using antlr4.

# Running a grammar file

A grammar file is named <grammar_name>.g4, same as the name of the grammar. The most basic command to create a lexer and parser for the grammar is the following- 

```sh
antlr4 -Dlanguage=Python3 <.g4 file>
```

You can also use the docker image in https://hub.docker.com/r/petervaczi/antlr, follow the instructions there and run

```sh
docker-antlr -Dlanguage=Python3 <.g4 file>
```