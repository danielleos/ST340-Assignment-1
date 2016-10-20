def merge(a1,a2):
	outArr = [] #initialise the output array
	outLen = len(a1) + len(a2) #set length of output array
	a1small = False #initialise a flag
	if (len(a1) <= len(a2)): #check which array has the fewest elements
		a1small = True #if a1 is the smallest array, set the flag to true

	for k in range(outLen): #start a loop that iterates a maximum of outLen times
		if (len(a1) != 0) & (len(a2) != 0): #check the lengths of the arrays are not 0
			if (a1[0] <= a2[0]): #compare the first elements of each array
				outArr.append(a1[0]) #add element to output array
				a1.remove(a1[0]) #remove that element from its original array
				#print("Element from a1 added: " + str(outArr))
			elif (a2[0] < a1[0]):
				outArr.append(a2[0])
				a2.remove(a2[0])
				#print("Element from a2 added: " + str(outArr))
		else: #check if either of the arrays are of length 0
			break #break out of loop

	if (a1small == True): #if a1 is the smallest array
		outArr.extend(a2) #add the rest of a2 to the output array
		#print("List a2 had elements leftover.")
	else: #otherwise if a2 is the smallest array
		outArr.extend(a1) #add the rest of a1 to the output array
		#print("List a1 had elements leftover.")
	
	return(outArr) #return complete array
