import re
from importlib.resources import files

from mau.environment.environment import Environment
from mau.visitors.jinja_visitor import JinjaVisitor, load_templates_from_path

templates = load_templates_from_path(files(__package__).joinpath("templates"))

DEFAULT_TEMPLATES = {}


class TexVisitor(JinjaVisitor):
    format_code = "tex"
    extension = "tex"

    default_templates = Environment(templates)
    default_templates.update(DEFAULT_TEMPLATES)

    def _escape_text(self, text):
        conv = {
            "&": r"\&",
            "%": r"\%",
            "$": r"\$",
            "#": r"\#",
            "_": r"\_",
            "{": r"\{",
            "}": r"\}",
            "~": r"\textasciitilde{}",
            "^": r"\^{}",
            "\\": r"\textbackslash{}",
            "<": r"\textless{}",
            ">": r"\textgreater{}",
        }
        regex = re.compile(
            "|".join(
                re.escape(str(key))
                for key in sorted(conv.keys(), key=lambda item: -len(item))
            )
        )
        return regex.sub(lambda match: conv[match.group()], text)

    def _visit_header(self, node, *args, **kwargs):
        command_map = {
            "1": r"chapter",
            "2": r"section",
            "3": r"subsection",
            "4": r"subsubsection",
            "5": r"paragraph",
            "6": r"subparagraph",
        }

        base = super()._visit_header(node, *args, **kwargs)
        level = str(base["data"].get("level", 6))
        base["data"]["command"] = command_map.get(level)

        return base

    def _visit_source__default(self, node, *args, **kwargs):
        # Highlighers like the package Minted
        # consider the first line as number 1
        node.highlights = [i + 1 for i in node.highlights]

        base = super()._visit_source__default(node, *args, escape=False, **kwargs)
        return base

    def _visit_text(self, node, *args, escape=True, **kwargs):
        base = super()._visit_text(node, *args, **kwargs)

        if escape:
            base["data"]["value"] = self._escape_text(base["data"]["value"])

        return base

    def _visit_verbatim(self, node, *args, **kwargs):
        base = super()._visit_verbatim(node, *args, **kwargs)

        base["data"]["value"] = self._escape_text(base["data"]["value"])

        return base
