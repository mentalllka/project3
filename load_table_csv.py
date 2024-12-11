import csv


def load_table_csv(filepath):
    try:
        with open(filepath, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            data = list(reader)
            return TableData(header, data)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {filepath}")
    except Exception as e:
        raise Exception(f"Ошибка загрузки CSV: {e}")
