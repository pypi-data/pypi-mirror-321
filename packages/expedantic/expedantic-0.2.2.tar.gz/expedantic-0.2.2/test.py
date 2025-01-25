from expedantic import ConfigBase
from rich.pretty import pprint
from test_config import Config


# from expedantic.utils import get_default_dict


# d = get_default_dict(Config)
# pprint(d)

# pprint(Config.model_json_schema())
# exit()

# c = Config.parse_args(default_file="_test.yaml")
# print_diff_mode = ["none", "tree", "table", ...]
# c = Config.parse_args(
#     diff_print_mode="tree", replace_underscore_to_hyphen=False, sep="."
# )

# c.save_as_yaml("test__.yaml")
# pprint(c)

Config.load_from_yaml("test__.yaml", diff_print_mode="tree")


from yaml import SafeDumper

# c.save_as_yaml("__test.yaml")

# class Dumper(SafeDumper):
#     def write_line_break(self, data: str | None = ...) -> None:
#         super().write_line_break(data)
#
#         # if self.
