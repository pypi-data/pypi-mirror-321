"""Manipulate semantic versioning (SemVer)

Manipulate semantic version strings:
1. Create a new version number,

1. initialize it with an existing number

1. Read it from an existing project setup.cfg file.

1. Validate the version string.

1. Compare one version number with another.

See also https://semver.org/
"""

import configparser
import logging
import re
import tempfile
from pathlib import Path
from pathlib import PosixPath
from pathlib import WindowsPath
from typing import Union

from beetools.utils import error

_PROJ_DESC = __doc__.split("\n")[0]
_PROJ_PATH = Path(__file__)
_PROJ_NAME = _PROJ_PATH.stem


class SemVerIt:
    """Manipulate semantic versioning (SemVer)

    Manipulate semantic version numbers.  Create a new version number,
    initialize it with an existing number or alternatively read it from an
    existing project setup.py file.  Compare a version number with another.

    See also https://semver.org/
    """

    def __init__(
        self,
        p_version: Path | str | list = None,
        # p_setup_cfg_pth: Path = None,
        p_parent_log_name: str = None,
        p_verbose: bool = True,
    ) -> None:
        """Create a new SemVerIt instance.

        :parm p_version:
            Initial version to start with.
        :parm p_setup_cfg_pth:
            setup.cfg file from where the version number can be read.
        :parm p_parent_log_name:
            Name of the parent.  In combination witt he class name it will
            form the logger name.
        :parm p_verbose:
            Write messages to the console.
        :return: SemverIt

        :Examples:
        >>> import src
        >>> svit = src.SemVerIt()
        >>> print(svit)
        0.0.0
        >>> svit = src.SemVerIt('5.5.5')
        >>> print(svit)
        5.5.5
        >>> svit = src.SemVerIt([5 ,5 ,5])
        >>> print(svit)
        5.5.5
        >>> svit = src.SemVerIt(['5' ,'5' ,'5'])
        >>> print(svit)
        5.5.5
        """
        self.success = True
        if p_parent_log_name:
            self._log_name = f"{p_parent_log_name}.{_PROJ_NAME}"
            self.logger = logging.getLogger(self._log_name)
        self.verbose = p_verbose

        if (isinstance(p_version, WindowsPath) or isinstance(p_version, PosixPath)) and p_version.exists():
            self.version = self.get_from_setup_cfg(p_version)
        elif isinstance(p_version, str):
            self.version = p_version
        elif isinstance(p_version, list):
            self.version = f"{p_version[0]}.{p_version[1]}.{p_version[2]}"
        else:
            self.version = "0.0.0"
        self.verify(self.version)
        major, minor, patch = self.version.split(".")
        self.maj = int(major)
        self.min = int(minor)
        self.patch = int(patch)

    def __eq__(self, p_other: Union[str, "SemVerIt"]) -> bool:
        """Equal: ==

        :param p_other: Union[str, 'SemVerIt']
            Version strings to compare.
        :return: bool
        examples::
        >>> import src
        >>> svit = src.SemVerIt('5.5.5')
        >>> svit == '5.5.5'
        True
        >>> svit == '5.5.4'
        False
        """
        rc = False
        if isinstance(p_other, str) and self.version == p_other:
            rc = True
        elif isinstance(p_other, SemVerIt) and self.version == p_other.version:
            rc = True
        return rc

    def __le__(self, p_other):
        """Less or equal: <=

        :param p_other:
            Version string to compare.
        :return: bool
        examples::
        >>> import src
        >>> svit = src.SemVerIt('5.5.5')
        >>> svit <= '5.5.5'
        True
        >>> svit <= '5.5.4'
        False
        >>> svit <= '5.5.6'
        True
        """
        rc = False
        if isinstance(p_other, str):
            o_major, o_minor, o_patch = p_other.split(".")
        elif isinstance(p_other, SemVerIt):
            o_major, o_minor, o_patch = p_other.version.split(".")
        else:
            return rc
        o_major = int(o_major)
        o_minor = int(o_minor)
        o_patch = int(o_patch)
        if self.maj < o_major:
            rc = True
        elif self.maj == o_major:
            if self.min < o_minor:
                rc = True
            elif self.min == o_minor:
                if self.patch < o_patch:
                    rc = True
                elif self.patch == o_patch:
                    rc = True
                elif self.patch > o_patch:
                    rc = False
            elif self.min > o_minor:
                rc = False
        elif self.maj > o_major:
            rc = False
        return rc

    def __lt__(self, p_other):
        """Less than: <

        :param p_other:
            Version string to compare.
        :return: bool
        examples::
        >>> import src
        >>> svit = src.SemVerIt('5.5.5')
        >>> svit < '5.5.5'
        False
        >>> svit < '5.5.4'
        False
        >>> svit < '5.5.6'
        True
        """

        rc = False
        if isinstance(p_other, str):
            o_major, o_minor, o_patch = p_other.split(".")
        elif isinstance(p_other, SemVerIt):
            o_major, o_minor, o_patch = p_other.version.split(".")
        else:
            return rc
        o_major = int(o_major)
        o_minor = int(o_minor)
        o_patch = int(o_patch)
        if self.maj < o_major:
            rc = True
        elif self.maj == o_major:
            if self.min < o_minor:
                rc = True
            elif self.min == o_minor:
                if self.patch < o_patch:
                    rc = True
                elif self.patch == o_patch:
                    rc = False
                elif self.patch > o_patch:
                    rc = False
            elif self.min > o_minor:
                rc = False
        elif self.maj > o_major:
            rc = False
        return rc

    def __ge__(self, p_other) -> bool:
        """Greater or equal: >=

        :param p_other:
            Version strings to compare.
        :return: bool
        examples::
        >>> import src
        >>> svit = src.SemVerIt('5.5.5')
        >>> svit >= '5.5.5'
        True
        >>> svit >= '5.5.4'
        True
        >>> svit >= '5.5.6'
        False
        """
        rc = False
        if isinstance(p_other, str):
            o_major, o_minor, o_patch = p_other.split(".")
        elif isinstance(p_other, SemVerIt):
            o_major, o_minor, o_patch = p_other.version.split(".")
        else:
            return rc
        o_major = int(o_major)
        o_minor = int(o_minor)
        o_patch = int(o_patch)

        if self.maj > o_major:
            rc = True
        elif self.maj == o_major:
            if self.min > o_minor:
                rc = True
            elif self.min == o_minor:
                if self.patch >= o_patch:
                    rc = True
                # elif self.patch == o_patch:
                #     return False
                elif self.patch < o_patch:
                    rc = False
            elif self.min < o_minor:
                rc = False
        elif self.maj < o_major:
            rc = False
        return rc

    def __gt__(self, p_other) -> bool:
        """Greater than: >

        :param p_other:
            Version string to compare.
        :return: bool
        examples::
        >>> import src
        >>> svit = src.SemVerIt('5.5.5')
        >>> svit > '5.5.5'
        False
        >>> svit > '5.5.4'
        True
        >>> svit > '5.5.6'
        False
        """
        rc = False
        if isinstance(p_other, str):
            o_major, o_minor, o_patch = p_other.split(".")
        elif isinstance(p_other, SemVerIt):
            o_major, o_minor, o_patch = p_other.version.split(".")
        else:
            return rc
        o_major = int(o_major)
        o_minor = int(o_minor)
        o_patch = int(o_patch)

        if self.maj > o_major:
            rc = True
        elif self.maj == o_major:
            if self.min > o_minor:
                rc = True
            elif self.min == o_minor:
                if self.patch > o_patch:
                    rc = True
                elif self.patch == o_patch:
                    rc = False
                elif self.patch < o_patch:
                    rc = False
            elif self.min < o_minor:
                rc = False
        elif self.maj < o_major:
            rc = False
        return rc

    def __ne__(self, p_other) -> bool:
        """Not equal: !=

        :param p_other:
            Version string to compare.
        :return: bool
        examples::
        >>> import src
        >>> svit = src.SemVerIt('5.5.5')
        >>> svit != '5.5.5'
        False
        >>> svit !='5.5.4'
        True
        >>> svit != '5.5.6'
        True
        """
        rc = False
        if isinstance(p_other, str) and self.version != p_other:
            rc = True
        elif isinstance(p_other, SemVerIt) and self.version != p_other.version:
            rc = True
        return rc

    def __repr__(self) -> str:
        """printable representation of the object

        :return: str
        examples::
        >>> import src
        >>> svit = src.SemVerIt('5.5.5')
        >>> svit
        5.5.5
        """
        return self.version

    def __str__(self) -> str:
        """printable representation of the object

        :return: str
        examples::
        >>> import src
        >>> svit = src.SemVerIt('5.5.5')
        >>> svit
        5.5.5
        """
        return self.version

    def bump_maj(self) -> str:
        """Bump the major version.

        The major version will be increased by 1. In the process the minor
        and patch versions will be reset to 0 i.e.
        0.0.1 -> 1.0.0.
        0.1.2 -> 1.0.0

        :return: str, Complete version string
        examples::
        >>> import src
        >>> svit = src.SemVerIt('5.5.5')
        >>> svit.bump_maj()
        '6.0.0'
        """
        self.maj += 1
        self.min = 0
        self.patch = 0
        self.version = f"{self.maj}.{self.min}.{self.patch}"
        return self.version

    def bump_min(self) -> str:
        """Bump the minor version.

        The minor version will be increased by 1. The major version will
        stay the same, but the patch version will be reset to 0 i.e.
        0.0.1 -> 0.1.0.
        0.1.2 -> 0.2.0

        :return: str, Complete version string
        examples::
        >>> import src
        >>> svit = src.SemVerIt('5.5.5')
        >>> svit.bump_min()
        '5.6.0'
        """
        self.min += 1
        self.patch = 0
        self.version = f"{self.maj}.{self.min}.{self.patch}"
        return self.version

    def bump_patch(self) -> str:
        """Bump the patch version.

        The patch version will be increased by 1. The major- and the minor
        version will stay the same.
        0.0.1 -> 0.0.2.
        0.1.2 -> 0.1.3

        :return: str, Complete version string
        examples::
        >>> import src
        >>> svit = src.SemVerIt('5.5.5')
        >>> svit.bump_patch()
        '5.5.6'
        """
        self.patch += 1
        self.version = f"{self.maj}.{self.min}.{self.patch}"
        return self.version

    def get_from_setup_cfg(self, p_pth) -> str:
        """Read the version number from the setup.cfg file.

        The project setup.cfg file (should) contain the version number for
        the current module and package.  Most projects already has a setup.py
        file and is most probably also the correct version currently pushed
        to git.  It makes sense to read it from there.

        :parm p_pth:
            Path to the setup.cfg file
        :return: str, Complete version string

        >>> import src
        >>> import tempfile
        >>> from pathlib import Path
        >>> cfg = Path(tempfile.mkdtemp(), 'setup.cfg')
        >>> cfg.write_text(_setup_cfg_contents)
        27
        >>> svit = src.SemVerIt()
        >>> svit.get_from_setup_cfg(p_pth = cfg)
        '2.3.4'
        >>> cfg.write_text(_setup_cfg_contents_faulty)
        33
        >>> svit = src.SemVerIt()
        >>> svit.get_from_setup_cfg(p_pth = cfg)
        '0.0.0'
        """
        setup_cfg = configparser.ConfigParser(inline_comment_prefixes="#")
        setup_cfg.read([p_pth])
        if setup_cfg.has_option("metadata", "version"):
            version = setup_cfg.get("metadata", "version")
            major, minor, patch = version.split(".")
            self.maj = int(major)
            self.min = int(minor)
            self.patch = int(patch)
            self.version = version
        else:
            version = self.version
        return version

    @staticmethod
    def verify(p_version: str | list):
        version = re.fullmatch(r"^[0-9]+\.[0-9]+\.[0-9]+$", p_version)
        if not version:
            raise FaultyVersionString(_status_codes[1100], p_version)
        return True


