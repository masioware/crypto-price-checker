from sqlite3 import connect

from app.models.btc_model import BTC_DDL_QUERY
from app.models.eth_model import ETH_DDL_QUERY

from app.utils.converter import float_to_usd, timestamp_to_date


class CryptoRepository:
    def __init__(self, database="crypto.db"):
        self.database = database
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = connect(self.database)
        self.cursor = self.connection.cursor()

        self.cursor.execute(BTC_DDL_QUERY)
        self.cursor.execute(ETH_DDL_QUERY)

        return self

    def insert_btc_data(self, timestamp, price):
        query = "INSERT INTO btc (timestamp, price) VALUES (?, ?)"
        self.cursor.execute(query, (timestamp, price))

    def insert_eth_data(self, timestamp, price):
        query = "INSERT INTO eth (timestamp, price) VALUES (?, ?)"
        self.cursor.execute(query, (timestamp, price))

    def get_btc_data(self):
        self.cursor.execute("SELECT * FROM btc")
        result = self.cursor.fetchall()

        return self._format_result(result)

    def get_eth_data(self):
        self.cursor.execute("SELECT * FROM eth")
        result = self.cursor.fetchall()

        return self._format_result(result)

    def close(self):
        if self.connection:
            self.connection.commit()
            self.connection.close()

    def _format_result(self, data):
        formatted_data = []

        for row in data:
            date = timestamp_to_date(row[1])
            price = float_to_usd(row[2])

            formatted_data.append({"date": date, "price": price})

        return formatted_data

    def __exit__(self, *_):
        self.close()
