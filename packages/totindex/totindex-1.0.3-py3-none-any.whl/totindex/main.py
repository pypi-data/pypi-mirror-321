# totindex/main.py

import tkinter as tk
from tkinter import filedialog, messagebox, Menu, ttk, Toplevel, Label
import pandas as pd
import numpy as np
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
import os
import pkg_resources  # 用于访问包内数据文件

# 在这里定义Tooltip类
class Tooltip:
    def __init__(self, widget, text='Tooltip'):
        self.widget = widget
        self.text = text
        self.tooltip_window = None

    def enter(self, event=None):
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tooltip_window = Toplevel(self.widget)
        self.tooltip_window.wm_overrideredirect(True)
        self.tooltip_window.wm_geometry("+%d+%d" % (x, y))
        label = Label(self.tooltip_window, text=self.text, justify='left',
                      background='#ffffff', relief='solid', borderwidth=1,
                      font=("times", "8", "normal"))
        label.pack(ipadx=1)

    def leave(self, event=None):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None

class App:
    def __init__(self, root):
        self.root = root
        self.setup_ui()
        self.df = None  # 初始化DataFrame为None

    def setup_ui(self):
        self.root.title("TOT指数计算器 V1.0")
        self.root.geometry('780x585')  # 设置初始窗口大小
        self.root.resizable(False, False)  # 禁用窗口大小调整，包括最大化按钮
        self.root.configure(bg='#f5f4f1')
        content_frame = tk.Frame(self.root)
        content_frame.pack(expand=True, fill="both")
        # 设置按钮颜色
        button_bg_color = "#b6ccd8"
        button_fg_color = "black"

        # 调整列的权重以使它们在窗口调整大小时能够均匀分配空间
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=1)
        content_frame.grid_columnconfigure(2, weight=1)


        # 大标题:
        row_1_bg = tk.Frame(content_frame, bg='#d3d3d3', height=120)
        row_1_bg.grid(row=0, column=0, columnspan=3, sticky='ew')
        row_1_bg.grid_propagate(False)  # 禁止背景Frame根据内部内容调整大小
        label_in_row_1 = tk.Label(row_1_bg,
                                  text="“主题-目标-工具(Topics-Objectives-Tools, TOT)”\n政策文本设计质量指数计算器",
                                  font=("Microsoft YaHei",18),bg='#d3d3d3')
        label_in_row_1.place(relx=0.5, rely=0.5, anchor='center')  # 使用place布局使标签居中

        # 开发者:
        developer_label = tk.Label(content_frame, text="开发者：张祚、侯文姣、刘晓歌", font=("KaiTi", 15))
        developer_label.grid(row=1, column=0, columnspan=3, sticky='ew', padx=(10, 10), pady=(10, 5))
        # 单位:
        unit_label = tk.Label(content_frame, text="单位：华中师范大学公共管理学院", font=("KaiTi", 15))
        unit_label.grid(row=2, column=0, columnspan=3, sticky='ew', padx=(10, 10), pady=(5, 10))

        # 计算模组:
        row_4_bg = tk.Frame(content_frame, bg='#d3d3d3', height=50)  # 设置背景色和高度
        row_4_bg.grid(row=3, column=0, columnspan=3, sticky='ew')  # 让背景Frame横跨所有列
        row_4_bg.grid_propagate(False)  # 禁止背景Frame根据内部内容调整大小
        module_label = tk.Label(row_4_bg, text="计算模组", font=("SimSun", 15,"bold"), bg='#d3d3d3')
        module_label.place(relx=0.17, rely=0.5, anchor='center')  # 使用place布局
        # step1-3:
        row_5_bg = tk.Frame(content_frame, bg='#d3d3d3', height=60)
        row_5_bg.grid(row=4, column=0, columnspan=3, sticky='ew')  # 确保背景Frame横跨所有列
        row_5_bg.grid_propagate(False)  # 禁止背景Frame根据内部内容调整大小
        row_5_bg.grid_columnconfigure(0, weight=1, uniform="group1")
        row_5_bg.grid_columnconfigure(1, weight=1, uniform="group1")
        row_5_bg.grid_columnconfigure(2, weight=1, uniform="group1")
        btn_import_options = tk.Button(row_5_bg, text="Step1:导入", command=self.open_file_options, bg=button_bg_color,
                                       fg=button_fg_color, padx=24, pady=8, font=("Microsoft YaHei", 11))
        btn_import_options.grid(row=0, column=0, padx=(5, 5), pady=(0, 15))
        btn_assign = tk.Button(row_5_bg, text="Step2:赋值", command=self.assign_values, bg=button_bg_color,
                               fg=button_fg_color, padx=24, pady=8, font=("Microsoft YaHei", 11))
        btn_assign.grid(row=0, column=1, padx=(5, 5), pady=(0, 15))
        btn_calculate = tk.Button(row_5_bg, text="Step3:计算", command=self.calculate, bg=button_bg_color,
                                  fg=button_fg_color, padx=24, pady=8, font=("Microsoft YaHei", 11))
        btn_calculate.grid(row=0, column=2, padx=(5, 5), pady=(0, 15))

        # 空白行：
        blank_row = tk.Frame(content_frame, height=35)  # 可以通过调整height的值来控制空白行的高度
        blank_row.grid(row=5, column=0, columnspan=3, sticky='ew')
        blank_row.grid_propagate(False)  # 防止Frame根据内部内容调整大小，确保高度保持为设置的值

        # 绘图模组：
        row_7_bg = tk.Frame(content_frame, bg='#d3d3d3', height=50)  # 设置背景色和高度
        row_7_bg.grid(row=6, column=0, columnspan=3, sticky='ew')  # 让背景Frame横跨所有列
        row_7_bg.grid_propagate(False)  # 禁止背景Frame根据内部内容调整大小
        module_label = tk.Label(row_7_bg, text="绘图模组", font=("SimSun", 15,"bold"), bg='#d3d3d3')
        module_label.place(relx=0.17, rely=0.5, anchor='center')  # 使用place布局
        # step4-6：
        row_8_bg = tk.Frame(content_frame, bg='#d3d3d3', height=60)
        row_8_bg.grid(row=7, column=0, columnspan=3, sticky='ew')  # 确保背景Frame横跨所有列
        row_8_bg.grid_propagate(False)  # 禁止背景Frame根据内部内容调整大小
        row_8_bg.grid_columnconfigure(0, weight=1, uniform="group1")
        row_8_bg.grid_columnconfigure(1, weight=1, uniform="group1")
        row_8_bg.grid_columnconfigure(2, weight=1, uniform="group1")

        btn_plot_1d = tk.Button(row_8_bg, text="Step4:单维绘图", command=self.plot_single_dimension, bg=button_bg_color,
                                fg=button_fg_color, padx=9, pady=8, font=("Microsoft YaHei", 11))
        btn_plot_1d.grid(row=0, column=0, padx=(5, 5), pady=(0, 25))
        btn_plot_2d = tk.Button(row_8_bg, text="Step5:二维绘图", command=self.plot_two_dimension, bg=button_bg_color,
                                fg=button_fg_color, padx=9, pady=8, font=("Microsoft YaHei", 11))
        btn_plot_2d.grid(row=0, column=1, padx=(5, 5), pady=(0, 25))
        btn_plot_3d = tk.Button(row_8_bg, text="Step6:三维绘图", command=self.plot_three_dimension, bg=button_bg_color,
                                fg=button_fg_color, padx=9, pady=8, font=("Microsoft YaHei", 11))
        btn_plot_3d.grid(row=0, column=2, padx=(5, 5), pady=(0, 25))

        # 软件详情:
        developer_label_1 = tk.Label(content_frame, text="软件详情可参考：《中国土地科学》2024年12月发表的论文：",
                                     font=("Microsoft YaHei", 11))
        developer_label_1.grid(row=8, column=0, columnspan=3, sticky='ew', padx=10, pady=(25, 5))


        developer_label_2 = tk.Label(content_frame, text="基于“主题-目标-工具”的耕地保护政策文本分析：框架、方法及其应用",
                                     font=("Microsoft YaHei", 11))
        developer_label_2.grid(row=9, column=0, columnspan=3, sticky='ew', padx=10, pady=(0, 5))

        # 软件说明：
        software_info_button = tk.Button(content_frame, text="软件说明", font=("Microsoft YaHei", 8),command=self.show_software_info)
        software_info_button.grid(row=10, column=2, sticky='se', padx=20, pady=(0, 5))

    def show_software_info(self):
        software_info = """
      一、本计算器的“导入”按钮提供两种选项。选择1可导入论文实验数据，选择2则允许用户自行加载数据。为确保本软件能够正确处理您的数据，请遵循以下Excel文件格式要求：
      （一）第一行：政策编号
       从第四列开始代表一个不同的政策（P1、P2、P3等）。
      （二）前三列：分别代表一级变量、二级变量和三级变量的名称
       1、第一列（一级变量）：描述政策的主题或其他（例如，“X政策主题”）。
       2、第二列（二级变量）：提供更具体的政策方面（例如，“X1加强示范试点”）。
       3、第三列（三级变量）：进一步细分政策的具体点，如果没有可标记为“无”。
      （三）数据行
       1、X数据：首4行包含与X政策主题相关的数据。
       2、Y数据：接下来的3行包含与Y政策目标相关的数据。
       3、Z数据：随后的14行包含与Z政策工具相关的具体数据。

      二、赋值原理：根据每行有效数据的分位数范围，分别赋值为0,0.25,0.5,0.75和1。

      三、计算结果默认保存在当前TOT程序所在位置。

        """

        tk.messagebox.showinfo("软件说明", software_info)

    def open_file_options(self):
        self.top = tk.Toplevel()
        self.top.title("选择导入方式")
        self.top.geometry('300x200')

        label = tk.Label(self.top, text="请选择要导入的数据方式：", font=("Arial", 12))
        label.pack(pady=10)

        button1 = tk.Button(self.top, text="选择1：论文的实验数据", command=self.choose_option1)
        button1.pack(pady=10)

        button2 = tk.Button(self.top, text="选择2：计算机本地数据", command=self.choose_option2)
        button2.pack(pady=10)

    def choose_option1(self):
        self.reset_df()  # 在加载数据前重置self.df

        try:
            # 使用 pkg_resources 访问包内的数据文件
            filename = pkg_resources.resource_filename('totindex', 'data/TOT_Experimental_Data.xlsx')
            self.df = pd.read_excel(filename)
            messagebox.showinfo("成功", "论文的实验数据已成功导入。")
            self.top.destroy()  # 关闭选择导入方式的小窗口
        except Exception as e:
            messagebox.showerror("错误", f"导入论文的实验数据时出错：{e}")

    def choose_option2(self):
        self.reset_df()  # 在加载数据前重置self.df
        filename = filedialog.askopenfilename(title="选择文件", filetypes=[("Excel files", "*.xlsx;*.xls")])
        if filename:
            try:
                self.df = pd.read_excel(filename)
                messagebox.showinfo("提示", "计算机本地数据文件成功加载！")
                self.top.destroy()  # 关闭选择导入方式的小窗口
            except Exception as e:
                messagebox.showerror("错误", f"导入计算机本地数据文件时出错：{e}")

    def reset_df(self):
        self.df = None  # 或者 self.df = pd.DataFrame()

    def assign_values(self):
        if self.df is not None:
            # 应用赋值逻辑，确保包括x1所在的行
            data = self.df.iloc[:, 3:]  # 假设x1等变量从第四列开始
            assigned_data = data.apply(self.apply_rules, axis=1)
            # 更新self.df以包含赋值后的数据
            self.df = pd.concat([self.df.iloc[:, :3], assigned_data], axis=1)
            # 保存赋值后的数据到Excel文件，同时优化排版
            self.save_to_excel(self.df, "赋值后数据.xlsx")
            messagebox.showinfo("信息", "赋值完成并已保存")
        else:
            messagebox.showwarning("警告", "数据未加载，请先加载数据。")

    def save_to_excel(self, df, file_name):
        with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)
            workbook = writer.book
            worksheet = writer.sheets['Sheet1']
            for col in worksheet.columns:
                max_length = max(len(str(cell.value)) for cell in col)
                adjusted_width = (max_length + 2)
                worksheet.column_dimensions[col[0].column_letter].width = adjusted_width

    def apply_rules(self, row):
        quantiles = np.quantile(row.dropna(), [0.125, 0.375, 0.625, 0.875])
        return row.apply(lambda x:
                         0 if x <= quantiles[0] else
                         0.25 if x <= quantiles[1] else
                         0.5 if x <= quantiles[2] else
                         0.75 if x <= quantiles[3] else
                         1)

    def display_data(self, df):
        self.tree["columns"] = [f"Column_{i}" for i in range(len(df.columns))]
        for i, col in enumerate(df.columns):
            col_id = f"Column_{i}"
            self.tree.heading(col_id, text=col)  # 使用原始列名作为标题文本
            self.tree.column(col_id, width=100, anchor='center')
        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))

    def calculate(self):
        if self.df is not None:
            # 获取政策数量，减去前三列非政策数据列
            num_policies = len(self.df.columns) - 3

            # 创建结果DataFrame的列标签，直接使用政策编号
            column_labels = ['得分类型'] + [f'P{i}' for i in range(1, num_policies + 1)]

            # 初始化结果DataFrame，此时不指定行索引，因为我们将使用一个列来表示得分类型
            results_df = pd.DataFrame(columns=column_labels)

            # 添加得分类型作为第一列数据
            results_df['得分类型'] = ['X得分', 'Y得分', 'Z1得分', 'Z2得分', 'Z3得分', 'Z得分', 'TOT结果']

            # 计算得分并填充到results_df中
            for i in range(num_policies):  # 遍历每一个政策
                col_data = self.df.iloc[:, i + 3]  # 跳过前三列
                x_score = col_data.iloc[0:4].mean()
                y_score = col_data.iloc[4:7].mean()
                z1_score = col_data.iloc[7:11].mean()
                z2_score = col_data.iloc[11:17].mean()
                z3_score = col_data.iloc[17:23].mean()
                z_score = np.mean([z1_score, z2_score, z3_score])
                tot_score = x_score + y_score + z_score

                # 填充得分到对应的列中
                results_df.loc[results_df['得分类型'] == 'X得分', f'P{i + 1}'] = x_score
                results_df.loc[results_df['得分类型'] == 'Y得分', f'P{i + 1}'] = y_score
                results_df.loc[results_df['得分类型'] == 'Z1得分', f'P{i + 1}'] = z1_score
                results_df.loc[results_df['得分类型'] == 'Z2得分', f'P{i + 1}'] = z2_score
                results_df.loc[results_df['得分类型'] == 'Z3得分', f'P{i + 1}'] = z3_score
                results_df.loc[results_df['得分类型'] == 'Z得分', f'P{i + 1}'] = z_score
                results_df.loc[results_df['得分类型'] == 'TOT结果', f'P{i + 1}'] = tot_score

            # 保存到Excel文件，不包括索引
            results_df.to_excel("计算结果.xlsx", index=False)

            # 添加计算完成的弹窗提示
            messagebox.showinfo("信息", "计算完成并已保存")
        else:
            messagebox.showwarning("警告", "数据未加载，请先加载数据。")

    def plot_single_dimension(self):
        # 检查是否已加载数据
        if self.df is None or self.df.empty:
            messagebox.showwarning("警告", "数据未加载，请先加载数据。")
            return
        # 加载 "计算结果.xlsx" 文件
        try:
            results_df = pd.read_excel("计算结果.xlsx")
            print("计算结果数据加载成功！")
        except Exception as e:
            print(f"加载计算结果数据时出错：{str(e)}")
            return

        plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置使用的中文字体
        plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题

        # 提取需要绘制的数据
        x_scores = results_df.loc[results_df['得分类型'] == 'X得分'].iloc[:, 1:].values.flatten()
        y_scores = results_df.loc[results_df['得分类型'] == 'Y得分'].iloc[:, 1:].values.flatten()
        z_scores = results_df.loc[results_df['得分类型'] == 'Z得分'].iloc[:, 1:].values.flatten()
        tot_results = results_df.loc[results_df['得分类型'] == 'TOT结果'].iloc[:, 1:].values.flatten()

        plt.figure(figsize=(10, 6))

        # 绘制散点图
        plt.scatter(range(1, len(x_scores) + 1), x_scores, color='r', label='X得分')
        plt.scatter(range(1, len(y_scores) + 1), y_scores, color='g', label='Y得分')
        plt.scatter(range(1, len(z_scores) + 1), z_scores, color='b', label='Z得分')
        plt.scatter(range(1, len(tot_results) + 1), tot_results, color='k', label='TOT结果')

        plt.title('单维得分与TOT结果')
        plt.xlabel('政策编号')
        plt.ylabel('得分')
        plt.legend()
        plt.show()

    def plot_two_dimension(self):
        if self.df is not None:
            # 加载 "计算结果.xlsx" 文件
            try:
                results_df = pd.read_excel("计算结果.xlsx")
                print("计算结果数据加载成功！")
            except Exception as e:
                print(f"加载计算结果数据时出错：{str(e)}")
                return
            # 获取X、Y和Z得分以及TOT结果
            x_scores = results_df.loc[results_df['得分类型'] == 'X得分'].iloc[:, 1:].values.flatten()
            y_scores = results_df.loc[results_df['得分类型'] == 'Y得分'].iloc[:, 1:].values.flatten()
            z_scores = results_df.loc[results_df['得分类型'] == 'Z得分'].iloc[:, 1:].values.flatten()
            tot_results = results_df.loc[results_df['得分类型'] == 'TOT结果'].iloc[:, 1:].values.flatten()

            # 绘制XY得分图
            self.plot_bubble_chart_2d(x_scores, y_scores, tot_results, 'XY得分', 'X得分', 'Y得分')

            # 绘制YZ得分图
            self.plot_bubble_chart_2d(y_scores, z_scores, tot_results, 'YZ得分', 'Y得分', 'Z得分')

            # 绘制XZ得分图
            self.plot_bubble_chart_2d(x_scores, z_scores, tot_results, 'XZ得分', 'X得分', 'Z得分')
        else:
            messagebox.showwarning("警告", "数据未加载，请先加载数据。")

    def plot_bubble_chart_2d(self, x_scores, y_scores, tot_results, title, x_label, y_label):
        plt.figure(figsize=(10, 6))
        plt.scatter(x_scores, y_scores, s=tot_results * 100, alpha=0.5)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.grid(True)
        plt.show()

    def plot_three_dimension(self):
        if self.df is not None:
            # 加载 "计算结果.xlsx" 文件
            try:
                results_df = pd.read_excel("计算结果.xlsx")
                print("计算结果数据加载成功！")
            except Exception as e:
                print(f"加载计算结果数据时出错：{str(e)}")
                return
            # 获取XY、YZ和XZ得分以及TOT结果
            x_scores = results_df.loc[results_df['得分类型'] == 'X得分'].iloc[:, 1:].values.flatten()
            y_scores = results_df.loc[results_df['得分类型'] == 'Y得分'].iloc[:, 1:].values.flatten()
            z_scores = results_df.loc[results_df['得分类型'] == 'Z得分'].iloc[:, 1:].values.flatten()
            tot_results = results_df.loc[results_df['得分类型'] == 'TOT结果'].iloc[:, 1:].values.flatten()

            # 绘制气泡图
            self.plot_bubble_chart(x_scores, y_scores, z_scores, tot_results, 'XYZ得分', 'X得分', 'Y得分', 'Z得分')
        else:
            messagebox.showwarning("警告", "数据未加载，请先加载数据。")

    def plot_bubble_chart(self, x_scores, y_scores, z_scores, tot_results, title, x_label, y_label, z_label):
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x_scores, y_scores, z_scores, s=tot_results * 100, alpha=0.5)
        ax.set_title(title)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_zlabel(z_label)
        plt.show()


def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
