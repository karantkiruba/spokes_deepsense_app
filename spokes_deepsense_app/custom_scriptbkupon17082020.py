import frappe
import erpnext
import json
from datetime import date

def update_salary_structure(self,method):
	salary_structure = frappe.get_doc('Salary Structure',  self.salary_structure)
	basic,gs,pft,esit,erpfc3,erpfc8,acno2,acno21,acno22,esice3,CTC,pf367,pf833,acn2,acn21,acn22,esi325,dailyallowance,Inc,LeaveDed,Ins,mobDed =0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00
	if self.employee_name:
		for earningdetails in self.earnings:
			if(earningdetails.salary_component == 'Basic'):
				basic=earningdetails.amount
		if(basic < 15000):
			basic = basic
		else:
			basic = 15000
		pft=basic
		if(self.gross_pay < 21000):
			gs = self.gross_pay
		else:
			gs = 0
		esit=gs
		if((pft * 0.0367)-round(pft * 0.0367) == 0.50):
			 pf367 = round(pft * 0.0367) + 1
		else:
			pf367 = round(pft * 0.0367)
		self.er_pf_contri_3_67 = pf367
		erpfc3 = pf367
		if((pft * 0.0833)-round(pft * 0.0833) == 0.50):
			pf833 = round(pft * 0.0833) + 1
		else:
			pf833 = round(pft * 0.0833)
		self.er_fpf_contri_8_33 =pf833
		erpfc8 =pf833
		if((pft * 0.005)-round(pft * 0.005) == 0.50):
			acn2 = round(pft * 0.005) + 1
		else:
			acn2 = round(pft * 0.005)
		self.ac_no_2=  acn2
		acno2 = acn2
		if((pft * 0.005)-round(pft * 0.005) == 0.50):
			acn21 = round(pft * 0.005) + 1
		else:
			acn21 = round(pft * 0.005)
		self.ac_no_21 = acn21
		acno21 = acn21
		if((pft * 0.0001 * 0)-round(pft * 0.0001 * 0) == 0.50):
			acn22 = round(pft * 0.0001 * 0) + 1
		else:
			acn22 = round(pft * 0.0001 * 0)
		self.ac_no_22_ = acn22
		acno22 = acn22
		if((esit * 0.0325)-round(esit * 0.0325) == 0.50):
			esi325 = round(esit * 0.0325) + 1
		else:
			esi325 = round(esit * 0.0325)
		self.esi_contribution_for_employer_3_25 = esi325
		esice3 = esi325
		self.ctc = (self.gross_pay+erpfc3+erpfc8+acno2+acno21+acno22+esice3)
