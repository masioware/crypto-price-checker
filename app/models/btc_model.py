# Bitcoin table
BTC_DDL_QUERY = """
CREATE TABLE IF NOT EXISTS btc (
    id INTEGER PRIMARY KEY,
    timestamp INTEGER,
    price REAL
)
"""
