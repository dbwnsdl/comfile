def run(file):
    v = {}
    with open(file, encoding='UTF-8') as a:
        code = a.read().split('\n')
        for i in code:
            g = i.split(' ')
            if len(g) == 3:
                if g[1] == 'str' or g[1] == 'number':
                    if g[0] == 'print':
                        if '+' in g[2] or '*' in g[2] or '/' in g[2] or '-' in g[2]:
                            try:
                                print(eval(g[2]))
                            except:
                                ZeroDivisionError('integer division or modulo by zero')
                        else:
                            print(g[2])
                elif g[0] == 'var':
                    if '+' in g[2] or '*' in g[2] or '/' in g[2] or '-' in g[2]:
                        try:
                            v[g[1]] = eval(g[2])
                        except:
                            ZeroDivisionError('integer division or modulo by zero')
                    else:
                        v[g[1]] = g[2]
                elif g[1] == 'var':
                    if g[0] == 'print':
                        print(v[g[2]])
            elif len(g) == 2:
                if g[0] == 'input':
                    wofj = input()
                    v[g[1]] = wofj