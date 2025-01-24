import json
import os
import shutil
import subprocess
import tempfile
from typing import Literal

from logzero import logger
from pydantic import BaseModel, PositiveInt
from rich.console import Console
from rich.table import Table

from wtf.constants.models import ALL_MODELS, ANTHROPIC_MODELS, OPENAI_MODELS

WTF_CONFIG_PATH = os.path.expanduser("~/.config/wtf/config.json")


class Config(BaseModel, frozen=True):
    logdir: str = os.path.expanduser("~/.config/wtf/log")
    logfile_env_var: str = "WTF_LOGGER_FILE"
    terminal_prompt_lines: PositiveInt = 1
    command_output_logger: Literal["script", "pty"] = "script"
    model: Literal[ALL_MODELS] = "gpt-4o-mini"  # type: ignore
    prompt_path: str = os.path.join(os.path.dirname(__file__), "constants", "prompt.txt")
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", "")

    def validate_config(self) -> None:
        if self.model not in ALL_MODELS:
            raise RuntimeError(f"Model `{self.model}` is not supported")

        if self.model in OPENAI_MODELS and not self.openai_api_key:
            raise RuntimeError(
                f"OpenAI API key is required for OpenAI models: {self.model}\n"
                "Please set the OPENAI_API_KEY environment variable or "
                "`wtf config --edit`"
            )

        if self.model in ANTHROPIC_MODELS and not self.anthropic_api_key:
            raise RuntimeError(
                f"Anthropic API key is required for Anthropic models: {self.model}\n"
                "Please set the ANTHROPIC_API_KEY environment variable or "
                "`wtf config --edit`"
            )

        if not os.path.exists(self.prompt_path):
            raise FileNotFoundError(f"Prompt file not found at {self.prompt_path}")

        self.save()

    def display(self) -> None:
        console = Console()
        table = Table(show_header=True, show_lines=True)
        table.add_column("Config")
        table.add_column("Value")
        table.add_column("Type")
        for field, field_info in self.model_fields.items():
            v = getattr(self, field)
            if field in ("openai_api_key", "anthropic_api_key") and v:
                v = "*" * 8
            table.add_row(field, str(v), str(field_info.annotation))
        console.print(table)

    def save(self) -> None:
        os.makedirs(os.path.dirname(WTF_CONFIG_PATH), exist_ok=True)
        with open(WTF_CONFIG_PATH, "w") as f:
            json.dump(self.model_dump(), f, indent=4)

    def edit(self) -> "Config":
        if not self.exists_config_file():
            raise FileNotFoundError(f"{WTF_CONFIG_PATH} not found")
        editor = os.getenv("EDITOR", "vim")
        config = self.from_file()
        try:
            with tempfile.NamedTemporaryFile("w+") as tmp_config:
                shutil.copyfile(WTF_CONFIG_PATH, tmp_config.name)
                subprocess.run([editor, tmp_config.name])
                config = self.from_file(tmp_config.name)
        except Exception as e:
            logger.error(e)
            logger.error("Failed to validate the config file. Please edit again.")
        return config

    @classmethod
    def exists_config_file(cls) -> bool:
        return os.path.exists(WTF_CONFIG_PATH)

    @classmethod
    def from_file(cls, config_file: str = WTF_CONFIG_PATH) -> "Config":
        with open(config_file) as f:
            config_dict = json.load(f)
        if not config_dict["openai_api_key"]:
            config_dict["openai_api_key"] = os.getenv("OPENAI_API_KEY", "")
        if not config_dict["anthropic_api_key"]:
            config_dict["anthropic_api_key"] = os.getenv("ANTHROPIC_API_KEY", "")
        return cls.model_validate(config_dict)
