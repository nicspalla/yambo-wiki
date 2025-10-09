==============================
``sphinx-design`` elements rST
==============================

These are enabled by the ``sphinx_design`` extension. Find `here <https://sphinx-design.readthedocs.io/en/latest/index.html>`__ the complete documentation.

``card``
--------

See `cards page <https://sphinx-design.readthedocs.io/en/latest/cards.html#cards>`__ on sphinx design.

Here's an example of clickable card with an external link:

.. card:: Title
   :link: https://wiki.yambo-code.eu/wiki/index.php/Main_Page

   Header
   ^^^
   Content
   +++
   Footer

Internal links require ``:link-type: ref``

.. card::
   :link: ref-sphinx-design-dropdown
   :link-type: ref

   Click to navigate to the ``dropdown`` section below.

Cards can also contain images:

.. card::
   :width: 25%
   :img-background: ./example_files/example_card.png
   :img-alt: https://www.yambo-code.eu
   :link: https://www.yambo-code.eu
   :text-align: center

.. _ref-sphinx-design-dropdown:

``dropdown``
------------

.. dropdown:: Click to open

   Hello!

.. dropdown::
   :open:

   The ``:open:`` option renders the dropdown already open.

.. dropdown:: open for a tip
   :animate: fade-in-slide-down

   .. tip::
   
      Dropdowns can also contain admonitions!
  
   ..

..

.. _ref-sphinx-design-tab:

``tab``
-------

They look like this:

.. tab-set::

    .. tab-item:: Label1

        Content 1

    .. tab-item:: Label2

        Content 2

See `here <https://sphinx-design.readthedocs.io/en/latest/tabs.html>`__ for all available options.
