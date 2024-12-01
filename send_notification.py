def send_notification(user, subject, message):
  """
  Sends a system notification to a specific user.

  Args:
    user: The username of the recipient.
    subject: The subject of the notification.
    message: The message body of the notification.
  """

  from frappe import notify

  notify.send(
      recipients=[user],
      subject=subject,
      message=message,
      is_system_notification=True
  )

