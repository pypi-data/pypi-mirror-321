import os
import pandas as pd
# 依赖包
# pip install openpyxl
# pip install pandas
def read_excel_files_in_folder(folder_path):
    """
    此函数用于读取指定文件夹下的所有 excel 文件的文件名，
    并将它们存储在一个列表中，按文件名升序排序
    :param folder_path: 要读取的文件夹路径
    :return: 存储 excel 文件名的列表，已排序
    """
    excel_filenames = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.xlsx') or file.endswith('.xls'):  # 仅添加 Excel 文件
                excel_filenames.append(file)
    excel_filenames.sort()
    return excel_filenames


def create_dataframe(excel_filenames):
    """
    此函数用于创建一个具有指定列名的空 DataFrame
    并根据 excel 文件名的数量添加新列
    :param excel_filenames: excel 文件名列表
    :return: 一个空的 DataFrame
    """
    columns = ['Mass', 'NeutralMass', 'C', 'H', 'N', 'O', 'C13', 'P', 'Na', 'S', 'Error_ppm', 'El_comp', 'Class', 'Candidates']
    for i in range(len(excel_filenames)):
        columns.append(f'dat_alls{i + 1}')
    d1 = pd.DataFrame(columns=columns)
    return d1


def read_excel_data_into_d1(d1, folder_path, excel_filenames):
    """
    此函数用于将 Excel 文件的数据读入到 d1 中，确保数据一致性和完整性。
    :param d1: 存储数据的 DataFrame
    :param folder_path: 文件夹路径
    :param excel_filenames: excel 文件名列表
    :return: 存储数据后的 DataFrame
    """
    for index, file in enumerate(excel_filenames):
        file_path = os.path.join(folder_path, file)
        try:
            # 尝试读取 Excel 文件
            df = pd.read_excel(file_path)

            # 确保所有所需列存在
            required_columns = ['ObservedM_z', 'calc_M_z', 'C', 'H', 'N', 'O', 'errPpm', 'ObservedIntens']
            for col in required_columns:
                if col not in df.columns:
                    df[col] = None  # 填充缺失列为 None

            # 创建 new_row
            new_row = pd.DataFrame({
                'Mass': df['ObservedM_z'].fillna(0),
                'NeutralMass': df['calc_M_z'].fillna(0),
                'C': df['C'].fillna(0).astype(int),
                'H': df['H'].fillna(0).astype(int),
                'N': df['N'].fillna(0).astype(int),
                'O': df['O'].fillna(0).astype(int),
                'C13': 0,
                'P': 0,
                'Na': 0,
                'S': 0,
                'Error_ppm': df['errPpm'].fillna(0),
                'El_comp': 'NA',
                'Class': 'NA',
                'Candidates': 'NA'
            })

            # 为每个文件追加特定的列
            for i in range(len(excel_filenames)):
                column_name = f'dat_alls{i + 1}'
                if i == index:
                    new_row[column_name] = df['ObservedIntens'].fillna(0)
                else:
                    new_row[column_name] = 0

            # 移除全空列和重复列
            new_row = new_row.dropna(axis=1, how='all')
            new_row = new_row.loc[:, ~new_row.columns.duplicated()]

            # 如果 new_row 不为空，合并到 d1
            if not new_row.empty:
                d1 = pd.concat([d1, new_row], ignore_index=True)

        except Exception as e:
            print(f"Error processing file {file}: {e}")

    # 全局清理 d1
    d1 = d1.loc[:, d1.notna().any(axis=0)]  # 移除全空列
    d1 = d1.loc[:, ~d1.columns.duplicated()]  # 移除重复列
    return d1

def merge_duplicate_mass_rows(d1):
    """
    此函数用于合并 Mass 列相同的行，保留第一个 Error_ppm 列的值
    :param d1: 存储数据的 DataFrame
    :return: 合并重复行后的 DataFrame
    """
    d1 = d1.groupby('Mass', as_index=False).first()
    return d1


def get_last_column_number(d1):
    """
    此函数用于获取最后一列 dat_alls 列的尾部数字
    :param d1: 存储数据的 DataFrame
    :return: 最后一列 dat_alls 列的尾部数字
    """
    last_column = d1.columns[-1]
    number = int(last_column.split('dat_alls')[-1])
    return number


