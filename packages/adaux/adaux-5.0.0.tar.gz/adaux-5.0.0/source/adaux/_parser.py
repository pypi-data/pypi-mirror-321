# Copyright (c) 2021-2025 Mario S. Könz; License: MIT
import configparser
import contextlib
import filecmp
import shutil
import tempfile
import typing as tp
from pathlib import Path

import jinja2
import tomlkit

from ._base_parser import BaseParser
from ._proto_namespace import _ProtoNamespace
from ._yaml import CommentedMap  # type: ignore
from ._yaml import CommentedSeq  # type: ignore
from ._yaml import yaml  # type: ignore

__all__ = ["ConfigParser", "YamlParser", "Jinja2Parser", "TomlParser"]


class ConfigParser(BaseParser):
    @classmethod
    def to_conf(cls, data: _ProtoNamespace) -> tp.Any:
        conf = configparser.ConfigParser()
        conf.read_dict(data)
        return conf

    @classmethod
    def from_conf(cls, conf: tp.Any) -> _ProtoNamespace:
        res = _ProtoNamespace()
        for key, val in conf.items():
            if key != "DEFAULT":
                res[key] = val

        cls.rec_walk(
            res,
            [
                (
                    lambda x: isinstance(x, configparser.SectionProxy),
                    lambda x: _ProtoNamespace(x.items()),
                ),
                (
                    lambda x: isinstance(x, str) and "\n" in x,
                    lambda x: x.strip().split("\n"),
                ),
            ],
        )
        return res

    @classmethod
    def read(cls, filename: Path) -> _ProtoNamespace:
        conf = configparser.ConfigParser()
        conf.read(filename)
        return cls.from_conf(conf)

    @classmethod
    def read_string(cls, text: str) -> _ProtoNamespace:
        conf = configparser.ConfigParser()
        conf.read_string(text)
        return cls.from_conf(conf)

    @classmethod
    def write(cls, data: _ProtoNamespace, dest: Path) -> bool:
        with tempfile.NamedTemporaryFile("w") as tmp:
            with open(tmp.name, "w", encoding="utf-8") as f:
                cls.write_stream(data, f)
            cls._remove_trailing_space(Path(f.name))
            if dest.exists() and filecmp.cmp(f.name, dest):
                return False
            cls.ensure_parent(dest)
            shutil.copyfile(f.name, dest)
            return True

    @classmethod
    def write_stream(cls, data: _ProtoNamespace, f: tp.TextIO) -> None:
        conf = cls.to_conf(data)
        cls.rec_walk(
            conf,
            [
                (
                    lambda obj: isinstance(obj, str)
                    and obj.startswith("[")
                    and obj.endswith("]"),
                    lambda x: (
                        "\n"
                        + "\n".join(
                            y[1:-1] if y[0] == "'" else y for y in x[1:-1].split(", ")
                        )
                        if x[1:-1]
                        else ""
                    ),
                ),
                (
                    lambda obj: isinstance(obj, str)
                    and obj.startswith("{")
                    and obj.endswith("}"),
                    lambda x: (
                        "\n"
                        + "\n".join(
                            (y[1:-1] if y[0] == "'" else y).replace("': '", " = ")
                            for y in x[1:-1].split(", ")
                        )
                        if x[1:-1]
                        else ""
                    ),
                ),
            ],
        )
        conf.write(f)

    @classmethod
    def _remove_trailing_space(cls, dest: Path) -> None:
        with dest.open("r") as f:
            lines = f.readlines()

        for i, x in enumerate(lines):
            if len(x) > 1 and x[-2] == " ":
                lines[i] = x[0:-2] + "\n"

        if lines[-1] == "\n":
            lines.pop(-1)

        with dest.open("w") as f:
            f.writelines(lines)


