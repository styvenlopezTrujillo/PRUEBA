
from odoo import models, fields, api


class SchoolSubject(models.Model):
    _name = 'school.subject'
    _description = 'CURSO'

    name = fields.Char(string="Nombre")
    credits = fields.Integer(string="creditos")
    max_students = fields.Integer(string="maximo de estudiantes")
    active = fields.Boolean(string="activo")

    student_ids = fields.Many2many(comodel_name="school.student",string="Estudiantes")
    teacher_id = fields.Many2one(comodel_name ="school.teacher", string="Profesor")
