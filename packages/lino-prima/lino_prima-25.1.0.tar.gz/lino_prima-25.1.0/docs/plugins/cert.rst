.. doctest docs/plugins/cert.rst
.. _prima.plugins.cert:

======================================
``cert`` (Certificates)
======================================

.. currentmodule:: lino_prima.plugins.cert

.. contents::
  :local:

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_prima.projects.prima1.settings')
>>> from lino.api.doctest import *

Plain-text representation
=========================

The plain-text representation methods of the :class:`Certificate` model are
defined as follows::

    def __str__(self):
        return f"{self.enrolment} {self.period}"

    def get_str_words(self, ar):
        if not ar.is_obvious_field("enrolment"):
            yield str(self.enrolment)
        if not ar.is_obvious_field("period"):
            yield str(self.period)

The following snippets test whether they work as expected.

>>> obj = cert.Certificate.objects.get(id=73)
>>> print(obj)
Marceau Broucq (5A) 1

>>> print(repr(obj))
Certificate #73 ('Marceau Broucq (5A) 1')


>>> res = AttrDict(get_json_dict("robin", "cert/Certificates/73"))
>>> print(res['title'])  #doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
<a ...>Certificates</a> » Marceau Broucq (5A) 1

When the certificate is an :term:`obvious field`, Lino does not show it:

>>> mt = contenttypes.ContentType.objects.get_for_model(prima.Enrolment).id
>>> res = get_json_dict("robin", "cert/CertificatesByEnrolment/73", mk=73, mt=mt)
>>> print(res['title'])  #doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
<a ...>Certificates of Marceau Broucq (5A)</a> » 1

The :attr:`Certificate.enrolment` field in the detail view

>>> print(res['data']['enrolment'])
Marceau Broucq in 5A



API reference
===============

.. class:: Certificate

  .. attribute:: enrolment

    The pupil for whom this certificate has been issued.

    Note that this labelled "Pupil" but actually points to an :term:`enrolment`,
    not to a pupil.
