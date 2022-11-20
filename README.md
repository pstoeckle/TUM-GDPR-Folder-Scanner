# TUM-GDPR-Folder-Scanner

Students at the [Technical University of Munich (TUM)](https://www.tum.de/en/) have the right to request to information on personal data after Art. 17 GDPR.
I wrote this script to check local folders for such information.

## Usage


```shell
$ tum-gdpr-folder-scanner --help
Usage: tum-gdpr-folder-scanner [OPTIONS] [DIRECTORY]

  Scans all relevant files (CSV, PDF, TXT, XLSX, XML) for the given name, TUM
  name, and matriculation number.

Arguments:
  [DIRECTORY]  The directory we want to analyze.  [default: .]

Options:
  -n, --name-to-search TEXT       The name we are looking for. Please write
                                  the name in the form `Lastname Firstname` or
                                  `Firstname Lastname`.
  -m, --matriculation-no TEXT     The matriculation number we are looking for.
  -t, --tum-id TEXT               The TUM ID, e.g., ga12acb.
  -S, --skip-pdfs                 The PDF extraction takes some time. You can
                                  skip it for a first run.
  -X, --skip-xlsx                 The XLSX extraction takes some time. You can
                                  skip it for a first run.
  -v, --version                   Shows the version and exits.
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.
```

## Contact

If you have any question, please contact [Patrick Stöckle](mailto:patrick.stoeckle@posteo.de).
