#!/usr/bin/python3
""" 0-prime game module """


def isWinner(x, nums):
    """ Chooses a winner based on x rounds with nums \
          integers to check for prime numbers """

    # number of players
    ben = maria = 0

    if (len(nums) < 1) or (x < 1):
        return None

    # 1 == Maria | 2 == Ben
    count = 0
    for rounds in range(x):
        y = nums[rounds]
        non_uniq = set()

        # prime numbers are picked out via sieve of erathosthenes algorithm

        for number in range(2, nums[rounds] + 1):

            if number in non_uniq:
                continue
            else:
                count = (2 if count == 1 else 1)
                multiplier = 1
                product = 0

                # add prime number & multiples to set
                while (product <= nums[rounds]):
                    product = number * multiplier
                    multiplier += 1

                    if (product <= nums[rounds]):
                        non_uniq.add(product)

        if (nums[rounds] == 1):
            count = (2 if count == 1 else 1)
        if (count == 2):
            ben += 1
        else:
            maria += 1

    # return None if equal
    if (maria != ben):
        return ("Maria" if maria > ben else "Ben")

    return (None)
