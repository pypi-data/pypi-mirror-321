import psycopg2

def connect_db():
    return psycopg2.connect(
        database="postgres",
        user="postgres",
        password="1111",
        host="localhost",
        port="5432"
    )

class DatabaseOperations:
    def get_table_data(self, table_name):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM "{table_name}"')
        data = cursor.fetchall()
        conn.close()
        return data

    def get_filtered_data(self, table_name, column, value):
        conn = connect_db()
        cursor = conn.cursor()

        # Маппинг столбцов для каждой таблицы
        column_mapping = {
            "Товары": {
                "ID товара": "ID товара",
                "Категория": "Категория",
                "Название": "Название",
                "Количество": "Количество",
                "Цена": "Цена",
                "ID поставщика": "ID поставщика"
            },
            "Поставщики": {
                "ID поставщика": "ID поставщика",
                "Название организации": "Название организации",
                "Контактная информация": "Контактная информация"
            },
            "Заказы": {
                "ID заказа": "ID заказа",
                "Название": "Название",
                "Количество": "Количество",
                "ID товара": "ID товара",
                "ID поставщика": "ID поставщика",
                "Категория": "Категория"
            }
        }

        # Получаем правильное имя столбца
        if table_name in column_mapping and column in column_mapping[table_name]:
            column = column_mapping[table_name][column]
        

        # Выполняем запрос
        cursor.execute(f'SELECT * FROM "{table_name}" WHERE "{column}" = %s', (value,))
        data = cursor.fetchall()
        conn.close()
        return data

    def update_item(self, table_name, values):
        conn = connect_db()
        cursor = conn.cursor()
        
        if table_name == "Товары":
            cursor.execute(
                'UPDATE "Товары" SET "Категория"=%s, "Название"=%s, "Количество"=%s, "Цена"=%s, "ID поставщика"=%s WHERE "ID товара"=%s',
                values[1:] + [values[0]]
            )
        elif table_name == "Поставщики":
            cursor.execute(
                'UPDATE "Поставщики" SET "Название организации"=%s, "Контактная информация"=%s WHERE "ID поставщика"=%s',
                values[1:] + [values[0]]
            )
        elif table_name == "Заказы":
            cursor.execute(
                'UPDATE "Заказы" SET "Название"=%s, "Количество"=%s, "ID товара"=%s, "ID поставщика"=%s, "Категория"=%s WHERE "ID заказа"=%s',
                values[1:] + [values[0]]
            )
        
        conn.commit()
        conn.close()

    def add_item(self, table_name, data):
        conn = connect_db()
        cursor = conn.cursor()

        if table_name == "Товары":
            cursor.execute(
                'INSERT INTO "Товары" ("Категория", "Название", "Количество", "Цена", "ID поставщика") VALUES (%s, %s, %s, %s, %s)',
                data
            )
        elif table_name == "Поставщики":
            cursor.execute(
                'INSERT INTO "Поставщики" ("Название организации", "Контактная информация") VALUES (%s, %s)',
                data
            )
        elif table_name == "Заказы":
            cursor.execute(
                'INSERT INTO "Заказы" ("Название", "Количество", "ID товара", "ID поставщика", "Категория") VALUES (%s, %s, %s, %s, %s) RETURNING "ID заказа"',
                data[:5]
            )
            order_id = cursor.fetchone()[0]
            cursor.execute(
                'INSERT INTO "Статус" ("ID заказа", "Сроки", "Статус") VALUES (%s, %s, %s)',
                [order_id, data[5], data[6]]
            )

        conn.commit()
        conn.close()

    def delete_item(self, table_name, item_id):
        conn = connect_db()
        cursor = conn.cursor()

        if table_name == "Товары":
            cursor.execute('DELETE FROM "Товары" WHERE "ID товара" = %s', (item_id,))
        elif table_name == "Поставщики":
            cursor.execute('DELETE FROM "Поставщики" WHERE "ID поставщика" = %s', (item_id,))
        elif table_name == "Заказы":
            cursor.execute('DELETE FROM "Статус" WHERE "ID заказа" = %s', (item_id,))
            cursor.execute('DELETE FROM "Заказы" WHERE "ID заказа" = %s', (item_id,))

        conn.commit()
        conn.close()

    def get_order_status(self, order_id):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT "Сроки", "Статус" FROM "Статус" WHERE "ID заказа" = %s', (order_id,))
        status_info = cursor.fetchone()
        conn.close()
        return status_info

    def update_order_status(self, order_id, deadline, status):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE "Статус" SET "Сроки" = %s, "Статус" = %s WHERE "ID заказа" = %s',
            (deadline, status, order_id)
        )
        conn.commit()
        conn.close()

    def get_popular_products(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT p."ID товара", p."Категория", p."Название", COUNT(*) as count
            FROM "Товары" p
            JOIN "Заказы" o ON p."ID товара" = o."ID товара"
            GROUP BY p."ID товара", p."Категория", p."Название"
            ORDER BY count DESC
        ''')
        data = cursor.fetchall()
        conn.close()
        return data

    def get_frequent_vendors(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT p."ID поставщика", v."Название организации", v."Контактная информация", COUNT(*) as count
            FROM "Товары" p
            JOIN "Поставщики" v ON p."ID поставщика" = v."ID поставщика"
            GROUP BY p."ID поставщика", v."Название организации", v."Контактная информация"
            ORDER BY count DESC
        ''')
        data = cursor.fetchall()
        conn.close()
        return data