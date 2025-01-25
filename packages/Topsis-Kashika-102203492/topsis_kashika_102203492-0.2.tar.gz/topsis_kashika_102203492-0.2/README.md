Topsis-Kashika-102203492
Topsis-Kashika-102203492 is a Python package that implements the TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) method for multi-criteria decision-making (MCDM). The TOPSIS method is used to rank and evaluate alternatives based on multiple criteria, helping decision-makers identify the best alternative.

Features
TOPSIS Algorithm: Implements the TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) method.
Customizable Weights and Impacts: Allows users to define the weights (importance) and impacts (positive or negative) of criteria.
CSV Input and Output: Takes an input CSV file with alternatives and their criteria, processes it, and generates an output CSV with the TOPSIS score and rank for each alternative.
Command-Line Interface: Easily run the package via the command line.
Installation
You can install the package directly from PyPi using the following command:

bash
Copy
pip install Topsis-Kashika-102203492
This will install the package and its dependencies.

Usage
After installing the package, you can use it via the command line.

Command Syntax:
bash
Copy
python -m 102203492.102203492 <InputDataFile> <Weights> <Impacts> <ResultFileName>
Where:

<InputDataFile>: The path to the input CSV file (e.g., 3492-data.csv).
<Weights>: A comma-separated string representing the weights for each criterion (e.g., "1,1,1,2,3").
<Impacts>: A comma-separated string of impacts (+ for positive impact, - for negative impact) (e.g., "+,+,-,+,+").
<ResultFileName>: The path to the output CSV file where the results will be saved (e.g., 3492_result.csv).
Example:
bash
Copy
python -m 102203492.102203492 3492-data.csv "1,1,1,2,3" "+,+,-,+,+" 3492_result.csv
This command will:

Read the data from 3492-data.csv.
Apply the TOPSIS method with the weights 1,1,1,2,3 and impacts +,+,-,+,+.
Save the resulting scores and ranks to 3492_result.csv.
Example Input (3492-data.csv):
The input CSV file should have the following format, where the first column contains the alternative names and the subsequent columns represent numeric values for each criterion.

Alternative	Criterion 1	Criterion 2	Criterion 3	Criterion 4	Criterion 5
A1	3.5	5.0	4.0	2.0	4.5
A2	4.0	4.0	3.5	3.0	4.0
A3	2.0	3.0	5.0	4.0	5.0
Example Output (3492_result.csv):
The output CSV file will include the original data along with two additional columns:

Topsis Score: The calculated score for each alternative.
Rank: The rank of each alternative based on the Topsis score.
Alternative	Criterion 1	Criterion 2	Criterion 3	Criterion 4	Criterion 5	Topsis Score	Rank
A1	3.5	5.0	4.0	2.0	4.5	0.85	1
A2	4.0	4.0	3.5	3.0	4.0	0.78	2
A3	2.0	3.0	5.0	4.0	5.0	0.65	3
Dependencies
This package requires the following Python libraries:

pandas: For data handling and CSV file manipulation.
numpy: For numerical calculations.
You can install these dependencies using:

bash
Copy
pip install pandas numpy
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Author
Kashika
Roll Number: 102203492

