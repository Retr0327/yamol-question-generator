from functools import reduce
from ...question_scraper import YamolQuestionGenerator


def create_latex_option_format(option_data: dict) -> str:
    """The create_latex_option_format function creates the format of LaTex options.

    Args:
        option_data (dict): the data downloaded by `YamolQuestionGenerator`

    Returns:
        a str
    """
    question = option_data["question"]
    option = option_data["option"]
    option_string = reduce(
        lambda prev, current: prev.strip() + f"}}{{{current.strip()}", option
    )

    if option == "題組題":
        return f"\\question {question}\n\n"

    return (
        f"\\question {question}\n\\choice{{{option_string}}}{{a}}\\vspace{{10pt}}\n\n"
    )


def create_options(test_id: int) -> str:
    """The create_options function uses the data downloaded from Yamol website to create
       LaTex's question

    Args:
        test_id (int): the id that represents a test

    Returns:
        a str
    """
    data = YamolQuestionGenerator(test_id).generate()
    options = tuple(map(create_latex_option_format, data))
    return " ".join(map(str, options))
