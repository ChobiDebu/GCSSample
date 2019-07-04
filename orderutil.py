import psycopg2


class OrderUtil():

    def __init__(self, db_connection_name, db_name, db_user, db_password):
        self.db_connection_name = db_connection_name
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password

    def GetOrderByOrderNumber(self, orderNumber):
        try:
            query = 'SELECT * from order_information where ordernumber = {};'
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

    def UpdateOrderByOrderNumber(self, orderNumber, status, deliveredDateTime):
        try:
            query = 'update order_information set order_status = {} orderer_order_status = {} delivered_datetime = {} where ordernumber = {}'
            host = '/cloudsql/{}'.format(self.db_connection_name)
            cnx = psycopg2.connect(
                dbname=self.db_name,
                user=self.db_user,
                password=self.db_password,
                host=host
                )
            with cnx.cursor() as cursor:
                result = cursor.execute(
                    query.format(
                        status,
                        status,
                        deliveredDateTime,
                        orderNumber)
                        )
            return result
        except Exception as e:
            cnx.rollback()
            raise e
        finally:
            cnx.commit()
            cnx.close()
