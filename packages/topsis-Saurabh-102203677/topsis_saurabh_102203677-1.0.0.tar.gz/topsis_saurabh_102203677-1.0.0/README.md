# TOPSIS Implementation in Python

This project demonstrates the implementation of the Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) algorithm in Python. The method is used to rank alternatives based on multiple criteria, considering their respective weights and impacts (benefit or cost).

## Key Features

- **Robust Input Validation**: Ensures the correctness of input parameters, file formats, and consistency in weights and impacts.
- **Comprehensive Error Handling**: Handles issues such as invalid data, incorrect file formats, and mismatched inputs gracefully.
- **Detailed Outputs**: Generates a CSV file containing the computed scores, rankings, and the original dataset columns.

---

You can access the package through this [link](https://pypi.org/project/topsis-Saurabh-102203677/#description).

## How to Use

1. Clone the repository and navigate to the project folder.
2. Ensure Python and required libraries are installed on your system.
3. Run the program using the following command:
   ```bash
   python -m topsis_Saurabh_102203677.topsis <InputDataSet.csv> <Weights> <Impacts> <ResultFile.csv>
   ```

## Example Input Dataset
![TOPSIS Example](images/ss1.png)
## Weights Example
Weights for criteria:
```python
[1, 1, 1, 1, 1]
```

## Impacts Example
Impacts for criteria:
```python
['-', '+', '+', '-', '+']
```
- `+` indicates a benefit criterion.
- `-` indicates a cost criterion.

## Example Output
![Result](images/ss2.png)
---


