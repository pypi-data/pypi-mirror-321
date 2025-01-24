from src.core.util import setup_logging
from src.db.util import get_cached_sqlalchemy_db


def command():
    setup_logging()
    get_cached_sqlalchemy_db().init()


if __name__ == '__main__':
    command()
