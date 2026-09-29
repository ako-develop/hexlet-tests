from capitalize import capitalize

assert capitalize("hello") == "Hello", "capitalize не делает первую букву заглавной"
assert capitalize("") == "", "capitalize ломается на пустой строке"

print("Все тесты пройдены!")
