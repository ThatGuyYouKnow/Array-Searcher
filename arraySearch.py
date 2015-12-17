existingCustomers=[]
newCustomers = []
returnArray = []
with open('C:/existing_customers.txt','r') as f:
	for line in f:
		existingCustomers.append(line)
f.closed

with open('C:/new_customers.txt','r') as f:
	for line in f:
		newCustomers.append(line)
f.closed

for cusNum in newCustomers:
	if cusNum not in existingCustomers:
		returnArray.append(cusNum)
		
print (returnArray)
