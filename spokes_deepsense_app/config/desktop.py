# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Spokes Deepsense App",
			"color": "default",
			"icon": "default",
			"type": "module",
			"label": _("Spokes Deepsense App")
		},
		{
                        "module_name": "Reports",
                        "color": "grey",
                        "icon": "octicon octicon-file-directory",
                        "type": "module",
                        "label": _("Reports")
                }

	]
