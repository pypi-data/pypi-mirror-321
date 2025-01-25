<!--
SPDX-FileCopyrightText: Peter Pentchev <roam@ringlet.net>
SPDX-License-Identifier: BSD-2-Clause
-->

# Detect a UTF-8-capable locale for running child processes in

\[[Home][ringlet-home] | [Download][ringlet-download] | [GitLab][gitlab] | [PyPI][pypi] | [crates.io][crates-io] | [ReadTheDocs][readthedocs]\]

## Overview

Sometimes it is useful for a program to be able to run a child process and
more or less depend on its output being valid UTF-8. This can usually be
accomplished by setting one or more environment variables, but there is
the question of what to set them to - what UTF-8-capable locale is present
on this particular system? This is where the `utf8_locale` module comes in.

## Examples

For the Rust implementation:

    use std::process;
    
    use utf8_locale;
    
    let utf8env = utf8_locale::Utf8Detect()::new().detect()?;
    let cmd = process::Command::new(...).env_clear().envs(utf8_env.env);

For the Python implementation:

    import subprocess
    
    import utf8_locale
    
    utf8env = utf8_locale.Utf8Detect().detect()
    subprocess.check_output([...], encoding="UTF-8", env=utf8env.env)

## Classes (Python and Rust)

### `LanguagesDetect`

The `detect()` method of this class examines either the provided environment
variables or the current process's environment and returns a list of language
codes in order of preference that may then be used for determining which
UTF-8-capable locale to use.

### `Utf8Detect`

The `detect()` method of this class runs the external `locale` command to
obtain a list of the supported locale names, and then picks a suitable one to
use so that programs are more likely to output valid UTF-8 characters and
language-neutral messages. It prefers the `C` base locale, but if neither
`C.UTF-8` nor `C.utf8` is available, it will fall back to a list of other
locale names that are likely to be present on the system. The list of
preferred language codes is configurable.

## Functions

Note that for the Python and Rust implementation it is recommended to
use the `Utf8Detect` and, if needed, the `LanguagesDetect` builder classes to
perform the detection.

### `detect_utf8_locale()`

The `detect_utf8_locale()` function runs the external `locale` command to
obtain a list of the supported locale names, and then picks a suitable one to
use so that programs are more likely to output valid UTF-8 characters and
language-neutral messages. It prefers the `C` base locale, but if neither
`C.UTF-8` nor `C.utf8` is available, it will fall back to a list of other
locale names that are likely to be present on the system.

### `get_utf8_vars()`

The `get_utf8_vars()` function invokes `detect_utf8_locale()` and then returns
a dictionary/hashmap containing two entries: `LC_ALL` set to the obtained
locale name and `LANGUAGE` set to an empty string so that recent versions of
the gettext library do not choose a different language to output messages in.

### `get_utf8_env()`

The `get_utf8_env()` function invokes `detect_utf8_locale()` and then returns
a dictionary/hashmap containing the current environment variables,
`LC_ALL` set to the obtained locale name, and `LANGUAGE` set to an empty
string so that recent versions of the gettext library do not choose
a different language to output messages in.

### `get_preferred_languages()`

The `get_preferred_languages()` function examines either the current process
environment or the provided dictionary and returns a list of the languages
specified in the locale variables (`LC_ALL`, `LANG`, `LC_MESSAGES`, etc).
It may be used by programs to add the user's currently preferred locale to
their own settings.

## Contact

The `utf8-locale` library was written by [Peter Pentchev][roam].
It is developed in [a GitLab repository][gitlab]. This documentation is
hosted at [Ringlet][ringlet-home] with a copy at [ReadTheDocs][readthedocs].

[roam]: mailto:roam@ringlet.net "Peter Pentchev"
[gitlab]: https://gitlab.com/ppentchev/utf8-locale "The utf8-locale GitLab repository"
[pypi]: https://pypi.org/project/utf8-locale/ "The utf8-locale Python Package Index page"
[crates-io]: https://crates.io/crates/utf8-locale "The utf8-locale crate on crates.io"
[readthedocs]: https://utf8-locale.readthedocs.io/ "The utf8-locale ReadTheDocs page"
[ringlet-home]: https://devel.ringlet.net/devel/utf8-locale/ "The Ringlet utf8-locale homepage"
[ringlet-download]: https://devel.ringlet.net/devel/utf8-locale/download/ "The Ringlet utf8-locale download page"
