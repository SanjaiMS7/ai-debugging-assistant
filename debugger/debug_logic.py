import traceback

def analyze_error(code):

    try:
        exec(code)
        return "No errors found. Your program executed successfully."

    except Exception as e:

        error_type = type(e).__name__
        message = str(e)

        explanation = f"Error Type: {error_type}\n"
        explanation += f"Message: {message}\n\n"

        if error_type == "SyntaxError":
            explanation += "Possible Fix: Check missing colon, brackets, or indentation."

        elif error_type == "NameError":
            explanation += "Possible Fix: Variable or function name might not be defined."

        elif error_type == "TypeError":
            explanation += "Possible Fix: You may be combining incompatible data types."

        elif error_type == "IndentationError":
            explanation += "Possible Fix: Check spaces or tabs for indentation."

        else:
            explanation += "Check your code logic carefully."

        explanation += "\n\nTraceback:\n"
        explanation += traceback.format_exc()

        return explanation