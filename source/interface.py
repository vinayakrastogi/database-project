from source import variables as var
import os,sys
import time
class Interface():
	def __init__(self):
		###################################
		# ----> Clear Variable for diff. OS
		###################################
		self.erase_var = ""

		if sys.platform == "linux":
			self.erase_var = "clear"

		elif sys.platform == "win32":
			self.erase_var = "cls"




	###################################
	# ----> Func. to clear CLI's Screen
	###################################
	def clear(self):
		os.system(self.erase_var)


	#############################
	# ----> Waits for a key press
	#############################
	def wait(self):
		print(var.wait)
		x = input()

	######################################################
	# ----> Transforms 1D List to 2D with N no. of Columns
	######################################################
	def menufy(self,options,columns,option_nums = False):

		temp = []
		menu = []

		x = 0
		y = columns

		while True:
			try:

				# Appends new elements ranging to new columns
				if x < len(options):
					menu.append(options[x:y])

				if len(options) < y:
					# breaks if reached end and no more element
					# to append
					break
			except:

				# Appends remaining element if they are no falling
				# in range of columns
				menu.append(options[x])

				if len(options) < y:
					break

			x = y
			y += columns

		# Adds empty elements to complete the Matrix
		for x in range(len(menu)):

			for y in range(columns):

				if len(menu[x]) != columns and len(options) > columns:

					for i in range(columns - len(menu[x])):

						menu[x].append(" ")

		if option_nums == False:
			# Menu Passed to Tabulate to Create Output
			self.tabulate(menu,"menu","",False)
		else:
			# Menu Passed to Tabulate to Create Output
			self.tabulate(menu,"menu")


	

	##################################################
	# Transforms a 2D to list to Readable Table Format
	##################################################

	def tabulate(self,table,ttype,table_name = "",option_nums = True,crt_r = 0,crt_c = 0,len_const = "False",go_up = False,go_down = False):


	# table : 2D list to be printed
	# ttype : menu , data , table

	# ttype (table) : shows table without pointer
	# ttype (data) : shows table with a pointer
	# ttype (menu) : Indexes the Table

	#option_nums : indexes tables items

	#crt_r : Current Row
	#crt_c : Current Column




		# Current Pointer Variable :: Left
		ptr_l = " "

		# Current Pointer Variable :: Right
		ptr_r = " "

		# main string top containg the table form output
		string = ""

		# Option No to Index the List of Options
		option_num = 1

		#if table Is a matrix Then Continue
		# else stop processing Tabulate
		if self.is_Matrix(table) == True:
			pass
		else:
			#THrow Error
			return None

		# Total No of rows in Table
		rows = len(table)

		# Total No of Columns in Each Row
		columns = len(table[0])

		# Max Length of Each Column Required
		columns_length = []

		# Max Length To Create Rows Seperators
		horizontal_length = 0


		# Assigning no of columns for max len
		for i in range(columns):
			columns_length.append(0)

		# Calculating Max Length Of each Column
		for i in range(0,rows):
			for j in range(0,columns):
				if len(str(table[i][j])) > columns_length[j]:
					columns_length[j] = len(str(table[i][j]))

		# Calculating Max length For Row Seperators
		for i in range(columns):
			horizontal_length += columns_length[i] + 4
		horizontal_length += 1

		if len_const == "Store":
			self.horizontal_length = horizontal_length
			self.columns_length = columns_length


		if len_const == "True":
			horizontal_length = self.horizontal_length
			columns_length = self.columns_length

		# Output Creation

		string += "\n"
		if table_name != "":
			string += var.tab + ("_" * (horizontal_length//2 - len(table_name)//2)) + table_name
			string += ("_" * ((horizontal_length//2) - len(str(table_name))//2))
			string += "\n\n"
		if go_up == True:
			print(" " * ((horizontal_length//2)+4),"︿")
		else:
			print()
		for i in range(rows):
			if ttype == "table" and i == 0:
				# Rows Seperator
				string += "\n\n"
			else:
				# Rows Seperator
				string += ((var.tab) + var.row_seperator * horizontal_length) + "\n\n"

			# Column Start
			string += (var.tab) + var.column_seperator

			for j in range(columns):

				# Assigning Pointers
				if i == crt_r and j == crt_c and ttype == "data":
					ptr_l = "["
					ptr_r = "]"
				else:
					ptr_l = " "
					ptr_r = " "

				if ttype == "menu" and table[i][j] != " " and option_nums == False:
					ptr_l = option_num
					option_num += 1

				if ttype == "table":
					ptr_l = " "
					ptr_r = " "

				# Left Pointer
				string += str(ptr_l) + " "

				# Cell Value
				string += str(table[i][j])

				# Extra Spaces for even Output Creation
				string += " " * (columns_length[j] - len(str(table[i][j])))

				# Right Pointer
				string += ptr_r

				# Column Seperator
				string += var.column_seperator

			# Row Ending
			string += "\n"

		# Table End
		string += (var.tab) + var.row_seperator * horizontal_length
		string += "\n"

		print(string)
		if go_down == True:
			print(" " * ((horizontal_length//2)+4),"﹀")
		else:
			print()


	############################################
	# ----> Checks if a 2D list is Matrix or Not
	############################################
	def is_Matrix(self,table):

		temp = len(table[0])
		for i in range(len(table)):
			if len(table[i]) == temp:
				pass
			else:
				return False
		return True



	#######################################
	# ----> Works as Notifier, displays LOG
	#######################################
	def message_box(self,mtype,message,length = 60):
		temp = ""
		if mtype == "dir" and type(message) == list :
			for i in range(len(message)):
				temp += str(message[i]) + " > "
			message = temp

		if mtype == "dir":
			mtype = var.mssg_title_dir

		if len(message) > length:
			length = len(message)

		length += 4
		string = "\n\n"

		string += (var.tab) + var.row_seperator * 5 
		string += mtype
		string += (var.row_seperator * (length - len(mtype) - 5))
		string += "\n\n"
		string += (var.tab) + var.column_seperator + " "
		string += message
		string += " " * (length - len(message) - 4)
		string += " " + var.column_seperator + "\n"
		string += (var.tab) + (var.row_seperator * length)
		string += "\n"
		print(string)

