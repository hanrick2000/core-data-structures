
'''
Scenario 1: One-time route cost check
You have a carrier route list with 100,000 (100K) entries (in arbitrary order) and a single phone number. 
How quickly can you find the cost of calling this number?
'''


def calculate_num_cost(phone_number, carrier_route_list):
	with open(carrier_route_list) as f:
		content = f.readlines()

	content = [x.strip() for x in content] 
	content.sort()
	

	route_dict = {}
	for i in range(len(content)):
		split_list = content[i].split(",")
		value = split_list[0]
		key = split_list[1]
		route_dict[value] = key

	found = []

	pattern_length = 2
	for key in route_dict:
		print(phone_number[:pattern_length])
		if key.startswith(phone_number[:pattern_length]):
			found.append(key)
			# if found > 1:
			# 	pattern_length += 1
			# calculate_num_cost(phone_number,carrier_route_list)
			# if found == 0:
			# 	pattern_length -= 1
			# 	calculate_num_cost(phone_number, carrier_route_list)
			
		print(found)
	# print(route_dict)
	# print(route_dict)
	# print(content)



def main():
	calculate_num_cost("861875032", "data/route-costs-106000.txt")

if __name__ == "__main__":
    main()