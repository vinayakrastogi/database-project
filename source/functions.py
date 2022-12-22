from source import variables as var
from source import interface
import matplotlib.pyplot as plt
import getch
import copy

ui = interface.Interface()

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

		print("\n\n")		
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
		print("\n\n")		
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

	#################################################
	# ----> Spreadsheet Mode (Manage Tables)
	#################################################
	def spreadsheet_mode(self,table,name):
		init_table = copy.deepcopy(table)
		_range = 10
		fields = table.pop(0)
		_max = len(table)
		top = 0
		bottom = 10
		crt_row = 0
		row = 0 	#Current Row
		columns = len(table[0])
		column = 0 	#Current Column
		event = 0
		first_loop = True
		gup = False
		gdown = False

		new_row = []
		for i in range(columns):
			new_row.append("")


		while True:

			functions_1 = f'''
{var.tab}Navigation  |   Document   |   File              |   Info
{var.tab}---------------------------------------------------------------------
{var.tab}Up    : ↑   |   save : s   |   Add new row : i   |   Table          : {name}
{var.tab}Down  : ↓   |   edit : e   |   Delete Row  : r   |   Total Rows     : {_max}
{var.tab}Left  : ←   |   exit : x   |                     |   Current Row    : {row + 1}
{var.tab}Right : →   |              |                     |   Current Column : {column + 1}
'''
			ui.clear()
			print(functions_1)

			if _max - row - 10 + crt_row > 0:
				gdown = True
			else:
				gdown = False

			if row - crt_row >0 :
				gup = True
			else:
				gup = False


			
			ui.tabulate(table[top:bottom],"data",crt_r = crt_row ,crt_c = column,len_const = "Store",go_up = gup,go_down = gdown)
			
			event = getch.getch()

			if event == "B":
				if crt_row == _range - 1 :
					for i in range(_range,0,-1):
						if bottom + i <= _max:
							top = bottom
							bottom += i
							row += 1
							crt_row = 0
							break
				elif row != _max - 1:
					crt_row += 1
					row += 1

			if event == "A":
				if crt_row == 0:
					for i in range(_range,0,-1):
						if top - 1 > 0 :
							bottom = top
							top -= i
							crt_row = _range - 1
							row -= 1
							break
				else:
					crt_row -= 1
					row -= 1

			if event == "C" and column < columns - 1:
				column += 1
			if event == "D" and column > 0:
				column -= 1




			if event.lower() == "x":
				ui.clear()
				return init_table

			if event.lower() == "e":
				value = input("Enter new value :: ")
				table[row][column] = value

			if event.lower() == "s":
				table.insert(0,fields)
				return table

			if event.lower() == "r":
				table.pop(row)
				_max = len(table)


			if event.lower() == "i":
				table.insert(row+1,copy.deepcopy(new_row))
				_max = len(table)

	def plot_graph(self,values,indexes,gtype,xlab,ylab):
		for i in range(len(values)):
			try:
				values[i] = int(values[i])
			except:
				values[i] = 0

		indexes.pop(0)
		values.pop(0)


		args1 = {"color":"#3c3f8c",
		"linestyle":"solid",
		"linewidth":"1",
		"marker":"s",
		"mfc":"#b00909",
		"mec":"#b00909"}
		plt.figure(facecolor = "#01020f")
		ax = plt.axes()
		ax.set_facecolor("#000229")
		ax.tick_params(axis = "x", colors = "white")
		ax.tick_params(axis = "y", colors = "white")
		ax.xaxis.label.set_color("white")
		ax.yaxis.label.set_color("white")
		plt.xticks(fontsize = 7,rotation = 90)
		plt.yticks(fontsize = 7)
		plt.grid(color = "#202020")
		ax.set_xlabel(xlab)
		ax.set_ylabel(ylab)

		if gtype == "line":
			plt.plot(indexes,values,**args1)
			plt.tight_layout()
			plt.show()

		if gtype == "bar":
			plt.bar(indexes,values)
			plt.tight_layout()
			plt.show()


	def max_min(self,table,col_no,mtype):

		output = []
		temp = self.get_column(table,col_no)
		temp.pop(0)
		for i in range(len(temp)):
			try:
				temp[i] = int(temp[i])
			except:
				temp[i] = 0

		if mtype == "max":
			mval = max(temp)
		elif mtype == "min":
			mval = min(temp)

		mindex = temp.index(mval)

		output.append(table[0])
		output.append(table[mindex + 1])

		return output

	def total(self,table,col_no,name):
		temp = self.get_column(table,col_no)
		temp.pop(0)

		for i in range(len(temp)):
			try:
				temp[i] = int(temp[i])
			except:
				temp[i] = 0

		output = [name,sum(temp)]
		return output