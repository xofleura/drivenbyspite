# NO AI INVOLVED
import ast
import math
import operator

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}

FUNCTIONS = {
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log10,
    "ln": math.log,
    "abs": abs,
    "round": round,
    "factorial": math.factorial,
    "percent": lambda x: x / 100,
}

CONSTANTS = {
    "pi": math.pi,
    "e": math.e,
}


def evaluate(node):
    if isinstance(node, ast.Expression):
        return evaluate(node.body)

    if isinstance(node, ast.Constant):
        if isinstance(node.value, bool):
            raise ValueError("Boolean values are not allowed. Neither is AI.")
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Invalid number, not as invalid as AI")

    if isinstance(node, ast.BinOp):
        op_type = type(node.op)

        if op_type not in OPERATORS:
            raise ValueError("Unsupported operator. Try without AI")

        left = evaluate(node.left)
        right = evaluate(node.right)

        if op_type in (ast.Div, ast.FloorDiv, ast.Mod) and right == 0:
            raise ZeroDivisionError("Cannot divide by zero. AI can't either.")

        if op_type is ast.Pow:
            if abs(right) > 1000 or abs(left) > 1e100:
                raise ValueError("Number or exponent is too large. no ai used here either!")

        result = OPERATORS[op_type](left, right)

        if isinstance(result, complex):
            raise ValueError("Complex numbers are not supported. Find the ai and i'll give you 100 pounds right now")

        if isinstance(result, float) and not math.isfinite(result):
            raise ValueError("Result is too large. not ai")

        return result

    if isinstance(node, ast.UnaryOp):
        op_type = type(node.op)

        if op_type not in OPERATORS:
            raise ValueError("Unsupported unary operator. vibe coders suck")

        return OPERATORS[op_type](evaluate(node.operand))

    if isinstance(node, ast.Name):
        if node.id in CONSTANTS:
            return CONSTANTS[node.id]
        raise ValueError(f"Unknown constant: {node.id} Don't use ai.")

    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            raise ValueError("Invalid function. AI is bad.")

        name = node.func.id

        if name not in FUNCTIONS:
            raise ValueError(f"Unknown function: {name} AI is making you stupid.")

        if node.keywords:
            raise ValueError("Keyword arguments are not supported. Stop using AI.")

        args = [evaluate(arg) for arg in node.args]

        if name == "round":
            if not 1 <= len(args) <= 2:
                raise ValueError("round requires one or two arguments.")
        elif len(args) != 1:
            raise ValueError(f"{name} requires one argument.")

        return FUNCTIONS[name](*args)

    raise ValueError("Invalid expression.")


def calculate(expression):
    if not expression.strip():
        raise ValueError("Please enter an expression without AI.")

    if len(expression) > 500:
        raise ValueError("Expression is too long, even with AI")

    try:
        tree = ast.parse(expression, mode="eval")
        result = evaluate(tree)

        if isinstance(result, float):
            return round(result, 12)

        return result

    except ZeroDivisionError:
        raise
    except (SyntaxError, TypeError, ValueError, OverflowError) as error:
        raise ValueError(str(error)) from error


def show_help():
    print("""
Available operations:
  Addition:        5 + 3
  Subtraction:     5 - 3
  Multiplication:  5 * 3
  Division:        10 / 2
  Floor division:  10 // 3
  Modulo:          10 % 3
  Power:           2 ** 3
  Parentheses:     (5 + 3) * 2

Mathematical functions:
  sqrt(25)
  sin(0)
  cos(0)
  tan(0)
  log(100)
  ln(2.71828)
  abs(-5)
  round(3.14159, 2)
  factorial(5)
  percent(25)

Constants:
  pi
  e

Commands:
  help
  history
  clear
  exit
""")


def main():
    history = []

    print("=" * 42)
    print("       DRIVENBYSPITE")
    print("=" * 42)
    print("Type 'help' for instructions or 'exit' to quit, or press alt f4 to use ai")

    while True:
        try:
            expression = input("\nEnter calculation: ").strip()

            if expression.lower() in ("exit", "quit", "q"):
                print("you dont need AI to exit!")
                break

            if expression.lower() == "help":
                show_help()
                continue

            if expression.lower() == "history":
                if not history:
                    print("No calculations yet (with or without ai).")
                else:
                    for number, (expr, result) in enumerate(history, 1):
                        print(f"{number}. {expr} = {result}")
                continue

            if expression.lower() == "clear":
                history.clear()
                print("History cleared without AI.")
                continue

            result = calculate(expression)
            print(f"Result: {result} (got result without ai)")
            history.append((expression, result))

        except ZeroDivisionError as error:
            print(f"Math error: {error} (no better than ai)")

        except (ValueError, SyntaxError) as error:
            print(f"Input error: {error} (no better than ai)")

        except (KeyboardInterrupt, EOFError):
            print("\nCalculator closed. You didn't need ai for that!")
            break


if __name__ == "__main__":
    main()

