from math import floor
import random

sizes_tests = [2, 5, 10, 50, 100]


def write_file(filename, content):
    f = open(f"{filename}.txt", "a")
    f.write(content)
    f.close()


def generate_random_number():
    return floor(random.random() * 100)


def generate_tests(n):
    matriz = ""

    for i in range(n):
        line = ""

        for j in range(n):
            line += str(generate_random_number()) + " "

        if i < n-1: matriz += line + "\n"
        else: matriz += line

    return matriz


def main():
    for size in sizes_tests:
        for i in range(20):
            test_content = f"{size} {size} \n" + generate_tests(size)
            write_file(f"./tests/{size}_{i+1}", test_content)


main()