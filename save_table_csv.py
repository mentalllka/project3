import csv

def save_table_csv(table, filepath):
    try:
        with open(filepath, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(table.header)
            writer.writerows(table.data)
    except Exception as e:
        raise Exception(f"Error saving CSV: {e}")
