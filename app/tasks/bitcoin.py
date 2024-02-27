from app.repositories.crypto_repository import CryptoRepository

from app.services.crypto_services import get_bitcoin_price

from app.tasks import scheduler


@scheduler.task('interval', id='btc', minutes=15)
def check_btc_price():
    timestamp, price = get_bitcoin_price()

    with CryptoRepository() as crypto:
        crypto.insert_btc_data(timestamp, price)
