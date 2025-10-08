===============
Admonitions rST
===============

These are coloured boxed useful to highlight information.

List of admonitions
===================

``admonition``
--------------

.. admonition:: Example

   This is an admonition block named example. You can choose the title.

``attention``
-------------

.. attention::

   This is an attention block.

``caution``
-----------

.. caution::

   This is a caution block.

``danger``
----------

.. danger::
   
   This is a danger block.

``error``
---------

.. error::

   This is an error block.

``hint``
--------

.. hint::

   This is a hint block.
   
``important``
-------------

.. important::

   This is an important block.

``note``
--------

.. note::

   This is a note block.

``seealso``
-----------

.. seealso::

   This is a seealso block.

``tip``
-------

.. tip::

   This is a tip block.

``todo``
--------

.. todo::

   This is a todo block. It needs the ``sphinx.ext.todo`` extension.

``todo`` blocks can be useful to track missing things. They can be swithced off in ``conf.py`` with

.. code-block:: python

   todo_include_todos = False

So if you don't see the ``todo`` above, this is why.

``warning``
-----------

.. warning::
   
   This is a warning block.

Collapsible option
==================

From version 8.2 of ``sphinx`` each admonition directive supports a ``:collapsible:`` option. See `here <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directives>`_.

.. note::
   :collapsible:

   Collapsible directives look a bit ugly tho (at least with Furo...)

