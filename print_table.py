def print_table(self):
    from tabulate import tabulate
    try:
        print(tabulate(self.data, headers=self.header, tablefmt="grid"))
    except Exception as e:
        raise Exception(f"Ошибка в print_table: {e}")