def do_examples(p_cls=True) -> bool:
    """A collection of implementation examples for SemVerIt.

    A collection of implementation examples for SemVerIt. The examples
    illustrate in a practical manner how to use the methods.  Each example
    show a different concept or implementation.

    :param p_cls:
        Clear the screen or not at startup of Archiver
    :return: bool, Execution status of the examples.
    """
    success = do_example1()
    success = do_example2() and success
    success = do_example3() and success
    success = do_example4() and success
    return success


def do_example1():
    """A working example of the implementation of SemVerIt.

    Example1 illustrate the following concepts:
    1. Create an abject with no parameters i.e. the default.
    2. Bump the patch version
    3. Bump the minor version.  The patch version is reset to 0.
    4. Bump the minor version.
    5. Bump the patch version
    6. Bump the major version.  The patch and minor version are reset to 0.

    :return: bool, Execution status of the examples.
    """
    success = True
    svit = SemVerIt()
    print(f"{svit.version} - Initialize")
    print(f"{svit.version} -> {svit.bump_patch()} - Bump patch version")
    print(f"{svit.version} -> {svit.bump_min()} - Bump minor version")
    print(f"{svit.version} -> {svit.bump_min()} - Bump minor version again")
    print(f"{svit.version} -> {svit.bump_patch()} - Bump patch version")
    print(f"{svit.version} -> {svit.bump_maj()} - Bump major version")
    return success


