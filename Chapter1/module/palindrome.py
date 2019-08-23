def palindrome(str):
    return list(str) == list(reversed(str))

if __name__ == "__main__":
    print(palindrome("aaa abs"))
    print(palindrome("sbaabs"))