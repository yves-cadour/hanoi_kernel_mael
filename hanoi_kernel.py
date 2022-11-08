from stack import Stack

class Hanoi:
    """
    a class to implement the hanoi tower game
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
        
        :param src: the source of the move, the tower you will move plate from
        :type src: int
        :param dest: the destination of the move, the tower you will move the plate into
        :type dest: int
        
        :return: return different things in different situation, if its a success, will return a 0, the source and the destination
            if the game as ended, will return 1, the source and the destination
            if it's an impossible move (a bigger plate a top a smaller one) will return 2 and two time the source
            if the source is the same as the destination will return 3 and two time the soruce
            if the source is empty will return 4
            if the soruce or the destination is invalid will return 5
            will return 6, the source and the destination if the game is a win but not optimal
        :rtype: tuple

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
        if mapping[3].size()==self._size: #cas 1 ou 6
            self._history.append((src, dest))
            if len(self.get_history())==(2**self.get_n())-1:
                return (1, (src, dest))
            else:
                return (1, (src, dest))
        self._history.append((src, dest))
        return (0, (src, dest)) #cas 0
        
        
        

    def get_history(self):
        """
        show all the move that happend in the game
        return a list
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
        """
        get the initial pile
        """
        return self._size
        

    def solve_hanoi(self):
        """
        will solve the hanoi tower with recursivity
        """
        if len(self.show()[0])!=self.get_n():
            return "impossible: to be solved the first tower must be full"
        n=self.get_n()
        
        def _recur_solve(self, n, src, auxi, dest):
            if n==1: # cas d'arret
                self.move(src, dest)
            else:
                #print(self.show())
                _recur_solve(self, n-1, src, dest, auxi)
                
                self.move(src, dest)
                _recur_solve(self, n-1, auxi, src, dest)
                #print(self.show())
        #call of the recursive function
        _recur_solve(self,n,1,2,3)
        return self
a=Hanoi(3)
a.move(1,2)
fin=a.solve_hanoi()
# 
# move the plate from source to destination
#         {1, 2, 3}
#         dest: integer {1, 2, 3}, must be diffenrent from src
#         return a tuple:
#         -first element is the status
#         -second element is the move (a tuple)
#         status:
#         - 0 success, (src, dest)
#         - 1: game over, (src, dest)
#         - 2: impossible move (src, src)
#         - 3: src=dest, (src, src) 
#         - 4: empty stack ()
#         - 5: invalid value
#         - 6: game over but not optimal, (src, dest)