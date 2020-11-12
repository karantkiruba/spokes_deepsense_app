import frappe
import erpnext
import json
from datetime import date

def update_salary_structure(self,method):
	salary_structure = frappe.get_doc('Salary Structure',  self.salary_structure)
	basic,gs,pft,esit,erpfc3,erpfc8,acno2,acno21,acno22,esice3,CTC,pf367,pf833,acn2,acn21,acn22,esi325,dailyallowance,Inc,LeaveDed,Ins,mobDed =0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00


def create_projectforsalesorder(self,method):
	project = frappe.get_doc({
		"doctype": "Project",
		"project_name": self.name ,
		"project_type":'Internal',
		"sales_order":self.name,
		"customer":self.customer
	})
	project.insert()
