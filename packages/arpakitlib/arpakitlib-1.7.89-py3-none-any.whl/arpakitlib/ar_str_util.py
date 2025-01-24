# arpakit

from typing import Optional

from bs4 import BeautifulSoup

from arpakitlib.ar_type_util import raise_for_type

_ARPAKIT_LIB_MODULE_VERSION = "3.0"


def str_in(string: str, main_string: str, *, max_diff: Optional[int] = None) -> bool:
    if string not in main_string:
        return False

    if max_diff is None:
        return True

    diff = len(main_string) - len(string)
    if diff <= max_diff:
        return True

    return False


def bidirectional_str_in(string1: str, string2: str, *, max_diff: Optional[int] = None) -> bool:
    if (
            str_in(string=string1, main_string=string2, max_diff=max_diff)
            or str_in(string=string2, main_string=string1, max_diff=max_diff)
    ):
        return True
    return False


def str_startswith(string: str, main_string: str, max_diff: Optional[int] = None) -> bool:
    if not main_string.startswith(string):
        return False

    if max_diff is None:
        return True

    diff = len(main_string) - len(string)
    if diff <= max_diff:
        return True

    return False


def bidirectional_str_startswith(string1: str, string2: str, max_diff: Optional[int] = None) -> bool:
    if str_startswith(string1, string2, max_diff=max_diff) or str_startswith(string2, string1, max_diff=max_diff):
        return True
    return False


def make_blank_if_none(string: Optional[str] = None) -> str:
    if string is None:
        return ""
    return string


def make_none_if_blank(string: Optional[str] = None) -> str | None:
    if not string:
        return None
    return string


def remove_html(string: str) -> str:
    raise_for_type(string, str)
    return BeautifulSoup(string, "html.parser").text


def remove_tags(string: str) -> str:
    raise_for_type(string, str)
    return string.replace("<", "").replace(">", "")


def remove_tags_and_html(string: str) -> str:
    raise_for_type(string, str)
    return remove_tags(remove_html(string))


def raise_if_string_blank(string: str) -> str:
    if not string:
        raise ValueError("not string")
    return string


def __example():
    print("str_in:")
    print(str_in(string="hello", main_string="hello world"))  # True
    print(str_in(string="bye", main_string="hello world"))  # False
    print(str_in(string="hello", main_string="hello world", max_diff=6))  # True
    print(str_in(string="hello", main_string="hello world", max_diff=1))  # False

    print("\nbidirectional_str_in:")
    print(bidirectional_str_in(string1="hello", string2="hello world"))  # True
    print(bidirectional_str_in(string1="world", string2="hello world"))  # True

    print("\nstr_startswith:")
    print(str_startswith(string="hello", main_string="hello world"))  # True
    print(str_startswith(string="world", main_string="hello world"))  # False

    print("\nbidirectional_str_startswith:")
    print(bidirectional_str_startswith(string1="hello", string2="hello world"))  # True
    print(bidirectional_str_startswith(string1="world", string2="hello world"))  # False

    print("\nmake blank_if_none:")
    print(make_blank_if_none())  # ""
    print(make_blank_if_none(string="test"))  # "test"

    print("\nremove_html:")
    print(remove_html(string="<div>Hello <b>World</b></div>"))  # "Hello World"

    print("\nremove_tags:")
    print(remove_tags(string="<div>Hello <b>World</b></div>"))  # "divHello bWorldbdiv"

    print("\nremove_tags_and_html:")
    print(remove_tags_and_html("<div>Hello <b>World</b></div>"))  # "Hello World"


if __name__ == '__main__':
    __example()
