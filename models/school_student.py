from odoo import models, fields, api
class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "ESTUDIANTE"
    
    name = fields.Char(string="Nombre")
    birth_date = fields.Date(string="Fecha de cumpleaños")
    age = fields.Integer(string="Edad",compute="_compute_get_age",store=True)
    final_exam_grade = fields.Float(string = "Calificacion del examen final")

    subject_ids = fields.Many2many(comodel_name="school.subject",string="Cursos")



    @api.depends('birth_date')
    def _compute_get_age(self):
        for record in self:
            if record.birth_date:
                today = fields.Date.today()
                record.age = today.year - record.birth_date.year - ((today.month, today.day) < (record.birth_date.month, record.birth_date.day))