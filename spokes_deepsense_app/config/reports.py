from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
	 {
		"label":_("Human Resources"),
		"icon": "octicon octicon-briefcase",
		"items": [
                  {
			 "type": "report",
			 "is_query_report": True,
			 "name": "Salary Register Report",
			 "doctype": "Salary Slip"
		 },
		]
	 },
	]
