# Copyright (c) 2021-2025 Mario S. Könz; License: MIT
import dataclasses as dc
import typing as tp
from pathlib import Path

from ._components import AllComponents
from ._components._payload._docker_executors import subprocess_run

__all__ = ["TickSetter"]


@dc.dataclass
class TickSetter:
    ns: AllComponents
    release_message: str
    major: bool
    minor: bool

    def _print(self, msg: str, **kwgs: tp.Any) -> None:
        # pylint: disable=protected-access
        self.ns._print(msg, **kwgs)

    @property
    def init_file(self) -> Path:
        data = self.ns.auxe.python_project
        res: Path = self.ns.auxcon_file.parent / data.module_dir / "__init__.py"
        return res

    @property
    def release_notes_file(self) -> Path:
        data = self.ns.auxe.project
        res: Path = self.ns.auxcon_file.parent / data.source_dir / "release-notes.txt"
        return res

    def bake(self) -> None:
        data = self.ns.auxe.python_project
        version = data.version

        prefix = "v"
        if version.startswith(prefix):
            version = version[1:]
        else:
            prefix = ""

        parts = version.split(".")
        if self.major:
            idx = 0
        elif self.minor:
            idx = 1
        else:
            idx = 2
        parts[idx] = str(int(parts[idx]) + 1)
        for i in range(idx + 1, len(parts)):
            parts[i] = "0"
        new_version = prefix + ".".join(parts)

        init = self.init_file
        with init.open("r", encoding="utf8") as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if "__version__" in line:
                    lines[i] = line.replace(version, new_version)

        self._print(f"{version}->{new_version}")
        with init.open("w", encoding="utf8") as f:
            f.writelines(lines)

        release_notes = self.release_notes_file
        with release_notes.open("r", encoding="utf8") as f:
            lines = f.readlines()

        for line in lines:
            if line.startswith(new_version):
                raise RuntimeError(f"{new_version} already found in {release_notes}")
        lines.insert(0, f"{new_version} {self.release_message}\n")
        with release_notes.open("w", encoding="utf8") as f:
            f.writelines(lines)

    def commit(self) -> None:
        subprocess_run(
            ["git", "add", self.init_file, self.release_notes_file], check=True
        )
        out = subprocess_run(
            ["git", "commit", "-m", self.release_message],
            check=True,
            capture_output=True,
        )
        self._print(out.stdout.decode().strip())
