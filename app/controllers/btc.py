from flask import Blueprint, jsonify

from app.services.crypto_services import get_bitcoin_price_history


btc_controller = Blueprint("Bitcoin Controller", __name__)


@btc_controller.route('/btc', methods=['GET'])
def get_btc_prices():
    bitcoin_history = get_bitcoin_price_history()
    return jsonify(bitcoin_history)


@btc_controller.route('/btc/last', methods=['GET'])
def get_last_btc_price():
    last_bitcoin_price = get_bitcoin_price_history().pop(0)
    return jsonify(last_bitcoin_price)


def start(app):
    app.register_blueprint(btc_controller)
