def remove_input_string(input_string: str, generate_string: str) -> str:
    """
    Removes the input string from the generated response.

    input_string (str): The input string to be removed.
    generate_string (str): The generated response.

    return (str): The generated response with the input string removed.
    """
    if generate_string.startswith(input_string):
        return generate_string[len(input_string):]
    else:
        return generate_string