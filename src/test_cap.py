import unittest
import cap

class TestCap(unittest.TestCase):


	#if Order and Warehouse are empty
	def test_case_one(self):
		result = cap.inventory_Allocator()
		self.assertEqual(result,"Invalid Order")


	#if Order is blank
	def test_case_two(self):
		order = ""
		warehouses = {"name" : "aaa" , "inventory" : {"apple" : 1 } }
		result = cap.inventory_Allocator(order,warehouses)
		self.assertEqual(result,"Invalid Order")

	#if Warehouses section is blank
	def test_case_three(self):
		order = { "apple" : 2}
		warehouses = ""
		result = cap.inventory_Allocator(order,warehouses)
		self.assertEqual(result,[])	

	#Sample Test Case - 1
	def test_case_four(self):
		order = { "apple" : 1}
		warehouses = [{ "name": "owd", "inventory": { "apple": 1 }} ]
		result = cap.inventory_Allocator(order,warehouses)
		self.assertEqual(result,[{'owd': {'apple': 1}}])

	#Sample Test Case - 2
	def test_case_five(self):
		order = { "apple" : 1}
		warehouses = [{ "name": "owd", "inventory": { "apple": 0 }} ]
		result = cap.inventory_Allocator(order,warehouses)
		self.assertEqual(result,[])

	#Sample Test Case - 3
	def test_case_six(self):
		order = { "apple" : 10 }
		warehouses =[{ "name": "owd", "inventory": { "apple": 5 }} , 
                     { "name": "dm", "inventory": { "apple": 5 } }]
		result = cap.inventory_Allocator(order,warehouses)
		self.assertEqual(result,[{'owd': {'apple': 5}}, {'dm': {'apple': 5}}])

	#To check that Higer Priority is given to Shipment from single warehouse
	def test_case_seven(self):
		order = {"apple" : 1 , "orange" : 1}
		warehouses = [{"name" : "aaa" , "inventory" : {"apple" : 1 } } ,
                        {"name" : "bbb" , "inventory" : {"orange" : 1 } } ,
                        {"name" : "ccc" , "inventory" : {"apple" : 1,"orange" : 1}}]
		result = cap.inventory_Allocator(order,warehouses)
		self.assertEqual(result,[{'ccc': {'apple': 1, 'orange': 1}}])

#To check if there are multiple ways to ship the order using same number of
#warehouses,we get the result of combination starting from the nearest warehouse¶
	def test_case_eight(self):
		order = {"apple" : 3 , "orange" : 2}
		warehouses = [{"name" : "aaa" , "inventory" : {"apple" : 1 } } , 
                      {"name" : "bbb" , "inventory" : {"apple" : 1 ,"orange" : 1}},
                      {"name" : "ccc" , "inventory" : {"apple" : 1 ,"orange" : 1}},
                      {"name" : "ddd" , "inventory" : {"apple" : 2 ,"orange" : 1}},
                      {"name" : "eee" , "inventory" : {"apple" : 1 ,"orange" : 1}}]
		result = cap.inventory_Allocator(order,warehouses)
		self.assertEqual(result,[{'bbb': {'apple': 1, 'orange': 1}}, {'ddd': {'apple': 2, 'orange': 1}}])

	# If the datatype of an order is incorrect
	def test_case_nine(self):
		order = [{"apple":3}]
		warehouses = [{ "name": "owd", "inventory": { "apple": 1 }} ]
		result = cap.inventory_Allocator(order,warehouses)
		self.assertEqual(result,"Invalid Order")

	# If Inventory contains items in lesser amount
	def test_case_ten(self):
		order = { "apple" : 2}
		warehouses = [{ "name": "owd", "inventory": { "apple": 1 }} ]
		result = cap.inventory_Allocator(order,warehouses)
		self.assertEqual(result,[])

	# Additinal Test Runs
	def test_case_eleven(self):
		order = {"apple" : 3 , "orange" : 1}
		warehouses = [{"name" : "aaa" , "inventory" : {"apple" : 1 } } , 
                      {"name" : "bbb" , "inventory" : {"banana" : 1,"apple" : 1}},
                      {"name" : "ccc" , "inventory" : {"orange" : 3 } } ,
                      {"name" : "ddd" , "inventory" : {"apple" : 2,"orange" : 3 } }]
		result = cap.inventory_Allocator(order,warehouses)
		self.assertEqual(result,[{'aaa': {'apple': 1}}, {'ddd': {'apple': 2, 'orange': 1}}])

	def test_case_twelve(self):
		order ={"apple" : 1 , "orange" : 1}
		warehouses = [{"name" : "aaa" , "inventory" : {"apple" : 1 } } , 
                      {"name" : "bbb" , "inventory" : {"orange" : 1 } } ,
                      {"name" : "ccc" , "inventory" : {"orange" : 1}}]
		result = cap.inventory_Allocator(order,warehouses)
		self.assertEqual(result,[{'aaa': {'apple': 1}}, {'bbb': {'orange': 1}}])

	def test_case_thirteen(self):
		order = { "apple" : 1 , "orange" : 1 }
		warehouses =[{ "name": "owd", "inventory": { "apple": 0 }} , 
                     { "name": "abc", "inventory": { "orange": 1 } }]
		result = cap.inventory_Allocator(order,warehouses)
		self.assertEqual(result,[])

	def test_case_fourteen(self):
		order = { "apple" : 5 , "banana" : 5 }
		warehouses = [{ "name": "aaa", "inventory": { "orange": 5, "apple" : 1 }} ,
                      { "name": "bbb", "inventory": { "orange": 3 } },
                      { "name": "ccc", "inventory": { "orange": 3, "banana" : 3 } },
                      { "name": "ddd", "inventory": { "apple": 4, "banana": 2 } },
                      { "name": "abc", "inventory": { "orange": 3 } }]
		result = cap.inventory_Allocator(order,warehouses)
		self.assertEqual(result,[{'aaa': {'apple': 1}}, {'ccc': {'banana': 3}}, {'ddd': {'apple': 4, 'banana': 2}}])





if __name__=='__main__':
	unittest.main()

