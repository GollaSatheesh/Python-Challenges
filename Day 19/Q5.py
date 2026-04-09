#Keyword Varible Lenth arguments
def DefaulVaribleArguments(*Values):
    print(sum(Values))

DefaulVaribleArguments(10,20,20,20,20,20,20,20,20)#we can pass any numbers of actual parameters
print("####################################################")
#Non-Keyword Variable length argunets
def NonKeywordVl(**Info):
    print(Info)

NonKeywordVl(Name="Satheesh",Village="Avulenna")
NonKeywordVl()
