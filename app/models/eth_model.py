# Ethereum table
ETH_DDL_QUERY = """
CREATE TABLE IF NOT EXISTS eth (
    id INTEGER PRIMARY KEY,
    timestamp INTEGER,
    price REAL
)
"""
