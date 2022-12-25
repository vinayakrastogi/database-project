from source import interface
from source import functions
from source import variables as var

import pandas
import sys

ui = interface.Interface()
functions = functions.Functions()

class App():
	def __init__(self):

		self.load_data_files()
		self.dir = []

	def change_directory(self,value):
		if value == "back":
			self.dir.pop()
		else :
			self.dir.append(value)



	#######################################
	# ----> Starts The main loop of program
	#######################################
	def execute(self):
		while True:
			ui.clear()
			ui.message_box(var.mssg_title_default,"")
			self.user()
	

	#########################################
	# ----> Load Files containing Store Info.
	#########################################
	def load_data_files(self):

		self.products = pandas.read_csv("data/products.csv")
		temp = self.products.columns.tolist()
		self.products = self.products.values.tolist()
		self.products.insert(0,temp)

		self.employees = pandas.read_csv("data/employee.csv")
		temp = self.employees.columns.tolist()
		self.employees = self.employees.values.tolist()
		self.employees.insert(0,temp)

		self.complaints = pandas.read_csv("data/complaints.csv")
		temp = self.complaints.columns.tolist()
		self.complaints = self.complaints.values.tolist()
		self.complaints.insert(0,temp)
		


	#####################################################
	# ----> Defines the Current User as Admin or Customer
	#####################################################
	def user(self):
		print(var.user)
		ui.menufy(var.user_list,1)
		choice = functions.get_input(var.user_list)

		if choice == 1:

			ui.clear()
			ui.message_box(var.mssg_title_default,"")
			self.check_admin()

		elif choice == 2:
			ui.clear()
			ui.message_box(var.mssg_title_default,var.cust_mssg)
			self.user()

		elif choice == 3:
			sys.exit()

		else:
			ui.clear()
			ui.message_box(var.mssg_title_error,var.err_01)
			self.user()


	####################################
	# ----> Checks login info for Admins
	####################################
	def check_admin(self):

		temp = 0
		start = False

		for i in range(3):

			name = input(var.get_admin_name)

			if name in var.admin_ids:

				temp = var.admin_ids.index(name)
				ui.clear()
				ui.message_box(var.mssg_title_default,var.admin_name_found)

				for j in range(3):

					pswd = input(var.get_admin_pswd)

					if pswd == var.admin_pswd[temp]:

						ui.clear()
						self.change_directory(var.admin)
						ui.message_box("dir",self.dir)
						start = True
						break

					else:
						ui.clear()
						ui.message_box(var.mssg_title_default,var.try_again_admin_pswd)
					if j == 2:
						ui.clear()
						ui.message_box(var.mssg_title_default,var.tries_done)
				if start == True:
					break

			else:
				ui.clear()
				ui.message_box(var.mssg_title_default,var.try_again_admin_name)

			if i == 2:
				ui.clear()
				ui.message_box(var.mssg_title_default,var.tries_done)
				self.user()
		if start == True:
			self.admin_main_menu()




	######################################
	# ----> Start Admins Program/Functions
	######################################
	def admin_main_menu(self):
		while True:
			ui.menufy(var.admin_menu_0,1)
			choice = functions.get_input(var.admin_menu_0)
			ui.clear()

			if choice == len(var.admin_menu_0):
				self.change_directory("back")
				break

			elif choice == 1:
				self.change_directory(var.admin_menu_0[0])
				ui.message_box("dir",self.dir)
				self.admin_menu_0_1()

			elif choice == 2:
				self.change_directory(var.admin_menu_0[1])
				ui.message_box("dir",self.dir)
				self.admin_menu_0_2()

			elif choice == 3:
				self.change_directory(var.admin_menu_0[2])
				ui.message_box("dir",self.dir)
				self.admin_menu_0_3()

			elif choice == 4:
				self.change_directory(var.admin_menu_0[3])
				ui.message_box("dir",self.dir)
				self.admin_menu_0_4()

			elif choice == 5:
				self.change_directory(var.admin_menu_0[4])
				ui.message_box("dir",self.dir)
				self.admin_menu_0_5()

			elif choice == 6:
				self.change_directory(var.admin_menu_0[5])
				ui.message_box("dir",self.dir)
				self.admin_menu_0_6()

			else:
				ui.message_box(var.mssg_title_error,var.err_01)


	###########################################
	# ----> Start Customer's Programs/Functions
	###########################################
	def customer_main_menu(self):
		while True:
			ui.menufy(var.customer_menu_0,1)
			choice = functions.get_input(var.customer_menu_0)
			if choice == len(var.customer_menu_0):
				self.change_directory("back")
				break
			
			if choice == 1:
				self.message_box(var.mssg_title_default,var.customer_menu_0[0])
			
			if choice == 2:
				self.message_box(var.mssg_title_default,var.customer_menu_0[1])
			
			if choice == 3:
				self.message_box(var.mssg_title_default,var.customer_menu_0[2])
			
			if choice == 4:
				self.message_box(var.mssg_title_default,var.customer_menu_0[3])
			


	########################################
	#
	# ----> Executes Command based on inputs
	#		for ADMIN
	########################################		


	def admin_menu_0_1(self):
		while True:
			ui.menufy(var.admin_menu_0_1,1)
			choice = functions.get_input(var.admin_menu_0_1)
			ui.clear()

			if choice == len(var.admin_menu_0_1):
				self.change_directory("back")
				ui.message_box("dir",self.dir)
				break
			
			elif choice == 1:
				self.change_directory(var.admin_menu_0_1[0])
				ui.message_box("dir",self.dir)
				ui.tabulate(self.products,"table","Products")
				ui.wait()
				ui.clear()
				self.change_directory("back")
				ui.message_box("dir",self.dir)

			elif choice == 2:
				self.change_directory(var.admin_menu_0_1[1])
				ui.message_box("dir",self.dir)
				output = functions.search_by_id(self.products,0,var.enter_pid,var.admin_menu_0[0])
				if output == "err_03":
					ui.clear()
					ui.message_box(var.mssg_title_error,var.err_03)
				elif output == "err_05":
					ui.clear()
					ui.message_box(var.mssg_title_error,var.err_05)

				else :
					ui.clear()
					ui.message_box("dir",self.dir)
					ui.tabulate(output,"table")



				ui.wait()
				ui.clear()
				self.change_directory("back")
				ui.message_box("dir",self.dir)

			elif choice == 3:

				self.change_directory(var.admin_menu_0_1[2])
				ui.message_box("dir",self.dir)

				output = functions.search_by_name(self.products,1,var.enter_pname,var.admin_menu_0[0])

				if output == "err_04":
					ui.clear()
					ui.message_box(var.mssg_title_error,var.err_04)
				else:
					ui.clear()
					ui.message_box("dir",self.dir)

					ui.tabulate(output,"table")

				ui.wait()
				ui.clear()
				self.change_directory("back")
				ui.message_box("dir",self.dir)

			else:

				ui.clear()
				ui.message_box(var.mssg_title_error,var.err_01)



	def admin_menu_0_2(self):
		while True:
			ui.menufy(var.admin_menu_0_2,1)
			choice = functions.get_input(var.admin_menu_0_2)
			ui.clear()

			if choice == 1:
				self.products = functions.spreadsheet_mode(self.products,"Products")
				temp = self.products.pop(0)
				self.products = pandas.DataFrame(self.products,columns = temp)
				self.products.to_csv("data/products.csv",index = False)
				self.load_data_files()
				ui.clear()
				ui.message_box("dir",self.dir)


			elif choice == len(var.admin_menu_0_2):
				self.change_directory("back")
				ui.message_box("dir",self.dir)
				break


			else:
				ui.clear()
				ui.message_box(var.mssg_title_error,var.err_01)


	def admin_menu_0_3(self):
		while True:
			ui.menufy(var.admin_menu_0_3,1)
			choice = functions.get_input(var.admin_menu_0_3)
			ui.clear()

			if choice == len(var.admin_menu_0_3):
				self.change_directory("back")
				ui.message_box("dir",self.dir)
				break


			elif choice == 1:
				self.change_directory(var.admin_menu_0_3[0])
				ui.message_box("dir",self.dir)
				ui.tabulate(self.employees,"table","Employees")

				ui.wait()
				ui.clear()
				self.change_directory("back")
				ui.message_box("dir",self.dir)

			elif choice == 2:
				self.change_directory(var.admin_menu_0_3[1])
				ui.message_box("dir",self.dir)
				output = functions.search_by_id(self.employees,0,var.enter_eid,var.admin_menu_0_3[0])
				if output == "err_03":
					ui.clear()
					ui.message_box(var.mssg_title_error,var.err_03)
				elif output == "err_05":
					ui.clear()
					ui.message_box(var.mssg_title_error,var.err_05)

				else :
					ui.clear()
					ui.message_box("dir",self.dir)
					ui.tabulate(output,"table")



				ui.wait()
				ui.clear()
				self.change_directory("back")
				ui.message_box("dir",self.dir)

			elif choice == 3:

				self.change_directory(var.admin_menu_0_3[2])
				ui.message_box("dir",self.dir)

				output = functions.search_by_name(self.employees,1,var.enter_ename,var.admin_menu_0_3[0])

				if output == "err_04":
					ui.clear()
					ui.message_box(var.mssg_title_error,var.err_04)
				else:
					ui.clear()
					ui.message_box("dir",self.dir)

					ui.tabulate(output,"table")

				ui.wait()
				ui.clear()
				self.change_directory("back")
				ui.message_box("dir",self.dir)

			else:

				ui.clear()
				ui.message_box(var.mssg_title_error,var.err_01)

	def admin_menu_0_4(self):
		while True:
			ui.menufy(var.admin_menu_0_4,1)
			choice = functions.get_input(var.admin_menu_0_4)
			ui.clear()

			if choice == 1:
				self.employees = functions.spreadsheet_mode(self.employees,"Employees")
				temp = self.employees.pop(0)
				self.employees = pandas.DataFrame(self.employees,columns = temp)
				self.employees.to_csv("data/employee.csv",index = False)
				self.load_data_files()
				ui.clear()
				ui.message_box("dir",self.dir)


			elif choice == len(var.admin_menu_0_2):
				self.change_directory("back")
				ui.message_box("dir",self.dir)
				break


			else:
				ui.clear()
				ui.message_box(var.mssg_title_error,var.err_01)

	def admin_menu_0_5(self):
		while True:
			ui.menufy(var.admin_menu_0_5,2)
			choice = functions.get_input(var.admin_menu_0_5)
			ui.clear()


			if choice == 1:
				self.change_directory(var.admin_menu_0_5[0])
				ui.message_box("dir",self.dir)

				functions.plot_graph(functions.get_column(self.products,4),functions.get_column(self.products,1),"line","Products","Quantity")
				ui.wait()
				self.change_directory("back")
				ui.clear()
				ui.message_box("dir",self.dir)


			if choice == 2:
				self.change_directory(var.admin_menu_0_5[1])
				ui.message_box("dir",self.dir)

				functions.plot_graph(functions.get_column(self.products,4),functions.get_column(self.products,1),"bar","Products","Quantity")
				ui.wait()
				self.change_directory("back")
				ui.clear()
				ui.message_box("dir",self.dir)


			if choice == 3:
				self.change_directory(var.admin_menu_0_5[2])
				ui.message_box("dir",self.dir)

				output = functions.max_min(self.products,4,"max")

				ui.tabulate(output,"table")

				ui.wait()
				self.change_directory("back")
				ui.clear()
				ui.message_box("dir",self.dir)

			if choice == 4:
				self.change_directory(var.admin_menu_0_5[3])
				ui.message_box("dir",self.dir)

				output = functions.max_min(self.products,4,"min")

				ui.tabulate(output,"table")

				ui.wait()
				self.change_directory("back")
				ui.clear()
				ui.message_box("dir",self.dir)

			if choice == 5:
				self.change_directory(var.admin_menu_0_5[4])
				ui.message_box("dir",self.dir)

				output = functions.total(self.products,4,"Products Sold")

				ui.menufy(output,1,True)

				ui.wait()
				self.change_directory("back")
				ui.clear()
				ui.message_box("dir",self.dir)

			if choice == 6:
				self.change_directory(var.admin_menu_0_5[5])
				ui.message_box("dir",self.dir)

				output = functions.max_min(self.employees,2,"max")

				ui.tabulate(output,"table")

				ui.wait()
				self.change_directory("back")
				ui.clear()
				ui.message_box("dir",self.dir)

			if choice == 7:
				self.change_directory(var.admin_menu_0_5[6])
				ui.message_box("dir",self.dir)

				output = functions.max_min(self.employees,2,"min")

				ui.tabulate(output,"table")

				ui.wait()
				self.change_directory("back")
				ui.clear()
				ui.message_box("dir",self.dir)

			if choice == 8:
				self.change_directory(var.admin_menu_0_5[7])
				ui.message_box("dir",self.dir)

				output = functions.total(self.employees,2,"Salary Given")

				ui.menufy(output,1,True)

				ui.wait()
				self.change_directory("back")
				ui.clear()
				ui.message_box("dir",self.dir)

			elif choice == len(var.admin_menu_0_5):
				self.change_directory("back")
				ui.message_box("dir",self.dir)
				break

			else:
				ui.clear()
				ui.message_box(var.mssg_title_error,var.err_01)

	def admin_menu_0_6(self):
		while True:
			ui.menufy(var.admin_menu_0_6,1)
			choice = functions.get_input(var.admin_menu_0_6)
			ui.clear()



			if choice == 1:
				self.change_directory(var.admin_menu_0_6[0])
				ui.message_box("dir",self.dir)
				ui.tabulate(self.complaints,"table","Complaints")

				ui.wait()
				self.change_directory("back")
				ui.clear()
				ui.message_box("dir",self.dir)


			elif choice == len(var.admin_menu_0_6):
				self.change_directory("back")
				ui.message_box("dir",self.dir)
				break

			else:
				ui.clear()
				ui.message_box(var.mssg_title_error,var.err_01)
			

if __name__ == "__main__":
	app = App()
	app.execute()