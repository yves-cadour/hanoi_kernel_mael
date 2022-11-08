from stack import Stack

class Hanoi:
    """
    a calss to implement the hanoi tower game
    """
    
    def __init__(self, n):
        self._size=n
        self._tower1=Stack()
        self._tower2=Stack()
        self._tower3=Stack()
        self._create()
        self._history=[]
        
        
    def move(self, src, dest):
        """
        move the plate from source to destination
        src: integer {1, 2, 3}
        dest: integer {1, 2, 3}, must be diffenrent from src
        return a tuple:
        -first element is the status
        -second element is the move (a tuple)
        status:
        - 0 success, (src, dest)
        - 1: game over, (src, dest)
        - 2: impossible move (src, src)
        - 3: src=dest, (src, src) 
        - 4: empty stack ()
        - 5: invalid value

        """
        if src not in (1, 2, 3) or dest not in (1, 2, 3): #cas 5
            return (5, ())
        mapping={1:self._tower1, 2:self._tower2, 3:self._tower3}
        sourc=mapping[src]
        desti=mapping[dest]
        if sourc.isEmpty(): #cas 4
            return (4, ())
        if desti.isEmpty()==False and desti.summit()<sourc.summit(): #cas 2
            return (2,( src, src))
        if sourc==desti: #cas 3
            return (3, (src, src))

        desti.push(sourc.pop())
        if mapping[3].size()==self._size: #cas 1
            self._history.append((src, dest))
            return (1, (src, dest))
        self._history.append((src, dest))
        return (0, (src, dest)) #cas 0
        
        
        

    def get_history(self):
        """
        a function that return all the move that happend in the game in a list
        """
        return self._history
    
        
    def show (self):
        """
        show what's on the three tower
        return a tuple of three tuples
        exemple: ( (2,3), (), (1) )
        """
        return (self._tower1.show(), self._tower2.show(), self._tower3.show())
    
    def _create(self):
        # TODO: check that n is in {3:10}
        for i in range(self._size, 0, -1):
            self._tower1.push(i)
                     
            
    def get_n(self):
        return self._size
        

a=Hanoi(6)
        
        