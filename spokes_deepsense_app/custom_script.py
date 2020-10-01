import frappe
import erpnext
import json
from datetime import date

def update_salary_structure(self,method):
	salary_structure = frappe.get_doc('Salary Structure',  self.salary_structure)
	basic,gs,pft,esit,erpfc3,erpfc8,acno2,acno21,acno22,esice3,CTC,pf367,pf833,acn2,acn21,acn22,esi325,dailyallowance,Inc,LeaveDed,Ins,mobDed =0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00
