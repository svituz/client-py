#!/bin/bash
PARSER_DIR=./fhir-parser
if [ ! -e fhir-parser ]; then
	git submodule update --init --recursive
fi
cp fhir-parser-resources/settings.py $PARSER_DIR/settings.py
cd $PARSER_DIR || exit
./generate.py $1
cd - || exit
