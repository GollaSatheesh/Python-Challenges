'''We cant directly modify elements in Tuple , we can modify elements in by converting 
tuple into list '''
m=("anantapur","tirupati","Puttur","Kalyandurg","bangalore")
ConvertedToList=list(m)
ConvertedToList.append("Mobile")
print(ConvertedToList)
ConvertedToList.remove("anantapur")
print(ConvertedToList)