def copy_dat_alls_columns(d1):
    """
    此函数用于复制 d1 中所有以 dat_alls 开头的列到一个新的数据结构 d2
    :param d1: 存储数据的 DataFrame
    :return: 存储 dat_alls 列的新 DataFrame d2
    """
    dat_alls_columns = [col for col in d1.columns if col.startswith('dat_alls')]
    d2 = d1[dat_alls_columns].copy()
    return d2


def rename_dat_alls_columns(d2, last_column_number, excel_filenames_length):
    """
    此函数用于修改 d2 的列名，按照指定规则进行递增
    :param d2: 存储 dat_alls 列的 DataFrame
    :param last_column_number: 最后一列 dat_alls 列的尾部数字
    :param excel_filenames_length: excel 文件名列表的长度
    :return: 修改列名后的 DataFrame d2
    """
    new_columns = []
    start_index = last_column_number + 1
    end_index = last_column_number + excel_filenames_length
    for i in range(start_index, end_index + 1):
        new_columns.append(f'dat_alls{i}')
    d2.columns = new_columns
    return d2


def append_d2_to_d1(d1, d2):
    """
    此函数用于将 d2 追加到 d1 中
    :param d1: 存储数据的 DataFrame
    :param d2: 存储 dat_alls 列的 DataFrame
    :return: 合并后的 DataFrame
    """
    d1 = pd.concat([d1, d2], axis=1)
    return d1


def write_to_csv(d1, output_path):
    """
    此函数用于将 d1 写入 csv 文件
    :param d1: 存储数据的 DataFrame
    :param output_path: 输出 csv 文件的路径
    """
    d1.to_csv(output_path, index=False)


def process_excel_files(input_folder_path, output_file_path):
    """
    封装函数，将步骤 1-10 进行封装，实现从指定输入文件夹读取 Excel 文件，处理数据并将结果写入指定输出文件
    :param input_folder_path: 输入文件夹路径
    :param output_file_path: 输出文件路径
    """
    # 步骤 1: 读取 data 文件夹下的所有 excel 文件文件名，并存入一个数据结构，并按照文件名升序存储
    excel_filenames = read_excel_files_in_folder(input_folder_path)
    print("Sorted excel filenames in data folder:")
    print(excel_filenames)

    # 步骤 2: 创建一个数据结构 d1 用于创建一个数据结构 d1 用于存储 excel 文件
    d1 = create_dataframe(excel_filenames)
    print("\nEmpty DataFrame with specified columns:")
    print(d1)

    # 步骤 3: 在 d1 尾部继续增加列
    d1 = create_dataframe(excel_filenames)
    print("\nDataFrame with additional columns:")
    print(d1)

    # 步骤 4: 分别按照第一步存储的文件名顺序读取 data 文件夹下面的 excel 文件存入的 d1
    d1 = read_excel_data_into_d1(d1, input_folder_path, excel_filenames)
    print("\nDataFrame with data from excel files:")
    print(d1)

    # 步骤 5: 对上面数据结构 d1 查找 Mass 列相同的，并将其合并成一行
    d1 = merge_duplicate_mass_rows(d1)
    print("\nDataFrame after merging duplicate Mass rows:")
    print(d1)

    # 步骤 6: 获取上面数据结构 d1 最后一列的列名 dat_alls 尾部的数字
    last_column_number = get_last_column_number(d1)
    print(f"\nLast column number of dat_alls: {last_column_number}")

    # 步骤 7: 复制 d1 所有 dat_alls 开头的列到一个新的数据结构 d2
    d2 = copy_dat_alls_columns(d1)
    print("\nDataFrame d2 with copied dat_alls columns:")
    print(d2)

    # 步骤 8: 分别修改 d2 这个数据结构的列名
    excel_filenames_length = len(excel_filenames)
    d2 = rename_dat_alls_columns(d2, last_column_number, excel_filenames_length)
    print("\nDataFrame d2 with renamed columns:")
    print(d2)

    # 步骤 9: 将 d2 这个数据结构追加到 d1
    d1 = append_d2_to_d1(d1, d2)
    print("\nDataFrame d1 after appending d2:")
    print(d1)

    # 步骤 10: 将 d1 写入一个 export.csv 里面
    write_to_csv(d1, output_file_path)
    print(f"\nDataFrame d1 written to {output_file_path}")


# 调用封装函数，指定输入文件夹和输出文件路径
# process_excel_files(input_folder_path, output_file_path)
