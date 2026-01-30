import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        logging.error("Division by zero error", exc_info=True)
        print("Error: Cannot divide by zero.")
    except TypeError as e:
        logging.error("Invalid data type", exc_info=True)
        print("Error: Please provide numeric values.")
    else:
        print("Result:", result)
    finally:
        print("Execution completed.\n")

# Simulate runtime errors
divide_numbers(10, 2)
divide_numbers(5, 0)
divide_numbers(8, "a")
