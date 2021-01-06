f1data = f2data = f3data = "" 
 
#with open('/home/soumya/Documents/covid19india/raw_data_integration.json') as f1: 
#  f1data = f1.read() 
with open('/home/soumya/Documents/covid19india/raw_data1.json') as f1: 
  f1data = f1.read() 
with open('/home/soumya/Documents/covid19india/raw_data2.json') as f2: 
  f2data = f2.read() 
with open('/home/soumya/Documents/covid19india/raw_data3.json') as f3: 
  f3data = f3.read() 
 
#f1data += "\n"
#f1data += f3data

result1 = f1data+f2data+f3data

#with open ('/home/soumya/Documents/covid19india/raw_data_integration.json', 'a') as f3: 
#	f3.write(f1data)

with open ('/home/soumya/Documents/covid19india/raw_data_integration.json', 'a') as result: 
  result.write(result1)