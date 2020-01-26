# 00006_cli

## info

### with_argparse

- `python with_argparse.py John` prints -> Hello, John
- `python with_argparse.py John -g Howdy` prints -> Howdy, John

argparse help `python with_argparse.py --help`

```bash
usage: with_argparse.py [-h] [-g GREETING] name

greetings

positional arguments:
name                  name of user

optional arguments:
-h, --help            show this help message and exit
-g GREETING, --greeting GREETING
                        optional alternate greeting
```

### with_click

- `python with_argparse.py John` prints -> Hello, John
- `python with_argparse.py John -g Howdy` prints -> Howdy, John

click help `python with_click.py --help`

```bash
Usage: with_click.py [OPTIONS] NAME

Options:
  -g, --greeting TEXT  optional alternate greeting
  --help               Show this message and exit.
```
