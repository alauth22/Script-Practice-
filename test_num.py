def compute_number(num):
	num = num + 2
	return num


def compute_lst(num):
	return ["A" for i in range(num)]


def square(num):
	return[num**2]


with open("result.txt", "w") as res_file:
	test_01 = str(compute_number(10) + compute_number(100))
	res_file.write(test_01 + "\n")

	