class YamlParser(BaseParser):
    @classmethod
    def read(cls, filename: Path) -> _ProtoNamespace:
        with filename.open("r") as f:
            res = yaml.load(f)
        return cls.from_conf(res)

    @classmethod
    def from_conf(cls, conf: tp.Mapping[str, tp.Any]) -> _ProtoNamespace:
        res = _ProtoNamespace()
        for key, val in conf.items():
            if key != "DEFAULT":
                res[key] = val

        cls.rec_walk(
            res,
            [
                (
                    lambda x: isinstance(x, CommentedMap),
                    lambda x: _ProtoNamespace(x.items()),
                ),
                (
                    lambda x: isinstance(x, CommentedSeq),
                    list,
                ),
            ],
        )
        return res

    @classmethod
    def to_conf(cls, config: _ProtoNamespace) -> tp.Any:
        return cls.rec_walk(
            config,
            [
                (
                    lambda x: isinstance(x, (_ProtoNamespace, dict)),
                    lambda x: CommentedMap(x.items()) if x else None,
                ),
                (
                    lambda x: isinstance(x, list),
                    lambda x: CommentedSeq(x) if x else None,
                ),
            ],
        )

    @classmethod
    def write(cls, data: _ProtoNamespace, dest: Path) -> bool:
        cls.ensure_parent(dest)

        with tempfile.NamedTemporaryFile("w") as f:
            config = cls.to_conf(data)
            yaml.dump(config, f)

            if dest.exists() and filecmp.cmp(  # pylint: disable=unreachable
                f.name, dest
            ):
                return False

            shutil.copyfile(f.name, dest)
        return True

    @classmethod
    def write_stream(cls, data: _ProtoNamespace, f: tp.TextIO) -> None:
        config = cls.to_conf(data)
        yaml.dump(config, f)


class Jinja2Parser(BaseParser):
    @classmethod
    def read(cls, filename: Path) -> jinja2.Template:
        adaux_src = Path(__file__).resolve().parent / "src"
        loc = filename.parent
        # as we can have custom dockerfiles,
        # we load the adaux and the custom.
        loader_path = [
            loc,
            adaux_src / "docker" / "services",
            adaux_src / "docker" / "services" / "jinja-snippets",
        ]
        # goes up 2 parents and checks for jinja-snippets dir
        for _ in range(2):
            for x in loc.iterdir():
                if not x.is_dir():
                    continue
                if x.name == "jinja-snippets":
                    loader_path.append(x)
            loc = loc.parent

        # deduplicate
        loader = [jinja2.FileSystemLoader(x) for x in set(loader_path)]

        env = jinja2.Environment(
            loader=jinja2.ChoiceLoader(loader), undefined=jinja2.StrictUndefined
        )
        return env.get_template(str(filename.name))

    @classmethod
    def write(cls, data: str, dest: Path) -> bool:
        if data[-1:] != "\n":  # ensure newline
            data += "\n"

        while data[-2:] == "\n\n":
            data = data[:-1]

        cls.ensure_parent(dest)
        if dest.exists():
            with dest.open("r") as f:
                comp = f.read()
            if comp == data:
                return False

        with dest.open("w") as f:
            f.write(data)

        return True

    @classmethod
    @contextlib.contextmanager
    def render_to_tmp(cls, src: Path, **kwgs: tp.Any) -> tp.Iterator[Path]:
        tmp = tempfile.NamedTemporaryFile()
        path = Path(tmp.name)
        cls.render_to_dest(src, path, **kwgs)
        yield path

    @classmethod
    def render_to_dest(cls, src: Path, dest: Path, **kwgs: tp.Any) -> bool:
        assert ".jinja2" in src.suffix
        tpl = cls.read(src)
        render = tpl.render(**kwgs)
        return cls.write(render, dest)


class TomlParser(BaseParser):
    @classmethod
    def read(cls, filename: Path) -> _ProtoNamespace:
        with open(filename, encoding="utf-8") as f:
            content = f.read()
        return cls.read_string(content)

    @classmethod
    def read_string(cls, text: str) -> _ProtoNamespace:
        res = tomlkit.parse(text)
        return cls.rec_walk(  # type: ignore
            res,
            [
                (
                    lambda x: isinstance(
                        x,
                        (
                            tomlkit.container.Container,
                            tomlkit.items.InlineTable,
                            tomlkit.container.Table,
                        ),
                    ),
                    lambda x: _ProtoNamespace(x.items()),
                ),
                (lambda x: isinstance(x, tomlkit.items.Integer), int),
                (lambda x: isinstance(x, tomlkit.items.Float), float),
                (lambda x: isinstance(x, tomlkit.items.Bool), bool),
            ],
        )

    @classmethod
    def write(cls, data: tp.Any, dest: Path) -> bool:
        with tempfile.NamedTemporaryFile("w") as tmp:
            with open(tmp.name, "w", encoding="utf-8") as f:
                f.write(tomlkit.dumps(data))

            if dest.exists() and filecmp.cmp(f.name, dest):
                return False
            cls.ensure_parent(dest)
            shutil.copyfile(f.name, dest)
            return True
