'''
Created on Sep 20, 2016

@author: jianwei
'''

from copy import copy

class pos:
    def __init__(self, xval, yval):
        setattr(self, 'x', xval)
        setattr(self, 'y', yval)
        
    def equals(self, other):
        return self.x == other.x and self.y == other.y


class solution:
    def shortestDistance(self, grid):
        blds = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    blds.append(pos(i,j))
        visited = grid
        curr = pos(0,1)
        next = self.minDist(grid, curr, visited, blds)
        while not curr.equals(next):
            curr = next
            next = self.minDist(grid, curr, visited, blds)
        
        return curr
        
        
    def minDist(self, grid, curr, visited, buildings):
        currdist = 0
        for bld in buildings:
            currdist += self.mdist(grid, curr, visited, bld)
        
        cpy = copy(visited)
        cpy[curr.x][curr.y] = 1
        nx = self.next(grid, curr, cpy)
        dists = []
        for n in nx:
            dist = 0
            for bld in buildings:
                dist += self.mdist(grid, n, cpy, bld)
            dists.append(dist)
            
        if min(dists) < currdist:
            for i in range(len(dists)):
                if dists[i] == min(dists):
                    return nx[i]
        else:
            return curr
        
        
    def next(self, grid, curr, visited):
        nx = []
        if curr.x > 0 and grid[curr.x-1][curr.y] == 0 and visited[curr.x-1][curr.y] == 0:
            nx.append(pos(curr.x-1, curr.y))
        if curr.x < len(grid)-1 and grid[curr.x+1][curr.y] == 0 and visited[curr.x+1][curr.y] == 0:
            nx.append(pos(curr.x+1, curr.y))
        if curr.y > 0 and grid[curr.x][curr.y-1] == 0 and visited[curr.x][curr.y-1] == 0:
            nx.append(pos(curr.x, curr.y-1))
        if curr.y < len(grid[0])-1 and grid[curr.x][curr.y+1] == 0 and visited[curr.x][curr.y+1] == 0:
            nx.append(pos(curr.x, curr.y+1))
        return nx
    
    def mdist(self, grid, curr, visited, loc):
        if curr.equals(loc):
            dist = 0
            return dist
        else:
            cpy = copy(visited)
            cpy[curr.x][curr.y] = 1
            nx = self.next(grid, curr, cpy)
            dists = []
            for n in nx:
                dist = self.mdist(grid, n, cpy, loc)
                if dist != None:
                    dists.append(dist+1)
            if len(dists) != 0:
                return min(dists)
        
        
def main():
    grid = [[1,0,2,0,1],
            [0,0,0,0,0],
            [0,0,1,0,0]]
    
    soln = solution()
    
    bestLoc = soln.shortestDistance(grid)
    
    print("The best location is: ({},{})".format(bestLoc.x, bestLoc.y))

if __name__ == '__main__':
    main()