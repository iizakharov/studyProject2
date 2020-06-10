from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Categories(Base):
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String(30), nullable=False)
    category_description = Column(String(250), nullable=False)

    def __init__(self, category_name, category_description):
        self.category_name = category_name
        self.category_description = category_description

    def __repr__(self):
        return self.category_name


class Units(Base):
    __tablename__ = 'units'
    unit_id = Column(Integer, primary_key=True)
    unit = Column(String(5), nullable=False)

    def __init__(self, unit):
        self.unit = unit

    def __repr__(self):
        return self.unit


class Positions(Base):
    __tablename__ = 'positions'
    position_id = Column(Integer, primary_key=True)
    position = Column(String(30), nullable=False)

    def __init__(self, position):
        self.position = position

    def __repr__(self):
        return self.position


class Goods(Base):
    __tablename__ = 'goods'
    good_id = Column(Integer, primary_key=True)
    good_name = Column(String(50), nullable=False)
    good_unit = Column(Integer, ForeignKey('units.unit_id'))
    good_cat = Column(Integer, ForeignKey('categories.category_id'))

    def __init__(self, good_name):
        self.good_name = good_name

    def __repr__(self):
        return self.good_name


class Employees(Base):
    __tablename__ = 'employees'
    employee_id = Column(Integer, primary_key=True)
    employee_fio = Column(String(50), nullable=False)
    employee_position = Column(Integer, ForeignKey('positions.position_id'))

    def __init__(self, employee_fio):
        self.employee_fio = employee_fio

    def __repr__(self):
        return self.employee_fio


class Vendors(Base):
    __tablename__ = 'vendors'
    vendor_id = Column(Integer, primary_key=True)
    vendor_name = Column(String(50), nullable=False)
    vendor_ownerchipform = Column(String(50), nullable=False)
    vendor_address = Column(String(200), nullable=False)
    vendor_phone = Column(String(20), nullable=False)
    vendor_email = Column(String(20), nullable=False)

    def __init__(self, vendor_name, vendor_ownerchipform,
                 vendor_address, vendor_phone, vendor_email):
        self.vendor_name = vendor_name
        self.vendor_ownerchipform = vendor_ownerchipform
        self.vendor_address = vendor_address
        self.vendor_phone = vendor_phone
        self.vendor_email = vendor_email

    def __repr__(self):
        return self.vendor_name


def make_session():
    engine = create_engine('sqlite:///database.sqlite3')
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    s = session()
    return s


def create_table(*args):
    session = make_session()
    session.add_all([*args])
    session.commit()


# def search_by_id(table, id):
#     session = make_session()
#     query = session.query(table).filter(table.id == id).update(
#         {Pool.description: new_desc}, synchronize_session=False)

def main():
    pass


if __name__ == "__main__":

    # category = Categories('Стулья', 'Разновидные стулья, кресла')
    # unit = Units('шт.')
    # good = Goods('Prestige')
    # position = Positions('менеджер')
    # employee = Employees('Иванов Петр Михаилович')
    # vendor = Vendors('team7', 'OOO', 'Moscow, Tverskaya str. 1',
    #                  '+7(499)799-95-65', 'team7@mail.com')
    # дополнительное наполнение
    category = Categories('Телефоны', 'Селефоны, смартфоны и планшеты')
    unit = Units('ед.')
    good = Goods('iPhoneX')
    position = Positions('кассир')
    employee = Employees('Тарасова Ироина Викторовна')
    vendor = Vendors('Apple', 'LLT', 'CL, Central str. 12b',
                     '+1(9955)123-274-75', 'info@apple.com')
    create_table(category, unit, good, position, employee, vendor)
