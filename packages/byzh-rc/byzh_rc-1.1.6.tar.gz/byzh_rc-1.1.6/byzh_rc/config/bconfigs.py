from ..drawer.terminal import BColor
class BConfigs():
    def __init__(self):
        self.group_lst = []
        self.dict_lst = []

    def set(self, key, value, group="default"):
        '''
        默认加入到default组内
        '''
        if not isinstance(group, str):
            raise Exception(f"{BColor.YELLOW}group({str(group)}) must be str{BColor.RESET}")
        if not isinstance(key, str):
            raise Exception(f"{BColor.YELLOW}key({str(key)}) must be str{BColor.RESET}")

        if group not in self.group_lst:
            self.group_lst.append(group)
            self.dict_lst.append(dict())

        index = self.__get_index(group)
        self.dict_lst[index][key] = value

    def copy_group(self, src_group, dst_group):
        if not isinstance(src_group, str):
            raise Exception(f"{BColor.YELLOW}group({str(src_group)}) must be str{BColor.RESET}")
        if not isinstance(dst_group, str):
            raise Exception(f"{BColor.YELLOW}group({str(dst_group)}) must be str{BColor.RESET}")
        if dst_group in self.group_lst:
            raise Exception(f"{BColor.YELLOW}group({str(dst_group)}) already exist{BColor.RESET}")

        import copy
        self.group_lst.append(dst_group)
        self.dict_lst.append(copy.deepcopy(self.dict_lst[self.__get_index(src_group)]))
    # show-方法
    def show_all(self):
        print(self)
    def show_group(self, group):
        result = self.__get_group_str(group)
        print(group+":\n"+result)
    # get-方法
    def get_str(self, group, key):
        self.__check(group, key)
        index = self.__get_index(group)
        return str(self.dict_lst[index][key])
    def get_int(self, group, key):
        self.__check(group, key)
        index = self.__get_index(group)
        return int(self.dict_lst[index][key])
    def get_float(self, group, key):
        self.__check(group, key)
        index = self.__get_index(group)
        return float(self.dict_lst[index][key])
    def get_bool(self, group, key):
        '''
        只有value为["False", "0", "None"]时，返回False
        '''
        self.__check(group, key)

        if self.get_str(key, group) in ["False", "0", "None"]:
            return False
        elif self.get_str(key, group) in ["True", "1"]:
            return True
        else:
            raise Exception(f"{BColor.YELLOW}value({str(key)}) cannot change to bool{BColor.RESET}")

    # save-方法
    def to_pickle(self, path):
        import pickle
        with open(path, 'wb') as f:
            pickle.dump([self.group_lst, self.dict_lst], f)
    def from_pickle(self, path):
        import pickle
        with open(path, 'rb') as f:
            [self.group_lst, self.dict_lst] = pickle.load(f)
    def to_json(self, path):
        import json
        with open(path, 'w') as f:
            for group, group_dict in zip(self.group_lst, self.dict_lst):
                entry = {"group": group, "dict": group_dict}
                json.dump(entry, f)
                f.write("\n")
    def from_json(self, path):
        import json
        with open(path, 'r') as f:
            self.group_lst = []
            self.dict_lst = []
            for line in f:
                entry = json.loads(line.strip())
                self.group_lst.append(entry["group"])
                self.dict_lst.append(entry["dict"])
    def to_yaml(self, path):
        import yaml
        with open(path, 'w') as f:
            yaml.dump([self.group_lst, self.dict_lst], f)
    def from_yaml(self, path):
        import yaml
        with open(path, 'r') as f:
            [self.group_lst, self.dict_lst] = yaml.load(f, Loader=yaml.FullLoader)
    def to_ini(self, path):
        import configparser
        config = configparser.ConfigParser()
        config.read(path)
        # 清空config
        with open(path, 'w') as f:
            f.write('')
        # 重新写入
        for group, dict in zip(self.group_lst, self.dict_lst):
            config.add_section(group)
            for key, value in dict.items():
                config.set(group, key, value)

        with open(path, 'w') as f:
            config.write(f)
    def from_ini(self, path):
        import configparser
        config = configparser.ConfigParser()
        config.read(path)
        self.group_lst = []
        self.dict_lst = []
        for section in config.sections():
            self.group_lst.append(section)
            self.dict_lst.append(dict(config.items(section)))

    def to_csv(self, path):
        import csv
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)

            # Write header: the first row is group names
            header = ['key'] + self.group_lst
            writer.writerow(header)

            # Find all unique keys across all groups
            all_keys = set()
            for group_dict in self.dict_lst:
                all_keys.update(group_dict.keys())

            # Write rows for each key
            for key in all_keys:
                row = [key]
                for group_dict in self.dict_lst:
                    row.append(group_dict.get(key, ''))  # Add value or empty if key is not present
                writer.writerow(row)
    def from_csv(self, path):
        import csv
        with open(path, 'r') as f:
            reader = csv.reader(f)

            # Read header: the first row is group names
            header = next(reader)
            group_lst = header[1:]  # The first column is 'key', rest are groups
            self.group_lst = group_lst
            self.dict_lst = [{} for _ in range(len(group_lst))]  # Initialize dicts for each group

            # Read the key-value pairs
            for row in reader:
                key = row[0]
                for i, value in enumerate(row[1:], start=0):
                    if value:  # Only add value if it's not empty
                        self.dict_lst[i][key] = value
    # 工具-方法
    def __str__(self):
        result = ""
        for group in self.group_lst:
            result += group + ":\n"
            result += self.__get_group_str(group) + "\n"
        # 去掉最后一个\n
        result = result[:-1]
        return result
    def __get_index(self, group):
        return self.group_lst.index(group)
    def __get_group_str(self, group):
        self.__check(group)
        index = self.__get_index(group)
        result = "\n".join([f"\t({key} -> {value})" for key, value in self.dict_lst[index].items()])
        return result
    def __check(self, group, key=None):
        # 检查group是否是字符串
        if not isinstance(group, str):
            raise Exception(f"{BColor.YELLOW}group({str(group)}) must be str{BColor.RESET}")
        # 检查group是否在group_list中
        if group not in self.group_lst:
            raise Exception(f"{BColor.YELLOW}group({str(group)}) not found{BColor.RESET}")

        if key is not None:
            # 检查key是否是字符串
            if not isinstance(key, str):
                raise Exception(f"{BColor.YELLOW}key({str(key)}) must be str{BColor.RESET}")
            # 检查key是否在dict中
            index = self.__get_index(group)
            if key not in self.dict_lst[index]:
                raise Exception(f"{BColor.YELLOW}key({str(key)}) not found{BColor.RESET}")


if __name__ == '__main__':
    a = BConfigs()

    a.set('a', 'None')
    a.set('b', '123')
    a.set('345', '33333')

    a.set('a532', 'No32ne', group='awa')
    a.set('b13', '123412', group='awa')
    a.set('321345', '33342333', group='awa')

    a.copy_group('default', 'qwq')
    a.set('345', 'aaaaaa', 'qwq')

    a.to_csv('config.csv')
    a.from_csv('config.csv')
    # a.to_yaml('config.yaml')
    # a.from_yaml('config.yaml')
    # a.to_pickle('config.pkl')
    # a.from_pickle('config.pkl')
    # a.to_json('config.json')
    # a.from_json('config.json')

    print(a.get_str('b13', group='awa'))
    print(a)