from typing import Any


DEFAULT_INDENT = 4


def pprint(value: Any, indent: int = DEFAULT_INDENT) -> None:
    printer = Printer(indent=indent)
    printer.print(value)


def _get_indent_string(length: int) -> str:
    return " " * length


class Printer:

    def __init__(self, indent: int = DEFAULT_INDENT):
        self._indent = indent

    def print(self, value: Any) -> None:
        print(self._get_pretty_string(value))

    def _get_pretty_string(self, value: Any, indent: int = 0) -> str:
        if isinstance(value, list):
            return self._get_list_string(value, indent)
        elif isinstance(value, dict):
            return self._get_dict_string(value, indent)
        elif isinstance(value, tuple):
            return self._get_tuple_string(value, indent)
        elif isinstance(value, set):
            return self._get_set_string(value, indent)
        else:
            return repr(value)

    def _get_list_string(self, list_: list, indent: int) -> str:
        if list_:
            lines = []
            indent += self._indent
            for item in list_:
                lines.append(_get_indent_string(indent) + self._get_pretty_string(item, indent))
            indent -= self._indent
            string = "[\n" + ",\n".join(lines) + "\n" + _get_indent_string(indent) + "]"
        else:
            string = "[]"

        return string

    def _get_dict_string(self, dict_: dict, indent: int) -> str:
        if dict_:
            lines = []
            indent += self._indent
            for key, value in dict_.items():
                lines.append(f"{_get_indent_string(indent)}{repr(key)}: "
                             f"{self._get_pretty_string(value, indent)}")
            indent -= self._indent
            string = "{\n" + ",\n".join(lines) + "\n" + _get_indent_string(indent) + "}"
        else:
            string = "{}"

        return string

    def _get_tuple_string(self, tuple_: tuple, indent: int) -> str:
        if tuple_:
            lines = []
            indent += self._indent
            for item in tuple_:
                lines.append(_get_indent_string(indent) + self._get_pretty_string(item, indent))
            indent -= self._indent
            if len(lines) == 1:
                item_lines = lines[0] + ","
            else:
                item_lines = ",\n".join(lines)
            string = "(\n" + item_lines + "\n" + _get_indent_string(indent) + ")"
        else:
            string = "()"

        return string

    def _get_set_string(self, set_: set, indent: int) -> str:
        if set_:
            lines = []
            indent += self._indent
            for item in set_:
                lines.append(_get_indent_string(indent) + self._get_pretty_string(item, indent))
            indent -= self._indent
            string = "{\n" + ",\n".join(lines) + "\n" + _get_indent_string(indent) + "}"
        else:
            string = "set()"

        return string
