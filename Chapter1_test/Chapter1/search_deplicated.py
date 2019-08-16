def search_deplicated(string):
    str_list = [char for char in string]
    for i in range(len(str_list)):
        if str_list.count(str_list[i]) > 1:
            return False
    return True


if __name__ == "__main__":
    print("こんにちは : " ,search_deplicated("こんにちは"))
    print("アンパンマン : " , search_deplicated("アンパンマン"))