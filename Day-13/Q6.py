'''Using update method we can update elements , where we elements can be iterable like list,tuple'''
Set=set()
List=[1,2,3,4,5]#List is a varibale not list function
Tuple=("Satheesh","Karthik","Akruthi")#Here also
Set.update(List,Tuple)#Parameters directly updating to the Set elements from "Tuple","List"
print(Set)