# walaa abo elhassan
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    payment_method = fields.Selection([
        ('cash', 'Cash'),
        ('credit', 'Credit'),
    ], string='Payment Method', default='cash')

    @api.onchange('amount_total')
    def _onchange_amount_total(self):
        if self.amount_total <= 5000:
            self.payment_method = 'cash'
        else:
            self.payment_method = 'credit'


# طريقة السداد كاش او اجل
# amount_total  هو اسم الحقل الذي يحتوي علي اجالي الفاتورة