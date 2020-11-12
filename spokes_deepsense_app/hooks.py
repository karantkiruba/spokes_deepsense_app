# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "spokes_deepsense_app"
app_title = "Spokes Deepsense App"
app_publisher = "Sybergate"
app_description = "Spokes Deepsense App"
app_icon = "default"
app_color = "default"
app_email = "benjamin.rosary@sybergate.co.in"
app_license = "MIT"

doc_events = {
        "Salary Slip":{
             "validate": "spokes_deepsense_app.custom_script.update_salary_structure"
         }
	#"Sales Order":{
        #     "on_submit": "spokes_deepsense_app.custom_script.create_projectforsalesorder"
        # }

}

fixtures = ["Custom Field", "Custom Script", "Property Setter", "Print Format"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/spokes_deepsense_app/css/spokes_deepsense_app.css"
# app_include_js = "/assets/spokes_deepsense_app/js/spokes_deepsense_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/spokes_deepsense_app/css/spokes_deepsense_app.css"
# web_include_js = "/assets/spokes_deepsense_app/js/spokes_deepsense_app.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "spokes_deepsense_app.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "spokes_deepsense_app.install.before_install"
# after_install = "spokes_deepsense_app.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "spokes_deepsense_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"spokes_deepsense_app.tasks.all"
# 	],
# 	"daily": [
# 		"spokes_deepsense_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"spokes_deepsense_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"spokes_deepsense_app.tasks.weekly"
# 	]
# 	"monthly": [
# 		"spokes_deepsense_app.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "spokes_deepsense_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "spokes_deepsense_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "spokes_deepsense_app.task.get_dashboard_data"
# }