def do_example2():
    """A working example of the implementation of SemVerIt.

    Example1 illustrate the following concepts:
    1.Initialize object with version = 3.2.1
    2. Bump the patch version
    3. Bump the minor version.  The patch version is reset to 0.
    4. Bump the minor version.
    5. Bump the patch version
    6. Bump the major version.  The patch and minor version are reset to 0.

    :return: bool, Execution status of the examples.
    """
    success = True
    svit = SemVerIt(p_version="3.2.1")
    print(f"{svit.version} - Initialize")
    print(f"{svit.version} -> {svit.bump_patch()} - Bump patch version")
    print(f"{svit.version} -> {svit.bump_min()} - Bump minor version")
    print(f"{svit.version} -> {svit.bump_min()} - Bump minor version again")
    print(f"{svit.version} -> {svit.bump_patch()} - Bump patch version")
    print(f"{svit.version} -> {svit.bump_maj()} - Bump major version")
    return success


def do_example3():
    """A working example of the implementation of SemVerIt.

    Example1 illustrate the following concepts:
    1. Read the version from the setup.cfg file
    2. Bump the patch version
    3. Bump the minor version.  The patch version is reset to 0.
    4. Bump the minor version.
    5. Bump the patch version
    6. Bump the major version.  The patch and minor version are reset to 0.

    :return: bool, Execution status of the examples.
    """
    success = True
    setup_pth = _create_setup_cfg()
    svit = SemVerIt(p_version=setup_pth)
    print(f"{svit.version} - Initialize")
    print(f"{svit.version} -> {svit.bump_patch()} - Bump patch version")
    print(f"{svit.version} -> {svit.bump_min()} - Bump minor version")
    print(f"{svit.version} -> {svit.bump_min()} - Bump minor version again")
    print(f"{svit.version} -> {svit.bump_patch()} - Bump patch version")
    print(f"{svit.version} -> {svit.bump_maj()} - Bump major version")
    return success


