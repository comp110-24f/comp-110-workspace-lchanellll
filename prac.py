def remove_chars(msg: str, char: str) -> str:
    copy: str = ""
    index: int = 0
    while index < len(msg):
        if not (msg[index] == char):
            copy +h= [index]
        index += 1
    return copy


print(remove_chars(msg="football", char="o"))
