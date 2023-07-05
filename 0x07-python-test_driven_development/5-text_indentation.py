#!/usr/bin/python3
"""
module that prints out texts in paragraph lines using delimeters
"""


def text_indentation(text):
    """
    Function to print out texts in paragraphs based on existing delimiters.

    Args:
        text (str): The text that constitutes the paragraph.

    Returns:
        None

    Raises:
        TypeError: If 'text' is not a string.
        ValueError: If 'text' is an empty string.
    """
    try:
        if not isinstance (text, str):
            raise TypeError("text must be a string")

        if not text.strip():
            raise ValueError("text cannot be an empty string")

        count = 0
        while count < len(text) and text[count] == ' ':
            count += 1

        while count < len(text):
            print(text[count], end="")
            if text[count] == "\n" or text[count] in ".?:":
                if text[count] in ".?:":
                    print("\n")
                count += 1
                while count < len(text) and text[count] == ' ':
                    count += 1
                continue
            count += 1

    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
