# -*- coding: UTF-8 -*-
# Copyright 2024 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)

import locale
import traceback
from decimal import Decimal
from django.db import models
from django.conf import settings
from django.utils.html import format_html, mark_safe, escape
from django.utils.text import format_lazy
from django.core.exceptions import ValidationError
from lino.utils.html import E, tostring, join_elems
from lino.utils.mldbc.mixins import BabelDesignated
from lino.modlib.users.mixins import UserAuthored, My
from lino.modlib.printing.mixins import CachedPrintable
from lino.modlib.system.choicelists import DisplayColors
from lino.mixins import Referrable, Sequenced, Created
from lino.api import dd, rt, _

from lino_prima.lib.prima.roles import PrimaStaff, PrimaTeacher
from lino_prima.lib.ratings.mixins import MaxScoreField, RatingSummary, Ratable, ScoreValue
from lino_prima.lib.ratings.mixins import RatingCollector
from lino_prima.lib.ratings.choicelists import Predicates, RatingTypes
from .mixins import CertificateStates



class CertTemplate(BabelDesignated):  # zeugnisse.ZeugnisVorlage
    class Meta:
        verbose_name = _("Certificate template")
        verbose_name_plural = _("Certificate templates")
        abstract = dd.is_abstract_model(__name__, 'CertTemplate')


class CertSection(Sequenced):  # zeugnisse.ZeugnisAbschnitt
    class Meta:
        verbose_name = _("Certificate section template")
        verbose_name_plural = _("Certificate section templates")
        abstract = dd.is_abstract_model(__name__, 'CertificateSection')

    cert_template = dd.ForeignKey('cert.CertTemplate')
    subject = dd.ForeignKey('prima.Subject')
    # advanced = dd.BooleanField(_("Advanced"), default=False)  # Komplexes Benotungsschema
    remark = dd.RichTextField(_("Remark"), blank=True, format="plain")
    max_score = MaxScoreField()
    rating_type = RatingTypes.field(blank=True, null=True)

    def get_siblings(self):
        return self.__class__.objects.filter(cert_template=self.cert_template)

    # def full_clean(self):
    #     if not self.rating_type:
    #         self.rating_type = self.subject.rating_type()
    #     super().full_clean()

    def __str__(self):
        return f"{self.seqno}) {self.subject}"
        # return f"{self.seqno}) {self.subject} in {self.cert_template}"
        # return f"{self.subject} in {self.cert_template}"
        # return f"{self.subject}"

    def as_paragraph(self, ar, **kwargs):
        s = ar.obj2htmls(self)
        if not ar.is_obvious_field("cert_template"):
            s += format_html(_(" (in {cert_template})"), cert_template=ar.obj2htmls(self.cert_template))
        # s += "<br/>x" + tostring(self.get_workflow_buttons(ar))
        qs = rt.models.cert.CertElement.objects.filter(cert_section=self)
        s += " ({})".format(", ".join(
            [e.as_summary_item(ar) for e in qs.order_by('seqno')]))
        return mark_safe(s)

    # def get_section_rating(self, cert):
    #     return SectionRating(self, cert)


class CertElement(Sequenced):  # zeugnisse.ZeugnisElement
    class Meta:
        verbose_name = _("Certificate element template")
        verbose_name_plural = _("Certificate element templates")
        abstract = dd.is_abstract_model(__name__, 'CertElement')
        unique_together = ('cert_section', 'skill')

    cert_section = dd.ForeignKey('cert.CertSection', blank=True, null=True)
    skill = dd.ForeignKey('prima.Skill', blank=True, null=True)
    max_score = MaxScoreField()

    def get_siblings(self):
        return self.__class__.objects.filter(cert_section=self.cert_section)

    def __str__(self):
        return f"{self.seqno}) {self.skill} in {self.cert_section}"


