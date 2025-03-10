import pandas as pd
import numpy as np
import openpyxl
import re
import ast


fisrt_page = pd.read_excel("C:/Users/user/Desktop/tables.xlsx")
second_page = pd.read_excel("C:/Users/user/Desktop/tables.xlsx", sheet_name=1)

# Добовляем поле request_id
fisrt_page["request_id"] = fisrt_page["special_marks"].apply(lambda x: ast.literal_eval(x)["request_id"])

# Объединяем таблицы
merged_df = fisrt_page.merge(second_page, left_on="request_id", right_on="id", how="inner")

# Добавляем поле total_amount
merged_df["total_amount"] = merged_df["requested_amount"] + merged_df["approved_amount"]

# # Группируем по промокоду и считаем сумму
result = merged_df.groupby("promocode")["total_amount"].sum().reset_index()
print(result)

with open("result.txt", "w") as f:
    f.write(result.to_string(index=False))