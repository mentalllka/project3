def set_column_types(self, types_dict, by_number=True):
    try:
        for key, col_type in types_dict.items():
            col_index = key if by_number else self.header.index(key)
            for row in self.data:
                row[col_index] = col_type(row[col_index])
    except ValueError as e:
        raise ValueError(f"Type conversion failed: {e}")
    except Exception as e:
        raise Exception(f"Error in set_column_types: {e}")
