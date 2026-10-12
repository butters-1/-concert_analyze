import duckdb

class DuckDBConnection:
    def __init__(self, db_path: str):
        self.con = duckdb.connect(db_path)
        self.create_virtual_view()

    def execute_query(self, query: str) -> pl.DataFrame:
        return self.con.execute(query).fetchdf()

    def create_virtual_view(self):
        self.con.execute("""
            CREATE OR REPLACE VIEW vw_concert_events AS
            SELECT * FROM read_parquet('data/raw/*/*/*.parquet')
        """)
