# -*- coding: utf-8 -*-

from openerp import fields, models, _


class MgmtSystemProbability(models.Model):

    """
    Define the Probability for management system.

    Allow you to manage scale of probability (or likelihood)
    used across different modules (health and safety, information security).
    """

    _name = "mgmtsystem.probability"
    _description = "Management System Probability"

    name = fields.Char("Name", required=True, translate=True)

    description = fields.Text("Description")

    value = fields.Integer("Value", required=True)

    category = fields.Selection((
        ("hazard", _("hazard")),
        ("security", _("security")),
    ), 'Category', required=True)
