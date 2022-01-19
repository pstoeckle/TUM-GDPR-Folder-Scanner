# Scan SVN

[[_TOC_]]


## scan-directory

Scans all relevant files (CSV, TXT, PDF) for the given name, TUM name, and matriculation number.

**Usage**:

```console
$ scan-directory [OPTIONS]
```

**Options**:

* `-s, --directory DIRECTORY`: The directory we want to analyze.  [default: .]
* `-n, --name-to-search TEXT`: The name we are looking for. Please write the name in the form `Lastname Firstname` or `Firstname Lastname`.
* `-m, --matriculation-no TEXT`: The matriculation number we are looking for.
* `-t, --tum-name TEXT`: The TUM name, e.g., ga12acb.
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.
