def get_rows_by_index(self, *values, copy_table=False):
    try:
       rows = [row for row in self.data if row[0] in values]
       if copy_table:
           return TableData(self.header, [row[:] for row in rows])
       return TableData(self.header, rows)
    except Exception as e:
       raise Exception(f"Error in get_rows_by_index: {e}")
