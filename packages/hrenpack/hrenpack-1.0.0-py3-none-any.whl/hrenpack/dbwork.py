import sqlite3
from typing import Union, Optional, Any, Literal
from hrenpack.listwork import split_list, tuplist, key_in_dict, merging_dictionaries

ulo_fields = Optional[Union[tuplist, Literal['*']]]


class Database:
    def __init__(self, connect, path: str, default_condition_title: Optional[str] = None, auto_save: bool = False):
        self.connect = connect
        self.cursor = self.connect.cursor()
        self.path = path
        self.default_condition_title = default_condition_title
        self.auto_save = auto_save

    def save(self):
        self.connect.commit()

    def save_auto(self):
        if self.auto_save:
            self.connect.commit()

    def read(self, table: str, fields: ulo_fields = '*', **order_by: Union[bool, dict[str, bool]]):
        """:param order_by: Пример: field1=True = ORDER BY field1 DESC"""
        def query(table: str, fields: ulo_fields) -> tuple:
            if fields in (None, '*'):
                fields = '*'
            else:
                fields = ', '.join(['{}'.format(f) for f in fields])
            return fields, table

        order_by = self.fields_kwargs(order_by, False)
        if order_by:
            order = ', '.join(['{} {}'.format(f, 'DESC' if o else 'ASC') for f, o in order_by.items()])
            order = 'ORDER BY ' + order
        else:
            order = ''
        self.cursor.execute('SELECT {} FROM [{}] {}'.format(*query(table, fields), order))
        return self.cursor.fetchall()

    @staticmethod
    def fields_kwargs(kwargs: dict, string_format: bool = True, fields_: str = '__fields__') -> dict:
        if key_in_dict(kwargs, '__fields__'):
            kwargs = merging_dictionaries(kwargs, kwargs[fields_])
            del kwargs['__fields__']
        for key, value in kwargs.items():
            if type(value) is str and string_format:
                value = f"'{value}'"
            kwargs[key] = str(value)
        return kwargs

    def create(self, table: str, **fields):
        fields = self.fields_kwargs(fields)
        keys = tuple(fields.keys())
        values = tuple(fields.values())
        self.cursor.execute('INSERT INTO [{}] ({}) VALUES ({})'.format(table, ', '.join(keys), ', '.join(values)))
        self.save_auto()

    def update(self, table: str, condition, condition_title: Optional[str] = None, **fields):
        if self.default_condition_title and condition_title is None:
            condition_title = self.default_condition_title
        fields = self.fields_kwargs(fields)
        for key, value in fields.items():
            self.cursor.execute('UPDATE [{}] SET {} = {} WHERE {} = {}'.format(table, key, value,
                                                                               condition_title, condition))
        self.save_auto()

    def delete(self, table: str, condition, condition_title: Optional[str] = None):
        if self.default_condition_title and condition_title is None:
            condition_title = self.default_condition_title
        self.cursor.execute('DELETE FROM [{}] WHERE {} = {}'.format(table, condition_title, condition))
        self.save_auto()

    def create_table(self, name: str, pk: str = 'id', **fields):
        """:param fields: Пример: id='INTEGER PRIMARY KEY'"""
        fields = self.fields_kwargs(fields, False)
        fields[pk] = 'AUTOINCREMENT PRIMARY KEY'
        fields_list = list()
        for key, value in fields.items():
            fields_list.append(f'{key} {value}')
        self.cursor.execute('CREATE TABLE [{}] ({})'.format(name, ', '.join(fields_list)))
        self.save_auto()

    def remove_table(self, name: str):
        self.cursor.execute('DROP TABLE [{}]'.format(name))

    def execute(self, query, *args, **kwargs) -> None:
        self.cursor.execute(query, *args, **kwargs)

    def clean_table(self, name: str):
        self.cursor.execute(f"DELETE FROM [{name}]")


class Sqlite3Database(Database):
    def __init__(self, path: str, default_condition_title: Optional[str] = None, auto_save: bool = False):
        super().__init__(sqlite3.connect(path), path, default_condition_title, auto_save)

    # def copy_to_access(self, *tables: str, output_db: AccessDatabase):
    #     self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    #     tables = self.cursor.fetchall()
    #
    #     for table in tables:
    #         table_name = table[0]
    #         self.cursor.execute(f"SELECT * FROM {table_name}")
    #         rows = self.cursor.fetchall()
