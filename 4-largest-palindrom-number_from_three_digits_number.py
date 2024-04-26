"<p>A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 \times 99$.</p>"
"<p>Find the largest palindrome made from the product of two $3$-digit numbers.</p>"


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

    multiply_results = []
    for number in range(100, 1000):
        multiply_result = number * number
        multiply_results.append(multiply_result)

    palindrome_list = []
    for multiply_result in multiply_results:
        is_palindrome = check_palindrome(multiply_result)
        if is_palindrome:
            palindrome_list.append(multiply_result)

    return max(palindrome_list)


x = largest_palindrome_number_result()
print(x)
