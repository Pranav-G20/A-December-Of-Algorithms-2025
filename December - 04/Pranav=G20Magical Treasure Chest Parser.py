def parse_chest(s):
    i = 0

    def parse():
        nonlocal i
        if s[i] != '[':
            neg = False
            if s[i] == '-':
                neg = True
                i += 1
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            return -num if neg else num

        i += 1
        arr = []
        while i < len(s) and s[i] != ']':
            if s[i] == ',':
                i += 1
            else:
                arr.append(parse())
        i += 1
        return arr

    return parse()


if __name__ == "__main__":
    s = input().strip()
    print(parse_chest(s))
