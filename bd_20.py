# ссылка на ER модель: https://editor.ponyorm.com/user/stvlal/communication_services_company/designer
# вариант 20

import psycopg

DB_NAME = 'provider'
USERNAME = 'vladimir'

with psycopg.connect(f'dbname={DB_NAME} user={USERNAME}') as conn:

    with conn.cursor() as cur:

        # СОЗДАЕМ ДАННЫЕ В БД

        cur.execute("""
        CREATE TABLE "services" (
        "id" SERIAL PRIMARY KEY,
        "name" VARCHAR(255) NOT NULL,
        "cost" INTEGER NOT NULL);
        """)

        cur.execute("""
        CREATE TABLE "tariffs" (
        "id" SERIAL PRIMARY KEY,
        "name" VARCHAR(255) NOT NULL);
        """)

        cur.execute("""
        CREATE TABLE "customers" (
        "id" SERIAL PRIMARY KEY,
        "name" VARCHAR(255) NOT NULL,
        "tariff_id" INTEGER NOT NULL);
        """)

        cur.execute("""
        ALTER TABLE "customers" 
        ADD CONSTRAINT "fk_customers__tariff_id" 
        FOREIGN KEY ("tariff_id") 
        REFERENCES "tariffs" ("id") 
        ON DELETE RESTRICT;
        """)

        cur.execute("""
        CREATE TABLE "tariff_service" (
        "tariff_id" INTEGER NOT NULL,
        "service_id" INTEGER NOT NULL,
        PRIMARY KEY ("tariff_id", "service_id"));
        """)

        cur.execute("""
        ALTER TABLE "tariff_service" 
        ADD CONSTRAINT "fk_tariff_service__service_id" 
        FOREIGN KEY ("service_id") 
        REFERENCES "services" ("id") 
        ON DELETE RESTRICT;
        """)

        cur.execute("""
        ALTER TABLE "tariff_service" 
        ADD CONSTRAINT "fk_tariff_service__tariff_id" 
        FOREIGN KEY ("tariff_id") 
        REFERENCES "tariffs" ("id") 
        ON DELETE RESTRICT;
        """)

        cur.execute("""
        INSERT INTO services(name, cost)
        VALUES
        ('Безлимитные звонки', 500),
        ('Безлимитные СМС', 300),
        ('Безлимитный интернет', 700),
        ('Антиспам', 200),
        ('Голосовой ассистент Борис', 230),
        ('100 минут', 80),
        ('300 минут', 200),
        ('600 минут', 400),
        ('100 СМС', 50),
        ('300 СМС', 150),
        ('600 СМС', 200),
        ('1 Гб интернета', 100),
        ('6 Гб интернета', 150),
        ('15 Гб интернета', 200),
        ('30 Гб интернета', 300),
        ('50 Гб интернета', 500),
        ('Звонки с подменой номера', 1000),
        ('Изменеине голоса', 800),
        ('Сокрытие базовой станции от тов. майора', 1800);
        """)

        cur.execute("""
        INSERT INTO tariffs(name)
        VALUES
        ('Начинающий звонарь'),
        ('Продолжающий звонарь'),
        ('Звонилка картонная'),
        ('Мастер звонарь'),
        ('Банковский специалист'),
        ('Поймай меня если сможешь'),
        ('Без интернета 1'),
        ('Без интернета 2'),
        ('Отдел взыскания банка'),
        ('Звони как в последний раз');
        """)

        cur.execute("""
        INSERT INTO tariff_service(tariff_id, service_id)
        VALUES
        (1, 6),
        (1, 9),
        (1, 12),
        (2, 7),
        (2, 10),
        (2, 13),
        (3, 6), 
        (4, 8),
        (4, 11),
        (4, 14),
        (4, 4),
        (4, 5),
        (5, 1),
        (5, 2),
        (5, 14),
        (5, 18),
        (5, 17),
        (6, 1),
        (6, 2),
        (6, 3),
        (6, 17),
        (6, 18),
        (6, 19),
        (7, 8),
        (7, 11),
        (7, 4),
        (7, 5),
        (8, 10),
        (8, 7),
        (9, 16),
        (9, 18),
        (9, 1),
        (9, 11),
        (10, 1),
        (10, 16),
        (10, 19);
        """)

        cur.execute("""
        INSERT INTO customers(name, tariff_id)
        VALUES
        ('Александра', 4),
        ('Виктор', 3),
        ('Николай', 5),
        ('Мария', 4),
        ('Сергей', 1),
        ('Михаил', 6),
        ('Владимир', 8),
        ('Арсен', 10),
        ('Дарья', 9),
        ('Елизавета', 7),
        ('Татьяна', 8),
        ('Дмитрий', 5),
        ('Алексей', 6),
        ('Владимир', 3),
        ('Анастасия', 7),
        ('Ольга', 1),
        ('Евгений', 2),
        ('Владислав', 3),
        ('Илья', 4),
        ('Ахмед', 7),
        ('Максим', 9),
        ('Станислав', 10),
        ('Сергей', 3),
        ('Виктория', 8),
        ('Алина', 7),
        ('Ульяна', 6),
        ('Андрей', 6),
        ('Александр', 1),
        ('Надежда', 4),
        ('Ярослав', 3),
        ('Анатолий', 2),
        ('Дарья', 1),
        ('Дарина', 6),
        ('Ксения', 7),
        ('Нина', 8),
        ('Ирина', 9),
        ('Елизавета', 3);
        """)

        # ДЕЛАЕМ ЗАПРОСЫ В БД

        cur.execute('SELECT * FROM services;')
        services_table = cur.fetchall()

        print('-------- СПИСОК ВСЕХ УСЛУГ --------')
        for service in services_table:
            print(service[1])

        cur.execute("""
        SELECT tariffs.name, services.name, services.cost
        FROM tariffs JOIN tariff_service
        ON tariffs.id = tariff_service.tariff_id
        JOIN services
        ON tariff_service.service_id = services.id;
        """)

        tariffs_services = cur.fetchall()

        print('\n-------- СПИСОК ТАРИФОВ И ВХОДЯЩИХ В НИХ УСЛУГ --------')
        tmp_tariff = tariffs_services[0][0]
        print(f'{tmp_tariff}:')
        for tariff_service in tariffs_services:
            if tariff_service[0] != tmp_tariff:
                tmp_tariff = tariff_service[0]
                print(f'{tmp_tariff}:')
            print(f'\t{tariff_service[1]} ({tariff_service[2]} руб)')

        TARIFF_INSTANCE = 'Без интернета 1'

        cur.execute(f"""
        SELECT * FROM
        (SELECT customers.name, tariffs.name AS tariff
        FROM customers JOIN tariffs
        ON customers.tariff_id = tariffs.id) AS foo
        WHERE tariff='{TARIFF_INSTANCE}';
        """)

        tariff_user = cur.fetchall()

        print(f'\n-------- СПИСОК АБОНЕНТОВ ИСПОЛЬЗУЮЩИХ ТАРИФ "{TARIFF_INSTANCE}" --------')
        for user in tariff_user:
            print(user[0])

        cur.execute("""
        SELECT tariffs.name, COUNT(*)
        FROM customers JOIN tariffs
        ON customers.tariff_id = tariffs.id
        GROUP BY tariffs.name
        ORDER BY count DESC;
        """)

        tariff_customers = cur.fetchall()

        cur.execute('SELECT MAX(id) FROM customers;')

        all_customers = cur.fetchone()[0]

        print(f'\n-------- СПИСОК САМЫХ РАСПРОСТРАНЕННЫХ ТАРИФОВ --------')
        idx = 1
        for tariff_customer in tariff_customers:
            popularity = round((tariff_customer[1] / all_customers * 100), 2)
            print(f'[{idx}] {tariff_customer[0]} \t({popularity} %)')
            idx += 1

        print(f'\n-------- СПИСОК САМЫХ РАСПРОСТРАНЕННЫХ ТАРИФОВ В ВИДЕ ГИСТОГРАММЫ --------')
        idx = 1
        for tariff_customer in tariff_customers:
            k = ']' * int(tariff_customer[1] / all_customers * 100)
            print(f'[{idx}] \t {k}')
            idx += 1
