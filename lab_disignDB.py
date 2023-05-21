# todo:
# Для модели вашего варианта БД создать ORM модель в SQLAlchemy. Сгенерировать ее в БД.
# Переписать запросы с SQL на ORM.

# ссылка на ER модель: https://editor.ponyorm.com/user/stvlal/communication_services_company/designer
# вариант 20

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database_data import *
from sqlalchemy import func, desc

DB_NAME = 'communication_services_company'
USERNAME = 'postgres'
PASSWORD = 'postgres'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{USERNAME}:{PASSWORD}@localhost:5432/{DB_NAME}'

db = SQLAlchemy()
db.init_app(app)


tariff_service = db.Table('tariff_service',
                          db.Column('tariff_id', db.Integer, db.ForeignKey('tariffs.id'), primary_key=True),
                          db.Column('service_id', db.Integer, db.ForeignKey('services.id'), primary_key=True)
                          )


class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    cost = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.name} ({self.cost} руб)'


class Tariffs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    customers = db.relationship('Customers', backref='customer')
    tariff_services = db.relationship('Services', secondary=tariff_service, backref='service')

    def __repr__(self):
        return f'{self.name}'


class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    tariff_id = db.Column(db.ForeignKey('tariffs.id'))

    def __repr__(self):
        return f'{self.name}'


with app.app_context():
    db.create_all()

    for service in DB_SERVICES:
        current_service = Services(name=service[0], cost=service[1])
        db.session.add(current_service)

    for tariff in DB_TARIFFS:
        current_tariff = Tariffs(name=tariff)
        idx = DB_TARIFFS.index(tariff)
        current_services = [el[1] for el in DB_TARIFF_SERVICES if el[0] == (idx+1)]
        for service in current_services:
            current_tariff.tariff_services.append(Services.query.filter_by(name=DB_SERVICES[service-1][0]).first())
        db.session.add(current_tariff)

    for customer_tariff in DB_CUSTOMER_TARIFF:
        db.session.add(Customers(name=customer_tariff[0], tariff_id=customer_tariff[1]))

    db.session.commit()

    print('-------- СПИСОК ВСЕХ УСЛУГ --------')
    services_all = Services.query.all()
    for service in services_all:
        print(service)

    print('\n-------- СПИСОК ТАРИФОВ И ВХОДЯЩИХ В НИХ УСЛУГ --------')
    tariff_service_all = db.session.query(tariff_service).all()
    tmp_tariff = tariff_service_all[0][0]
    print(f'{db.session.get(Tariffs, tmp_tariff)}:')
    for tariff_service in tariff_service_all:
        if tariff_service[0] != tmp_tariff:
            tmp_tariff = tariff_service[0]
            print(f'{db.session.get(Tariffs, tmp_tariff)}:')
        print(f'\t{db.session.get(Services, tariff_service[1])}')

    TARIFF_INSTANCE = 6
    print(f'\n-------- СПИСОК АБОНЕНТОВ ИСПОЛЬЗУЮЩИХ ТАРИФ "{db.session.get(Tariffs, TARIFF_INSTANCE)}" --------')
    customers = db.session.execute(db.select(Customers).filter_by(tariff_id=TARIFF_INSTANCE)).all()
    for customer in customers:
        print(customer[0])

    print(f'\n-------- СПИСОК САМЫХ РАСПРОСТРАНЕННЫХ ТАРИФОВ --------')
    tariff_customers_sorted = db.session.query(Customers.tariff_id, func.count(Customers.tariff_id))\
        .group_by(Customers.tariff_id).order_by(desc(func.count(Customers.tariff_id))).all()
    all_customers = db.session.query(func.count(Customers.name)).scalar()
    idx = 1
    for tariff_customer in tariff_customers_sorted:
        popularity = round((tariff_customer[1] / all_customers * 100), 2)
        tariff = db.session.get(Tariffs, tariff_customer[0])
        print(f'[{idx}] {tariff} \t({popularity} %)')
        idx += 1

    print(f'\n-------- СПИСОК САМЫХ РАСПРОСТРАНЕННЫХ ТАРИФОВ В ВИДЕ ГИСТОГРАММЫ --------')
    idx = 1
    for tariff_customer in tariff_customers_sorted:
        k = ']' * int(tariff_customer[1] / all_customers * 100)
        print(f'[{idx}] \t {k}')
        idx += 1
