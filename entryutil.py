import psycopg2


class EntryUtil():

    def __init__(self, db_connection_name, db_name, db_user, db_password):
        self.db_connection_name = db_connection_name
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password

    def GetEntryByEntryID(self, entryID):
        try:
            query = 'SELECT * from entry_information where entry_id = {};'
            host = '/cloudsql/{}'.format(self.db_connection_name)
            cnx = psycopg2.connect(
                dbname=self.db_name,
                user=self.db_user,
                password=self.db_password,
                host=host
                )
            with cnx.cursor() as cursor:
                cursor.execute(query.format(entryID))
                result = cursor.fetchall()
            return result
        except Exception as e:
            raise e
        finally:
            cnx.commit()
            cnx.close()

    def GetEntryListByOrderNumber(self, orderNumber):
        try:
            query = 'SELECT * from entry_information where ordernumber = {};'
            host = '/cloudsql/{}'.format(self.db_connection_name)
            cnx = psycopg2.connect(
                dbname=self.db_name,
                user=self.db_user,
                password=self.db_password,
                host=host
                )
            with cnx.cursor() as cursor:
                cursor.execute(query.format(orderNumber))
                result = cursor.fetchall()
            return result
        except Exception as e:
            raise e
        finally:
            cnx.commit()
            cnx.close()
