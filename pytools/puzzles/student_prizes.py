
def _perms(s):
    '''

    :param s:
    :return:
    '''

    if len(s) < 2:
        return set(s)

    subs = _perms(s[1:])

    out = set()
    for sub in subs:
        for i in xrange(len(s)):
            perm = sub[:i] + s[0] + sub[i:]
            out.add(perm)

    return out


def prize_combos(n):
    '''

    :param n:
    :return:
    '''

    stack = ['A', 'L', 'O']
    s = ''
    cnt = 0

    while stack:
        if len(s) < n-1:
            s += stack.pop()
            stack.append(s[-1])
        else:
            for c in stack:
                perms = _perms(s+c)
                cnt += len(perms)
            stack.pop()
            s = s[:-1]

    return cnt