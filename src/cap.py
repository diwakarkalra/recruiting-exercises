"""
Explanation of The Solution
The driver function takes into account the order and the warehouses.

A) Assumptions:

1. Best way to ship order is by using minimum number of warehouses.
2. The quantities can be postitive or zero but never negative.
3. The cost of items/inventory in each warehouse is same.


B) Priority Distribution:
1. Order can be fulfilled by single warehouse.
2. Order can be fullfilled by more than one warehouse but higher priority to path with lesser number of  
      warehouses.
3. If there are more than one path with least number of warehouses, higher priority will be given to the path 
    starting with nearest warehouse.

C) Workflow
1. To check if the order can be completed using one warehouse with the help of "completeOrder" function
2. If not, check if a part of the order can be completed using a warehouse with the help of the "halfOrder" function
3. 'items_found' checks if the current warehouse can help with some items to fulfill the existing order. If yes it is added to path_Exists.
4. path_Exists keeps track if a path is possible with the current warehouse, if yes it is added to All_paths.
5. All_paths keeps a track of differnet ways to deliver the order.
6. smallest_Path returns the best way to fullfill the order based upon Assumptions and Priority Distribution mentioned above. 
"""




"""Function "completeOrder" to check if the current warehouse can fullfill
    the entire order
    @parameter order = order needs to be fulfilled
    @Paremeter warehouse = warehouse in consideration
    Returns Boolean 
"""
def completeOrder(order , warehouse):  
    for item in order.keys():
        if item not in warehouse["inventory"].keys() or warehouse["inventory"][item] < order[item]:
            return False
    return True


""" 
    Function "halfOrder" to check if the current Warehouse can provide some items of the Order
     @parameter remainig_Order = order needs to be fulfilled
     @Paremeter warehouse = warehouse in consideration
     @parameter start = index of current warehouse
     @parameter end = index of the last Warehouse
     Returns the number of items taken from one warehouse to fulfill the order
     Handles the case if Order cannot be shipped because there is not enough inventory
"""
def halfOrder(remainig_Order, warehouse, start, end) :
    order_filled = {}
    for item in remainig_Order.keys():
        if remainig_Order[item] == 0 :
            continue
        else:
            if item in  warehouse["inventory"].keys() : 
                if warehouse["inventory"][item] >= remainig_Order[item]:   
                    order_filled[item] = remainig_Order[item]
                    remainig_Order[item] = 0
                elif warehouse["inventory"][item] < remainig_Order[item] and warehouse["inventory"][item] > 0:
                    order_filled[item] = warehouse["inventory"][item]
                    remainig_Order[item] -= warehouse["inventory"][item]
            if start == end and remainig_Order[item] > 0:
                return [],remainig_Order
    if not order_filled:
        return {} ,remainig_Order
    else:
        return {warehouse["name"] : order_filled} ,remainig_Order 
        


""" Function "smallest_Path" to return the best way to ship order
     @parameter All_paths = Ways to fulfill the order
     Returns the path with least number of warehouses
"""
import math
def smallest_Path(All_paths):
    minimum_length = math.inf
    index = 0
    for i,path in enumerate(All_paths):
        if len(path) < minimum_length:
            minimum_length = len(path)
            index = i
    return All_paths[index]


""" Driver Function - inventory_Allocator
    @Parame order = Order to be completed
    @Warehouses = Set of all all warehouse available to satisfy the order
    Returns a path if order can be fulfilled
"""
def inventory_Allocator(order={}, warehouses=[]):
    if not order or type(order) != dict:
        return ("Invalid Order")
    
    if not warehouses or type(warehouses) != list:
        return [] 
    
    All_paths = []
    Original_order = order.copy()
    break_condition = False
    
    for index in range(len(warehouses)) : #Checks all warehouses starting from the nearest 
        if completeOrder(Original_order , warehouses[index]) : 
                return [{warehouses[index]["name"] : Original_order}]
        path_Exists = []
        order_ = order.copy()  #Preserving the state to compute differenet Paths
        
        for sub_index in range( index , len(warehouses)): #checks if we can complete orders using multiple warehouses
            
            for i in range(sub_index+1, len(warehouses)): #checks if at any instant remaing order can be completely 
                                                    # filled by a single warehouse amongst the remaining warehouses
                if completeOrder(order_ , warehouses[i]) :   
                    path_Exists.append({warehouses[i]["name"] : order_})
                    break_condition = True  # Since this is already the best path using current Warehouse[sub_index]
                    break                    # We need not to check any further
                else:
                    continue
                    
            if break_condition == True:
                break_condition = False
                break
                
            items_found , order_ = halfOrder(order_,warehouses[sub_index],sub_index, len(warehouses) -1) 
            
            if items_found == []:
                if not All_paths and sub_index == len(warehouses) -1:
                    return []  #if we have checked all warehouses and we cannot fulfill order
                else:
                    path_Exists = [] #if we cannot fulfill order just using the current warehouse, flush curr_path
                    break
            elif items_found:
                path_Exists.append(items_found)
                        
        if path_Exists and  path_Exists not in All_paths:
            All_paths.append(path_Exists)
            path_Exists = []
    #print(All_paths)
    return smallest_Path(All_paths)