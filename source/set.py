

class Set(object):
	def __init__(self, elements=None):
		#a set is an unordered list, so we initialize a list
		self.set_list = list()
		
		#an empty list has a size of 0
		self.size = 0


		if elements is not None:
			for element in elements:
				#parses through inputted elements and adds them to set
				self.set_list.append(element)
				#every time we add an element, we increment the size
				self.size += 1


	def contains(self, element):
		#will return false if elements not in list
		return element in self.set_list

	def add(self, element):
		#check for duplicated before appending
	    if self.contains(element) is False:
	    	self.set_list.append(element)
	    	#increment the size after adding
	    	self.size += 1

	def remove(self, element):
		#checks if element in list before attempting to delete
	    if set_list.contains(element):
	    	#delete if found
	    	self.delete(element)
	    	#decremenet size by 1
	    	size -= 1
	    else:
	    	raise KeyError("this element is not in this set.")

	def union(self, other_set):
		union_set = Set(self.list)
		#traversing through other set
		for element in other_set.list:
			#check for duplicates
			if not self.contains(element):
				#if not already set add element
				union_set.add(element)
		return union_set

	def intersection(self, other_set):
	    intersection_set = Set(self.list)
	    #traversing through other set
	    for element in other_set.list:
	    	#if the element is already in the list
	    	if self.contains(element):
	    		#add it to new set
	    		intersection_set.add(element)
	    return intersection_set

	def difference(self, other_set):
	    difference_set = Set(self.list)

	   	#traverse through other set
	    for element in other_set.list:
	    	#check if element already in self.list
	    	if self.contains(element):
	    		self.remove(element)
	    	#if not in the list add the element
	    	else:
	    		self.add(element)
	    return difference_set

	def is_subset(other_set):
		#if every element in other set in self.list
		#return True
		if self.contains(other_set.list):
			return True
		return False

	
