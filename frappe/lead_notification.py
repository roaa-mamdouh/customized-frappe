import frappe

def send_notification(doc, method):
    """
    Sends a notification to the specified recipient when the 'duplicated' label of a CRM Lead is changed to 'true'.
    """
    if doc.doctype == "CRM Lead" and doc.duplicated and doc.has_value_changed('duplicated'):
        # Get all users with the role "CRM Team Leader"
        recipients = frappe.get_all('Has Role', filters={'role': 'CRM Team Leader'}, fields=['parent'])
        
        subject = "Duplicate Lead Detected"
        message = f"Lead {doc.name} has been marked as duplicate."

        for recipient in recipients:
            notification_doc = frappe.get_doc({
                "doctype": "Notification Log",
                "for_user": recipient['parent'],
                "subject": subject,
                "email_content": message,
                "type": "Alert"
            })

            notification_doc.insert(ignore_permissions=True)
            frappe.msgprint(f"Notification sent to {recipient['parent']}.")

        frappe.db.commit()
