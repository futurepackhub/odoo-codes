from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    company_name = fields.Char(string="اسم الشركة", required=True)
    purchase_manager_name = fields.Char(string="اسم مدير المشتريات", required=True)
    contact_number = fields.Char(string="رقم التواصل", required=True)
    commercial_register = fields.Char(string="السجل التجاري", required=True)
    tax_number = fields.Char(string="الرقم الضريبي", required=True)
    national_address = fields.Char(string="العنوان الوطني", required=True)
    email = fields.Char(string="البريد الإلكتروني", required=True)
    otp = fields.Char(string="كود التحقق", required=True)

    @api.model
    def create(self, vals):
        # لتتحقق من otp
        if vals['otp'] != '123456':
            raise ValidationError("كود التحقق غير صحيح")

        # انشاء العميل الجديد
        new_partner = super(ResPartner, self).create(vals)

        # ممكن نبعت ميل ترحيبي
        self.env['mail.template'].send_mail(
            template_id=self.env.ref('odoo_custom.email_template_new_customer').id,
            model='res.partner',
            res_id=new_partner.id,
        )

        return new_partner













