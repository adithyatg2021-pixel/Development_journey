
def division(num1,num2):
    result = 0
    try:
        result = num1 / num2
        if num1 < num2:
            raise Exception(num1,"cannot be less than",num2)

    except Exception as e:
        print(e)

    finally:
        print("Execution completed")
    return result

print(division(1,2))
    