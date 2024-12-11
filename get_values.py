def get_values(self, column=0):
    try:
        col_index = column if isinstance(column, int) else self.header.index(column)
        return [row[col_index] for row in self.data]
    except ValueError:
        raise ValueError(f"Column {column} not found.")
    except Exception as e:
        raise Exception(f"Error in get_values: {e}")
