#Back In Time

Copyright (C) 2008-2016 Oprea Dan, Bart de Koning, Richard Bailey, Germar Reitze, Taylor Raack

[![Build Status](https://travis-ci.org/bit-team/backintime.svg?branch=master)](https://travis-ci.org/bit-team/backintime)
[![Coverage Status](https://coveralls.io/repos/bit-team/backintime/badge.svg?branch=master&service=github)](https://coveralls.io/github/bit-team/backintime?branch=master)

##About

Back In Time is a simple backup tool for Linux, inspired by "flyback project".

It provides a command line client 'backintime' and a Qt4 GUI 'backintime-qt4'
both written in Python3.

You only need to specify 3 things:
* where to save snapshots
* what folders to backup
* backup frequency (manual, every hour, every day, every month)

#####Credits

* Francisco Manuel García Claramonte: Spanish translation
* Michael Wiedmann: German translation
* Niklas Grahn: Swedish translation
* Vanja Cvelbar: Slovenian translation
* Michel Corps: French translation
* Tomáš Vadina: Slovak translation
* Paweł Hołuj: Polish translation
* Vadim Peretokin: Russian translation
* translators from [Launchpad](https://translations.launchpad.net/backintime/trunk/+pots/back-in-time)

##Support

Please ask questions and report bug on
https://github.com/bit-team/backintime/issues

##Download

Please find the latest versions on
https://github.com/bit-team/backintime/releases/latest

##INSTALL

Back In Time is included in many distributions and can be installed from their
repositories.

#####Ubuntu PPA

We provide a PPA (private package archive) with current stable version (ppa:bit-team/stable)
and a testing PPA (ppa:bit-team/testing)

    sudo add-apt-repository ppa:bit-team/stable
    sudo apt-get update
    sudo apt-get install backintime-qt4

#####Debian/Ubuntu make packages

    ./makedeb.sh
    sudo dpkg -i ../backintime-common-<version>.deb
    sudo dpkg -i ../backintime-qt4-<version>.deb

#####ArchLinux

Back In Time is available through AUR. You need to import a public key once
before installing

    gpg --keyserver pgp.mit.edu --recv-keys 615F366D944B4826
    wget https://aur.archlinux.org/cgit/aur.git/snapshot/backintime.tar.gz
    tar xvzf backintime.tar.gz
    cd backintime
    makepkg -srci

###From sources

#####Common

* dependencies
    - python3 (>= 3.3)
    - rsync
    - cron-daemon
    - openssh-client
    - python3-keyring
    - python3-dbus

* recomended
    - sshfs
    - encfs

* Command

        cd common
        ./configure
        make
        make test
        sudo make install


#####Qt4 GUI

* dependencies
    - x11-utils
    - python3-pyqt4
    - libnotify-bin
    - policykit-1
    - python3-dbus.mainloop.qt
    - backintime-common

* recomended
    - python3-secretstorage or
    - python3-keyring-kwallet or
    - python3-gnomekeyring
    - kompare or
    - meld

* Command

        cd qt4
        ./configure
        make
        sudo make install


##configure options

    first value is default:
    --fuse-group | --no-fuse-group (only COMMON)
        Some distributions require user to be in group 'fuse' to use
        sshfs and encfs. This toggles the check on or off.

    --python3 | --python (all)
        Use either 'python3' or 'python' to start Python Version 3.x

##NewsFeed

Back In Time has a RSS feed
http://feeds.launchpad.net/backintime/announcements.atom

##Contribute

There is a dev-docu on http://backintime.rtfd.org/
It's not complete yet but I'm working on it. If you'd like to contribute
please add docstrings following the
[Google style guide](http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html)
and add unittests for new methods in common. To run unittest locally you can
run `cd common && ./configure && make unittest`

<sub>Jan 2016</sub>
