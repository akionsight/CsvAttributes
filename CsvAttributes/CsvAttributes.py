class CsvAttributes:
    def __init__(self, filename: str):
        self.filename = filename

    def rows(self):
        with open(self.filename) as file:
            rows = file.readlines(1)
            refined_rows = rows[-1].replace('\n', '').split(',')
            no_of_rows = len(refined_rows)
            return {"row_names": refined_rows, "no_of_rows": no_of_rows}

    def no_of_columns(self):
        with open(self.filename) as file:
            no_of_lines = 0
            for _ in file:
                no_of_lines += 1
            return no_of_lines


file = CsvAttributes('governors_county_candidate.csv')
print(file.no_of_columns())
print(file.rows())