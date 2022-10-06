# Implement the main simmulation class
from multiprocessing.dummy import Array
from array import Array
from Pybook.llistqueue import Queue
from simpeople import TicketAgent, Passenger

class TicketCounterSimulation:
    # Create a simulation object
    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        # Parameters sublied by the user
        self._arriveProb = 1.0/betweenTime
        self._serviceTime = serviceTime
        self._numMinuties = numMinutes

        # Simulation Components
        self._passengerQ = Queue()
        self._theAgents = Array(numAgents)
        for i in range(numAgents):
            self._theAgents[i] = TicketAgent[i+1]
        
        # Computed during the simulation
        self._totalWaiteTime = 0
        self._numPassengers = 0
    
    # Run the simulation using parameters supplied earlier
    def run(self):
        for curTime in range(self._numMinuties + 1):
            self._handleArrival(curTime)
            self._handleBeginService(curTime)
            self._handleEndService(curTime)

    # Print the simulation results
    def printResults(self):
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float(self._totalWaiteTime) / numServed
        print("")
        print( "Number of passengers served = ", numServed )
        print( "Number of passengers remaining in line = %d" %len(self._passengerQ) )
        print( "The average wait time was %4.2f minutes." % avgWait )
    
    # The remaining methods that have yet to be implemented.
    # def _handleArrive( curTime ): # Handles simulation rule #1.
    # def _handleBeginService( curTime ): # Handles simulation rule #2.
    # def _handleEndService( curTime ): # Handles simulation rule #3.
