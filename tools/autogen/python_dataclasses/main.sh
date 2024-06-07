#!/bin/bash

# Check if the correct number of arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <input_path> <output_path>"
    exit 1
fi

# Assign input and output paths to variables
input_path=$1
output_path=$2

# Check if the input file exists
if [ ! -f "$input_path" ]; then
    echo "Error: Input file '$input_path' not found."
    exit 1
fi

# Install datamodel-codegen if not already installed
if ! command -v datamodel-codegen &> /dev/null; then
    echo "Installing datamodel-codegen..."
    pip3 install datamodel-codegen
fi

# Run datamodel-codegen with the specified input and output paths
datamodel-codegen --input "$input_path" --input-file-type jsonschema --output "$output_path"
