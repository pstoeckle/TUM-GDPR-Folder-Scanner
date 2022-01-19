# Scan SVN

[[_TOC_]]


## scan-directory

```bash
scan-svn --help
Usage: scan-svn [OPTIONS]

  Scans all relevant files (CSV, PDF, TXT, XLSX, XML) for the given name, TUM
  name, and matriculation number.

Options:
  -s, --directory DIRECTORY    The directory we want to analyze.  [default: .]
  -n, --name-to-search TEXT    The name we are looking for. Please write the
                               name in the form `Lastname Firstname` or
                               `Firstname Lastname`.
  -m, --matriculation-no TEXT  The matriculation number we are looking for.
  -t, --tum-id TEXT            The TUM ID, e.g., ga12acb.
  -S, --skip-pdfs              The PDF extraction takes some time. You can
                               skip it for a first run.
  -X, --skip-xlsx              The XLSX extraction takes some time. You can
                               skip it for a first run.
  -v, --version                Shows the version and exits.
  --install-completion         Install completion for the current shell.
  --show-completion            Show completion for the current shell, to copy
                               it or customize the installation.
  --help                       Show this message and exit.
```
