# 1. ფიბონაჩის მიმდევრობა


def fibonacci(n):
    result = []
    a = 0
    b = 1
    for i in range(n):
        result.append(a)
        temp = a + b
        a = b
        b = temp
    return result


print(fibonacci(7))


# 2. ანაგრამების შემოწმება


def is_anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False


print(is_anagram("race", "care"))
print(is_anagram("hello", "world"))


# 3. ფაქტორიალი


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


print(factorial(5))


# 4. სიმბოლოს რაოდენობა სტრიქონში


def count_char(string, char):
    count = 0
    for c in string:
        if c == char:
            count = count + 1
    return count


print(count_char("hello world", "l"))
