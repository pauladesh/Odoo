# -*- coding: utf-8 -*-

from odoo import models, fields


class LibrarySchool(models.Model):
    _name = 'lib.student'

    name = fields.Char(string='Book Name', required=True)
