# TOPSIS Implementation in Python
A Python implementation of the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) for multi-criteria decision-making problems. This package processes an input dataset, calculates the TOPSIS scores, and ranks alternatives based on their scores.

## Installation
You can install this package directly from PyPI:
```pip install 102203584```

## Usage
### Command-Line Interface
Run the script using the following format:
``` python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName> ```

### Arguments:

1. InputDataFile: Path to the input .csv file containing the dataset.
-The first column should contain the names of the alternatives.
-The remaining columns should contain numeric criteria values.

2. Weights: Comma-separated values representing the importance of each criterion.

3. Impacts: Comma-separated values (+ or -) indicating whether the criterion is beneficial (+) or non-beneficial (-).

4. ResultFileName: Name of the output .csv file where the results (TOPSIS scores and ranks) will be saved

## Dependencies
This package requires the following Python libraries:
-pandas
-numpy

## License
This repository is licensed under the MIT license. See LICENSE for details.