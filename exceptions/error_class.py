# a = "The sky is blue"
# print(a)
#
# for letter in a:
#     print(letter)

def function_name():
    # a = []
    # print(a[1]) # IndexError

    # "hello".equals("goodbye") # AttributeError
    # int("hello") # ValueError
    # "hello" + 1 # TypeError
    # assert False # AssertionError

    # a = {}
    # a["Hello"] = 0
    # print(a["Goodbye"])

    # 1/0 # ZeroDivisionError

    # import my_calc # ModuleNotFoundError

    # try:
    #     from my_calc import sqrt
    # except ModuleNotFoundError:
    #     from math import sqrt
    # x = sqrt(4)
    # print(x)

    # a = []
    # try:
    #     print(a[1])
    # except IndexError:
    #     print("Error: You can't index beyond the bounds of your list.")
    # except Exception:
    #     print("Error: Some error other than IndexError is raised by code.")

    try:
        from my_calc import sqrt
    except ModuleNotFoundError:
        from math import sqrt
    except Exception as error:
        print(error)
    x = sqrt(4)
    print(x)

def main():
    function_name()

if __name__ == "__main__":
    main()
