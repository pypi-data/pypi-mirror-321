# -*- coding: UTF-8 -*-
# Copyright 2024 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)

from django.db import models
from django.conf import settings
from django.utils.html import format_html, mark_safe
from etgen import html as xghtml
from lino.utils.html import E, join_elems, tostring, SAFE_EMPTY
from lino.core import constants
from lino.modlib.users.mixins import UserAuthored, My
from lino.modlib.system.choicelists import DisplayColors
from lino.mixins import Referrable, Sequenced, Created
from lino.api import dd, rt, _, gettext

from lino_prima.lib.prima.roles import PrimaStaff, PrimaTeacher, PrimaPupil

# NOT_RATED = '▨'
# NOT_RATED = '◻' # 25fb white medium square
# NOT_RATED = '□' # 25a1 white square
# NOT_RATED = '▭' # 25ad white rectagle
NOT_RATED = '☐' # 2610 ballot box


class CertificateDetail(dd.DetailLayout):
    main = "ratings verdict"

    ratings = dd.Panel("""
    enrolment period state id
    SectionResponsesByCertificate
    # RatingsByCertificate
    """, _("Ratings"))

    verdict = dd.Panel("""
    social_skills_comment
    final_verdict
    """, _("Verdict"))

class Certificates(dd.Table):
    required_roles = dd.login_required(PrimaStaff)
    model = 'cert.Certificate'
    column_names = "enrolment period state *"
    detail_layout = "cert.CertificateDetail"
    insert_layout = """
    enrolment
    period
    """

# class MyCertificates(Certificates, My):
#     required_roles = dd.login_required(PrimaTeacher)

class CertificatesByEnrolment(Certificates):
    required_roles = dd.login_required(PrimaTeacher)
    master_key = "enrolment"
    default_display_modes = { None: constants.DISPLAY_MODE_SUMMARY}
    # row_template = "{row.period.nickname}"


class CertTemplates(dd.Table):
    required_roles = dd.login_required(PrimaStaff)
    model = 'cert.CertTemplate'
    detail_layout = """
    designation
    cert.SectionsByTemplate
    """

class CertSections(dd.Table):
    required_roles = dd.login_required(PrimaStaff)
    model = 'cert.CertSection'
    column_names = "cert_template seqno subject remark *"
    detail_layout = """
    cert_template seqno subject id
    remark
    cert.ElementsBySection
    """

class SectionsByTemplate(CertSections):
    master_key = 'cert_template'
    column_names = "seqno subject remark *"


class CertElements(dd.Table):
    required_roles = dd.login_required(PrimaStaff)
    model = 'cert.CertElement'
    column_names = "cert_section seqno skill max_score *"
    # detail_layout = """
    # cert_section
    # seqno
    # skill max_score
    # id
    # """

class ElementsBySection(CertElements):
    master_key = 'cert_section'
    column_names = "seqno skill max_score *"


class CertRatings(dd.Table):
    required_roles = dd.login_required(PrimaStaff)
    model = 'cert.CertRating'

    detail_layout = """
    response response__certificate__enrolment response__certificate__period
    cert_element cert_element__skill max_score
    # ratings_done total_max_score total_score
    computed_rating score rating_buttons
    ratings_report
    """

class RatingsBySkill(CertRatings):
    # master = 'cert.Certificate'
    master_key = 'cert_element__skill'
    required_roles = dd.login_required(PrimaTeacher)
    column_names = "cert_element max_score score *"
    # order_by = ['cert_element__cert_section', 'cert_element']
    default_display_modes = { None: constants.DISPLAY_MODE_SUMMARY}
    row_template = "{row.response.certificate.enrolment}"

class RatingsByResponse(CertRatings):
    master_key = 'response'
    required_roles = dd.login_required(PrimaTeacher)
    column_names = "cert_element #total_score score max_score  *"
    default_display_modes = { None: constants.DISPLAY_MODE_LIST}
    obvious_fields = {'certificate', 'section'}

# class RatingsByCertificate(CertRatings):
#     # master = 'cert.Certificate'
#     master_key = 'response__certificate'
#     required_roles = dd.login_required(PrimaTeacher)
#     column_names = "cert_element total_score max_score score *"
#     order_by = ['cert_element__cert_section', 'cert_element']
#     group_by = [lambda obj: obj.cert_element.cert_section]
#     default_display_modes = { None: constants.DISPLAY_MODE_LIST}
#     # row_template = "{row.cert_element} {row.total_score} / {row.score or '☐'} ({row.ratings_done}% done)"
#
#     @classmethod
#     def before_group_change(cls, gh, obj):
#         return format_html("<h2>{}</h2>", obj.cert_element.cert_section)
#
#     @classmethod
#     def row_as_paragraph(cls, ar, self):
#         text = str(self.cert_element.skill) + " (" + _("computed") + " "
#         text += self.computed_text()
#         # text += " " + str(self.ratings_done) + "% done)"
#         text += "): "
#         # text += ar.obj2htmls(self, str(self.score or NOT_RATED))
#
#         elems = list(map(tostring, self.get_rating_buttons(ar)))
#         text += " | ".join(elems)
#         return mark_safe(text)

from lino.core.roles import Explorer

class SectionResponses(dd.Table):
    required_roles = dd.login_required(Explorer)
    model = "cert.SectionResponse"
    detail_layout = """
    certificate section rating_type max_score score smiley predicate
    remark
    cert.RatingsByResponse
    """

class SectionResponsesByCertificate(SectionResponses):
    required_roles = dd.login_required(PrimaTeacher)
    master_key = "certificate"
    column_names = "section total_score total_max_score rating_buttons remark *"
