class py_solution:
    def roman_to_integer(self, num):
        roman_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_value = 0
        for i in range(len(num)):
            if i > 0 and roman_value[num[i]] > roman_value[num[i - 1]]:
                int_value += roman_value[num[i]] - 2 * roman_value[num[i - 1]]
            else:
                int_value += roman_value[num[i]]
        return int_value



roman_numeral = input("Enter the roman numeral you would like to convert: ")
print(py_solution().roman_to_integer(roman_numeral))