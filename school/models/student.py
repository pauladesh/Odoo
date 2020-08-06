# -*- coding: utf-8 -*-
from odoo import models, fields


class StudentStudent(models.Model):
    _name = 'student.student'

    t_name = fields.Char(string="Test")
    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    student_class_id = fields.Many2one('class.student', string='Class')
    section = fields.Char(string='Section')
    subject_ids = fields.Many2many('subject.subject', 'subject_student_rel',
                                   'subject_id', 'student_id', string='Subject')
    lib_ids = fields.Many2many('lib.student', 'lib_student_rel',
                               'lib_id', 'stud_id', string='Books Issued')
    photo = fields.Binary(string='Image')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender')
    student_dob = fields.Date(string="Date of Birth")
    student_blood_group = fields.Selection(
        [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
         ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
        string='Blood Group')
    nationality = fields.Many2one('res.country', string='Nationality')
    student_marks_lines_ids = fields.One2many('student.marks.line', 'student_id', string='Student Marks Lines')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('approved', 'Approved'),
    ], string='Status', index=True, readonly=True, default='draft')
    date_time = fields.Datetime("Open Date", readonly=True, default=fields.Datetime.now())

    def action_pending(self):
        for rec in self:
            rec.state = 'pending'
        print("self.lsakfhsdakhfsahdf shdfihasidhf", self)

    def action_approved(self):
        for rec in self:
            rec.state = 'approved'
        print("self.lsakfhsddkjsahghgi sdggsdhg", self)


class StudentMarksLine(models.Model):
    _name = 'student.marks.line'

    marks = fields.Integer(string='Marks')
    sub_id = fields.Many2one('subject.subject', string='Subject Marks')
    student_id = fields.Many2one('student.student', string='Student')
