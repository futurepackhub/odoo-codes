# walaa abo elhassan
from odoo import models, fields, api

class AccountOpeningForm(models.Model):
    _name = 'account.opening.form'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    phone_number = fields.Char(string='Phone Number', required=True)
    country_id = fields.Many2one('res.country', string='Country')
    company_name = fields.Char(string='Company Name')
    company_type = fields.Selection([
        ('individual', 'Individual'),
        ('company', 'Company'),
    ], string='Company Type')

    @api.model
    def create(self, vals):
        res = super(AccountOpeningForm, self).create(vals)

        # إنشاء حساب جديد
        account = self.env['res.partner'].create({
            'name': vals['name'],
            'email': vals['email'],
            'phone': vals['phone_number'],
            'country_id': vals['country_id'],
            'company_type': vals['company_type'],
            'company_name': vals['company_name'],
        })

        # إرسال بريد إلكتروني تأكيدي
        self.env['mail.template'].send_mail(
            self.env.ref('account_opening_form.email_template_account_opening'),
            res.id,
            force_send=True,
        )

        return res
