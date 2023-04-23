from odoo import models, fields, api

class SchoolTeacher(models.Model):
    _name = 'school.teacher'
    _description = 'PROFESOR'

    name = fields.Char(string="Nombre")
    profile = fields.Text(string="Perfil")

    subject_ids = fields.One2many("school.subject", "teacher_id", string="Cursos")