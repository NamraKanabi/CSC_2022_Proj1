from SampleStructures import Stack
import random

#defining class Card
class Card:
    def __init__(self,num_color,depth):
        """
        class Card: accepts num_color(int) and depth(int) to create target for player 
                    and perform several functions with it
        Parameters: num_color(int), depth(int)
        Return: None
        """
        self.__num_color=num_color
        self.__depth=depth
        size=num_color*depth
        colours=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.__beads=[]
        
        for color in range(num_color):
            for rep in range(depth):
                self.__beads.append(colours[color])
        
    def reset(self): #defining function reset
        """
        function reset: rearranges the card (self.__beads)
        Parameters: None
        Return: None
        """
        random.shuffle(self.__beads)
    
    def show(self): #defining function show
        """
        function show: displays the card(self.__beads) in a format
        Parameters: None
        Return: None
        """
        shown=False
        counter=0
        reps=1
        while not shown:
            if counter>len(self.__beads)-1:
                if counter!=len(self.__beads)-1:
                    print("|",end="")
                    print("")
                    counter=reps
                    reps+=1
            else:
                if counter==reps-1:
                    print("|",end="")
                
                if not shown:
                    if (counter+self.__depth)>len(self.__beads)-1:
                        print(self.__beads[counter],end="")
                    else:
                        print(self.__beads[counter],end=" ")
                
                if counter==len(self.__beads)-1:
                    print("|",end="")
                    shown=True
                
                counter=counter+self.__depth
    
    def stack(self,number): #defining function stack
        """
        function stack: returns specified stack from card (self.__beads)
        Parameters: number(int)
        Return: stack(list)
        """
        if number>self.__num_color:
            raise Exception("Entered number out of Index")
        found=False
        reps=0
        n=0
        
        while not found:
            if reps==number:
                found=True
            else:
                stack=[]
                reps+=1
                for x in range(n,n+self.__depth):
                    stack.append(self.__beads[x])
                    
                n=n+self.__depth
            
        return stack
    
    def __str__(self): #defining function __str__
        """
        function __str__: returns string of card(self.__beads)
        Parameters: None
        Return: string(string)
        """
        string=""
        string+="|"
        for x in range(0,len(self.__beads)):
            if x>0 and x%self.__depth==0:
                string+="||"
            string+=str(self.__beads[x])
        string+="|"
        return string
    
    def replace(self,filename,n): #defining replace
        """
        function replace: replaces card(self.__beads) with card from specified text file
        Parameters: filename(string), n(int)
        Return: None
        """
        opener=open(filename,"r")
        reader=opener.read()
        splitted=reader.splitlines()
        opener.close()
        
        temp=splitted[n]
        temp=temp.upper()
        
        self.__beads=[]
        for x in temp:
            self.__beads.append(x)
        
        return self.__beads

#defining class Bstack    
class BStack:
    def __init__(self,capacity):
        """
        class Bstack: accepts capacity(int) and creats a bounded stack according to it
        Parameters: capacity(int)
        Returns: None
        """
        assert isinstance(capacity, int), ('Error: Type error: %s' % (type(capacity))) # throws an assertion error on not true
        assert capacity >= 0, ('Error: Illegal capacity: %d' % (capacity))        
        self.__items = []
        self.__capacity=capacity
    
    def push(self, item): #defining function push
        """
        function push: adds item on top of stack
        Parameters: item
        Returns: None
        """
        if len(self.__items)==self.__capacity:
            raise Exception("Error:Bstack is at max capacity")
        else:
            self.__items.append(item)
    
    def pop(self): #defining function pop
        """
        function pop: removes and returns item on top of stack
        Parameters: None
        Returns: item on top of stack
        """
        if len(self.__items)==0:
            raise Exception("Error:Bstack is empty")
        else:
            return self.__items.pop()
    
    def peek(self): #defining function peek
        """
        function peek: returns item on top of stack
        Parameters: None
        Returns: item on top of stack
        """
        if len(self.__items)==0:
            raise Exception("Error:Bstack is empty")
        else:
            return self.__items[len(self.__items)-1]      
    
    def isEmpty(self): #defining function isEmpty
        """
        function isEmpty: checks if stack is empty
        Parameters: None
        Returns: Boolean 
        """
        return self.__items == []
    
    def isFull(self): #defining function isFull
        """
        function isFull: check if stack is full
        Parameters: None
        Returns: Boolean
        """
        return len(self.__items)==self.__capacity
    
    def size(self): #defining function size
        """
        function size: returns size of stack
        Parameters: None
        Returns: size of stack(Boolean)
        """
        return len(self.__items)
    
    def show(self): #defining function show
        """
        function show: returns stack
        Parameters: None
        Returns: self.__items(list)
        """
        print(self.__items)
    
    def __str__(self): #defining function __str__
        """
        function __str__: returns string of stack
        Parameters: None
        Returns: stackAsString(string)
        """
        stackAsString = ''
        for item in self.__items:
            stackAsString += item + ' '
        return stackAsString
    
    def clear(self): #defining function clear
        """
        function clear: clears the stack
        Parameters: None
        Returns: None
        """
        if len(self.__items)==0:
            pass
        else:
            self.__items.clear()
    
    def IgnorePop(self): #defining function IgnorePop
        """
        function IgnorePop: returns item on pop of the stack while ignoring all "." in the stack
        Parameters: None
        Returns: item
        """
        if len(self.__items)==0:
            raise Exception("Error:Bstack is empty")
        x=len(self.__items)-1
        item="."
        empty=True
        while item=="." and x>=0:
            item=self.__items[x]
            if item!=".":
                empty=False
            x-=1
        if empty:
            raise Exception("Error:Bstack is empty")
        else:
            self.__items.pop(x+1)
            return item
    
    def IgnorePush(self,item): #defining function IgnorePush
        """
        function IgnorePush: adds item on top the item while ignoring "." in the stack
        Parameters: item
        Returns: None
        """
        if not "." in self.__items:
            raise Exception("Error:Bstack is full")
        else:
            x=self.__items.index(".")
            self.__items[x]=item
    
    def IgnoreFull(self): #defining function IgnoreFull
        """
        function IgnoreFull: checks if stack is full while ignoring "." in the stack
        Parameters: None
        Returns: isFull(boolean)
        """
        isFull=False
        if not "." in self.__items:
            isFull=True
        return isFull
    
    def Give(self): #defining function Give
        """
        function Give: returns stack with top to bottom order
        Parameters: None
        Returns: temp(list)
        """
        temp=[]
        for x in reversed(self.__items):
            temp.append(x)
        return temp
    
    def Capacity(self): #defining function Capacity
        """
        function Capacity: returns capacity of stack
        Parameters: None
        Returns: self__capacity(int)
        """
        return self.__capacity

