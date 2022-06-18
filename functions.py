#from curses import erasechar
import variables
import os,sys
import getch
import pandas


class functions():

	def __init__(self):
		self.started = True
		self.msg_back = False

		###################################
		# ----> Clear Variable for diff. OS
		###################################
		self.erase_var = ""

		if sys.platform == "linux":
			self.erase_var = "clear"

		elif sys.platform == "win32":
			self.erase_var = "cls"

		##########################
		# ----> Reading Data Files
		##########################

		self.products = pandas.read_json('products.json')
		self.temp = self.products.columns.tolist()
		self.products = self.products.values.tolist()
		self.product_IDs = self.get_column(self.products,0)
		self.products.insert(0,self.temp)

		self.employees = pandas.read_json('employee.json')
		self.temp = self.employees.columns.tolist()
		self.employees = self.employees.values.tolist()
		self.employee_ID = self.get_column(self.employees,0)
		self.employees.insert(0,self.temp)


	#######################################
	# ----> Starts The main loop of program
	#######################################
	def execute(self):
		while True:
			self.clear()
			self.message_box(variables.mssg_title_default,"")
			self.user()

	###################################
	# ----> Func. to clear CLI's Screen
	###################################
	def clear(self):
		os.system(self.erase_var)

	####################################
	# ----> Checks login info for Admins
	####################################
	def check_admin(self):

		self.temp = 0
		self.start = False

		for i in range(3):

			self.name = input(variables.get_admin_name)

			if self.name in variables.admin_ids:

				self.temp = variables.admin_ids.index(self.name)
				self.clear()
				self.message_box(variables.mssg_title_default,variables.admin_name_found)

				for j in range(3):

					self.pswd = input(variables.get_admin_pswd)

					if self.pswd == variables.admin_pswd[self.temp]:

						self.clear()
						self.message_box(variables.mssg_title_default,variables.admin_logged_in)
						self.start = True
						break

					else:
						self.clear()
						self.message_box(variables.mssg_title_default,variables.try_again_admin_pswd)
					if j == 2:
						self.clear()
						self.message_box(variables.mssg_title_default,variables.tries_done)
				if self.start == True:
					break

			else:
				self.clear()
				self.message_box(variables.mssg_title_default,variables.try_again_admin_name)

			if i == 2:
				self.clear()
				self.message_box(variables.mssg_title_default,variables.tries_done)
				self.user()
		if self.start == True:
			self.admin_menu_0()





	#############################################
	# ----> Func. to get User Input :: type(CHAR)
	#############################################
	def get_input(self,table):
		# Table to get Range of Valid Inputs 
		self.table = table

		self.rangeL = 1
		self.rangeR = len(table)

		self.test_num = "0123456789"

		print(variables.get_input_menu)

		self.char = getch.getch()
		

		try:
			self.char = int(self.char)
		except:
			self.clear()
			self.message_box(variables.mssg_title_error,variables.err_mssg_01)
			return None

		if self.char <= self.rangeR and self.char >= self.rangeL:
			self.clear()
			return self.char

		else:
			self.clear()
			self.message_box(variables.mssg_title_error,variables.err_mssg_01)


	#########################################
	# ----> Input mode for table (excel type)
	#########################################
	def get_input_table(self):
		valid_inputs = [65,66,67,68]
		print(" :: ")
		x = ord(getch.getch())

		if x in valid_inputs:
			return x




	############################################
	# ----> Checks if a 2D list is Matrix or Not
	############################################
	def is_Matrix(self,table):
		self.table = table
		self.temp = len(self.table[0])
		for i in range(len(self.table)):
			if len(self.table[i]) == self.temp:
				pass
			else:
				return False
		return True



	######################################################
	# ----> Transforms 1D List to 2D with N no. of Columns
	######################################################
	def menufy(self,options,columns,option_nums = False):
		# 1D List of menu Options
		self.options = options

		# new no. of columns
		self.columns = columns

		self.temp = []
		self.menu = []

		self.x = 0
		self.y = self.columns

		while True:
			try:

				# Appends new elements ranging to new columns
				if self.x < len(self.options):
					self.menu.append(options[self.x:self.y])

				if len(self.options) < self.y:
					# breaks if reached end and no more element
					# to append
					break
			except:

				# Appends remaining element if they are no falling
				# in range of columns
				self.menu.append(self.options[self.x])

				if len(self.options) < self.y:
					break

			self.x = self.y
			self.y += self.columns

		# Adds empty elements to complete the Matrix
		for self.x in range(len(self.menu)):

			for self.y in range(self.columns):

				if len(self.menu[self.x]) != self.columns and len(self.options) > self.columns:

					for i in range(self.columns - len(self.menu[self.x])):

						self.menu[self.x].append(" ")

		if option_nums == True:
			# Menu Passed to Tabulate to Create Output
			self.tabulate(self.menu,"menu","",True)
		else:
			# Menu Passed to Tabulate to Create Output
			self.tabulate(self.menu,"menu")


	

	##################################################
	# Transforms a 2D to list to Readable Table Format
	##################################################

	def tabulate(self,table,ttype,table_name = "",option_nums = False,crt_r = 0,crt_c = 0):
		# List of Menus to print
		self.table = table

		# Type of Table , Data or Options Menu
		self.ttype = ttype

		# Name of the table while printing Data
		self.table_name = table_name
		# Current Pointer Location :: Row (TABLE MODE)
		self.crt_r = crt_r

		# Current Pointer Location :: Column (TABLE MODE)
		self.crt_c = crt_c

		# Current Pointer Variable :: Left
		self.ptr_l = " "

		# Current Pointer Variable :: Right
		self.ptr_r = " "

		# main string top containg the table form output
		self.string = ""

		# Option No to Index the List of Options
		self.option_num = 1

		#if table Is a matrix Then Continue
		# else stop processing Tabulate
		if self.is_Matrix(self.table) == True:
			pass
		else:
			#THrow Error
			return None

		# Total No of rows in Table
		self.rows = len(self.table)

		# Total No of Columns in Each Row
		self.columns = len(self.table[0])

		# Max Length of Each Column Required
		self.columns_length = []

		# Max Length To Create Rows Seperators
		self.horizontal_length = 0


		# Assigning no of columns for max len
		for self.i in range(self.columns):
			self.columns_length.append(0)

		# Calculating Max Length Of each Column
		for self.i in range(0,self.rows):
			for self.j in range(0,self.columns):
				if len(str(self.table[self.i][self.j])) > self.columns_length[self.j]:
					self.columns_length[self.j] = len(str(self.table[self.i][self.j]))

		# Calculating Max length For Row Seperators
		for self.i in range(self.columns):
			self.horizontal_length += self.columns_length[self.i] + 4
		self.horizontal_length += 1


		# Output Creation

		self.string += "\n"
		if self.table_name != "":
			self.string += variables.tab + ("_" * (self.horizontal_length//2 - len(self.table_name)//2)) + self.table_name
			self.string += ("_" * ((self.horizontal_length//2) - len(str(self.table_name))//2))
			self.string += "\n\n"

		for self.i in range(self.rows):
			if ttype == "table" and self.i == 0:
				# Rows Seperator
				self.string += "\n\n"
			else:
				# Rows Seperator
				self.string += ((variables.tab) + variables.row_seperator * self.horizontal_length) + "\n\n"

			# Column Start
			self.string += (variables.tab) + variables.column_seperator

			for self.j in range(self.columns):

				# Assigning Pointers
				if self.i == self.crt_r and self.j == self.crt_c and self.ttype == "data":
					self.ptr_l = "["
					self.ptr_r = "]"
				else:
					self.ptr_l = " "
					self.ptr_r = " "

				if self.ttype == "menu" and self.table[self.i][self.j] != " " and option_nums == False:
					self.ptr_l = self.option_num
					self.option_num += 1

				if self.ttype == "table":
					self.ptr_l = " "
					self.ptr_r = " "

				# Left Pointer
				self.string += str(self.ptr_l) + " "

				# Cell Value
				self.string += str(self.table[self.i][self.j])

				# Extra Spaces for even Output Creation
				self.string += " " * (self.columns_length[self.j] - len(str(self.table[self.i][self.j])))

				# Right Pointer
				self.string += self.ptr_r

				# Column Seperator
				self.string += variables.column_seperator

			# Row Ending
			self.string += "\n"

		# Table End
		self.string += (variables.tab) + variables.row_seperator * self.horizontal_length
		self.string += "\n"

		print(self.string)



	#######################################
	# ----> Works as Notifier, displays LOG
	#######################################
	def message_box(self,mtype,message,length = 60):
		self.length = length
		self.mtype = mtype
		self.message = message
		if self.msg_back == True:
			self.message = ""

		if len(self.message) > self.length:
			self.length = len(self.message)

		self.length += 4
		self.string = "\n\n"

		self.string += (variables.tab) + variables.row_seperator * 5 
		self.string += self.mtype
		self.string += (variables.row_seperator * (self.length - len(self.mtype) - 5))
		self.string += "\n\n"
		self.string += (variables.tab) + variables.column_seperator + " "
		self.string += self.message
		self.string += " " * (self.length - len(self.message) - 4)
		self.string += " " + variables.column_seperator + "\n"
		self.string += (variables.tab) + (variables.row_seperator * self.length)
		self.string += "\n"
		self.msg_back = False
		print(self.string)



	#############################
	# ----> Waits for a key press
	#############################
	def wait(self):
		print(variables.wait)
		x = input()


	#####################################################
	# ----> Defines the Current User as Admin or Customer
	#####################################################
	def user(self):
		print(variables.user)
		self.menufy(variables.user_list,1)
		self.choice = self.get_input(variables.user_list)

		if self.choice == 1:

			#self.clear()
			self.message_box(variables.mssg_title_default,"")
			self.check_admin()

		elif self.choice == 2:

			#self.clear()
			self.message_box(variables.mssg_title_default,variables.customer_logged_in)
			self.customer_menu_0()

		elif self.choice == 3:
			sys.exit()

		else:

			self.user()

	########################################
	# ----> To extract a column from 2D list
	########################################
	def get_column(self,table,column):
		self.table = table
		self.column = column
		self.list = []

		for self.x in range(len(self.table)):

			self.list.append(self.table[self.x][self.column])
		return self.list


	################################################
	# ----> Table Editing similar to Microsoft Excel
	################################################
	def modify_table(self,table):
		
		column_names = table[0]

		table.remove(table[0])

		rows = len(table)
		crt_row = 0
		crt_column = 0

		limit = 10

		top = 0
		bottom = 0

		for i in range(limit,0,-1):
			if bottom + i <= rows:
				bottom += i
				break
		#self.message_box(variables.mssg_title_default,"")
		while True:
			self.menufy(column_names,len(column_names),True)
			self.tabulate(table[top:bottom],"data",crt_r = crt_row,crt_c = crt_column)

			print(" TOP         :: ",top)
			print(" BOTTOM      :: ",bottom)
			print(" CURRENT ROW :: ",crt_row)


			choice = self.get_input_table()

			self.clear()
			
			if choice == 65 and crt_row > top:
				crt_row -= 1
				#self.message_box(variables.mssg_title_default,"")

			if choice == 66 and crt_row < bottom:
				crt_row += 1
				#self.message_box(variables.mssg_title_default,"")



			if choice == 66 and crt_row == bottom:
				for i in range(limit,0,-1):
					if bottom + i <= rows:
						top = bottom
						bottom += i
						crt_row = 0
						break

			if choice == 65 and crt_row == top:
				for i in range(limit,0,-1):
					if top - i >= 0:
						bottom = top
						top -= i
						crt_row = top
						break


















	#################################################
	# ----> Search for value in 1st column of 2D list
	#################################################
	def search_by_id(self,table,column,id_type,menu_return):
		
		self.table = table
		self.column = column
		self.index = 0
		self.IDs = self.get_column(self.table,self.column)
		self.id_type = id_type
		self.output = []

		for self.i in range(3):
			self.temp = input(self.id_type)
			try:
				self.temp = int(self.temp)
				if self.temp in self.IDs:
					self.index = self.IDs.index(self.temp)

					self.output.append(self.table[0])
					self.output.append(self.table[self.index])

					self.tabulate(self.output,"menu",option_nums = True)
					print("\n\n")
					self.wait()
					self.clear()
					self.message_box(variables.mssg_title_default,menu_return)
					break
				else:
					self.clear()
					self.message_box(variables.mssg_title_error,variables.err_mssg_03)


			except:
				self.clear()
				self.message_box(variables.mssg_title_error,variables.err_mssg_02)

	#################################################
	# ----> Search for value in 1st column of 2D list
	#################################################
	def search_by_name(self,table,column,name,menu_list):
		
		self.table = table
		self.column = column
		self.index = 0
		self.names = self.get_column(self.table,self.column)
		self.name = name
		self.output = []

		for self.i in range(3):

			self.temp = input(self.name)

			if self.temp in self.names:
				self.index = self.names.index(self.temp)
				self.output.append(self.table[0])
				self.output.append(self.table[self.index])
				self.tabulate(self.output,"menu",option_nums = True)
				print("\n\n")
				self.wait()
				self.clear()
				self.message_box(variables.mssg_title_default,menu_return)
				break
			else:
				self.clear()
				self.message_box(variables.mssg_title_error,variables.err_mssg_04)

			if self.i == 2:
				self.clear()
				self.message_box(variables.mssg_title_default,variables.admin_menu_0[0])







































	
	######################################
	# ----> Start Admins Program/Functions
	######################################
	def admin_menu_0(self):
		while True:
			self.menufy(variables.admin_menu_0,1)
			self.choice = self.get_input(variables.admin_menu_0)
			if self.choice == len(variables.admin_menu_0):
				break
			self.exec_admin_menu_0(self.choice)

	###########################################
	# ----> Start Customer's Programs/Functions
	###########################################
	def customer_menu_0(self):
		while True:
			self.menufy(variables.customer_menu_0,1)
			self.choice = self.get_input(variables.customer_menu_0)
			if self.choice == len(variables.customer_menu_0):
				break;
			self.exec_customer_menu_0(self.choice)




	###########################################
	# ----> Start Admin's Show Products Program
	###########################################
	def admin_menu_0_1(self):
		while True:
			self.menufy(variables.admin_menu_0_1,1)
			self.choice = self.get_input(variables.admin_menu_0_1)
			if self.choice == len(variables.admin_menu_0_1):
				self.msg_back = True
				break
			
			if self.choice == 1:

				self.message_box(variables.mssg_title_default,variables.admin_menu_0_1[0])
				self.tabulate(self.products,"table","Products")
				self.wait()
				self.clear()
				self.message_box(variables.mssg_title_default,variables.admin_menu_0[0])

			if self.choice == 2:

				self.message_box(variables.mssg_title_default,variables.admin_menu_0_1[1])
				self.search_by_id(self.products,0,variables.enter_pid,variables.admin_menu_0[0])

			if self.choice == 3:

				self.message_box(variables.mssg_title_default,variables.admin_menu_0_1[2])
				self.search_by_name(self.products,1,variables.enter_pname,variables.admin_menu_0[0])



	def admin_menu_0_3(self):
		while True:
			self.menufy(variables.admin_menu_0_3,1)
			self.choice = self.get_input(variables.admin_menu_0_3)
			if self.choice == len(variables.admin_menu_0_3):
				self.msg_back = True
				break
			
			if self.choice == 1:
				self.message_box(variables.mssg_title_default,variables.admin_menu_0_3[0])
				self.tabulate(self.employees,"table","Employees")
				self.wait()
				self.clear()
				self.message_box(variables.mssg_title_default,variables.admin_menu_0[2])

			if self.choice == 2:
				self.message_box(variables.mssg_title_default,variables.admin_menu_0_3[1])
				self.search_by_id(self.employees,0,variables.enter_eid,variables.admin_menu_0[2])

			if self.choice == 3:
				self.message_box(variables.mssg_title_default,variables.admin_menu_0[2])
				self.search_by_name(self.employees,1,variables.enter_ename,variables.admin_menu_0[2])





	########################################
	#
	# ----> Executes Command based on inputs
	#
	########################################


	def exec_admin_menu_0(self,choice):
		self.choice = choice
		
		if self.choice == 1:
			self.message_box(variables.mssg_title_default,variables.admin_menu_0[0])
			self.admin_menu_0_1()
		if self.choice == 2:
			self.message_box(variables.mssg_title_default,variables.admin_menu_0[1])
			self.modify_table(self.employees)
		if self.choice == 3:
			self.message_box(variables.mssg_title_default,variables.admin_menu_0[2])
			self.admin_menu_0_3()
		if self.choice == 4:
			self.message_box(variables.mssg_title_default,variables.admin_menu_0[3])
		if self.choice == 5:
			self.message_box(variables.mssg_title_default,variables.admin_menu_0[4])
		if self.choice == 6:
			self.message_box(variables.mssg_title_default,variables.admin_menu_0[5])



	def exec_customer_menu_0(self,choice):
		self.choice = choice

		if self.choice == 1:
			self.message_box(variables.mssg_title_default,variables.customer_menu_0[0])
		if self.choice == 2:
			self.message_box(variables.mssg_title_default,variables.customer_menu_0[1])
		if self.choice == 3:
			self.message_box(variables.mssg_title_default,variables.customer_menu_0[2])
		if self.choice == 4:
			self.message_box(variables.mssg_title_default,variables.customer_menu_0[3])
