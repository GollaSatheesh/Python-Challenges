'''By Copying the set we clone the set without same id of the set'''
Set={10,20,30,40,50,60,70}
print(Set)
print(id(Set))
CopiedSet=Set.copy()
print(CopiedSet)
print(id(CopiedSet))
################################
#OUTPUT
#{50, 20, 70, 40, 10, 60, 30}
#2334818829024                  #The ID Was different
#{50, 20, 70, 40, 10, 60, 30}
#2334819115392                  #The ID was different Comapared to original set