#defining class AbacoStack
class AbacoStack:
    def __init__(self,num,depth):
        """
        class AbacoStack: accepts num(int) and depth(int) to create a card and perform functions on it
        Parameters: num(int) and depth(int)
        Returns: None
        """
        self.__top=["."]*(num+2)
        self.__lister=[]
        self.__moves=0
        self.__colours=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        for x in range(num):
            self.__lister.append(BStack(depth))
            for y in range(depth):
                self.__lister[x].push(self.__colours[x])
    
    def moveBead(self,move): #defining function moveBead
        """
        function moveBead: accepts move(string) and moves the bead according to parameter
        Parameters: move(string)
        Returns: None
        """
        assert isinstance(move, str), ('Error: Type error: %s' % (type(move)))
        if len(move)>2:
            raise Exception("Error: invalid move")
        elif (not move[0].isdigit()) or (not move[1].isalpha()):
            raise Exception("Error: invalid move")
        elif int(move[0])>len(self.__top)-1:
            raise Exception("Error: invalid move")
        elif move[1] not in ["r","l","u","d"]:
            raise Exception("Error: invalid move")
        else:
            if move[0]=="0":
                if move[1]=="l" or self.__top[0]=="." or self.__top[1]!=".":
                    raise Exception("Error: invalid move")
                else:
                    temp=self.__top[0]
                    self.__top[1]=temp
                    self.__top[0]="."
                    self.__moves+=1
                    
            elif int(move[0])==len(self.__top)-1:
                if move[1]=="r" or self.__top[len(self.__top)-1]=="." or self.__top[len(self.__top)-2]!=".":
                    raise Exception("Error: invalid move")
                else:
                    temp=self.__top[len(self.__top)-1]
                    self.__top[len(self.__top)-2]=temp
                    self.__top[len(self.__top)-1]="."
                    self.__moves+=1
            else:
                if move[1]=="u":
                    if self.__lister[int(move[0])-1].isEmpty() or self.__top[int(move[0])]!=".":
                        raise Exception("Error: invalid move")
                    else:
                        temp=self.__lister[int(move[0])-1].IgnorePop()
                        self.__top[int(move[0])]=temp
                        self.__lister[int(move[0])-1].push(".")
                        self.__moves+=1
                        
                if move[1]=="d":
                    if self.__lister[int(move[0])-1].IgnoreFull() or self.__top[int(move[0])]==".":
                        raise Exception("Exception: invalid move")
                    else:
                        temp=self.__top[int(move[0])]
                        self.__lister[int(move[0])-1].IgnorePush(temp)
                        self.__top[int(move[0])]="."
                        self.__moves+=1
                        
                if move[1]=="r":
                    if self.__top[int(move[0])]=="." or self.__top[int(move[0])+1]!=".":
                        raise Exception("Exception: invalid move")
                    else:
                        temp=self.__top[int(move[0])]
                        self.__top[int(move[0])+1]=temp
                        self.__top[int(move[0])]="."
                        self.__moves+=1
                
                if move[1]=="l":
                    if self.__top[int(move[0])]=="." or self.__top[int(move[0])-1]!=".":
                        raise Exception("Exception: invalid move")
                    else:
                        temp=self.__top[int(move[0])]
                        self.__top[int(move[0])-1]=temp
                        self.__top[int(move[0])]="."
                        self.__moves+=1 
    
    def show(self,card=None): #defining function show
        """
        function show: displays the card in a format
        Parameters: card(optional)
        Returns: None
        """
        for x in range(len(self.__top)):
            print(x,end=" ")
        print("")
        for x in self.__top:
            print(x,end=" ")
        main_list=[]
        for stack in self.__lister:
            temp=stack.Give()
            main_list=main_list+temp
            
        if card==None:
            print("")
            shown=False
            counter=0
            reps=1
            while not shown:
                if counter>len(main_list)-1:
                    if counter!=len(main_list)-1:
                        print("|",end=" ")
                        print("")
                        counter=reps
                        reps+=1
                else:
                    if counter==reps-1:
                        print("|",end=" ")
                                    
                    print(main_list[counter],end=" ")
                                    
                    if counter==len(main_list)-1:
                        print("|",end=" ")
                        shown=True
                        print("")
                                    
                    counter=counter+self.__lister[0].size() 
        else:
            card_list=[]
            for x in range(1,len(self.__lister)+1):
                card_list=card_list+card.stack(x)
            
            print("       card")
            shown=False
            counter=0
            counter2=0
            reps=1
            reps2=0
            reset=1
            while not shown:
                done=False
                if counter>len(main_list)-1:
                    if counter!=len(main_list)-1:
                        print("|",end=" ")
                        print("     | ",end="")
                        while not done:
                            if reps2==len(self.__lister):
                                reps2=0
                                counter2=reset
                                reset+=1
                                done=True
                            else:
                                print(card_list[counter2],end=" ")
                                counter2+=self.__lister[0].size() 
                                reps2+=1
                        
                        print("|")
                        counter=reps
                        reps+=1
                else:
                    if counter==reps-1:
                        print("|",end=" ")
                                    
                    print(main_list[counter],end=" ")
                                    
                    if counter==len(main_list)-1:
                        print("|",end=" ")
                        print("     | ",end="")
                        while not done:
                            if reps2==len(self.__lister):
                                done=True
                            else:
                                print(card_list[counter2],end=" ")
                                counter2+=self.__lister[0].size()
                                reps2+=1
                        shown=True
                        print("|")
                                    
                    counter=counter+self.__lister[0].size()
        print("+ "+"- "*len(self.__lister)+"+     "+str(self.__moves)+" moves")
        
    def reset(self): #defining function reset
        """
        function reset: resets card(self.__lister), moves(int) , top(list) to original state
        Parameters: None
        Returns: None
        """
        for x in self.__lister:
            for y in range(x.size()):
                x.pop()
                
        for x in range(len(self.__lister)):
            for y in range(self.__lister[x].Capacity()):
                self.__lister[x].push(self.__colours[x])
                
        self.__top=["."]*(len(self.__lister)+2)
        self.__moves=0
    
    def isSolved(self,card): #defining function isSolved
        """
        function isSolved: checks whether user's card matches target card
        Parameters: card
        Returns: Solved(boolean)
        """
        Solved=True
        main_list=[]
        card_list=[]
        for stack in self.__lister:
            temp=stack.Give()
            main_list=main_list+temp
            
        for x in range(1,len(self.__lister)+1):
            card_list=card_list+card.stack(x)
            
        for x in range(len(main_list)):
            if main_list[x]!=card_list[x]:
                Solved=False
        return Solved

