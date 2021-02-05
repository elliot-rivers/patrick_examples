# Welcome to python modules

## files as modules
Any loose file sitting on your current path is a python module:

```bash
python3 -m my_module
```

This has limitations. No ability to split your thoughts out and organize anything.

## Directories as modules (and submodules)

Directories can be modules too.

```bash
python3 -m another_module
```

`__init__.py` and `__main__.py` are special:
 * `__init__.py` runs when your module is imported the first time
 * `__main__.py` runs when your module is invoked as main (with `python3 -m`) 

## Representative example

Just dig around. Invoking the module will use the hard-coded values in the function:
```bash
python3 -m representative_example
```

### Getting silly with entrypoints

`__main__.py` doesnt' have to be your only entrypoint. Here, I've provided two more that allow user input in different ways:

```bash
# Prints help
python3 -m representative_example.cli --help

# Yells at you
python3 -m representative_example.cli

# Uses a default
python3 -m representative_example.cli -d1 22 

# Prints help
python3 -m representative_example.cli -d1 22 -d2 1.2
```

Or let it read a file:
```bash
python3 -m representative_example.file_io --json_file ./example_data.json
```

## More representative example

first generate the example mat file:
```bash
python3 -m weee.gen_example
```

run like this:
```bash
python3 -m weee --mat_file ./testo.mat
```

