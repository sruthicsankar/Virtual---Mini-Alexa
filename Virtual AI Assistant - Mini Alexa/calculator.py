OPERATOR_ALIASES = {
    "+": "+", "plus": "+", "add": "+",
    "-": "-", "minus": "-", "subtract": "-",
    "*": "*", "x": "*", "times": "*", "multiply": "*",
    "/": "/", "divide": "/", "divided": "/",
}


def parse_exp(text):
    tokens = text.replace("calculate","").strip().split()
    numbers= []
    operator = None

    for token in tokens:
        token_lower = token.lower()
        if token_lower in OPERATOR_ALIASES:
            operator = OPERATOR_ALIASES[token_lower]
            continue
        try:
            numbers.append(float(token))

        except ValueError:
            continue

    if operator is not None and len(numbers) >= 2:
        return numbers[0],operator,numbers[1]

    return None


#  print(parse_exp("3 plus 4")) gives 
#   (3.0, '+', 4.0)


def calculate(num1,operator,nums):
    try:
        if operator  =="+":
            result = num1+nums
        elif operator == "-":
            result = num1-nums
        elif operator == "*":
            result = num1*nums
        elif operator == "/":
            if nums == 0:
                return "You are too smart, aren't you"
            result = num1/nums
        else:

            return f"can't understand the Operator {operator} try from this pool '+','-','*','/'"
        return f"{num1} {operator} {nums} = {result}"
    except (TypeError,ValueError) as error:
        return f"Error: {error}"
    