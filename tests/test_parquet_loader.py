from src.ingestion.parquet_loader import load_parquet, process_data


def test_load_parquet():
    file_path = "path/to/test.parquet"
    df = load_parquet(file_path)
    assert not df.is_empty()


def test_process_data():
    df = pl.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    processed_df = process_data(df)
    assert not processed_df.is_empty()
