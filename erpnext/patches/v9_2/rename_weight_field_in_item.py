import frappe
from frappe import _

from frappe.model.utils.rename_field import rename_field

def execute():
	frappe.reload_doc("stock", "doctype", "item")
	if frappe.db.has_column('Item', 'weight'):
		rename_field("Item", "weight", "weight_per_unit")
