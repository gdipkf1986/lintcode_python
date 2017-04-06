# coding = utf-8
__author__ = 'jovi'


cache = {}


def minimum_number_coins(target, coin_set=(1, 2, 3, 5)):
    if target in cache:
        return cache[target]

    if target == 0:
        return 0

    possible = []
    for picked in coin_set:
        required = target - picked
        if required > 0:
            possible.append(minimum_number_coins(required, coin_set) + 1)
        elif required == 0:
            possible.append(1)

    minimum = min(possible)
    cache[target] = minimum
    print("target %d, minimum: %d" % (target, minimum))

    return minimum


def loop(target, coin_set=(2, 3, 5, 6)):
    # init
    min_coins_of_each_step = [-1 for i in range(target + 1)]

    # calculate from 0 to target, each one will depends on previous results
    for step_target in range(target + 1):

        print('\n')
        possible = []

        # find all available coins which is less than step_target
        available_coins = [c for c in coin_set if c <= step_target]
        if len(available_coins) < 1:
            print('skip %s, no available coins' % step_target)
            continue

        print('step target %s, available coins %s, ' % (step_target, available_coins))

        # try pick any available one, then check left required how much coins
        # select the minimum ones
        for picked in available_coins:
            required = step_target - picked
            if required > 0:
                possible.append(min_coins_of_each_step[required] + 1)
            elif required == 0:
                possible.append(1)

        possible = [c for c in possible if c >= 1]
        if len(possible) > 0:
            min_coins_of_each_step[step_target] = min(possible)
        else:
            min_coins_of_each_step[step_target] = -1

        print('best solution is use %s coins' % min_coins_of_each_step[step_target])

    print('\n\nmin coins of each step %s' % min_coins_of_each_step)
    return min_coins_of_each_step[target]


if __name__ == '__main__':
    # minimum_number_coins(11)
    loop(13)
