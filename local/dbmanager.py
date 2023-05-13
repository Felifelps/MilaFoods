import sqlite3

class DbManager:
    def __init__(self, database='database.db'):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
    
    def commit(self): 
        self.conn.commit()
    
    def close(self): 
        self.conn.close()
        
    def execute(self, sql):
        self.cursor.execute(sql)
    
    def select_all(self, table): 
        self.cursor.execute('select * from {};'.format(table))
        return list(self.cursor.fetchall())
    
    def create_table(self, table_name: str, fields: list[list]):
        '''
        Creates a table. The fields parameter follows the pattern:
        [(name, *attributes)] or [(all_line)]
        '''
        sql = f'create table {table_name} (\n'
        for field in fields:
            sql += f'{field[0]}'
            for attr in field:
                if attr == field[0]: continue
                sql += f' {attr}'
            sql += (',' if field != fields[-1] else '') + '\n'
        self.execute(sql + ');')
    
    def insert(self, table_name: str, insert: dict):
        '''
        Inserts data into a table.
        '''
        sql = f'insert into {table_name} '
        columns = list(insert.keys())
        values = list(insert.values())
        if len(columns) > 0: sql += '('
        for column in columns:
            sql += column 
            if column != columns[-1]: sql += ', '
        if len(columns) > 0: sql += ')'
        sql += ' values ('
        for value in values:
            if 'str' in str(type(value)): sql += f"'{value}'"
            else: sql += f'{value}'
            if value != values[-1]: sql += ', '
        sql += ');'
        self.execute(sql)
        self.commit()

    def update(self, table_name: str, update: dict, where: str):
        '''
        Updates data into a table. 
        Update must be {name_of_column: new_value}.
        '''
        sql = f'update {table_name} set '
        for column, value in update.items():
            sql += column + ' = '
            if 'str' in str(type(value)): sql += f"'{value}'"
            else: sql += f'{value}'
            if column != list(update)[-1]: sql += ', '
        sql += ' where ' + where + ';'
        self.execute(sql)
        self.commit()
    
    def delete(self, table_name: str, where: str):
        '''
        Deletes data into a table.
        '''
        sql = f'delete from {table_name} where {where};'
        self.execute(sql)
        self.commit()
    
    def new_column(self, table_name: str, column_line: list[str]):
        sql = f'alter table {table_name} add column {column_line};'
        self.execute(sql)
        self.commit()
    
    def delete_table(self, table_name: str):
        sql = f'drop table {table_name};'
        self.execute(sql)
        self.commit()
        