def test_Card(): #testing Card class
    card= Card(3,3)
    card.show()
    print(card.stack(3))

def test_BStack(): #testing Bstack class
    stack= BStack(5)
    for x in range(5):
        stack.push(x)
    stack.show()
    print(stack.isFull())
    stack.pop()
    print(stack.isFull())
    print(stack.isEmpty())
    for x in range(4):
        stack.pop()
    print(stack.isEmpty())
    for x in range(3):
        stack.push(x)
    for x in range(2):
        stack.push(".")
    stack.show()
    print(stack.IgnorePop())
    stack.show()
    stack.push(".")
    stack.show()
    print(stack.IgnorePop())
    print(stack.IgnorePop())
    stack.clear()
    for x in range(3):
        stack.push(x)
    for x in range(2):
        stack.push(".")
    stack.show()
    stack.IgnorePush(3)
    stack.IgnorePush(4)
    stack.show()
    print(stack.IgnoreFull())
    print(stack.Give())
    stack.pop()
    stack.pop()
    stack.push(".")
    print(stack.Give())

def test_AbacoStack(): #testing AbacoStack class
    test=AbacoStack(3,3)
    card=Card(3,3)
    card.replace("test.txt",1)
    test.show()
    running=True
    while running:
        try:
            print("")
            m=input("test it")
            test.moveBead(m)
        except Exception:
            print("error detected")
            test.show(card)
            if m=="tt":
                running=False            
        else:
            test.show(card)
            
    print(test.isSolved(card))

if __name__=="__main__": #testing in isolation
    test_Card()
    test_BStack()
    test_AbacoStack()  