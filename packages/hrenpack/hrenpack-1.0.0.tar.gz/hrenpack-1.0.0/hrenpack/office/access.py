import pyodbc
from typing import Optional
from hrenpack.dbwork import Database


class AccessDatabase(Database):
    def __init__(self, path: str, default_condition_title: Optional[str] = None, auto_save: bool = False):
        con_str = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            fr'DBQ={path};'
        )
        super().__init__(pyodbc.connect(con_str), path, default_condition_title, auto_save)


if __name__ == '__main__':
    db = AccessDatabase('D:/Воронины/Воронины.accdb', '№', True)
    # db.create("Галя, жрать", __fields__={"Сезон": 13, "Серия": 19, "Таймкод": "13:50"})
    for el in db.read("Галя, жрать", __fields__={"Сезон": True, "Серия": True}):
        print(*el)
