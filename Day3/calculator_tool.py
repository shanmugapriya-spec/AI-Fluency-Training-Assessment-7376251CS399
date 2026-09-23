def calculator(expression):
    try:
        return eval(expression)
    except Exception as e:
        return f"Calculator error: {e}"


if __name__ == "__main__":
    print(calculator("30000 - 30000 * 0.10"))