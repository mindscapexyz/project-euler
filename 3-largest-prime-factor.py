"<p>The prime factors of $13195$ are $5, 7, 13$ and $29$.</p>"
"<p>What is the largest prime factor of the number $600851475143$?</p>"


def largest_prime_factor(ori_num):
    prime_factors = []
    divided_num = ori_num
    while divided_num > 1:
        # + 1 to include its own number in the range
        for i in range(2, divided_num + 1):
            check_divisibility = divided_num / i
            if check_divisibility.is_integer():
                prime_factors.append(i)
                divided_num = divided_num / i
                print(divided_num)
                divided_num = int(divided_num)
                break

    return max(prime_factors)


number = 600851475143
result = largest_prime_factor(number)
print(result)
