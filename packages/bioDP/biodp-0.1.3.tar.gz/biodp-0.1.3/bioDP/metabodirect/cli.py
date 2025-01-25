import argparse
from bioDP.metabodirect.excel_process import process_excel_files


def main():
    # 创建一个 ArgumentParser 对象，用于解析命令行参数
    parser = argparse.ArgumentParser(description='Process excel files and generate a csv output.')
    # 添加一个命令行参数 input_folder，用于指定包含 Excel 文件的输入文件夹的路径
    parser.add_argument('input_folder', type=str,
                        help='The path to the folder containing the original data.  '
                             'If it is a Windows path, use a backslash \\ instead / '
                             'e.g: C:/data should be C:\\data.')
    # 添加一个命令行参数 output_file，用于指定输出 CSV 文件的路径
    parser.add_argument('output_file', type=str,
                        help='The path to the processed file, in the format of folder path + file name. '
                             'If it is a Windows path, use a backslash \\ instead / '
                             'e.g: C:\\dispose\\report.csv.')
    # 解析命令行参数
    args = parser.parse_args()

    # 调用 process_excel_files 函数处理 Excel 文件并将结果存储在指定的输出文件中
    process_excel_files(args.input_folder, args.output_file)


if __name__ == "__main__":
    main()