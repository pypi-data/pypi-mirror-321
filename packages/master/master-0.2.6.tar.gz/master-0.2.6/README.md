# Master

[![Deploy pages](https://github.com/jpedro/master/actions/workflows/pages.yaml/badge.svg)](https://github.com/jpedro/master/actions/workflows/pages.yaml)

Generates deterministic passwords.


<!-- ![Pictutre](https://raw.githubusercontent.com/jpedro/master/master/docs/strong.jpg) -->
<!-- ![Strong password](https://raw.githubusercontent.com/jpedro/master/master/docs/blink.gif) -->

This is inspired by [spectre.app](https://spectre.app/) but simpler.
This uses a sha256 hashed combination of
`username + password + service + version` (`version` is now locked to
`0`) to generate the same password, over and over again, thus
eliminating the need to store, maintain and back up other generated
passwords.

[jpedro.github.io/master](https://jpedro.github.io/master/) has the
browser experience.

The used service name list is kept under the file
`~/.config/master/list.txt` (or whatever `MASTER_LIST` points to)
*purely for autocompletion*, which will be added later.

Eventually, the idea is to create a simple browser extension that uses
the URL domain name as the service.


## Install

    pip install master

<!--
Yes, yes. The package is called `masterpass` but the binary is called
`master`. To be fixed after [#2582](https://github.com/pypi/support/issues/2582)
is resolved.
-->


## Usage

```
$ master --help

NAME
    master — Generates deterministic passwords for services

USAGE
    master NAME                 Gets the password for service NAME
    master -l, --list           Lists all stored services
    master -r, --remove NAME    Removes service NAME from the stored list
    master -v, --version        Shows the version
    master -h, --help           Shows this help

```


## Environment variables

| Name                | Default                       |
| ------------------- | ----------------------------- |
| `MASTER_LIST`       | `~/.config/master/list.txt`   |
| `MASTER_USERNAME`   | (None) [1]                    |
| `MASTER_PASSWORD`   | (None) [1]                    |
| `MASTER_SEPARATOR`  | `-`                           |
| `MASTER_LENGTH`     | `6`                           |
| `MASTER_CHUNKS`     | `6`                           |

Using these default settings, it will generate a password that's 41
characters long. 6 chunks of 6 character long with 5 separators in
between.

> *Note*
> [1] If you don't set the `MASTER_USERNAME` or the `MASTER_PASSWORD` you
> will be prompted for them.


## Todos

- [ ] Make the `MASTER_LIST` a directory to avoid git conflicts.
- [ ] Integrate the user name with Oauth2 providers.
      Maybe the `sub` after an authentication flow can be used instead
      of the flat username. Cons: the email provider can change for the
      same email address. Plus, not 100% sure if one wants to tie
      passwords to an email.
- [ ] Lock (close) the master page after 30 seconds of inactivity.
