import ping3
import openpyxl
import re
import sys


class PingExcelWebsites:
    def __init__(self, file_name, sheet_name):
        try:
            self.wb = openpyxl.load_workbook(file_name)
        except Exception:
            print("Read Excel file failed.")
        try:
            self.ws = self.wb[sheet_name]
        except Exception:
            print("No such sheet. Check if there exists misspelling please.")
        self.start_row = 0
        self.end_row = 0

    def set_start_and_end_row(self, start_row, end_row):
        self.start_row = start_row
        self.end_row = end_row

    def input_start_and_end_row(self):
        print("Input two number: start and end row, seperate them with space.")
        input_row_nums = input().split(' ')
        row_nums = [int(i) for i in input_row_nums]
        self.set_start_and_end_row(row_nums[0], row_nums[1])

    def read(self, col_no):
        cell_val_list = []
        for i in range(self.start_row, self.end_row):
            cell_val = self.ws.cell(row=i, column=col_no).value.strip()
            # protocols, port and resource path cannot be resolved by ping command
            if re.search('^https?://', cell_val.lower()):
                cell_val = re.sub('^https?://', '', cell_val)
            if '/' in cell_val:
                cell_val = re.sub('/.*', '', cell_val)
            if ':' in cell_val:
                cell_val = re.sub(':.*', '', cell_val)
            cell_val_list.append(cell_val)
        return cell_val_list

    def ping_addrs(self, addrs):
        """ return a list contains the ping-value of the pinged addresses

            Arg:
                addrs(list): 
        """
        ping_result_list = []
        for addr in addrs:
            response = ping3.ping(addr)
            if response is None:
                ping_result_list.append(-1)
            else:
                ping_result_list.append(int(response*1000))
        return ping_result_list

    def get_string_width(self, string):
        """ For beautifying the printed lists, each columns should be aligned
            so the length of each elements in the list should be counted
            to determining the gap between lists

            Regard full-width character as 2 width,
            and half-width character as 1 width.
            Then count the total width of the string.

            Args:
                string(str): an element from a list.
            Returns:
                length of the string-width
        """
        str_width = 0
        for char in string:
            if u'\u4e00' <= char <= u'\u9fa5':
                str_width = str_width+2
            else:
                str_width = str_width+1
        return str_width

    def is_len_of_each_list_all_equals(self, *lists):
        """lists' length must be equal while they were being printed
            Args:
                list(list): a list of lists
            Returns:
                True
                False
        """
        len_of_each_list = [len(_list) for _list in lists]
        if len(set(len_of_each_list)) == 1:
            return True
        return False

    def print_lists(self, *lists, gap=3):
        """print list(s) in formated way

        Args:
            *lists(list(list)): a list of lists
            gap(int): minimum amount of space(s) between each column
        Returns:
            return if the length of each lists doesn't equal
        """
        if not self.is_len_of_each_list_all_equals(lists):
            print("error")
            return
        # width of the longest string(added width of gap) in each lists
        longest_widths = []
        # a list contains one or more lists than each list reveals
        # the width of every strings in it
        str_widths_of_lists = []
        for _list in lists[:-1]:
            width_of_strs = [self.get_string_width(ele) for ele in _list]
            str_widths_of_lists.append(width_of_strs)
            longest_widths.append(max(width_of_strs)+gap)
        # len(lists[0]) means the number of rows being printed
        for i in range(0, len(lists[0])):
            for j, _list in enumerate(lists[:-1]):
                print(_list[i], end='')
                for _ in range(0, longest_widths[j]-str_widths_of_lists[j][i]):
                    print(' ', end='')
            print(lists[-1][i])


if __name__ == '__main__':
    pew = PingExcelWebsites(sys.argv[1], sys.argv[2])
    pew.input_start_and_end_row()
    loop_sign = ''
    while loop_sign.upper() != 'Q':
        print("Input address name and number of website column in Excel file, seperate them with space.")
        inputed_list = input().split(' ')
        num_list = [int(inputed_list[i]) for i in range(len(inputed_list))]
        addr_name_list = pew.read(num_list[0])
        addr_list = pew.read(num_list[1])
        ping_result_list = pew.ping_addrs(addr_list)
        pew.print_lists(addr_name_list, addr_list, ping_result_list)
        print("Press \"Q\" for quit. Press \"C\" for changing numbers of start row and end row. Press other key for continue。")
        loop_sign = input()
        if loop_sign.upper() == 'C':
            pew.input_start_and_end_row()
