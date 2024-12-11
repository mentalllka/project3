import pickle

def save_table_pickle(table, filepath):
    try:
        with open(filepath, 'wb') as file:
            pickle.dump(table, file)
    except Exception as e:
        raise Exception(f"Ошибка в загрузке pickle: {e}")
