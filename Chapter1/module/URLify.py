def URLify(str , num):
    list_str = [char for char in str]
    list_str = list_str[:-1:]

    for idx in range(len(list_str)):
        if list_str[idx] == ' ':
            list_str[idx] = '%20'

    return ''.join(list_str)

if __name__ == "__main__":
    print(URLify("aaa sss s ", 1))