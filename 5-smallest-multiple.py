"<p>$2520$ is the smallest number that can be divided by each of the numbers from $1$ to $10$ without any remainder.</p>"
"<p>What is the smallest positive number that is <strong class='tooltip'>evenly divisible<span class='tooltiptext'>divisible with no remainder</span></strong> by all of the numbers from $1$ to $20$?</p>"


def smallest_multiple(divisible_range):
    i = 0
    is_break = False
    num = 2520
    divisible_number = 0
    while not is_break:
        num += 2520
        for i in range(1, divisible_range + 1):
            is_divisible = num / i
            if is_divisible.is_integer():
                if i == divisible_range:
                    divisible_number = num
                    is_break = True
                    break
            else:
                break
        print(divisible_number)


smallest_multiple(20)
