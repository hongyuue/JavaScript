with open("16.txt") as read_a_file:
	read_a_line = read_a_file.readline()
	
print read_a_line

for line in read_a_line:
	s_line = line.lstrip()
	print s_line
