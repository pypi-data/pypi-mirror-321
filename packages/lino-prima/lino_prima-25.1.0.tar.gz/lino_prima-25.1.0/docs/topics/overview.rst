.. doctest docs/topics/overview.rst
.. _prima.topics.overview:

========
Overview
========

This document should give an overview over Lino Prima.

.. contents::
  :local:

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_prima.projects.prima1.settings')
>>> from lino.api.doctest import *


>>> print(analyzer.show_complexity_factors())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- 25 plugins
- 36 models
- 6 user types
- 122 views
- 12 dialog actions
<BLANKLINE>



The prima1 project uses a demo date in **October 2024** for all its data, which
means that there is only one :term:`accounting period`: everything happens
during the **first semester** of academic year 2024/25, and this semester lasts
from **September 2024** to **February 2025**.

>>> dd.plugins.periods.year_name
'Academic year'
>>> dd.plugins.periods.period_name
'Period'

>>> print(dd.today())
2024-10-09

>>> rt.show(periods.StoredPeriods)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
=========== ============ ============ =============== ======= ========
 Reference   Start date   End date     Academic year   State   Remark
----------- ------------ ------------ --------------- ------- --------
 2024/25-1   01/09/2024   28/02/2025   2024/25         Open
=========== ============ ============ =============== ======= ========
<BLANKLINE>
