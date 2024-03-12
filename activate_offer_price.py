from odoo import models, fields, api

# تفعيل عرض السعر
def activate_offer_price(self, sale_order_id):
  """
تفعيل عرض السعر لامر البيع
  """
  sale_order = self.env['sale.order'].browse(sale_order_id)
  sale_order.write({
      'pricelist_id': False,  # Remove default pricelist
  })

def activate_offer_price_for_product(self, product_tmpl_id):
      """
تفعيل عرض السعر لمنتج معين
      """
      product_template = self.env['product.template'].browse(product_tmpl_id)
      product_template.write({
          'sale_ok': True,  # Ensure product is saleable
          'can_be_sold': True,  # Ensure product can be sold
          'offer_price': True
          # Activate Offer Price (adjust character based on your Odoo language)
      })