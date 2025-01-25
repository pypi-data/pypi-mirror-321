# TOPSIS Package

This repository contains a Python implementation of the **TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution) method, a multi-criteria decision-making technique. The package supports command-line execution and enables users to calculate TOPSIS scores and rankings based on input data.

---

## **Features**
- Calculates TOPSIS scores and rankings for multi-criteria decision-making.
- Handles both positive and negative impacts of criteria.
- Provides results in a CSV file with scores and rankings.
- Fully customizable through weights and impacts specified as command-line arguments.

---

## **Installation**

To install the package from PyPI:

```bash
pip install topsis-Prince-3619
```

---

## **Usage**

### **Command-Line Interface (CLI)**
Run the TOPSIS program directly from the command line:

```bash
python3 -m Topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

### **Arguments**
1. `<InputDataFile>`: Path to the input CSV file.
   - The first column must contain object names (e.g., M1, M2, M3).
   - The remaining columns must contain numeric values for criteria.

2. `<Weights>`: Comma-separated weights for the criteria (e.g., `"1,1,1,2"`).

3. `<Impacts>`: Comma-separated impacts for the criteria (`+` for positive impact, `-` for negative impact).

4. `<ResultFileName>`: Name of the output CSV file where results will be saved.

---

## **Example**

### **Input Data**
Input file (`102203619-data.csv`):

| Model | Criterion 1 | Criterion 2 | Criterion 3 | Criterion 4 |
|-------|-------------|-------------|-------------|-------------|
| M1    | 250         | 16          | 12          | 5           |
| M2    | 200         | 18          | 8           | 3           |
| M3    | 300         | 14          | 16          | 10          |
| M4    | 275         | 17          | 10          | 8           |

### **Command**
```bash
topsis 102203619-data.csv "1,1,1,2" "+,+,-,+" result.csv
```

### **Output File**
Output file (`result.csv`):

| Model | Criterion 1 | Criterion 2 | Criterion 3 | Criterion 4 | Topsis Score | Rank |
|-------|-------------|-------------|-------------|-------------|--------------|------|
| M1    | 250         | 16          | 12          | 5           | 0.5346       | 2    |
| M2    | 200         | 18          | 8           | 3           | 0.3084       | 4    |
| M3    | 300         | 14          | 16          | 10          | 0.6912       | 1    |
| M4    | 275         | 17          | 10          | 8           | 0.5340       | 3    |

---

## **How It Works**
1. **Normalization**:
   The decision matrix is normalized using vector normalization:
   
   \[
   R_{ij} = \frac{a_{ij}}{\sqrt{\sum_{k=1}^{m} a_{kj}^2}}
   \]

2. **Weighted Normalized Matrix**:
   Each criterion is weighted according to user-defined weights:
   
   \[
   V_{ij} = R_{ij} \cdot w_j
   \]

3. **Identify Ideal Solutions**:
   - **Positive Ideal Solution (PIS)**: Maximum values for positive impacts and minimum values for negative impacts.
   - **Negative Ideal Solution (NIS)**: Minimum values for positive impacts and maximum values for negative impacts.

4. **Calculate Separation Measures**:
   - Separation from PIS (\( S_i^+ \)) and NIS (\( S_i^- \)) are computed using Euclidean distance.

5. **Calculate TOPSIS Scores**:
   - The score is calculated as:
     \[
     C_i = \frac{S_i^-}{S_i^+ + S_i^-}
     \]

6. **Rank Alternatives**:
   - Alternatives are ranked based on their scores, with higher scores indicating better performance.

---

## **Development**

### **Project Structure**
```
topsis-package/
├── topsis/
│   ├── __init__.py
│   ├── __main__.py
├── README.md
├── LICENSE
├── setup.py
├── pyproject.toml
└── MANIFEST.in
```

### **Dependencies**
- `numpy`
- `pandas`

### **Setup for Development**
1. Clone the repository:
   ```bash
   git clone https://github.com/Prince-05/TOPSIS
   ```
2. Navigate to the project directory:
   ```bash
   cd Topsis-Prince-3619
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Testing**
Run the tests to ensure the package works correctly:
```bash
pytest
```

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Contributing**
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed explanation of your changes.

---

## **Contact**
For any questions or issues, please contact:
- **Name**: Prince
- **Email**: pprince_be22@thapar.edu
- **GitHub**: [Prince-05](https://github.com/Prince-05)

