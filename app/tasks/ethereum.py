from app.repositories.crypto_repository import CryptoRepository

from app.services.crypto_services import get_ethereum_price

from app.tasks import scheduler


@scheduler.task('interval', id='eth', minutes=15)
def check_eth_price():
    timestamp, price = get_ethereum_price()

    with CryptoRepository() as crypto:
        crypto.insert_eth_data(timestamp, price)
