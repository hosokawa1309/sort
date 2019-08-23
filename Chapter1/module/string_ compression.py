def str_compression(string):
    count = 1
    ans = ''
    for i in range(len(string)):
        char = string[i]
        if i != len(string) - 1 and char == string[i + 1]  :
            count += 1
        else:
            ans = ans + char + str(count)
            count = 1
    if len(ans) >= len(string):
        return string
    else:
        return ans

if __name__ == "__main__":
    print(str_compression("aaabbbbccca"))
    print(str_compression("aabb"))