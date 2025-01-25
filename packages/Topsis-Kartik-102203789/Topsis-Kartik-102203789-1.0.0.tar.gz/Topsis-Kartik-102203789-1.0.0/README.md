# Topsis-KartikSidana-102203789

A Python implementation for Multi-Criteria Decision Making (MCDM) using the TOPSIS method (Technique for Order of Preference by Similarity to Ideal Solution). This package helps decision makers evaluate alternatives based on multiple criteria with different weights and impacts.

## Installation

To install the package, run:
bash
pip install Topsis-KartikSidana-102203789


## Usage

Execute the package through command line:
bash
topsis <input_file> <weights> <impacts> <output_file>


Example:
bash
topsis data.xlsx "1,1,1,1,1" "+,+,+,+,+" output.csv


## Input Requirements

- Input file (CSV/Excel) must contain numeric values except for the first column
- First column should contain the names of alternatives
- All other columns should contain numerical data
- At least 3 columns required for meaningful results

## Parameters

1. <input_file>: Path to your dataset file (supports .csv and .xlsx)
2. <weights>: Weighted importance of each criterion (comma-separated numbers)
3. <impacts>: Nature of each criterion (comma-separated '+' or '-')
   - '+' indicates benefit criterion (higher values desired)
   - '-' indicates cost criterion (lower values desired)
4. <output_file>: Name of file to store results

## Output Format

The output file includes:
- All columns from input file
- TOPSIS Score: Calculated similarity to ideal solution
- Rank: Position of each alternative based on TOPSIS score

## Error Handling

The package includes robust error checking for:
- Incorrect number of weights or impacts
- Invalid file formats
- Non-numeric values in criteria columns
- Missing or incomplete data

## License
MIT License

## Author
Kartik Sidana
Roll Number: 102203789
