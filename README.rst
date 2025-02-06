Plone-Entwicklerhandbuch
========================

.. badges::

Status
------

.. image:: https://img.shields.io/github/contributors/veit/plone-entwicklerhandbuch.svg
   :alt: Contributors
   :target: https://github.com/veit/plone-entwicklerhandbuch/graphs/contributors
.. image:: https://img.shields.io/github/license/veit/plone-entwicklerhandbuch.svg
   :alt: License
   :target: https://github.com/veit/plone-entwicklerhandbuch/blob/master/LICENSE

.. first-steps::

Installation
------------

#. Download and unpack:

   .. code-block:: console

    $ curl -O https://codeload.github.com/veit/plone-entwicklerhandbuch/zip/main
    $ unzip main
    Archive:  main
    …
       creating: plone-entwicklerhandbuch-main/
    …

#. Install uv

   Refer to `uv Installation
   <https://python-basics-tutorial.readthedocs.io/en/latest/libs/install.html#installation>`_

#. Install Python packages:

   .. code-block:: console

    $ cd plone-entwicklerhandbuch-main
    $ uv sync

#. Create HTML documentation:

   Note that pandoc has to be installed. On Debian/Ubuntu you can just run

   .. code-block:: console

    $  sudo apt-get install pandoc

    To create the HTML documentation run these commands:

   .. code-block:: console

    $ uv run python -m sphinx -b html docs/ docs/_build/

#. Create a PDF:

   For the creation of a PDF file you need additional packages.

   For Debian/Ubuntu you get them with the following command:

   .. code-block:: console

    $ sudo apt-get install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended latexmk

   or for macOS with:

   .. code-block:: console

    $ brew cask install mactex
    …
    🍺  mactex was successfully installed!
    $ curl --remote-name https://www.tug.org/fonts/getnonfreefonts/install-getnonfreefonts
    $ sudo texlua install-getnonfreefonts
    …
    mktexlsr: Updating /usr/local/texlive/2020/texmf-dist/ls-R...
    mktexlsr: Done.

   Then you can generate a PDF with:

   .. code-block:: console

    $ cd docs/
    $ uv run make latexpdf
    …
    The LaTeX files are in _build/latex.
    Run 'make' in that directory to run these through (pdf)latex
    …

   You can find the PDF at ``docs/_build/latex/plone-entwicklerhandbuch.pdf``.
