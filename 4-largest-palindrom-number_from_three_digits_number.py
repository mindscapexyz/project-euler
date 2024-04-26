"<p>A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 \times 99$.</p>"
"<p>Find the largest palindrome made from the product of two $3$-digit numbers.</p>"

from itertools import combinations_with_replacement


def largest_palindrome_number_result():
    def check_palindrome(number):
        str_num = str(number)
        len_num = len(str_num)
        for i in range(len_num):
            back_count = -(i + 1)
            if str_num[i] == str_num[back_count]:
                continue
            else:
                return False
        return True

    def get_all_possible_three_digit_multiply_pairing():
        all_possible_numbers = []
        for number in range(100, 1000):
            all_possible_numbers.append(number)

        combination_pair_iter = combinations_with_replacement(all_possible_numbers, 2)

        return list(combination_pair_iter)

    all_pairings = get_all_possible_three_digit_multiply_pairing()
    multiply_results = []
    for pair in all_pairings:
        multiply_result = pair[0] * pair[1]
        multiply_results.append(multiply_result)

    palindrome_list = []
    for multiply_result in multiply_results:
        is_palindrome = check_palindrome(multiply_result)
        if is_palindrome:
            palindrome_list.append(multiply_result)

    return max(palindrome_list)


result = largest_palindrome_number_result()
print(result)
