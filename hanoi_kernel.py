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
        
        
    def move(self, src, dest):
        """
        move the plate from source to destination
        src: integer {1, 2, 3}
        dest: integer {1, 2, 3}, must be diffenrent from src
        return something i guess?
        """
        mapping={1:self._tower1, 2:self._tower2, 3:self._tower3}
        plateau_souhait=mapping[dest].summit()
        if plateau_souhait!=0:
            if mapping[dest].summit()<plateau_souhait:
                plateau=mapping[src].pop()
                mapping[dest].push(plateau)
            else:
                return "impossible there is already a smaller disk in the destination"
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
        
        