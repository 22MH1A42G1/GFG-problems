# insert into dictionary
def insert_dict(query, dict):
    
    # Your code here
    dict.update({query[1]:query[2]})
    

# deleting from dictionary
def del_dict(query, dict):
    
    # Your code here
    if query[1] in dict.keys():
        del dict[query[1]]
    
    
    

# print marks of required name
def print_dict(key, dict):
    
    # Your code here
    if key in dict.keys():
        print("Marks of %s is %s" %(key,dict[key]))
    else:
        return False
    
    