def do_example4():
    """A working example of the implementation of SemVerIt.

    Example4 illustrate the comparison of versions/releases

    :return: bool, Execution status of the examples.
    """
    success = True
    # setup_pth = _create_setup_cfg()
    sample = [
        "4.0.0",
        "4.6.4",
        "4.4.6",
        "5.4.5",
        "5.5.4",
        "5.5.5",
        "5.5.6",
        "5.6.5",
        "6.0.0",
        "6.4.6",
        "6.6.4",
    ]
    svit = SemVerIt("5.5.5")
    for ver in sample:
        if svit == ver:
            print(f"{svit} == {ver}")
        elif svit > ver:
            print(f"{svit} > {ver}")
        elif svit < ver:
            print(f"{svit} < {ver}")
    return success


_setup_cfg_contents = """\
[metadata]
version = 2.3.4
"""

_setup_cfg_contents_faulty = """\
[metadata]
    something = 2.3.4
"""


def _create_setup_cfg():
    working_dir = Path(tempfile.mktemp())
    working_dir.mkdir()
    setup_cfg_pth = working_dir / "setup.cfg"
    setup_cfg_pth.write_text(_setup_cfg_contents)
    return setup_cfg_pth


class SemVerItException(Exception):
    """
    Error handling in SemVerIt is done with exceptions. This class is the base of all exceptions raised by SemVerIt
    Some other types of exceptions might be raised by underlying libraries.
    """

    def __init__(self, status, data):
        super().__init__()
        self.__code = status[0]
        self.__data = data
        self.__title = status[1]
        print(error(f"{self.__code}:{self.__title}"))
        print(error(f"Source = {self.__data}"))

    @property
    def code(self):
        """
        The (decoded) data returned by the PackageIt API
        """
        return self.__code

    @property
    def data(self):
        """
        The (decoded) data returned by the PackageIt API
        """
        return self.__data

    @property
    def title(self):
        """
        The status returned by the PackageIt API
        """
        return self.__title

    def __str__(self):
        return f"{self.__code}: {self.__title}"


class FaultyVersionString(SemVerItException):
    """
    Exception raised if the version string is invalid.
    """


_status_codes = {
    # Informational.
    1000: (
        1000,
        "Placeholder",
    ),
    # Faulty version.
    1100: (
        1100,
        "The version string is faulty.  It should be in the form of n.n.n i.e. 1.2.3",
    ),
}

if __name__ == "__main__":
    do_examples()
