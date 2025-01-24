import argparse
import logging
import os
import shutil
import subprocess
import time
from dataclasses import dataclass

import logzero
from haystack.dataclasses.streaming_chunk import StreamingChunk
from logzero import logger
from rich.prompt import Prompt

from wtf.command_output_loggers import factroy_command_output_logger
from wtf.command_output_loggers.base import CommandOutputLoggerBase
from wtf.configs import Config
from wtf.constants.models import ALL_MODELS
from wtf.llms.pipeline import CommandOutputAnalyzer
from wtf.shells import factroy_shell
from wtf.shells.base import ShellBase


@dataclass(frozen=True)
class WhatTheFuck:
    command_output_logger: CommandOutputLoggerBase
    shell: ShellBase
    pipeline: CommandOutputAnalyzer

    def run(self) -> None:
        session_name = self.command_output_logger.session_name
        if not self.command_output_logger.is_available():
            logger.info("`Ctrl+d` to exit")
            try:
                self.shell.set_session(session_name)
                self.command_output_logger.begin()
            finally:
                self.shell.restore(session_name)
            return

        last_command = self.shell.get_session_histories(session_name)[-1]
        command_outputs = self.command_output_logger.extract_command_outputs()
        if not command_outputs:
            logger.info("The previous command(`%s`) has no output", last_command)
            return
        command_output = command_outputs[-1]

        logger.debug("Last command: %s", last_command)
        logger.debug("Last command output: \n%s\n", command_output.output)
        llm_output = self.pipeline.run(command=last_command, command_output=command_output.output)
        if llm_output.fixed_command:
            confirmation = Prompt.ask(f"\n\nRun `{llm_output.fixed_command}`?", choices=["y", "N"])
            if confirmation == "y":
                res = subprocess.run(llm_output.fixed_command, shell=True, capture_output=True)
                print(llm_output.fixed_command)
                print(res.stdout.decode())

    @classmethod
    def from_config(cls, config: Config) -> "WhatTheFuck":
        logfile = os.getenv(config.logfile_env_var, "")
        if not os.path.exists(logfile):
            logfile = os.path.join(config.logdir, f"{time.time_ns()}.log")
            os.makedirs(os.path.dirname(logfile), exist_ok=True)
            # NOTE: For child processes
            os.environ[config.logfile_env_var] = logfile

        cmd_output_logger = factroy_command_output_logger(
            config.command_output_logger, logfile, config.terminal_prompt_lines
        )
        shell = factroy_shell()

        with open(config.prompt_path) as f:
            prompt_template = f.read()

        def streaming_callback(chunk: StreamingChunk) -> None:
            print(chunk.content, end="", flush=True)

        cmd_output_analyzer = CommandOutputAnalyzer(
            prompt_template,
            config.model,
            config.openai_api_key,
            config.anthropic_api_key,
            streaming_callback=streaming_callback,
        )

        return cls(cmd_output_logger, shell, cmd_output_analyzer)


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="cmd")
    parser_clean = subparsers.add_parser("clean")  # noqa
    parser_config = subparsers.add_parser("config")
    parser_config.add_argument("-i", "--init", action="store_true")
    parser_config.add_argument("-e", "--edit", action="store_true")
    parser.add_argument("-l", "--loglevel", choices=["debug", "info"], default="info")
    parser.add_argument("-m", "--model", choices=ALL_MODELS)
    args = parser.parse_args()
    logzero.loglevel(getattr(logging, args.loglevel.upper(), logging.INFO))

    if not Config.exists_config_file():
        Config().save()
    config = Config.from_file()
    if args.model is not None:
        config_dict = config.model_dump()
        config_dict["model"] = args.model
        config = Config.model_validate(config_dict)
        config.validate_config()
        logger.info("Default model is set to `%s`", args.model)

    if args.cmd == "clean":
        shutil.rmtree(config.logdir, ignore_errors=True)
    elif args.cmd == "config":
        if args.init:
            config = Config()
            config.save()
        if args.edit:
            config = config.edit()
            config.validate_config()
        config.display()
    else:
        config.validate_config()
        wtf = WhatTheFuck.from_config(config)
        wtf.run()


if __name__ == "__main__":
    main()
