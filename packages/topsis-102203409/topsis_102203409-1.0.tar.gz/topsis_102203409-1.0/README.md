# **TOPSIS 102203409**

[![PyPI Version](https://img.shields.io/pypi/v/topsis_102203409.svg)](https://pypi.org/project/topsis-102203409/) 
A Python package for implementing the **Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS)**. This is a multi-criteria decision analysis method that helps in ranking alternatives based on multiple criteria.

---

## **Installation**

Install the package using pip:

```bash
pip install topsis-102203409
```

---

## **Usage**

### **Command-Line Interface (CLI)**

You can run the TOPSIS method directly from the command line.

#### **Syntax**
```bash
topsis <input_file> <weights> <impacts> <output_file>
```

#### **Arguments**
1. **`<input_file>`**: Path to the input CSV file containing the data.  
   - The first column should contain the names of the alternatives.  
   - The remaining columns should contain numerical values for the criteria.  

2. **`<weights>`**: A comma-separated string of weights for each criterion (e.g., `"1,1,1,1"`).

3. **`<impacts>`**: A comma-separated string of impacts (`+` for positive, `-` for negative) corresponding to each criterion (e.g., `"+,+,-,+"`).

4. **`<output_file>`**: Path to save the resulting output file, which will include the computed scores and ranks.

---

### **Example**

#### **Input File (`input.csv`)**
| Alternative | Criterion1 | Criterion2 | Criterion3 | Criterion4 |
|-------------|------------|------------|------------|------------|
| Alt1        | 250        | 16         | 12         | 5          |
| Alt2        | 200        | 32         | 8          | 3          |
| Alt3        | 300        | 24         | 10         | 4          |
| Alt4        | 275        | 20         | 11         | 4.5        |
| Alt5        | 225        | 28         | 9          | 4          |

#### **Command**
```bash
topsis input.csv "1,1,1,1" "+,+,-,+" output.csv
```

#### **Output File (`output.csv`)**
| Alternative | Criterion1 | Criterion2 | Criterion3 | Criterion4 | Score      | Rank |
|-------------|------------|------------|------------|------------|------------|------|
| Alt1        | 250        | 16         | 12         | 5          | 0.8729     | 1    |
| Alt2        | 200        | 32         | 8          | 3          | 0.3243     | 4    |
| Alt3        | 300        | 24         | 10         | 4          | 0.2985     | 5    |
| Alt4        | 275        | 20         | 11         | 4.5        | 0.7315     | 3    |
| Alt5        | 225        | 28         | 9          | 4          | 0.4532     | 2    |

---

## **Library Usage**

You can also use the package programmatically in Python.

```python
from topsis_package.main import topsis

topsis("input.csv", "1,1,1,1", "+,+,-,+", "output.csv")
```

---

## **Dependencies**

- Python >= 3.7
- pandas
- numpy

---

## **How TOPSIS Works**

1. **Normalize the Decision Matrix**  
   Convert each criterion to a unit vector.

2. **Calculate the Weighted Normalized Decision Matrix**  
   Multiply each normalized value by its weight.

3. **Determine the Ideal Best and Worst Solutions**  
   - For positive impacts: Max value.  
   - For negative impacts: Min value.

4. **Calculate Separation Measures**  
   - Distance from the ideal best.  
   - Distance from the ideal worst.

5. **Compute Relative Closeness to the Ideal Solution**  
   Rank the alternatives based on their closeness.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Author**

**Arin Goyal**  
Email: [aringoyal15@gmail.com](mailto:aringoyal15@gmail.com)
