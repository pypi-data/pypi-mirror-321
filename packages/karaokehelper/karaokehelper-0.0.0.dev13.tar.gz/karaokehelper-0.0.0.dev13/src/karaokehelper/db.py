import pymysql.cursors
from typing import List
import logging

logger = logging.getLogger(__name__)


class DB:
    def  __init__(self, hostname: str = 'mysql', username: str = 'root', password: str = 'password', database: str = 'karaoke'):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database
        logger.info(f'Connecting to {self.hostname}/{self.database} as {self.username}')
        self.connection = self.get_connection()

    def get_connection(self):
        return pymysql.connect(host=self.hostname,
                             user=self.username,
                             password=self.password,
                             database=self.database,
                             cursorclass=pymysql.cursors.DictCursor)

    def select(self, what: str = '*', table: str = 'request', where: str = None) -> tuple:
        where = f" where {where}" if where is not None else ''
        with self.connection.cursor() as cursor:
            sql = f"SELECT {what} from {table}{where}"
            logger.debug(f"About to run: {sql}")
            cursor.execute(sql)
            results = cursor.fetchall()
            logger.debug(f"Results: {results}")
            return results

    def update(self, table: str = 'request', key: str = '', value: str or bool = '', where: str = None):
        where = f" where {where}" if where is not None else ''
        with self.connection.cursor() as cursor:
            sql = f'UPDATE {table} set {key} = "{value}"{where}'
            logger.debug(f"About to run: {sql}")
            cursor.execute(sql)
            logger.debug(f"Committing changes")
            self.connection.commit()


    def update_many(self, kv_dict: dict, table: str = 'request', where: str = None):
        where = f" where {where}" if where is not None else ''
        with self.connection.cursor() as cursor:
            values = []
            for k in kv_dict.keys():
                values.append(f'{k} = "{kv_dict[k]}"')
            sql = f"UPDATE {table} set {', '.join(values)}{where}"
            logger.debug(f"About to run: {sql}")
            cursor.execute(sql)
            logger.debug(f"Committing changes")
            self.connection.commit()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, 
                        format='%(asctime)s - %(filename)s:%(lineno)d - %(funcName)s - %(levelname)s - %(message)s', 
                        datefmt='%Y-%m-%d %H:%M:%S')
    db = DB()
    db.select(where='url = "https://www.youtube.com/watch?v=FilQhY2Pjq0"')
