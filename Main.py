def is_buzz(replace_array, count):
    """
    This function checks whether the count is a multiple of any of the numbers in replace_array[0] are replaces the
    output with the text with the same index in replace_array[1]. If it is not a multiple with any of the numbers it
    will return the number as a string.

    :param replace_array: A two dimensional array that stores the integers to be checked against at index 0 and the
    string replacements at index 1
    :param count: An integer to be checked
    :return: A string that outputs the text that is associated to count
    """

    output = ""
    for number in replace_array[0]:
        if count % number == 0:
            output += replace_array[1][replace_array[0].index(number)]

    if output == "":
        output = str(count)

    return output


if __name__ == '__main__':
    replacements = [[3, 5], ["Fizz", "Buzz"]]
    for i in range(1, 101):
        print(is_buzz(replacements, i))
