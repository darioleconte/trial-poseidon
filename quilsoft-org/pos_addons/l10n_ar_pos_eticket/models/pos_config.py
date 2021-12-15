# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class pos_config(models.Model):
    # Heredamos la clase CONFIGURACIÓN DEL POS"
    _inherit = "pos.config"

    pos_auto_invoice = fields.Boolean(
        'POS auto invoice',
        help='POS auto to checked to invoice button',
        default=True
    )
    receipt_invoice_number = fields.Boolean(
        'Receipt show invoice number',
        default=True
    )
    receipt_customer_vat = fields.Boolean(
        'Receipt show customer VAT',
        default=True
    )
    partner_default = fields.Many2one(
      'res.partner',
      string='Partner default'
    )
    print_pdf_invoice = fields.Boolean(
      'Print PDF Invoice',
      default=True
    )
