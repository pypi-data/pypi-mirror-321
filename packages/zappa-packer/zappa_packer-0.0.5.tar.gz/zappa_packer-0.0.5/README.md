## Zappa Packer

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## About
This is not an official zappa package, this is just the `zappa package` command isolated
**Zappa Packager** makes it super easy to pack server-less, event-driven Python applications (including, but not limited to, WSGI web apps) on AWS Lambda + API Gateway. This package only includes the packing command. For full official zappa you can go here

https://github.com/zappa/Zappa

If you've got a Python web app (including Django and Flask apps), it's as easy as:

```
$ pip install zappa-packer
$ zappa-packer
```
### Package

For using, just run the following command:

    $ zappa-packer

#### How Zappa Makes Packages

Zappa will automatically package your active virtual environment into a package which runs smoothly on AWS Lambda.

During this process, it will replace any local dependencies with AWS Lambda compatible versions. Dependencies are included in this order:

  * Lambda-compatible `manylinux` wheels from a local cache
  * Lambda-compatible `manylinux` wheels from PyPI
  * Packages from the active virtual environment
  * Packages from the local project directory

It also skips certain unnecessary files, and ignores any .py files if .pyc files are available.

