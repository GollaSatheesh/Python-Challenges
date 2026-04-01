'''The difference between removing an element and discarding an element in a set is while 
removing an element in a set which element is not the set , it raises an error , when discarding the 
element which is not in the set it doesnt show error '''
ExampleSet={10,20,30,40,50,60,70}
ExampleSet.remove(99) #It raises an error ,99 is not in the set
print(ExampleSet)
ExampleSet.discard(99)#It wont raise error , when 99 is also not there
print(ExampleSet)
