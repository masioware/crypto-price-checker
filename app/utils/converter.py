from datetime import datetime


def timestamp_to_date(timestamp):
    date = datetime.fromtimestamp(timestamp / 1e3)

    return date.strftime("%m/%d/%Y, %H:%M:%S")


def float_to_usd(value):
    return f"{value:,.2f} USD"
