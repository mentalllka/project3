import pickle

def load_table_pickle(filepath):
    try:
        with open(filepath, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {filepath}")
    except Exception as e:
        raise Exception(f"Ошибака загрузки pickle: {e}")
