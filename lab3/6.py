def solve(head,legs):
    rabbit = ()
    chicken = ()
    rabbit=(legs-2*head)/2
    chicken=head-rabbit
    print('Rabbits :',rabbit ,'Chickens :',chicken)
    
print('gime me numbers of head and legs ')
x = int(input())
y=int(input())
solve(x,y)