========
Math rST
========

This is an equation:

.. math::
   :label: dummyeq

   a^2 + b^2 = c^2 + \sum_i (i-i)

Equations can be numbered and also referenced using the ``:label:`` option.

.. math::
   :label: euler
   
   e^{i\pi} + 1 = 0

Cross-referencing equations using ``:eq:<label>`` (like this :eq:`euler` or :eq:`dummyeq`) only works within the same document.


