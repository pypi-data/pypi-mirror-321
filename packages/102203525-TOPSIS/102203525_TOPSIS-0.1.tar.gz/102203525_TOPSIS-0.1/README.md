# 102203525_TOPSIS

`102203525_TOPSIS` is a Python package that implements the TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) method, which is a multi-criteria decision analysis method. This package allows users to calculate TOPSIS scores and ranks for given datasets.

## Installation

You can install the package using pip:

```bash
pip install 102203525_TOPSIS
```

## Command-Line Usage

After installation, you can use the `run-topsis` command to perform the analysis.

### Command Syntax

```bash
run-topsis <input_data_file> <weights> <impacts> <result_file_name>
```

- `<input_data_file>`: Path to the input data file (CSV or Excel).
- `<weights>`: Comma-separated list of weights for each criterion.
- `<impacts>`: Comma-separated list of impacts for each criterion (`+` for beneficial, `-` for non-beneficial).
- `<result_file_name>`: Path to save the result file (CSV or Excel).

### Sample Command

```bash
run-topsis data/input.xlsx "0.4,0.3,0.2,0.1" "+,+,-,+" result/output.xlsx
```

### How It Works

1. **Data Loading**: The script reads the input data from the specified file.
2. **Normalization**: Each column is normalized to make the data comparable.
3. **Weighting**: The normalized data is weighted according to the provided weights.
4. **Ideal Solutions**: Ideal best and worst solutions are determined based on the impacts (`+` or `-`).
5. **Separation Measures**: The distance of each alternative from the ideal best and worst solutions is calculated.
6. **TOPSIS Score**: The relative closeness to the ideal solution is computed.
7. **Ranking**: Alternatives are ranked based on their TOPSIS scores.

## Example

### Input Data (`input.xlsx`):

| Alternative | Criterion 1 | Criterion 2 | Criterion 3 | Criterion 4 |
|-------------|-------------|-------------|-------------|-------------|
| A           | 250         | 16          | 12          | 5           |
| B           | 200         | 20          | 8           | 3           |
| C           | 300         | 11          | 15          | 7           |
| D           | 275         | 15          | 10          | 4           |

### Running the Command:

```bash
run-topsis input.xlsx "0.4,0.3,0.2,0.1" "+,+,-,+" output.xlsx
```

### Result Data (`output.xlsx`):

| Alternative | Criterion 1 | Criterion 2 | Criterion 3 | Criterion 4 | topsis_scores | rank |
|-------------|-------------|-------------|-------------|-------------|---------------|------|
| A           | 250         | 16          | 12          | 5           | 0.691         | 2    |
| B           | 200         | 20          | 8           | 3           | 0.437         | 4    |
| C           | 300         | 11          | 15          | 7           | 0.824         | 1    |
| D           | 275         | 15          | 10          | 4           | 0.620         | 3    |

---

By following the above steps, you can easily perform TOPSIS analysis using the `102203525_TOPSIS` package. For any issues or suggestions, feel free to open an issue on the [GitHub repository](https://github.com/NotLovishGarg/102203525_topsis).
