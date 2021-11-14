# includeがうまく表示されないので，カッコなしで
def solve():
    ABC = list(map(int, input().split()))
    if ((ABC[0] == 5) and (ABC[1] == 5) and (ABC[2] == 7))\
            or ((ABC[0] == 5) and (ABC[1] == 7) and (ABC[2] == 5))\
            or ((ABC[0] == 7) and (ABC[1] == 5) and (ABC[2] == 5)):
        print('YES')
        return

    print('NO')


def main():
    solve()


# 実行
main()
