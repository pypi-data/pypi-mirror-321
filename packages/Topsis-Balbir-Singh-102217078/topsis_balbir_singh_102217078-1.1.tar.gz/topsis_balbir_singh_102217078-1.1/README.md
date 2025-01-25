# Topsis-Balbir-102217078

`Topsis-Balbir-102217078` is a Python package that implements the TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) method for multi-criteria decision making. This tool is ideal for evaluating and ranking alternatives based on multiple criteria, which is essential in fields like supply chain management, finance, and engineering.

## Installation

You can install `Topsis-Balbir-102217078` directly from the Python Package Index using pip:

```bash
pip install Topsis-Balbir-Singh-102217078
```

## Usage

To use Topsis-Balbir-102217078, you will need to prepare your data in a CSV format where the first column contains the names/labels of the alternatives, and the subsequent columns contain the criteria values. The command line interface can be used as follows:

```bash
topsis data.csv "1,2,3" "+,-,+" results.csv
```

Where:
- `data.csv` is your input file.
- `"1,2,3"` is a comma-separated string of weights for each criterion.
- `"+,-,+"` is a comma-separated string of impacts for each criterion, where `+` indicates that higher is better, and `-` that lower is better.
- `results.csv` will be the output file with the TOPSIS scores and rankings.

## Features

- Easy integration with Pandas DataFrames.
- Customizable weights and criteria impacts.
- Automatic normalization and ranking of alternatives.
- Command line interface for easy access and usage.