class Certificate(CachedPrintable):   # zeugnisse.Zeugnis
    class Meta:
        verbose_name = _("Certificate")
        verbose_name_plural = _("Certificates")
        abstract = dd.is_abstract_model(__name__, 'Certificate')
        unique_together = ['enrolment', 'period']

    period = dd.ForeignKey('periods.StoredPeriod')
    enrolment = dd.ForeignKey('prima.Enrolment', verbose_name=_("Pupil"))
    state = CertificateStates.field(default="default")
    social_skills_comment = dd.TextField(_("Social skills comment"), blank=True)
    final_verdict = dd.TextField(_("Final verdict"), blank=True)

    # print_certificate = PrintCertificate(show_in_toolbar=False)
    # print_certificate_html = PrintCertificate(
    #     show_in_toolbar=False,
    #     build_method='weasy2html',
    #     label=format_lazy("{}{}", _("Certificate"), _(" (HTML)")))

    def __str__(self):
        return f"{self.enrolment} {self.period.nickname}"

    def get_str_words(self, ar):
        # yield str(self._meta.verbose_name)
        if not ar.is_obvious_field("enrolment"):
            yield str(self.enrolment)
        if not ar.is_obvious_field("period"):
            yield self.period.nickname

    def filename_root(self):
        return f"{self._meta.verbose_name}-{self.enrolment.pupil}-{self.period.nickname}-{self.pk}"

    def get_printable_context(self, ar=None, **kwargs):
        kwargs.update(use_bulma_css=True)
        return super().get_printable_context(ar, **kwargs)

    # @dd.displayfield(_("Print"))
    # def print_actions(self, ar):
    #     if ar is None:
    #         return ''
    #     elems = []
    #     elems.append(ar.instance_action_button(self.print_certificate))
    #     elems.append(ar.instance_action_button(self.print_presence_sheet_html))
    #     return E.p(*join_elems(elems, sep=", "))

    # def get_printable_context(self, bm, elem, ar):
    #     ctx = super().get_printable_context(bm, elem, ar)
    #     p = rt.models.periods.StoredPeriod.get_for_date(dd.today())
    #     certificate, created = rt.models.prima.Certificate.get_or_create(
    #         enrolment=self, period=p)
    #     ctx.update(certificate=certificate)


# dd.update_field(Certificate, "user", verbose_name=_("Teacher"))


class SectionResponse(Ratable, RatingSummary):
    # imported from ZeugnisFachKommentar and ZeugnisPrädikatNote
    class Meta:
        verbose_name = _("Certificate section")
        verbose_name_plural = _("Certificate sections")
        abstract = dd.is_abstract_model(__name__, 'SectionResponse')
        app_label = "cert"
        ordering = ["certificate", "section__seqno"]
        # unique_together = ['enrolment', 'period', 'subject']

    certificate = dd.ForeignKey('cert.Certificate', editable=False)
    section = dd.ForeignKey('cert.CertSection', editable=False)
    # enrolment = dd.ForeignKey('prima.Enrolment', verbose_name=_("Pupil"), editable=False)
    # period = dd.ForeignKey('periods.StoredPeriod')
    remark = dd.RichTextField(_("Remark"), blank=True, format="plain")

    def __str__(self):
        return f"{self.section}"

    _numbers = None

    @property
    def numbers(self):
        if self._numbers is None:
            try:
                self._numbers = SectionNumbers(self)
            except Exception as e:
                traceback.print_exc(e)
        return self._numbers

    def get_max_score(self):
        return self.section.max_score

    def get_rating_type(self):
        return self.section.subject.rating_type

    def get_scores_to_summarize(self):
        for r in self.get_challenge_ratings():
            yield (r.score, r.challenge.max_score)
        for r in self.get_final_ratings():
            yield (r.score, r.exam.max_score)
        # for r in self.get_project_ratings():
        #     yield (r.score, r.project_skill.max_score)
        # what about GeneralRatings?

    def get_challenge_ratings(self):
        return rt.models.ratings.ChallengeRating.objects.filter(
            enrolment=self.certificate.enrolment,
            period=self.certificate.period,
            challenge__skill__subject=self.section.subject)

    def get_final_ratings(self):
        if self.get_rating_type() is not None:
            return []
        return rt.models.ratings.FinalExamRating.objects.filter(
            enrolment=self.certificate.enrolment,
            period=self.certificate.period,
            exam__skill__subject=self.section.subject)


# class CertRating(RatingSummary, Ratable):  # zeugnisse.ZeugnisKompetenzNote + zeugnisse.ZeugnisSozialNote

