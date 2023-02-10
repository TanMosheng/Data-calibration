# -*- coding: UTF-8 -*-
# @Time : 2022/10/8 23:38
# @Author : Yao
# @File : data_rating.py
# @Software : PyCharm
import csv
import xlrd
import os
import pandas as pd
import sqlite3


class data_rating(object):
    excel_path = ""  # 工况记录表路径
    csv_path = ""  # 数据记录表路径
    file_path = ""  # 训练集存储路径
    file_name = ""  # 文件名称
    file_format = ""  # 文件格式
    conn = None
    cursor = None

    # 初始化函数
    def __init__(self, excel_path, csv_path, file_path, file_name, file_format):
        self.excel_path = excel_path
        self.csv_path = csv_path
        self.file_path = file_path
        self.file_name = file_name
        self.file_format = file_format

    # 根据输入字符串判断工况并输出对应的标号
    def judge_conditions(self, condition):
        if "钻头出井" in condition:
            return [0, 0]
        elif "钻进" in condition:
            return [1, 0]
        elif "划眼" in condition or "循环" in condition:
            return [2, 0]
        elif "接单根" in condition or "接立柱" in condition:
            return [3, 0]
        elif "起钻" in condition:
            return [4, 0]
        elif "下钻" in condition:
            return [5, 0]
        elif "设备维修" in condition or "拆" in condition or "装" in condition or "损坏" in condition:
            return [6, 0]
        elif "溢流" in condition:
            return [0, 1]
        else:
            return [7, 0]

    # 读取Excel表中的信息
    def read_excle(self, filePath, index, ishead=False):  # ishead为真，则不读取第一行
        try:
            excel = xlrd.open_workbook(filePath)
            sheet = excel.sheet_by_index(index)  # 获取工况工作簿
            data = []
            for i in range(sheet.nrows):
                data_list_i = sheet.row_values(i)
                if i == 0:
                    if ishead:
                        continue
                data.append(data_list_i)
            return data
        except Exception as e:
            print('Reason:', e)

    # 获取工况信息存入record,record中包含各个工况开始的时间以及序偶对
    # 工况第一行必须有数据
    def getrecord(self, filePath):
        condition_data = self.read_excle(filePath, 0, False)
        index_date = condition_data[0].index("日期")
        index_time = condition_data[0].index("时间")
        index_condition = condition_data[0].index("工况")
        record_date = condition_data[1][index_date]
        record_time = condition_data[1][index_time]
        record_condition = self.judge_conditions(condition_data[1][index_condition])
        tmp_list = [record_date, record_time, record_condition]
        records = []
        records.append(tmp_list)
        for i in range(2, len(condition_data)):
            if condition_data[i][index_date]:
                record_date = condition_data[i][index_date]
            if condition_data[i][index_time]:
                record_time = condition_data[i][index_time]
            if condition_data[i][index_condition]:
                # 出现新工况，将工况信息存入records
                if record_condition != self.judge_conditions(condition_data[i][index_condition]):
                    if self.judge_conditions(condition_data[i][index_condition]) == [7, 0]:
                        continue
                    record_condition = self.judge_conditions(condition_data[i][index_condition])
                    tmp_list = [record_date, record_time, record_condition]
                    records.append(tmp_list)
        return records

    # 读取csv中的信息
    def read_csv(self, filePath):
        data_list = []
        try:
            with open(filePath, 'r', encoding='utf-8') as f:
                f_reader = csv.reader(f)
                for row in f_reader:
                    data_list.append(row)
            return data_list
        except UnicodeDecodeError:
            with open(filePath, 'r', encoding='gbk') as f:
                f_reader = csv.reader(f)
                for row in f_reader:
                    data_list.append(row)
            return data_list
        except Exception as e:
            print('Reason:', e)

    # 判断日期先后，前者先于后者返回1，等于返回0，后于返回-1
    def judge_date(self, d1, d2):
        d1 = d1.replace("-", ".")
        d1 = "20" + d1
        if d1 < d2:
            return 1
        elif d1 == d2:
            return 0
        else:
            return -1

    # 根据日志和和数据获取xy训练集
    def get_xy_train(self, record, parameter_data):
        date_index = parameter_data[0].index("DateTime")
        cnt = 0  # 工况表计数器
        date_r = record[cnt][0]  # 日志日期
        time_r = record[cnt][1]  # 日志时间
        x_train = []
        y_train = []
        tmp = parameter_data[1][date_index]
        indexkong = tmp.find(' ')
        date_p = tmp[:indexkong]  # 参数日期
        time_p = float((int(tmp[indexkong + 1:indexkong + 3]) * 3600 + int(tmp[indexkong + 4:indexkong + 6]) * 60 +
                        int(tmp[indexkong + 7:])) / 86400)  # 参数时间
        # cnt为参数记录表起始工况的下标
        while self.judge_date(date_p, record[cnt + 1][0]) == -1 or (
                self.judge_date(date_p, record[cnt + 1][0]) == 0 and time_p >= record[cnt + 1][1]):
            cnt += 1
            date_r = record[cnt][0]
            time_r = record[cnt][1]
        for i in range(1, len(parameter_data)):
            tmp = parameter_data[i][date_index]
            date_p = tmp[:indexkong]
            time_p = float((int(tmp[indexkong + 1:indexkong + 3]) * 3600 + int(tmp[indexkong + 4:indexkong + 6]) * 60 +
                            int(tmp[indexkong + 7:])) / 86400)  # 参数时间
            # 参数日期早于当前日期，状态设空井
            if self.judge_date(date_p, date_r) == 1 or (self.judge_date(date_p, date_r) == 0 and time_p < time_r):
                y_train.append([0, 0])
            elif cnt == len(record) - 1:  # 工况日志到尾部，后面的工况不确定，状态设空井
                y_train.append([0, 0])
            # 工况情况发生变化
            elif self.judge_date(date_p, record[cnt + 1][0]) == -1 or (
                    self.judge_date(date_p, record[cnt + 1][0]) == 0 and time_p >= record[cnt + 1][1]):
                y_train.append(record[cnt + 1][2])
                cnt += 1
                date_r = record[cnt][0]
                time_r = record[cnt][1]
            else:
                y_train.append(record[cnt][2])
            x_train.append(parameter_data[i])
        return x_train, y_train

    # 将xy训练集输入csv文件中
    def write_csv(self, xfilePath, yfilePath, x_train, y_train):
        try:
            f1 = open(xfilePath, 'w', newline="")
            csv_write1 = csv.writer(f1)
            for data in x_train:
                csv_write1.writerow(data)
            f1.close()
        except Exception as e:
            print('Reason:', e)
        try:
            f2 = open(yfilePath, 'w', newline="")
            csv_write2 = csv.writer(f2)
            for data in y_train:
                csv_write2.writerow(data)
            f2.close()
        except Exception as e:
            print('Reason:', e)

    # 将xy训练集输入到db文件中
    def write_db(self, x_train, y_train):
        db_path = self.file_path + "/" + self.file_name + ".sqlite"
        self.conn = sqlite3.connect(db_path)  # 打开或创建 链接数据库文件
        cnt = 0
        train = []
        for i in range(len(x_train)):
            tmp = x_train[cnt] + y_train[cnt]
            train.append(tmp)
            cnt += 1
        try:
            # 创建训练集的数据库
            try:
                self.cursor = self.conn.cursor()  # 获取游标

                create_db_sql = """create table if not exists trainTable 
                                (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    DateTime datetime not null,
                                    WorkTime number not null,
                                    井深 varchar(20) not null,
                                    垂深 varchar(20) not null,
                                    钻头深度 varchar(20) not null,
                                    钻头垂深 varchar(20) not null,
                                    平均钻速 varchar(20) not null,
                                    平均钻压 varchar(20) not null,
                                    大钩负荷 varchar(20) not null,
                                    转盘转速 varchar(20) not null,
                                    扭矩 varchar(20) not null,
                                    方入 varchar(20) not null,
                                    大钩位置 varchar(20) not null,
                                    大钩速度 varchar(20) not null,
                                    立压log varchar(20) not null,
                                    套压 varchar(20) not null,
                                    泵冲1 varchar(20) not null,
                                    泵冲2 varchar(20) not null,
                                    泵冲3 varchar(20) not null,
                                    总池体积 varchar(20) not null,
                                    迟到时间 varchar(20) not null,
                                    泥浆溢漏 varchar(20) not null,
                                    入口流量log varchar(20) not null,
                                    出口流量log varchar(20) not null,
                                    入口密度log varchar(20) not null,
                                    出口密度log varchar(20) not null,
                                    入口温度 varchar(20) not null,
                                    出口温度 varchar(20) not null,
                                    总烃 varchar(20) not null,
                                    H2S varchar(20) not null,
                                    C1 varchar(20) not null,
                                    C2 varchar(20) not null,
                                    PWD深度 varchar(20) not null,
                                    PWD垂深 varchar(20) not null,
                                    PWD钻柱压力 varchar(20) not null,
                                    PWD环空压力 varchar(20) not null,
                                    PWD环空温度 varchar(20) not null,
                                    PWD测量ECD varchar(20) not null,
                                    PWD井斜 varchar(20) not null,
                                    PWD方位 varchar(20) not null,
                                    注替体积 varchar(20) not null,
                                    上返深度 varchar(20) not null,
                                    MPD_ST varchar(20) not null,
                                    PT103 varchar(20) not null,
                                    PT104 varchar(20) not null,
                                    FDT101 varchar(20) not null,
                                    FDT101_DT varchar(20) not null,
                                    FDT201 varchar(20) not null,
                                    循环回压 varchar(20) not null,
                                    附加回压 varchar(20) not null,
                                    入口流量 varchar(20) not null,
                                    定点深度 varchar(20) not null,
                                    定点垂深 varchar(20) not null,
                                    定点压力 varchar(20) not null,
                                    井口调节压力 varchar(20) not null,
                                    定点压耗 varchar(20) not null,
                                    波动压力 varchar(20) not null,
                                    压耗修正因子 varchar(20) not null,
                                    起下钻速度 varchar(20) not null,
                                    起下钻加速度 varchar(20) not null,
                                    定点ECD varchar(20) not null,
                                    钻头ECD varchar(20) not null,
                                    钻柱压降 varchar(20) not null,
                                    钻头压降 varchar(20) not null,
                                    环空压耗 varchar(20) not null,
                                    目标回压 varchar(20) not null,
                                    静液压力 varchar(20) not null,
                                    正常工况 varchar(2) not null,
                                    异常工况 varchar(2) not null
                                );
                            """
                self.cursor.execute(create_db_sql)  # 执行建表操作
                self.conn.commit()  # 提交数据库操作
                self.cursor.close()
            except sqlite3.Error as error:
                print("Failed to create a trainTable", error)

            sqlite_insert_query = """insert into trainTable( DateTime, WorkTime, 井深, 垂深, 钻头深度, 钻头垂深, 平均钻速, 平均钻压, 
                大钩负荷, 转盘转速, 扭矩, 方入, 大钩位置, 大钩速度, 立压log, 套压, 泵冲1, 泵冲2, 泵冲3, 总池体积, 迟到时间, 泥浆溢漏, 
                入口流量log, 出口流量log, 入口密度log, 出口密度log, 入口温度, 出口温度, 总烃, H2S, C1, C2, PWD深度, PWD垂深, 
                PWD钻柱压力, PWD环空压力, PWD环空温度, PWD测量ECD, PWD井斜, PWD方位, 注替体积, 上返深度, MPD_ST, PT103, PT104,
                FDT101, FDT101_DT, FDT201, 循环回压, 附加回压, 入口流量, 定点深度, 定点垂深, 定点压力, 井口调节压力, 定点压耗, 波动压力,
                压耗修正因子, 起下钻速度, 起下钻加速度, 定点ECD, 钻头ECD, 钻柱压降, 钻头压降, 环空压耗, 目标回压, 静液压力, 正常工况, 异常工况 ) values (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """
            self.cursor = self.conn.cursor()
            self.cursor.executemany(sqlite_insert_query, train)
            self.conn.commit()
            self.cursor.close()
        except sqlite3.Error as error:
            print("Failed to insert variables into trainTable:", error)
        finally:
            if self.conn:
                self.conn.close()

    # 处理数据
    def handle_data(self):
        csv_path = self.csv_path
        name = self.file_name
        xfilePath = self.file_path + "/trainx_" + name + ".csv"
        yfilePath = self.file_path + "/trainy_" + name + ".csv"
        record = self.getrecord(self.excel_path)
        parameter_data = self.read_csv(csv_path)
        (x_train, y_train) = self.get_xy_train(record, parameter_data)
        if self.file_format == "csv":
            self.write_csv(xfilePath, yfilePath, x_train, y_train)
        elif self.file_format == "db":
            self.write_db(x_train, y_train)
