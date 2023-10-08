# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и текст найден в ее выводе
# и False в противном случае.
# Передаваться должна только одна строка,
# разбиение вывода использовать не нужно.

# Доработать функцию таким образом, чтобы у нее появился дополнительный режим работы,
# в котором вывод разбивается на слова с удалением всех знаков пунктуации
# (их можно взять из списка string.punctuation модуля string).
# В этом режиме должно проверяться наличие слова в выводе.

import subprocess
from string import punctuation


def test_one(com: str, text: str):
    result = subprocess.run(com, shell=True, stdout=subprocess.PIPE, encoding="UTF-8")
    out = result.stdout
    for i in punctuation:
        if i in out:
            out = out.replace(i, ' ')
    out = out.split()
    # print(out)
    if result.returncode == 0:
        if text in out:
            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    print(test_one("cat /etc/os-release", "Jammy"))
