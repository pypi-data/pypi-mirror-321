# pynpdc

`pynpdc` is a library for accessing the
[Norwegian Polar Data Centre](https://data.npolar.no/) using Python3. It
provides clients with simple methods for logging in and out as well as fetching
and manipulating datasets, attachments, and records.

It is based on the following REST APIs:

- [NPDC Auth API (Komainu)](https://beta.data.npolar.no/-/docs/auth)
- [NPDC Dataset API (Kinko)](https://beta.data.npolar.no/-/docs/dataset/)

## Getting started

Use

```
pip3 install pynpdc
```

to install `pynpdc` into your project.

## Jupyter

If you want to run the examples, install:

```sh
pip install jupyter urllib3
```

_(`urllib3` helps to get rid of the InsecureRequestWarning when you deal with
staging entrypoints.)_

Then execute

```sh
jupyter lab
```

to run the user interface. The examples are found in the folder
`jupyter-notebooks`.
