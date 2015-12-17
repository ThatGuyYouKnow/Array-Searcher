existingCustomers=[]
newCustomers = []
with open('C:/existing_customers.txt','r') as f:
	for line in f:
		existingCustomers.append(line)
f.closed

with open('C:/new_customers.txt','r') as f:
	for line in f:
		newCustomers.append(line)
f.closed

f = open('C:/return_file.txt','w+')
for cusNum in newCustomers:
	if cusNum not in existingCustomers:
		f.write(cusNum)
f.close()
