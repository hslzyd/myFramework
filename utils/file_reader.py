"""
读取ini，excel等文件的工具类
"""
import configparser
import os
from xlrd import open_workbook


class INIReader:
    """
    读取ini文件，实例化时传入ini文件名
    """
    def __init__(self, ini_file):
        if os.path.exists(ini_file):
            self.ini_file = ini_file
        else:
            raise FileNotFoundError("配置文件不存在！")
        self._data = None

    @property
    def data(self):
        if not self._data:
            cp = configparser.ConfigParser()
            cp.read(self.ini_file, encoding="utf-8")
            self._data = cp
        return self._data


class SheetTypeError(Exception):
    pass


class ExcelReader:
    """
    读取excel文件，实例化时传入excel文件名，sheet表索引index（从0开始算）或表名，表格列数，以及第一行是否为标题
    """
    def __init__(self, excel, sheet=0, title_line=True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError("Excel文件不存在！")
        self.sheet = sheet
        self.title_line = title_line
        self._data = list()

    @property
    def data(self):
        if not self._data:
            workbook = open_workbook(self.excel)
            if type(self.sheet) == int:
                table = workbook.sheet_by_index(self.sheet)
            elif type(self.sheet) == str:
                table = workbook.sheet_by_name(self.sheet)
            else:
                raise SheetTypeError("输入的sheet类型应是<int>索引值或<str>表名，不是{0}".format(type(self.sheet)))

            if self.title_line:
                title = table.row_values(0)  # 第一行是标题
                for col in range(1, table.nrows):
                    self._data.append(dict(zip(title, table.row_values(col))))
            else:
                for col in range(0, table.nrows):
                    self._data.append(table.row_values(col))
        return self._data


if __name__ == "__main__":
    e1 = 'D:\\Work\\test\\projects\\myFramework\\data\\test1.xlsx'
    e2 = 'D:\\Work\\test\\projects\\myFramework\\data\\test2.xlsx'
    reader1 = ExcelReader(e1, title_line=True)
    reader2 = ExcelReader(e2, title_line=False)
    print(reader1.data)
    print("——————————————————————————————————")
    print(reader2.data)
