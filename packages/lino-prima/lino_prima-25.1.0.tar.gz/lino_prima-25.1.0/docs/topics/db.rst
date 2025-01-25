.. doctest docs/topics/db.rst
.. _prima.topics.db:

================================
Database structure of Lino Prima
================================

This document describes the database structure.

.. contents::
  :local:

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_prima.projects.prima1.settings')
>>> from lino.api.doctest import *


>>> prima.Groups.simple_parameters
('year',)


>>> from lino.utils.diag import analyzer
>>> analyzer.show_db_overview()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
25 plugins: lino, bulma, printing, system, users, periods, prima, ratings, projects, cert, uploads, contenttypes, gfks, office, linod, checkdata, summaries, jinja, weasyprint, export_excel, help, about, react, staticfiles, sessions.
36 models:
========================== =========================== ========= =======
 Name                       Default table               #fields   #rows
-------------------------- --------------------------- --------- -------
 cert.CertElement           cert.CertElements           5         52
 cert.CertRating            cert.CertRatings            6         5616
 cert.CertSection           cert.CertSections           7         16
 cert.CertTemplate          cert.CertTemplates          3         2
 cert.Certificate           cert.Certificates           8         216
 cert.SectionResponse       cert.SectionResponses       10        1728
 checkdata.Message          checkdata.Messages          6         0
 contenttypes.ContentType   gfks.ContentTypes           3         36
 linod.SystemTask           linod.SystemTasks           24        2
 periods.StoredPeriod       periods.StoredPeriods       7         1
 periods.StoredYear         periods.StoredYears         5         6
 prima.Cast                 prima.Casts                 4         36
 prima.Course               prima.Courses               3         78
 prima.Enrolment            prima.Enrolments            3         216
 prima.Grade                prima.Grades                5         7
 prima.Group                prima.Groups                5         12
 prima.Role                 prima.Roles                 3         6
 prima.Skill                prima.Skills                6         26
 prima.Subject              prima.Subjects              8         8
 projects.Project           projects.Projects           14        0
 projects.ProjectSection    projects.ProjectSections    5         4
 projects.ProjectTemplate   projects.ProjectTemplates   7         5
 ratings.Challenge          ratings.Challenges          6         60
 ratings.ChallengeRating    ratings.ChallengeRatings    9         1620
 ratings.Exam               ratings.Exams               8         30
 ratings.ExamResponse       ratings.ExamResponses       4         540
 ratings.FinalExam          ratings.FinalExams          4         0
 ratings.FinalExamRating    ratings.FinalExamRatings    9         0
 ratings.RatingsSummary     ratings.RatingsSummaries    7         0
 sessions.Session           users.Sessions              3         ...
 system.SiteConfig          system.SiteConfigs          3         1
 uploads.Upload             uploads.Uploads             12        5
 uploads.UploadType         uploads.UploadTypes         7         0
 uploads.Volume             uploads.Volumes             4         1
 users.Authority            users.Authorities           3         0
 users.User                 users.AllUsers              21        104
========================== =========================== ========= =======
<BLANKLINE>
