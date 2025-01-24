import psycopg2
from psycopg2 import sql

class DatabaseConnection:
    def __init__(self, dbname, user, password, host):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host
            )
            self.cursor = self.conn.cursor()
        except Exception as e:
            raise Exception(f"Не удалось подключиться к базе данных: {str(e)}")

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise Exception(f"Ошибка при выполнении запроса: {str(e)}")

    def fetch_data(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except Exception as e:
            raise Exception(f"Ошибка при получении данных: {str(e)}")

class BuildingManager:
    def __init__(self, db_connection):
        self.db = db_connection

    def get_objects(self):
        query = "SELECT * FROM Объекты"
        return self.db.fetch_data(query)

    def add_object(self, name, start_date, end_date, area, contract_id, status, developer_id, construction_type):
        query = """
            INSERT INTO "Объекты" ("Название", "Дата начала", "Дата окончания", "Площадь объекта", "ID договора", "Статус", "ID застройщика", "Тип строительства")
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (name, start_date, end_date, area, contract_id, status, developer_id, construction_type)
        self.db.execute_query(query, params)

    def update_object(self, object_id, name, start_date, end_date, area, contract_id, status, developer_id, construction_type):
        query = """
            UPDATE "Объекты"
            SET "Название" = %s, "Дата начала" = %s, "Дата окончания" = %s, "Площадь объекта" = %s, 
            "ID договора" = %s, "Статус" = %s, "ID застройщика" = %s, "Тип строительства" = %s
            WHERE "ID объекта" = %s
        """
        params = (name, start_date, end_date, area, contract_id, status, developer_id, construction_type, object_id)
        self.db.execute_query(query, params)

    def delete_object(self, object_id):
        query = "DELETE FROM Объекты WHERE \"ID объекта\" = %s"
        self.db.execute_query(query, (object_id,))

class DeveloperManager:
    def __init__(self, db_connection):
        self.db = db_connection

    def get_developers(self):
        query = "SELECT * FROM Застройщики"
        return self.db.fetch_data(query)

    def add_developer(self, name, phone, email, responsible):
        query = """
            INSERT INTO "Застройщики" ("Название организации", "Телефон", "Электронная почта", "ФИО ответственного лица")
            VALUES (%s, %s, %s, %s)
        """
        params = (name, phone, email, responsible)
        self.db.execute_query(query, params)

    def update_developer(self, developer_id, name, phone, email, responsible):
        query = """
            UPDATE "Застройщики"
            SET "Название организации" = %s, "Телефон" = %s, "Электронная почта" = %s, "ФИО ответственного лица" = %s
            WHERE "ID застройщика" = %s
        """
        params = (name, phone, email, responsible, developer_id)
        self.db.execute_query(query, params)

    def delete_developer(self, developer_id):
        query = "DELETE FROM Застройщики WHERE \"ID застройщика\" = %s"
        self.db.execute_query(query, (developer_id,))

class ContractManager:
    def __init__(self, db_connection):
        self.db = db_connection

    def get_contracts(self):
        query = "SELECT * FROM Договоры"
        return self.db.fetch_data(query)

    def add_contract(self, contract_date, contract_type, contract_status):
        query = """
            INSERT INTO "Договоры" ("Дата заключения", "Тип строительства", "Статус договора")
            VALUES (%s, %s, %s)
        """
        params = (contract_date, contract_type, contract_status)
        self.db.execute_query(query, params)

    def update_contract(self, contract_id, contract_date, contract_type, contract_status):
        query = """
            UPDATE "Договоры"
            SET "Дата заключения" = %s, "Тип строительства" = %s, "Статус договора" = %s
            WHERE "ID договора" = %s
        """
        params = (contract_date, contract_type, contract_status, contract_id)
        self.db.execute_query(query, params)

    def delete_contract(self, contract_id):
        query = "DELETE FROM Договоры WHERE \"ID договора\" = %s"
        self.db.execute_query(query, (contract_id,))