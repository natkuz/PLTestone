# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и текст найден в ее выводе
# и False в противном случае.
# Передаваться должна только одна строка,
# разбиение вывода использовать не нужно.

import subprocess


def test_one(com: str, text: str) -> bool:
    result = subprocess.run(com, shell=True, stdout=subprocess.PIPE, encoding="UTF-8")
    out = result.stdout
    if result.returncode == 0:
        if text in out:
            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    print(test_one("cat /etc/os-release", "22.04.1"))
