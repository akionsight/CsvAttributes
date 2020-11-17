# CsvAttributes
Get Row and Column attributes of any csv file

## Usage
- Import the `CsvAttributes` file present in the `CsvAttributes` folder
```python
import CsvAttributes.CsvAttributes
```
- Create a instance of the `CsvAttributes` Class and pass in the name of your csv file; eg:
```python
file = CsvAttributes(test.csv)
```
- Now access the various methords in the class to row and coloumn info of your csv file.

## Various methords of the CsvAttributes class
1. **`rows` methord**: This allows you to access the name of the different rows in the csv file and the total number of rows in the csv file. Returns a dictionary
Example Usage:
```python
file = CsvAttributes('test.csv')
print(file.rows())
## returns something like this: {'row_names': ['column 1', ['column 2'], 'no_of_columns': 2}
```
2. **`no_of_columns` methord**: This returns the number of columns in the csv file. Returns a integer
```python
file = CsvAttributes('test.csv')
print(file.no_of_columns())
## returns something like 13567, 902383 etc depending on the number of columns
```
## Some sample code
```python
file = CsvAttributes('test.csv')
print(file.no_of_columns())
print(file.rows())
```
