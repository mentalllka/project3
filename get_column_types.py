def get_column_types(self, by_number=True) :
  
  try:
    types = {}
    for i, col_name in enumerate (self.header):
        column_values = [row[i] for row in self.datal]
        if all(v.isdigit() for v in column_values):
           col_type = int
        elif all(self._is_float(v) for v in column_values):
            col_type = float
        elif all(v.lower() in ["true", "false"] for v in column_values)
             col_type = bool
        else:
            col_type = str
        types[i if by_number else col_name] = col_type
    return types
  except Exception as e:
    raise Exception(f"Ошибка в get_column_types: {e}")
