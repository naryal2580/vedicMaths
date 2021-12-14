#!/shebang

def ignore_0n9s(number):
    ignored_0n9s = str(number).replace('0', '').replace('9', '')
    if not ignored_0n9s:
        return 0
    return int(ignored_0n9s)

def digital_root(number):
    _ditital_root = 0; number = ignore_0n9s(number)
    for n in str(number):
        _ditital_root += int(n)
    if len(str(ignore_0n9s(_ditital_root))) == 2:
        return digital_root(_ditital_root)
    return ignore_0n9s(_ditital_root)
