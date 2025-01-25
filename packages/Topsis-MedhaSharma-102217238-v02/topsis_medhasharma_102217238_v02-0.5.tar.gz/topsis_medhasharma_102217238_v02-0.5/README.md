# TOPSIS Package

This is a Python implementation of the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method. It helps evaluate and rank alternatives based on multiple criteria.

---

## Installation

Install the package using pip:

```bash
pip install Topsis-MedhaSharma-102217238

---
```
## Verify Installation

After installation, verify it using:

```bash
pip show Topsis-MedhaSharma-102217238
```
This will show details about the installed package, including its version, dependencies, and other metadata.


## Input File Requirements

File Format: The input file must be a .csv file.

Columns: The first column should contain the names of alternatives (e.g., M1, M2, M3).
          The remaining columns should contain numeric values for criteria.


## Usage
After installation, you can run the program using the command line.

### Syntax:
```bash
python -m topsis <input_file> <weights> <impacts> <result_file>
```

### Example Command:
```bash
python -m topsis data.csv "1,1,2" "+,+,-" result.csv
```

## Output File
The output file will contain:

All columns from the input file.
Two additional columns:
  Topsis Score: The calculated score for each alternative.
  Rank: The rank of each alternative (1 = best).


## Detailed Steps for Beginners
  ### Prepare Your Input File:
  1) Use a spreadsheet program (e.g., Excel) to create a .csv file.
  2) Ensure the first column has names, and the rest have numeric data.

  ### Run the Command:
  1) Open the terminal in the directory where your input file is located.
  2) Run the TOPSIS command as explained above.
     
  ### View the Results:
  Open the output file (result.csv) in any spreadsheet program.


## Common Issues

  ### I don't have Python installed:
  Download Python from python.org and install it.
  
  ### I get a ModuleNotFoundError:
  Ensure the package is installed using pip install.
  
  ### I see unexpected results:
  1) Double-check the weights and impacts.
  2) Ensure all criteria values are numeric.


