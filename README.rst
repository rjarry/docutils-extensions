===================
Docutils Extensions
===================

A Docutils extension for allowing easy directive contribution. All contributions should go into the ``docutilsextensions`` package that will be copied in your Python installation.

Docutils Extensions, installs a single ``rst.py`` script in your Python installation directory. 
From this script, you can invoke any docutils script (such as ``rst2html``, ``rst2odt``, etc.)


Usage
-----

Here's the usage: ::

	rst <output_format> <original_docutils_scripts_options_and_arguments>

``output_format``
	Can be choosed amongst any built-in format delivered with docutils [html, latex, odt, xml, etc.] But you can also implement your own output formats. Docutils Extensions will try to invoke your scripts with the following rule ``"rst2%s.py" % output_format``.
``original_docutils_scripts_options_and_arguments``
	These will be passed to the invoked script




Required python libraries
-------------------------

* docutils: http://docutils.sourceforge.net/
