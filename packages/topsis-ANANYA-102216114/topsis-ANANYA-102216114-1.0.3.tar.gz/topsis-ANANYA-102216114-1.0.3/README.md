# Topsis PyPi Package (CLI)

Submitted By: **Ananya Gaur 102216114**

A Python package that can be used as a CLI tool for implementing Topsis method used for multi-criteria decision analysis by calculating performance and ranks. Topsis stands for '**T**echnique for **O**rder of **P**reference by **S**imilarity to **I**deal **S**olution'.
<br>
Checkout the package 👉: <https://pypi.org/project/topsis-ANANYA-102216114/>

> CLI scripts takes `csv/excel` files as input!

## Installation of the package
```
$ pip install topsis-ANANYA-102216114
```

## Command Line Usage
```
$ topsis-ANANYA-102216114 input_filePath weights impacts output_filePath
```
### Arguments
| Arguments | Description |
|------------| -----------------|
| input_file |  Input CSV file path |
| weights | Comma separated string of numbers(weights) |
| impacts | Comma separated string of '+' or '-' |
| output_file | Output CSV file path |

### Output
Creates a csv *output_file*, that contains the original data alongwith additional cloumns of Topsis Performance score and rank.

Example:
```bash
$topsis-ANANYA-102216114 data.csv "1,0.25,1,1" "+,-,+,-,+" output.csv 
```

<br>

## Sample dataset

### 1. Structure of the Decision Matrix
- The file must contain **three or more columns**.
- The **first column** contains the names or identifiers of the Model/Product alternatives (e.g., M1, M2, etc.).
- The **remaining columns** (from the second column onwards) contain **Numeric** or **Nominal** values representing the criteria for evaluation.

**Example Decision Matrix:**
Model | Cost | Quality | Durability | Ease of use
------------ | ------------- | ------------ | ------------- | ------------
M1 |	250 | 8.5	| 7.0 | 9.0
M2 |    300 | 7.8	| 8.5 | 8.0
M3 |	200 | 9.0	| 6.5 | 7.5
M4 |	290 | 8.2	| 7.8 | 8.8
M5 |	350 | 9.5	| 8.2 | 7.9

<br>


## License
Licensed under the [MIT License](https://github.com/ananyagr02/topsis-ANANYA-102216114/blob/main/LICENSE). 

