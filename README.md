# notify-log


<details>
<summary>installation and usage</summary>

1. get latest [release](https://github.com/digitalduke/notify-log/releases)
1. install && run
```shell
$ sudo dpkg -i notify-log_<version-number>.deb
$ notify-log
```
If everything is ok you will see greetings message, like this `notify-log started...`

</details>

<details>
<summary>build from scratch</summary>


Install dependent packages for build 

dbus-python:
```shell
$ sudo apt install pkg-config libdbus-1-dev libglib2.0-dev
```

PyGObject:
```shell
$ sudo apt install libcairo2-dev libgirepository1.0-dev
```

Build & upload python package (in an activated environment):
```shell
$ python setup.py sdist
$ python -m twine upload
```
Build .deb-package:
```shell
$ dpkg-buildpackage -us -uc --build=binary --post-clean
```

</details>

<details>
<summary>tests and debug</summary>

Emit message for test:
```shell
$ sudo apt install ruby-notify
$ notify-send 'test'
```

View all notifications signals on the bus:
```
$ dbus-monitor "interface='org.freedesktop.Notifications'"
```

</details>

For any ideas, issues reporting, etc. feel free to ask me via [Telegram](http://t.me/digitalduke)
