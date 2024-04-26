"<p>If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.</p>"
"<p>Find the sum of all the multiples of $3$ or $5$ below $1000$.</p>"

from functools import reduce


def sum_of_multiple_of_three_and_four_below_thousand():
    list_of_multiples_of_three_and_five = []
    for i in range(1, 1000):
        multi_of_three_check = i / 3
        multi_of_five_check = i / 5
        if multi_of_three_check.is_integer() or multi_of_five_check.is_integer():
            list_of_multiples_of_three_and_five.append(i)

    return reduce((lambda x, y: x + y), list_of_multiples_of_three_and_five)


result = sum_of_multiple_of_three_and_four_below_thousand()
print(result)
