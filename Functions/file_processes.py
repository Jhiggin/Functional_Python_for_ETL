import pandas as pd


def read_csv_file(file_path):
    df = pd.read_csv(filepath_or_buffer=file_path)
    return df


def read_excel_file(file_path):
    df = pd.read_excel(io=file_path)
    return df


def write_to_csv(dataset, file_path):
    dataset.to_csv(path_or_buf=file_path, index=False)


def write_to_excel(dataset, file_path):
    dataset.to_excel(excel_writer=file_path, index=False)


def write_to_parquet(dataset, file_path):
    dataset.to_parquet(path=file_path, index=False)


def write_to_feather(dataset, file_path):
    dataset.to_feather(path=file_path)


def write_to_pickle(dataset, file_path):
    dataset.to_pickle(path=file_path, compression='gzip')
