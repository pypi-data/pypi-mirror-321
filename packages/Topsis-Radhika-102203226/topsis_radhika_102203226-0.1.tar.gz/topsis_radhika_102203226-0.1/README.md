Here’s a completely rewritten version of your README.md, tailored for your project:

---

# TOPSIS-RADHIKA-102203226

*A Python package to implement the TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) decision-making method.*

---

## 📘 Overview

TOPSIS is a widely used multi-criteria decision analysis technique. It ranks alternatives by comparing their relative distance to an ideal (best) solution and a nadir (worst) solution. This package streamlines the process, enabling users to compute ranks easily by specifying their criteria, weights, and impacts.

---

## 🛠️ Installation

### Install via PyPI:
Run the following command to install the package directly:
```bash
pip install topsis-Radhika-102203226
```

### Manual Installation:
Clone the repository and install required dependencies:
```bash
git clone https://github.com/radhikaaggarwal1509/topsis-Radhika-102203226.git
cd topsis-Radhika-102203226
pip install -r requirements.txt
```

---

## 🚀 Usage Instructions

Run the script through the command line with the following syntax:

```bash
python <program.py> <InputFile> "<Weights>" "<Impacts>" <OutputFile>
```

### Example Command:
```bash
python 102203226.py data.csv "1,2,3,1" "+,-,+,-" result.csv
```

### Parameters:
1. **`<InputFile>`**: Path to the CSV file containing the input data.
2. **`<Weights>`**: A string of comma-separated weights (e.g., `"1,2,3,1"`).
3. **`<Impacts>`**: A string of comma-separated impacts, using `+` for beneficial and `-` for non-beneficial criteria (e.g., `"+,-,+,-"`).
4. **`<OutputFile>`**: Path where the output file (ranked alternatives) will be saved.

---

## 🗂️ Input Data Format

- **File Type:** CSV (.csv) with the following structure:
  - The first column contains alternative names (e.g., A1, A2).
  - All other columns should contain numeric values representing criteria.

### Example Input File (`data.csv`):
| Alternative | Criterion 1 | Criterion 2 | Criterion 3 | Criterion 4 |
|-------------|-------------|-------------|-------------|-------------|
| A1          | 70          | 60          | 50          | 80          |
| A2          | 85          | 55          | 45          | 90          |

---

## 📊 Output Data Format

The output file is a CSV that includes the input data along with two additional columns:
1. **Topsis Score**: Numerical score reflecting proximity to the ideal solution.
2. **Rank**: Rank of the alternatives based on the score.

### Example Output File (`result.csv`):
| Alternative | Criterion 1 | Criterion 2 | Criterion 3 | Criterion 4 | Topsis Score | Rank |
|-------------|-------------|-------------|-------------|-------------|--------------|------|
| A1          | 70          | 60          | 50          | 80          | 0.75         | 2    |
| A2          | 85          | 55          | 45          | 90          | 0.89         | 1    |

---

## 🌟 Features

- **Error Validation**: Ensures correct input file formatting, numeric-only criteria, and matching weights/impacts.
- **Customizable Weights and Impacts**: Specify your own preferences for criteria.
- **Simple CLI Usage**: User-friendly command-line interface for quick execution.
- **Robust Ranking**: Provides reliable and interpretable rankings.

---

## ✅ Requirements

- **Python Version**: Python 3.6 or later
- **Dependencies**:
  - pandas
  - numpy

Install dependencies manually:
```bash
pip install -r requirements.txt
```

---

## 📖 References

- [Wikipedia: TOPSIS](https://en.wikipedia.org/wiki/TOPSIS)
- [Guide to Publishing Python Packages on PyPI](https://realpython.com/pypi-publish-python-package/)

---

## ✨ Author Information

- **Name**: Radhika Aggarwal  
- **Roll Number**: 102203226  
- **Email**: [raagarwal_be22@thapar.edu](mailto:raagarwal_be22@thapar.edu)  
- **GitHub**: [radhikaaggarwal1509](https://github.com/radhikaaggarwal1509)

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

--- 

Let me know if you'd like further refinements!