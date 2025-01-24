import hashlib
import os
import platform
import subprocess
from dataclasses import dataclass
from shutil import get_terminal_size

import pyte
from logzero import logger

from wtf.command_output_loggers.base import CommandOutput, CommandOutputLoggerBase
from wtf.constants.constants import TERMINAL_PROMPT_END_MARKER


@dataclass(frozen=True)
class ScriptCmdLogger(CommandOutputLoggerBase):
    logfile: str
    terminal_prompt_lines: int = 1

    @property
    def session_name(self) -> str:
        return hashlib.sha256(self.logfile.encode()).hexdigest()

    def begin(self) -> None:
        platform_system = platform.system()
        logger.debug("Platform system: %s", platform_system)
        if platform_system == "Darwin":
            subprocess.run(["script", "-q", "-F", self.logfile])
        elif platform_system == "Linux":
            subprocess.run(["script", "-q", "-f", self.logfile])
        else:
            raise NotImplementedError("Only Unix-like systems are supported")

    def is_available(self) -> bool:
        return os.path.exists(self.logfile)

    def _emulate_terminal(self, data: str, width: int, height: int) -> list[str]:
        screen = pyte.Screen(width, height)
        stream = pyte.Stream(screen)
        stream.feed(data)
        return screen.display

    def extract_command_outputs(self) -> list[CommandOutput]:
        with open(self.logfile, "r+b") as f:
            data = f.read().decode("utf-8", "ignore")
            # NOTE: Clear the log file
            f.truncate(0)
        terminal_width = get_terminal_size().columns
        # NOTE: The terminal prompt lines are not included in the output
        terminal_prompt_lines = self.terminal_prompt_lines - 1

        cmd_outputs = []
        block: list[str] = []
        end_marker_counter = 0
        for row in self._emulate_terminal(data, terminal_width, data.count("\n") + 1):
            row = row.strip()
            if TERMINAL_PROMPT_END_MARKER in row:
                end_marker_counter += 1
                if terminal_prompt_lines:
                    block = block[:-terminal_prompt_lines]
                output = "\n".join(block).strip()
                if output:
                    cmd_outputs.append(CommandOutput(output=output))
                block = []
                continue
            if row:
                block.append(row)

        if end_marker_counter == 0:
            # NOTE: When the last output is too long, it may not contain the terminal prompt
            cmd_outputs.append(CommandOutput(output="\n".join(block).strip()))
        return cmd_outputs
