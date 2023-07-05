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

        paragraphs = []
        paragraph = ""

        for char in text:
            paragraph += char
            if char in ['.', '?', ':']:
                paragraphs.append(paragraph.strip())
                paragraph = " "

        if paragraph.strip():
            paragraphs.append(paragraph.strip())

        for i, paragraph in enumerate(paragraphs):
            print(paragraph)
            if i < len(paragraphs) - 1:
                print()

    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")