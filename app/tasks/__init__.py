from flask_apscheduler import APScheduler


scheduler = APScheduler()


def start(app):
    scheduler.init_app(app)
    scheduler.start()
