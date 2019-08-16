def judge_anagram(str1 , str2):
    list_str1 = [char for char in str1]
    list_str2 = [char for char in str2]
    '''
    list_str1.sort
    list_str2.sort
    print(list_str1)
    print(list_str2)
    '''
    if sorted(list_str1) == sorted(list_str2):
        return True
    else:
        return False

if __name__ == "__main__":
    print(judge_anagram("hoge","geho"))

