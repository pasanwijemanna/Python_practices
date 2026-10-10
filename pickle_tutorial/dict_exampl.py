import pickle 

# pickling

# data = {
#     "Name":"pasan",
#     "age" :25
# } 
# filename = "dict.pickle"

# with open (filename,"wb") as f:
#     pickle.dump(data,f)

#unpickling

with open('dict.pickle','rb') as x :
    print(pickle.load(x))
    
    
    