# -*- coding: utf-8 -*-

from odoo import models, fields


class SubjectSubject(models.Model):
    _name = 'subject.subject'
    _rec_name = 'sub_name'

    sub_name = fields.Char(string='Subject Name', required=True)
    code = fields.Integer(string='Subject code')
    subject_list = fields.Selection(
        [('HND', 'Hindi'), ('ENG', 'English'), ('MAT', 'Mathematics'), ('SCI', 'Science'), ('SST', 'Social Studies'), ('GK', 'General Knowledge') ],
        string='Subject')