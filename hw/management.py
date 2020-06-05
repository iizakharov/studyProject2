from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from models import Units, Categories

PATH_DB = 'shop_base.sqlite3'


class Management:
    def __init__(self, path_db):
        self.engine = create_engine(f'sqlite:///{path_db}?check_same_thread=False')
        self.unit = Units('шт.')
        self.create_base()
        self.session = self.get_session()

    def create_base(self):
        base = declarative_base()
        base.metadata.create_all(self.engine)

    def get_session(self):
        session = sessionmaker(bind=self.engine)
        session = session()
        return session

    def add_new_pool(self, *args):
        """
        Создает новую запись в таблице
        """
        self.args = args
        try:
            self.session.add(self)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            return 'Error!'
        return 'Success! Created'

    def update_description(self, table, id_to_update, new_desc):
        try:
            query = self.session.query(table).filter(
                table.id == id_to_update).first()
            query.description = new_desc
            self.session.commit()
        except SQLAlchemyError:
            self.session.rollback()
            return {'error': 'error'}
        return True

    def get_pool_list(self):
        """
        Получает список всех элементов в таблице
        """
        try:
            query_pool_list = self.session.query(Pool)
        except SQLAlchemyError:
            self.session.rollback()
            return {'error': 'error in query \"get_pool_list\"'}
        pool_dict = {}
        for pool in query_pool_list:
            pool_dict[pool.name] = pool.description
        return pool_dict


if __name__ == '__main__':
    base = Management(PATH_DB)
    # base.create_base('test')




