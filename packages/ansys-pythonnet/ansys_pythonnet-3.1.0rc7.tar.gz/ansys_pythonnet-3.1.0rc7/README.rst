Ansys fork of `pythonnet <https://github.com/pythonnet/pythonnet>`_.

We will try to keep this up-to-date with pythonnet and upstream changes that might benefit the pythonnet community

Changes relative to pythonnet:

* Revert of `#1240 <https://github.com/pythonnet/pythonnet/pull/1240>`_.
* Opt-into explicit interface wrapping, `#19 <https://github.com/ansys/ansys-pythonnet/pull/19>`_. This opts into the behavior that became the default in #1240 if ToPythonAs<T> is explicitly used
* Option to bind explicit interface implementations, `#23 <https://github.com/ansys/ansys-pythonnet/pull/23>`_. This provides a runtime option to expose C# explicit interface implementations to Python.
* Option to bind pep8 aliases `#24 <https://github.com/ansys/ansys-pythonnet/pull/24>`_.