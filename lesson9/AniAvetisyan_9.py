import sqlite3

class DB_class:
    def create_connection(self):
        connect = sqlite3.connect("new.db")
        return connect

    def select_info(self):
        db = self.create_connection()
        cursor = db.cursor()
        sql_select = "SELECT * FROM Trainings WHERE Training_center = 'Center1'"
        cursor.execute(sql_select)
        rows = cursor.fetchall()
        for row in rows:
            if len(rows) == 0:
                print("There is no record found")
            else:
                print(row)
        db.close()        

    def update_info(self):
        db = self.create_connection()
        cursor = db.cursor()
        sql_update = """UPDATE Trainings
                    SET Training_name = 'automation_qa'
                    WHERE Training_name = 'test'
                    """
        cursor.execute(sql_update)
        db.commit()
        print(cursor.rowcount)
        db.close()

obj = DB_class()
obj.select_info()
obj.update_info()