import getch
from source import variables as var


class Functions():
	def __init__(self):
		pass


	########################################
	# ----> To extract a column from 2D list
	########################################
	def get_column(self,table,column):
		list = []

		for x in range(len(table)):

			list.append(table[x][column])
		return list

	###############################################
	# ----> to get User Input  (MENU) :: type(CHAR)
	###############################################
	def get_input(self,table):
		# Table to get Range of Valid Inputs
		table

		rangeL = 1
		rangeR = len(table)

		test_num = "0123456789"

		print(var.get_input_menu)

		char = getch.getch()
		

		try:
			char = int(char)
		except:
			return "err_01"

		if char <= rangeR and char >= rangeL:
			return char

		else:
			return "err_02"


	#####################################################
	# ----> Search for value in desired column of 2D list
	#####################################################
	def search_by_id(self,table,column,input_var,menu_return):
		
		index = 0
		IDs = self.get_column(table,column)
		output = []

		
		temp = input(input_var)
		try:
			# check if input is integer
			temp = int(temp)
			if temp in IDs:
				# index of row, containing ID
				index = IDs.index(temp)
				# Column Names
				output.append(table[0])
				# Column Values
				output.append(table[index])
				return output

			else:
				return "err_03"
				
		except:
			pass
			return "err_05"


	#################################################
	# ----> Search for value in 1st column of 2D list
	#################################################
	def search_by_name(self,table,column,input_var,menu_return):
		
		index = 0
		names = self.get_column(table,column)
		output = []

		temp = input(input_var)

		if temp in names:
			#index of the rows containing the Name
			index = names.index(temp)
			# Column Names
			output.append(table[0])
			# Column Values
			output.append(table[index])
			return output
		else:
			return "err_04"