class CertRating(Ratable):  # zeugnisse.ZeugnisKompetenzNote + zeugnisse.ZeugnisSozialNote

    # todo: renamce CertRating to ElementResponse (and its field 'response' to
    # 'section' and 'cert_element' to 'element')

    class Meta:
        verbose_name = _("Certificate element")
        verbose_name_plural = _("Certificate elements")
        abstract = dd.is_abstract_model(__name__, 'CertRating')

    response = dd.ForeignKey('cert.SectionResponse', editable=False, related_name="elements")
    cert_element = dd.ForeignKey('cert.CertElement', editable=False)

    quick_search_fields = 'response__certificate__enrolment__pupil__first_name response__certificate__enrolment__pupil__last_name'

    _numbers = None

    def get_skill(self):
        return self.cert_element.skill

    def get_max_score(self):
        return self.cert_element.max_score

    def get_rating_type(self):
        return self.cert_element.skill.subject.rating_type

    def __str__(self):
        # return f"{self.ratings_done} {self.total_score} / override {self.score}"
        ce = self.cert_element
        # return f"{self.score} / {ce.max_score} in {ce.skill} for {response.certificate.enrolment}"
        return f"Override {self.score} in {ce} for {self.response.certificate.enrolment}"

    def unused_as_paragraph(self, ar, **kwargs):
        if ar.is_obvious_field('certificate'):
            text = str(self.cert_element.skill)
            # text += " (total " + str(self.total_score)
            # text += "%, " + str(self.ratings_done) + "% done)"
            # text += ": " + ar.obj2htmls(self, str(self.score or NOT_RATED))
            text += ": " + ar.obj2htmls(self)
            return mark_safe(text)
        return ar.obj2htmls(self)

    # useful for debugging exceptions during numbers property:
    # def get_numbers(self):
    #     return self.numbers

    @property
    def numbers(self):
        if self._numbers is None:
            self._numbers = ElementNumbers(self)
        return self._numbers

    @dd.displayfield(_("Computed rating"), max_length=3)
    def computed_rating(self, ar=None):
        # max_score = self.get_max_score()
        # score = self.numbers.total.score * 100 / self.numbers.total.max_score
        # reduced = ScoreValue(self.numbers.total * 100 / max_score)
        rebased = self.numbers.total.rebase(self.get_max_score())
        # self.max_score
        return f"{self.numbers.total} = {rebased}"

    @dd.htmlbox(_("Ratings detail"))
    def ratings_report(self, ar):
        s = ""
        if ar is not None:
            lst = [ar.obj2htmls(r) for r in self.get_challenge_ratings()]
            if len(lst):
                s += "<p>"
                s += escape(rt.models.ratings.ChallengeRating._meta.verbose_name_plural) + ": "
                s += " + ".join(lst)
                s += " = " + str(self.numbers.period)
                s += "</p>"
            lst = [ar.obj2htmls(r) for r in self.get_final_ratings()]
            if len(lst):
                s += "<p>"
                s += escape(rt.models.ratings.FinalExamRating._meta.verbose_name_plural) + ": "
                s += " + ".join(lst)
                s += " = " + str(self.numbers.final)
                s += "</p>"
        return mark_safe(s)

    def get_challenge_ratings(self):
        return rt.models.ratings.ChallengeRating.objects.filter(
            enrolment=self.response.certificate.enrolment,
            period=self.response.certificate.period,
            challenge__skill=self.cert_element.skill)

    def get_final_ratings(self):
        return rt.models.ratings.FinalExamRating.objects.filter(
            enrolment=self.response.certificate.enrolment,
            period=self.response.certificate.period,
            exam__skill=self.cert_element.skill)

    def disabled_fields(self, ar):
        df = super().disabled_fields(ar)
        df.add("response__certificate__enrolment")
        df.add("response__certificate__period")
        df.add("cert_element__skill")
        df.add("cert_element__max_score")
        return df

dd.update_field(CertRating, "rating_buttons", verbose_name=_("Override score"))


from lino.modlib.checkdata.choicelists import Checker

