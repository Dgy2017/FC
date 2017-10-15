file_path = 'RGG.txt'


def get_RGG():
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('无法打开' + file_path)
    sign = {' ', ',', '{', '\n'}
    sign2 = sign | {'\n', '{', '=', ';', '(', ')'}
    n = set()
    t = set()
    p = {}
    s = -1
    end = False
    while fin.read(1) not in {'g', 'G'}:
        continue
    while not end:
        ch = fin.read(1)
        # 处理集合Vn
        if ch in {'t', 'T', 'n', 'N'}:
            copy_ch = ch
            over = False
            while fin.read(1) != '{':
                continue
            while not over:
                ch = fin.read(1)
                if ch == '}':
                    break
                elif ch in sign:
                    continue
                else:
                    _word = ch
                    # 考虑到状态可能不是由一个字节组成
                    while True:
                        ch = fin.read(1)
                        if ch in sign:
                            break
                        elif ch == '}':
                            over = True
                            break
                        else:
                            _word += ch
                    if copy_ch in {'t', 'T'}:
                        t.add(_word)
                    else:
                        n.add(_word)
        # 处理集合P
        elif ch == 'p' or ch == 'P':
            while fin.read(1) != '{':
                continue
            over = False
            left = True
            while not over:
                ch = fin.read(1)
                if ch == '}':
                    break
                elif ch in sign:
                    continue
                else:
                    key = ch
                    # ->前面的部分
                    while True:
                        ch = fin.read(1)
                        if ch in {' ', '-', '>'}:
                            break
                        else:
                            key += ch
                    # ->后面的部分
                    if key not in p.keys():
                        p[key] = set()
                    while ch in {' ', '-', '>'}:
                        ch = fin.read(1)
                    value = ch
                    while True:
                        ch = fin.read(1)
                        if ch == '|':
                            p[key].add(value)
                            value = ''
                        elif ch in sign:
                            break
                        elif ch == '}':
                            over = True
                        else:
                            value += ch
                    p[key].add(value)
        elif ch not in sign2:
            _word = ch
            while True:
                ch = fin.read(1)
                if ch == ')':
                    end = True
                    break
                elif ch in sign2:
                    break
                else:
                    _word += ch
            s = _word
        elif ch == ')' or '':
            end = True
    return n, t, p, s


def right_split(str, n, t):
    l = len(str)
    for i in range(l + 1):
        if str[0:i] in t and str[i:l] in n:
            if str[0:i] == '':
                return 'ep', str[i:l]
            elif str[i:l] == '':
                return str[0:i], '_final'
            else:
                return str[0:i], str[i:l]
    return '', ''


def RGG2NFA():
    n, t, p, S = get_RGG()
    sigma = set(t)
    k = set(n | {'_final'})
    s = {S, }
    z = {'_final'}
    f = {}
    n.add('')
    t.add('')
    for key in p.keys():
        f[key] = {}
    f['_final'] = {}
    for key in p.keys():
        for str in p[key]:
            str1, str2 = right_split(str, n, t)
            if str1 == '' and str2 == '':
                print('无法匹配到正确的终结符和非终结符')
                exit()
            if str1 not in f[key].keys():
                f[key][str1] = set()
            f[key][str1].add(str2)
    return k, sigma, f, s, z
