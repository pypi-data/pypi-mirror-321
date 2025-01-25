# -*- coding: UTF-8 -*-
# Copyright 2016-2024 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)
"""
The main plugin for Lino Prima.

.. autosummary::
   :toctree:

    migrate
    user_types

"""


from lino.ad import Plugin, _


class Plugin(Plugin):

    verbose_name = _("School")
    menu_group = "prima"
    needs_plugins = ['lino.modlib.periods']

    def setup_main_menu(self, site, user_type, m, ar=None):
        mg = self.get_menu_group()
        # mg = site.plugins.office
        m = m.add_menu(mg.app_label, mg.verbose_name)
        m.add_action('prima.MyGroups')
        m.add_action('prima.MyCasts')

    def setup_config_menu(self, site, user_type, m, ar=None):
        mg = self.get_menu_group()
        m = m.add_menu(mg.app_label, mg.verbose_name)
        m.add_action('prima.Groups')
        m.add_action('prima.Subjects')
        m.add_action('prima.Roles')
        m.add_action('prima.Grades')

    def setup_explorer_menu(self, site, user_type, m, ar=None):
        mg = self.get_menu_group()
        m = m.add_menu(mg.app_label, mg.verbose_name)
        m.add_action('prima.Skills')
        # m.add_action('prima.Exams')
        # m.add_action('prima.ProjectSkills')
        # m.add_action('prima.ProjectTemplates')
        # m.add_action('prima.ProjectSections')
        m.add_action('prima.Enrolments')
        m.add_action('prima.Casts')
        m.add_action('prima.Courses')
        # m.add_action('prima.AllChallenges')
        # m.add_action('prima.AllChallengeRatings')
        # m.add_action('prima.AllProjectRatings')

    # def setup_quicklinks(self, tb):
    #     tb.add_action("prima.MyCasts")
    #     tb.add_action("prima.MyGroups")

    def get_dashboard_items(self, user):
        # yield self.site.models.prima.MyCasts
        yield self.site.models.prima.MyGroups
