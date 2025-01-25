# licomp-osadl

Implementation of Licomp using OSADL's matrix

Licomp Osadl provides compatibility data:

* between an Open Source outbound license and inbound Open Source licenses
* when copying code from one Open Source component to another and
* the Open Source components are unmodified

Licomp Osadl uses OSADL's [license matrix](https://www.osadl.org/fileadmin/checklists/matrix.json), part of [OSADL's license checklist](https://www.osadl.org/Access-to-raw-data.oss-compliance-raw-data-access.0.html)

## Introduction 

Licomp Osadl implements the [Licomp](https://github.com/hesa/licomp) api for communication with the Licomp resources. For a better understanding of Licomp we suggest you read:

* [Licomp basic concepts](https://github.com/hesa/licomp/#licomp-concepts)
* [Licomp reply format](https://github.com/hesa/licomp/blob/main/docs/reply-format.md)

The various licomp resources below can be accessed as a group by:
* [licomp-toolkit](https://github.com/hesa/licomp-toolkit) - (`pip install licomp-toolkit`)

Licomp is used be the following compatibility resources:
* [licomp-hermione](https://github.com/hesa/licomp-hermione) - (`pip install licomp-hermione`)
* [licomp-proprietary](https://github.com/hesa/licomp-proprietary) - (`pip install licomp-proprietary`)
* [licomp-reclicense](https://github.com/hesa/licomp-reclicense) - (`pip install licomp-reclicense`)
* [licomp-dwheeler](https://github.com/hesa/licomp-dwheeler) - (`pip install licomp-dwheeler`)

# Using Licomp Osadl

Since Licomp Osadl implements [Licomp](https://github.com/hesa/licomp) we refer to the Licomp guides (both cli and python api).

## Command line interface

See [Licomp Comand Line Interface](https://github.com/hesa/licomp/blob/main/docs/cli-guide.md)

_Note: the commmad line program for Licomp Osadl is called `licomp-osadl`._

## Python module

See [Licomp Python API](https://github.com/hesa/licomp/blob/main/docs/python-api.md)

# Installing Licomp Osadl

## From pypi.org

Licomp Osadl is available via [pypi.org](https://pypi.org/) at: [https://pypi.org/project/licomp-osadl/](https://pypi.org/project/licomp-osadl/).


To install, simply do the following:

```
$ pip install licomp-osadl
```

## From github

Installing from github assumes you already have `pip` installed.

```
$ git clone https://github.com/hesa/licomp-osadl
$ pip install -r requirements.txt
$ pip install -r requirements-dev.txt
$ pip install .
```
