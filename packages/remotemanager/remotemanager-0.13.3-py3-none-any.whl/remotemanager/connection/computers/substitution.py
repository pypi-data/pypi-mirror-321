import logging
import warnings
from typing import Union

from remotemanager.connection.computers.dynamicvalue import DynamicMixin

logger = logging.getLogger(__name__)


class Substitution(DynamicMixin):
    """
    Stores a jobscript template substitution

    Args:
        target:
            String to _replace_ in the template.
            Ideally should begin with a commenting character (#)
        name:
            String to replace _with_. At script generation, `target`
            will be replaced with `name`
        mode:
            Used by JUBETemplate

    .. note::
        For other args see the DynamicMixin class
    """

    __slots__ = ["target", "mode", "executed", "dependencies"]

    def __init__(self, target: str, name: str, mode: Union[str, None] = None, **kwargs):
        super().__init__(assignment=name, **kwargs)

        self.target = target
        self.mode = mode

        self.executed = False
        self.dependencies = []  # must calculate the value of these first

    def __hash__(self) -> int:
        return hash(self.target + self.name)

    def __str__(self):
        return str(self.value)

    def __repr__(self) -> str:
        return f"Substitution({self.target}, {self.name}) -> {self.value}"

    def __bool__(self):
        """
        Makes objects "falsy" if no value has been set, "truthy" otherwise
        """
        return self.value is not None

    @classmethod
    def from_string(
        cls, string: str, warn_invalid: bool = True, **kwargs
    ) -> "Substitution":
        """
        Create a substitution object from template string

        Args:
            string (str): Input string to generate from
            warn_invalid (bool): Invalid args name, target will be deleted. Warn if True
            kwargs: Any keyword args to override the string with
        """

        content = string.strip("#")  # actual internal "content"
        sym = content.split(":")[0]  # name, drop args for function extract
        string_args = cls.get_target_kwargs(string)

        logger.debug("\ttarget=%s, symbol=%s, args=%s", string, sym, string_args)

        invalid_args = ["name", "target"]
        for arg in invalid_args:
            if arg in kwargs:
                if warn_invalid:
                    warnings.warn(f"Invalid kwarg {arg}={kwargs[arg]} deleted")
                del kwargs[arg]

        string_args.update(kwargs)

        name = sym.lower()

        logger.debug("\tprocessed symbol: %s", string)

        return cls(name=name, target=string, **string_args)

    @property
    def target_kwargs(self):
        """Attempts to extract the kwargs from the target string"""
        return self.get_target_kwargs(self.target)

    @staticmethod
    def get_target_kwargs(string: str) -> dict:
        """Attempts to generate kwargs from input string"""
        args = string.strip("#").split(":")  # list of arg=val pairs

        return {arg.split("=")[0]: "=".join(arg.split("=")[1:]) for arg in args[1:]}

    @property
    def value(self) -> any:
        """
        Returns:
            value if present, else default
        """
        val = super().value

        if len(self.dependencies) == 0:
            return val
        # if we have dependents, we need to evaluate them
        evaluate = {}
        # int values cause this replace to fail
        # non strings probably shouldn't end up here,
        # but it's best not to error weirdly
        val = str(val)
        for dep in self.dependencies:
            evaluate[dep.arg] = dep.value
            # replace the target $value with the evaluated arg
            # print(f"replacing {dep.arg} -> {dep.value}")
            val = val.replace(f"${dep.arg}", str(dep.value))
        # now everything is replaced, we can freely eval
        # print(f"evaluating {val}")
        val = eval(str(val.strip()))
        # print(f"{self.arg}={val}\n")
        # cache the result
        self.value = val
        self.dependencies = {}

        return val

    @value.setter
    def value(self, value):
        super().set_value(value)

    @property
    def arg(self) -> str:
        """
        Returns:
            Argument which is exposed to the underlying URL for setting
        """
        return self.name.strip("$")

    @property
    def entrypoint(self) -> str:
        """Returns the name/name for this sub"""
        return self.name

    def pack(self, collect_value: bool = True) -> dict:
        """Store this Substitution in dict form"""
        data = super().pack(collect_value=collect_value)

        if self.mode is not None:
            data["mode"] = self.mode
        if self.target is not None:
            data["target"] = self.target

        return data
