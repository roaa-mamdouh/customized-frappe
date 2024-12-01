frappe.views.calendar['Event'] = {
 field_map: {
 start: 'starts_on',
 end: 'ends_on',
 id: 'name',
 allDay: 'all_day',
 title: 'subject',
 status: 'event_type',
 color: 'color'
 },
 gantt: { // The values set here will override the values set in the object just for Gantt View
 order_by: 'starts_on',
 }
 style_map: {
 Public: 'success',
 Private: 'info'
 },
 order_by: 'starts_on',
 get_events_method: 'frappe.desk.doctype.event.event.get_events'
}
