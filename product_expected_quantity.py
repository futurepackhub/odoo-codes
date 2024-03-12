# walaa abo elhassan
from odoo import models, fields, api

class Product(models.Model):
    _inherit = 'product.product'

    @api.model
    def calculate_expected_quantity(self, start_date, end_date):
        """
        لحساب الكميات المتوقعة خلال فترة زمنية

        Args:
            start_date: تاريخ البداية
            end_date: تاريخ النهاية

        Returns:
            الكميات المتوقعة
        """

        # البحث في سجلات المبيعات
        sales_records = self.env['sale.order.line'].search([
            ('product_id', '=', self.id),
            ('order_date', '>=', start_date),
            ('order_date', '<=', end_date),
        ])

        # اجمالي المبيعات للمنتج
        total_quantity_sold = sum(sale_record.product_uom_qty for sale_record in sales_records)

        # عدد الايام خلال الفترة
        number_of_days = (end_date - start_date).days

        # معدل الاستهلاك
        daily_consumption_rate = total_quantity_sold / number_of_days

        # واخيرا الاستهلاك المتوقع
        expected_quantity = daily_consumption_rate * 30

        return expected_quantity