## Project description
# MCDM solution using TOPSIS using CLI
A Python package made by me to solve the problem of MCDM (Multi Criteria Decision Making) implemented using TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) algorithm. 
This package supports both CSV and Excel files.

### Installation

Follow the steps below to install and use the package:

Install the Package from PyPI (recommended):

`pip install 102203092_topsis`

Repo Clone (optional):

`git clone`

`cd TOPSIS-pypi`

(Optional) Install Locally: If you have the source code and want to install the package locally:

`pip install setuptools wheel`

`python setup.py sdist bdist_wheel`

`pip install .`

| Argument   | Description                         |
|------------|-------------------------------------|
| input_file | "CSV/Excel" file path              |
| weights`   | Comma-separated numbers            |
| impacts  | Comma-separated '+' or '-'         |
| output_file | Output CSV/Excel file path         |


### Usage
1. After installation, you can use the package directly from the command line using topsis-cli.
2. The CLI supports both .csv and .xlsx formats for input and output files.
3. Command-Line Interface (CLI)
4. Package installed from PyPi can be globally used irrespective of directory

`topsis-cli <input_file> <weights> <impacts> <output_file>`

### Args:
1. **input_file:** Path to the input file (must be .csv or .xlsx).
2. **weights:** Comma-separated list of weights for the criteria (e.g., 0.4,0.3,0.3).
3. **impacts:** Comma-separated list of impacts for the criteria (+ for positive, - for negative).
4. **output_file:** Path to save the output file (can be .csv or .xlsx).

### Input File Format

| Col 1       | Col 2             | Col 3           |
|-------------|-------------------|-----------------|
| Alternte ID | Criterion 1 Value | Criterion 2 Value |


### Output File Format

| Col 1       | Col 2            | Col 3             | Col 4          | Col 5       |
|-------------|------------------|-------------------|----------------|------------|
| Alternate ID| Criterion 1 Value | V2                | Topsis Score   | Rank       |
              
**_Uday Sharma_**

**_102203092_**