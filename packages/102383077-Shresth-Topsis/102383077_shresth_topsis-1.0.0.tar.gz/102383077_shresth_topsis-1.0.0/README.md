# TOPSIS Implementation

## 1. Methodology
- **Step 1**: Data Collection  
- **Step 2**: Data Pre-Processing (Normalization and Validation)  
- **Step 3**: Weighted Normalization  
- **Step 4**: Calculation of Ideal Best and Ideal Worst Solutions  
- **Step 5**: Calculation of Separation Measures  
- **Step 6**: Calculation of Relative Closeness (TOPSIS Score)  
- **Step 7**: Ranking  

## 2. Description
- **Objective**: To implement the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method for multi-criteria decision analysis.  
- **Inputs**:  
  - A CSV file containing alternatives and their performance across criteria.  
  - Weights for criteria and their respective impacts (benefit or cost).  
- **Outputs**:  
  - A CSV file with TOPSIS scores and ranks for the alternatives.  
- **Error Handling**:  
  - File existence and format validation.  
  - Ensures impacts are '+' (benefit) or '-' (cost).  
  - Ensures the number of weights and impacts matches the criteria count.

## 3. Input / Output
### **Input File Example**: `<RollNumber>-data.csv`

| Alternative | Criterion 1 | Criterion 2 | Criterion 3 |
|-------------|-------------|-------------|-------------|
| A1          | 50          | 60          | 70          |
| A2          | 60          | 80          | 90          |
| A3          | 70          | 85          | 80          |

### **Output File Example**: `<RollNumber>-result.csv`

| Alternative | Criterion 1 | Criterion 2 | Criterion 3 | TOPSIS Score | Rank |
|-------------|-------------|-------------|-------------|--------------|------|
| A1          | 50          | 60          | 70          | 0.556        | 2    |
| A2          | 60          | 80          | 90          | 0.890        | 1    |
| A3          | 70          | 85          | 80          | 0.467        | 3    |

## 4. Usage Instructions
Run the program from the command line with the following format:  
```bash
python <RollNumber>.py <InputDataFile> <Weights> <Impacts> <ResultFileName>
