# TOPSIS-Tanisha-102203818

*Effortlessly rank and evaluate alternatives using the TOPSIS method for multi-criteria decision-making.*

---

## 🌟 Introduction

TOPSIS (*Technique for Order of Preference by Similarity to Ideal Solution*) is a decision-making approach designed to handle complex scenarios involving multiple criteria. With this package, users can seamlessly compute rankings based on their data, weights, and impact preferences.

---

## 💡 Key Features

- Simplifies multi-criteria decision-making through an easy-to-use command-line interface.
- Fully customizable to user-defined weights and impacts.
- Provides accurate scores and ranks for alternatives based on the TOPSIS methodology.
- Supports flexible .csv input and output formats.

---

## 🔧 Installation Guide

Install the package directly from PyPI:
bash
pip install topsis-Tanisha-102203818


Alternatively, clone the GitHub repository to use it locally:
bash
git clone https://github.com/tanisha1234-sys/topsis-Tanisha-102203818.git
cd topsis-Tanisha-102203818
pip install -r requirements.txt


---

## 🚀 How to Use

The package can be executed via the command line with the following syntax:

bash
python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>

### Example Usage:
bash
python 102203818.py data.csv "1,2,3,4" "+,-,+,-" result.csv


### Parameters:
- **InputDataFile**: Path to the input .csv file containing the data.
- **Weights**: Comma-separated numeric values representing the weights of each criterion.
- **Impacts**: Comma-separated values (+ or -) indicating whether the criterion is beneficial or non-beneficial.
- **ResultFileName**: Path to save the result as a .csv file.

---

## 📝 Input Requirements

The input .csv file must:
1. Contain at least three columns:
   - The *first column* should list the alternatives (e.g., Option1, Option2).
   - The remaining columns should contain numeric values representing criteria.
2. Be properly formatted with no missing or non-numeric values in the criteria columns.

### Sample Input (data.csv):

| Object | Criterion 1 | Criterion 2 | Criterion 3 | Criterion 4 |
|--------|-------------|-------------|-------------|-------------|
| A1     | 25          | 30          | 45          | 20          |
| A2     | 35          | 25          | 50          | 15          |

---

## 📊 Output File

The output .csv file includes all the columns from the input file with two additional columns:
- **Topsis Score**: The relative closeness to the ideal solution.
- **Rank**: The position of each alternative based on its TOPSIS score.

### Example Output (result.csv):

| Object | Criterion 1 | Criterion 2 | Criterion 3 | Criterion 4 | Topsis Score | Rank |
|--------|-------------|-------------|-------------|-------------|--------------|------|
| A1     | 25          | 30          | 45          | 20          | 0.76         | 1    |
| A2     | 35          | 25          | 50          | 15          | 0.65         | 2    |

---

## 🛠 Error Handling

The program ensures:
- Correct input format and number of parameters.
- Validation of numeric criteria and proper weights/impacts format.
- Graceful handling of file-related errors (e.g., missing files).

---

## 📦 Dependencies

Ensure the following libraries are installed:
- numpy
- pandas

Install them via:
bash
pip install numpy pandas


---

## 📚 Additional Resources

- [TOPSIS Explanation on Wikipedia](https://en.wikipedia.org/wiki/TOPSIS)
- [Guide to Upload Python Packages to PyPI](https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56)

---

## 👤 About the Author

- *Name:* Tanisha  
- *Roll Number:* 102203818  
- *Email:* [tanishajain286@gmail.com](mailto:tanishajain286@gmail.com)  
- *GitHub Profile:* [tanisha1234-sys](https://github.com/tanisha1234-sys)

---

## 📝 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
