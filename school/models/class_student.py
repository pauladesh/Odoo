# -*- coding: utf-8 -*-

from odoo import models, fields


class ClassStudent(models.Model):
    _name = 'class.student'

    name = fields.Char(string='Class', required=True)
    priority_one = fields.Boolean(string="First Priority")
    priority_two = fields.Boolean(string="Second Priority")