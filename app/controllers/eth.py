from flask import Blueprint, jsonify

from app.services.crypto_services import get_ethereum_price_history


eth_controller = Blueprint("Ethereum Controller", __name__)


@eth_controller.route('/eth', methods=['GET'])
def get_eth_prices():
    ethereum_history = get_ethereum_price_history()
    return jsonify(ethereum_history)


@eth_controller.route('/eth/last', methods=['GET'])
def get_last_btc_price():
    last_ethereum_price = get_ethereum_price_history().pop(0)
    return jsonify(last_ethereum_price)


def start(app):
    app.register_blueprint(eth_controller)
