# TOPSIS Implementation in Python

This Python project implements the Technique for Order Preference by Similarity to Ideal Solution (TOPSIS). The algorithm ranks alternatives based on multiple criteria, considering their relative importance (weights) and impacts (benefit or cost).

## Features

- **Input Validation**: Checks for correct input parameters, file format, and consistency in weights/impacts.
- **Error Handling**: Handles file-related errors, invalid data, and incorrect inputs gracefully.
- **Outputs**: Saves results including scores, rankings, and all original columns into a CSV file.

---

## How to Use

1. Clone the repository and navigate to the project directory.
2. Ensure you have Python installed with the necessary packages.
3. Use the following command to run the program:
   ```bash
   python topsis.py <InputDataSet.csv> <Weights> <Impacts> <ResultFile.csv>


## Input dataset
![TOPSIS Example](images/ss1.png)

## Weights used
[1,1,1,1,1]

## Impacts used
[0,1,1,0,1]
### 1 for benifit
### 0 for cost

## Output
![Result](images/ss2.png)