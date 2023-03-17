from subprocess import check_output
from datetime import datetime

sizes_tests = [2, 5, 10, 50, 100]

def write_file(filename, content):
    f = open(f"{filename}.txt", "a")
    f.write(content)
    f.close()


def message(msg):
    print("==========================")
    print(f"  {msg}  ")
    print("==========================")


def get_command(language, file):
    ans = ""

    if (language == "cpp"):
        ans = "./D"
    elif (language == "python"):
        ans = f"python {file}"
    elif (language == "java"):
        ans = f"java D"
    elif (language == "php"):
        ans = f"php D"
    elif (language == "javascript"):
        ans = f"node D.js"

    return ans


def execute_tests(language, file, test_index):
    out = ""

    for i in range(5):
        test_name = sizes_tests[i]

        time = 0
        start_time = datetime.now()
        comando = f"{get_command(language, file)} < ./tests/{test_name}_{test_index}.txt"
        check_output(comando, shell=True)
        time = datetime.now() - start_time

        out += f"{language} Test {i+1} ({test_name}x{test_name}), {str(time)[6:len(str(time))]} \n"

    return out


def run_all():
    data = [
        {
            "language": "java",
            "file": "./D.java"
        },
        {
            "language": "cpp",
            "file": "./D.cpp"
        },
        {
            "language": "python",
            "file": "./D.py"
        },
        {
            "language": "php",
            "file": "./D.php"
        },
        {
            "language": "javascript",
            "file": "./D.js"
        },
    ]

    for i in range(len(data)):
        content_file_out = ""
        language = data[i]["language"]
        filename = data[i]["file"]

        if language == "cpp":
            check_output(f"c++ {filename} -o D", shell=True)
        elif language == "java":
            check_output(f"javac {filename}", shell=True)

        message(f"TEST {language} START")

        for i in range(20):
            content_file_out += f"Test {i+1}\n"
            content_file_out += execute_tests(language, filename, i+1)
            print(f"Test {i+1} executed")

        write_file(f"./output/out_{language}", content_file_out)

        message(f"TEST {language} FINISHED")


run_all()

