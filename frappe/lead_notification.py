import frappe

def send_notification(doc, method):
    """
    Sends a notification to the specified recipient when the 'duplicated' label of a CRM Lead is changed to 'true'.
    """
    if doc.doctype == "CRM Lead" and doc.duplicated and doc.has_value_changed('duplicated'):
        recipient = "mamdouhroaa3@gmail.com"  # Replace with the actual user ID
        subject = "Duplicate Lead Detected"
        message = f"Lead {doc.name} has been marked as duplicate."

        notification_doc = frappe.get_doc({
            "doctype": "Notification Log",
            "for_user": recipient,
            "subject": subject,
            "email_content": message,
            "type": "Alert"
        })

        notification_doc.insert(ignore_permissions=True)
        frappe.db.commit()
        frappe.msgprint(f"Notification sent to {recipient}")