class CertificateChecker(Checker):
    verbose_name = _("Check for missing or duplicate certificate ratings")
    model = Certificate
    msg_missing = _("No certificate rating for {} elements.")
    msg_duplicate = _("Duplicate certificate rating(s) for {} elements.")

    def get_checkdata_problems(self, obj, fix=False):
        CertElement = rt.models.cert.CertElement
        CertRating = rt.models.cert.CertRating
        SectionResponse = rt.models.cert.SectionResponse
        missing = []
        duplicate = 0
        tpl = obj.enrolment.group.grade.cert_template
        for ce in CertElement.objects.filter(cert_section__cert_template=tpl):
            qs = CertRating.objects.filter(response__certificate=obj, cert_element=ce)
            if qs.count() == 0:
                missing.append(ce)
                # missing.append(CertRating(response=resp, cert_element=ce))
            elif qs.count() > 1:
                duplicate += 1
        if duplicate > 0:
            yield (False, format_lazy(self.msg_duplicate, duplicate))
        if len(missing) > 0:
            yield (True, format_lazy(self.msg_missing, len(missing)))
            if fix:
                for ce in missing:
                    qs = SectionResponse.objects.filter(
                        certificate=obj, section=ce.cert_section)
                    n = qs.count()
                    if n == 0:
                        resp = SectionResponse(certificate=obj, section=ce.cert_section)
                        resp.full_clean()
                        resp.save()
                    elif n == 1:
                        resp = qs.first()
                    else:
                        print(f"20241128 Oops there are multiple SectionResponse for {obj} {ce.cert_section}")
                        # raise Exception("")
                    row = CertRating(response=resp, cert_element=ce)
                    row.full_clean()
                    row.save()

CertificateChecker.activate()


# class SectionRating:
#     # volatile object used for printing certificates
#     def __init__(self, cs: CertSection, cert):
#         raise Exception("Must replace this by SectionResponse")
#         self.total = RatingCollector()
#
#         for r in rt.models.ratings.ChallengeRating.objects.filter(
#             enrolment=cert.enrolment, period=cert.period,
#             challenge__skill__subject=cs.subject,
#             score__isnull=False):
#             self.total.collect(r.score, r.challenge.max_score)
#
#         skills = CertElement.objects.filter(cert_section=cs).values_list('skill', flat=True)
#         # skills = rt.models.prima.Skill.objects.filter(subject__in=subjects)
#         for r in rt.models.ratings.FinalExamRating.objects.filter(
#             enrolment=cert.enrolment, period=cert.period,
#             exam__skill__in=skills, score__isnull=False):
#             self.total.collect(r.score, r.exam.max_score)
#
#         for r in rt.models.cert.CertRating.objects.filter(
#             cert_element__cert_section=cs,
#             certificate=cert, score__isnull=False):
#             self.total.collect(r.score, r.challenge.max_score)

class SectionNumbers:

    def __init__(self, sr: SectionResponse):
        cert = sr.certificate
        self.average = ScoreValue()
        year = cert.period.year
        self.by_period = [ScoreValue() for p in year.periods.all() ]
        self.elements = []

        for er in sr.elements.all():
            self.elements.append(er)
            for i, value in enumerate(er.numbers.by_period):
                self.by_period[i] += value
                self.average += value


class ElementNumbers:
    # Volatile object used when printing the certificate
    # Attributes:
    # period: challenge ratings during the period of this certificate
    # final: final exam ratings for this certificate

    def __init__(self, ce: CertRating):
        cert = ce.response.certificate
        skill = ce.cert_element.skill
        ms = ce.get_max_score()

        year = cert.period.year
        self.ccoll = {p.id: RatingCollector() for p in year.periods.all()}
        self.fcoll = {p.id: RatingCollector() for p in year.periods.all()}

        for r in rt.models.ratings.ChallengeRating.objects.filter(
            enrolment=cert.enrolment,
            challenge__skill=skill, score__isnull=False):
                c = self.ccoll[r.period_id]
                c.collect(r.score, r.challenge.max_score)

        for r in rt.models.ratings.FinalExamRating.objects.filter(
            enrolment=cert.enrolment,
            exam__skill=skill, score__isnull=False):
                c = self.fcoll[r.period_id]
                c.collect(r.score, r.exam.max_score)

        # for r in rt.models.cert.CertRating.objects.filter(
        #     response__certificate=cert, element=ce, score__isnull=False):
        #     self.final.collect(r.score, r.challenge.max_score)

        self.by_period = []
        self.average = ScoreValue()
        for p in year.periods.all():
            i = self.ccoll[p.id].value.rebase(ms) + self.fcoll[p.id].value.rebase(ms)
            i = i.rebase(ms)
            self.by_period.append(i)
            self.average += i

        self.average = self.average.rebase(ms)

        self.period = self.ccoll[cert.period.id].value
        self.final = self.fcoll[cert.period.id].value

        self.total = self.period.rebase(ms) + self.final.rebase(ms)
        self.total = self.total.rebase(ms)



from .ui import *
