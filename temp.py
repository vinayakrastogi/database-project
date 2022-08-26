import getch,os

_max = 100
_range = 10
top = 0
bottom = 10
crt = 0
x = 0
while True:
	print("MAX ",_max)
	print("RANGE ",_range)
	print("TOP ",top)
	print("BOTTOM ",bottom)
	print("ROW ",row)
	print("CRT ",crt)
	print("INPUT",x)
	print("\n\n")
	x = getch.getch()
	os.system("clear")

	if x == "B":
		if crt == _range-1:
			for i in range(_range,0,-1):
				if bottom + i < _max:
					top = bottom
					bottom += i
					crt = 0
					break

		if row != bottom - 1:
			crt_row += 1
			row += 1

	if x == "A":
		if crt == 0:
			for i in range(_range,0,-1):
				if top - i > 0 :
					bottom = top
					top -= i
					crt = 9
					break
		else:
			crt -= 1