import random
import sys


def randomizer(map):
    cities = list(range(len(map)))
    route = []

    for i in range(len(map)):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        route.append(randomCity)
        cities.remove(randomCity)
    
    return route

def routeDistance(map, route):
    distance = 0
    for i in range(len(route)):
        distance += map[route[i - 1]][route[i]]
    return distance

def neighboursList(route):
    neighbours = []
    for i in range(len(route)):
        for j in range (i + 1, len(route)):
            neighbour = route.copy()
            neighbour[i] = route[j]
            neighbour[j] = route[i]
            neighbours.append(neighbour)
    return neighbours
    
def bestNeighbourFunc(map, neighbours):
    bestDistance: int = routeDistance(map, neighbours[0])
    bestNeighbour = neighbours[0]
    for neighbour in neighbours:
        currentDistance: int = routeDistance(map, neighbour)
        if currentDistance < bestDistance:
            bestDistance = currentDistance
            bestNeighbour = neighbour
        
    return bestNeighbour, bestDistance


def hillClimbing(map):
    currentSolution = randomizer(map)
    currentRouteLength = routeDistance(map, currentSolution)
    neighbours = neighboursList(currentSolution)
    bestNeighbour, bestNeighbourRouteLength = bestNeighbourFunc(map, neighbours)

    while bestNeighbourRouteLength < currentRouteLength:
        currentSolution = bestNeighbour
        currentRouteLength = bestNeighbourRouteLength
        neighbours = neighboursList(currentSolution)
        bestNeighbour, bestNeighbourRouteLength = bestNeighbourFunc(map, neighbours)

    return currentSolution, currentRouteLength

def main():
    cities = ['c1', 'c2', 'c3', 'c4', 'c5','c6', 'c7', 'c8', 'c9', 'c10' ]
    map = [ [0,30, 84, 56, sys.maxsize, sys.maxsize, sys.maxsize, 75, sys.maxsize, 80,],
        [30,0, 65, sys.maxsize, sys.maxsize, sys.maxsize, 70, sys.maxsize, sys.maxsize, 40],
        [84, 65, 0, 74,52,55,sys.maxsize,60,143,48],
        [56,sys.maxsize,74,0,135,sys.maxsize,sys.maxsize,20,sys.maxsize,sys.maxsize],
        [sys.maxsize,sys.maxsize,52,135,0,70,sys.maxsize,122,98,80],
        [70,sys.maxsize,55,sys.maxsize,70,0,63,sys.maxsize,82,35],
        [sys.maxsize,70,sys.maxsize,sys.maxsize,sys.maxsize,63,0,sys.maxsize,120,57],
        [75, sys.maxsize,135,20,122,sys.maxsize,sys.maxsize,0,sys.maxsize,sys.maxsize],
        [sys.maxsize,sys.maxsize,143,sys.maxsize,98,82,120,sys.maxsize,0,sys.maxsize],
       [80,40,48,sys.maxsize,80,35,57,sys.maxsize,sys.maxsize,0]]    

    for i in range(0,10):
        print(hillClimbing(map))

if __name__ == "__main__": main()