"""This is the "standard" way to include a multiple-line comment in your code."""

# This is a single line comment

def print_list(the_list, indent = False, level = 0):
	for item in the_list:
		if isinstance(item, list):
			print_list(item, indent, level + 1)
		else:
			if indent:
				for i in range(level):
					print("\t", end="")
			print(item)

