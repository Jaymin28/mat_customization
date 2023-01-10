import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def create_custom_fields():
    custom_fields = {
        "Item": [
            dict(fieldname='booking_item',
                 label='Booking Item',
                 fieldtype='Check',
                 insert_after='disabled',
                 print_hide=1),
            dict(fieldname='service_item',
                 label='Service Item',
                 fieldtype='Link',
                 insert_after='booking_item',
                 options='Item',
                 depends_on='eval:doc.booking_item',
                 read_only=0, print_hide=1),
            dict(fieldname='is_service_item',
                 label='Is Service Item',
                 fieldtype='Check',
                 insert_after='service_item',
                 options='Item',
                 depends_on='eval:!doc.booking_item',
                 read_only=0, print_hide=1)
        ]
    }

    create_custom_fields(custom_fields)
    frappe.msgprint("Custom Field Updated!")