# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# A4B3C2XYZD4E3F3A6B28


def compress(str):
    str_copy = "{} ".format(str)
    result = ""
    prev = str[0]
    counter = 0

    for s in str_copy:
        if s != prev:
            result = "{}{}{}".format(result, prev, counter if counter > 1 else "")
            counter = 0
        else:
            counter = counter + 1

        prev = s

    return result


if __name__ == "__main__":
    print(compress("AAB"))
