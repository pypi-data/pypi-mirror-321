# Topsis-Shreeya Kesarwani-102203815

A Python package for implementing the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) method.

## Installation

```bash
pip install Topsis-Shreeya-102203815
```

## Usage

The package can be used through command line:

```bash
topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

### Example

```bash
topsis data.xlsx "1,1,1,2,1" "+,+,-,+,+" output.csv
```

### Input Format
* Input file (CSV/Excel) should contain numeric values for all columns except the first one.
* First column is the object/variable name.
* Second to last columns contain numeric values only.

### Parameters
1. `<InputDataFile>`: Input file name including path (csv/xlsx)
2. `<Weights>`: Comma separated weight values for each column
3. `<Impacts>`: Comma separated impacts (+/-) for each column
4. `<ResultFileName>`: Output file name including path

### Output
The output file contains all the columns of input file along with two additional columns having TOPSIS Score and Rank.

## License
MIT License

## Author
Shreeya Kesarwani