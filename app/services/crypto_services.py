from httpx import get

from app.repositories.crypto_repository import CryptoRepository


def get_bitcoin_price():
    response = get("https://api.coincap.io/v2/assets/bitcoin").json()

    timestamp = response.get("timestamp")
    price = response.get("data").get("priceUsd")

    return timestamp, price


def get_ethereum_price():
    response = get("https://api.coincap.io/v2/assets/ethereum").json()

    timestamp = response.get("timestamp")
    price = response.get("data").get("priceUsd")

    return timestamp, price


def get_bitcoin_price_history():
    with CryptoRepository() as crypto_repo:
        return crypto_repo.get_btc_data()


def get_ethereum_price_history():
    with CryptoRepository() as crypto_repo:
        return crypto_repo.get_eth_data()
