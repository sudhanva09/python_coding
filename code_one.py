#This code basically contains addition of all the numbers after a selected number to the end of the list
#Or else from the start of the list to the selected number
#If the number selected is even then the algorithm will add after the selected number to the end of the list
#If the number selected is an odd number the algorithm will add from the starting of the list to the selected number
#Two different lists for the sums are created depending upon even or odd numbers
#A predefined list is given
#A list from the user can also be taken as an input to make the algorithm 


l=[1,2,3,3,2,2,1]                                                                  #given list
sum=0
newlisteven=[]                                                                     #list for even numbers
newlistodd=[]                                                                      #list for odd numbers

selectedno=int(input("select the no in the list after which you want the nos to be added\n"))


if(l[selectedno-1]%2==0):                                                          #Code if the number from the list is even
    for i in range(selectedno,len(l)):
        sum+=l[i]
        newlisteven.append(sum)

if(l[selectedno-1]%2!=0):                                                          #Code if the number fromthe list is odd
    for i in range(0,selectedno-1):
        sum += l[i]
        newlistodd.append(sum)

print(sum)



