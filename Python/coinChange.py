value = 7
coins = [25, 10, 5, 1]
memo = {}


def coin_change(value, coins, memo):
    if not coins and value > 0:
        return 0
    if value <= 0:
        return 1
    max = value // coins[0] + 1
    key = str(value) + ': ' + str(coins)

    if key in memo:
        return memo[key]
    ways = 0
    for i in range(max):
        ways += coin_change(value - i * coins[0], coins[1:], memo)
    print(key, ways)
    return ways


print(coin_change(value,coins,memo))


"""





        v = 69, c = [10,5,1]    ...




                                    v = 44, c = [5,1]

                                    v = 34

        v = 44, c = [10,5,1]        v = 24

                                    v = 14

                                    v = 4

                                                        v = 19
                                                        v = 14
                                v = 19, c = [5,1]       v = 9
                                                        v = 4
        v = 19, c = [10,5,1]        

                                v = 9, c = [5,1]  ways=2  v = 9, c=[1]        v=9 (0) ; v=8 ; v=7 ... v=0 (1)
                                                          v = 4, c=[1]


"""
