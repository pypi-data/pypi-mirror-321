import unittest

from expedantic import ConfigBase, Field


class Config(ConfigBase):
    batch_size: int = Field(512, description="batch size")
    this_config_is_very_important: bool = Field(False, description="very important")
    another_boolean: bool = True


class TestUnderscore(unittest.TestCase):
    def test_underscore(self):
        config = Config.parse_args(
            replace_underscore_to_hyphen=True, args=["--batch-size", "256"]
        )
        self.assertEqual(config.batch_size, 256)

        config = Config.parse_args(
            replace_underscore_to_hyphen=True,
            args=["--this-config-is-very-important"],
        )
        self.assertTrue(config.this_config_is_very_important)


if __name__ == "__main__":
    c = Config.parse_args(replace_underscore_to_hyphen=True)
