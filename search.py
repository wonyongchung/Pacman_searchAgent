# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""



class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    import util
    firststep = problem.getStartState()  # 현재 입력된 problem에서 시작점을 반환한다.
    print("startstate: ",firststep)  # 시작 위치 확인.
    # Stack 클래스의 인스턴스로 state를 생성한다. DFS는 stack구조와 같은 원리(Last in First Out)이기 때문에 stack을 사용한다.
    state = util.Stack()
    road = util.Stack()
    state.push(firststep)  # 가장 먼저, firststep 노드를 push한다.
    nowstep = state.pop()  # 지금의 위치.
    visitnode = []  # 방문한 노드를 기록하는 리스트.
    finalroad = []  # 최종적으로 결정된 direction.
    while not problem.isGoalState(nowstep):  # 현재 목표지점이 아니면 계속 loop를 돈다.
        if nowstep in visitnode:  # 만약 nowstep이 이미 방문한 노드라면.
            pass  # 그냥 통과하고.
        else:  # 방문한 노드가 아니라면.
            visitnode.append(nowstep)  # 현위치를 visitnode에 추가하고.
            successors = problem.getSuccessors(nowstep)  # 후손노드를 저장한다.
            for nextstate, action, cost in successors:  #후손노드들에 대해서 state, direction값을 반환한다.(cost는 쓰이지않음)
                state.push(nextstate)  #다음state인 next를 state에 추가한다.
                road.push(finalroad + [action])  #최종 경로에 반환된 action(direction)을 추가한다.
        nowstep = state.pop()  #이제 현재step은 state에서 pop한 값이다.
        finalroad = road.pop()   #finalroad역시 road에서 pop한 값이다.
        print("nowstep: ",nowstep)   #iteration마다 위치 확인.
        print("direction: ",finalroad[-1])   #iteration마다 방향 확인.
    return finalroad   #최종적으로 while문을 빠져나온후 finalroad값을 return하면 된다.
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    import util
    firststep = problem.getStartState()  # 현재 입력된 problem에서 시작점을 반환한다.
    print("startstate: ", firststep)  # 시작 위치 확인.
    # Queue 클래스의 인스턴스로 state를 생성한다. BFS는 Queue구조와 같은 원리(First in First Out)이기 때문에 queue을 사용한다.
    state = util.Queue()
    road = util.Queue()
    state.push(firststep)  # 가장 먼저, firststep 노드를 push한다.
    nowstep = state.pop()  # 지금의 위치.
    visitnode = []  # 방문한 노드를 기록하는 리스트.
    finalroad = []  # 최종적으로 결정된 direction.
    while not problem.isGoalState(nowstep):  # 현재 목표지점이 아니면 계속 loop를 돈다.
        if nowstep in visitnode:  # 만약 nowstep이 이미 방문한 노드라면.
            pass  # 그냥 통과하고.
        else:  # 방문한 노드가 아니라면.
            visitnode.append(nowstep)  # 현위치를 visitnode에 추가하고.
            successors = problem.getSuccessors(nowstep)  # 후손노드를 저장한다.
            for nextstate, action, cost in successors:  # 후손노드들에 대해서 state, direction값을 반환한다.(cost는 쓰이지않음)
                state.push(nextstate)  # 다음state인 next를 state에 추가한다.
                road.push(finalroad + [action])  # 최종 경로에 반환된 action(direction)을 추가한다.
        nowstep = state.pop()  # 이제 현재step은 state에서 pop한 값이다.
        finalroad = road.pop()  # finalroad역시 road에서 pop한 값이다.
        print("nowstep: ", nowstep)  # iteration마다 위치 확인.
        print("direction: ", finalroad[-1])  # iteration마다 방향 확인.
    return finalroad  # 최종적으로 while문을 빠져나온후 finalroad값을 return하면 된다.
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    import util
    firststep = problem.getStartState()  # 현재 입력된 problem에서 시작점을 반환한다.
    print("startstate: ", firststep)  # 시작 위치 확인.
    # PriorityQueue 클래스의 인스턴스로 state를 생성한다. UCS는 cost로 우선순위를 결정하기 때문에 PriorityQueue를 사용해야한다.
    state = util.PriorityQueue()
    road = util.PriorityQueue()
    state.push(firststep,0)  # 가장 먼저, firststep 노드, 그리고 cost로 0값을 push한다.
    nowstep = state.pop()  # 지금의 위치.
    visitnode = []  # 방문한 노드를 기록하는 리스트.
    finalroad = []  # 최종적으로 결정된 direction.
    while not problem.isGoalState(nowstep):  # 현재 목표지점이 아니면 계속 loop를 돈다.
        if nowstep in visitnode:  # 만약 nowstep이 이미 방문한 노드라면.
            pass  # 그냥 통과하고.
        else:  # 방문한 노드가 아니라면.
            visitnode.append(nowstep)  # 현위치를 visitnode에 추가하고.
            successors = problem.getSuccessors(nowstep)  # 후손노드를 저장한다.
            for nextstate, action, cost in successors:  # 후손노드들에 대해서 state, direction, cost 값을 반환한다.
                #필요한 것은, 현재 가는 방향에 대한 정보와 그 cost값이다. 즉 getCostOfActions을 사용해야 한다.
                realcost = problem.getCostOfActions(finalroad + [action])
                if nextstate not in visitnode:  #만약 다음 state로 지정받은 것이 방문하지 않은 것이라면, push한다.
                    state.push(nextstate,realcost)
                    road.push(finalroad+[action],realcost)
        nowstep = state.pop()  # 이제 현재step은 state에서 pop한 값이다.
        finalroad = road.pop()  # finalroad역시 road에서 pop한 값이다.
        print("nowstep: ", nowstep)  # iteration마다 위치 확인.
        print("direction: ", finalroad[-1])  # iteration마다 방향 확인.
    return finalroad  # 최종적으로 while문을 빠져나온후 finalroad값을 return하면 된다.
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    import util
    firststep = problem.getStartState()  # 현재 입력된 problem에서 시작점을 반환한다.
    print("startstate: ", firststep)  # 시작 위치 확인.
    # PriorityQueue 클래스의 인스턴스로 state를 생성한다. UCS는 cost로 우선순위를 결정하기 때문에 PriorityQueue를 사용해야한다.
    state = util.PriorityQueue()
    road = util.PriorityQueue()
    state.push(firststep, 0)  # 가장 먼저, firststep 노드, 그리고 cost로 0값을 push한다.
    nowstep = state.pop()  # 지금의 위치.
    visitnode = []  # 방문한 노드를 기록하는 리스트.
    finalroad = []  # 최종적으로 결정된 direction.
    while not problem.isGoalState(nowstep):  # 현재 목표지점이 아니면 계속 loop를 돈다.
        if nowstep in visitnode:  # 만약 nowstep이 이미 방문한 노드라면.
            pass  # 그냥 통과하고.
        else:  # 방문한 노드가 아니라면.
            visitnode.append(nowstep)  # 현위치를 visitnode에 추가하고.
            successors = problem.getSuccessors(nowstep)  # 후손노드를 저장한다.
            for nextstate, action, cost in successors:  # 후손노드들에 대해서 state, direction, cost 값을 반환한다.
                # A*에서는 실제 cost값과 heuristic을 더한것을 이용하므로 더해준다.
                realcost = problem.getCostOfActions(finalroad + [action])+heuristic(nextstate,problem)
                if nextstate not in visitnode:  # 만약 다음 state로 지정받은 것이 방문하지 않은 것이라면, push한다.
                    state.push(nextstate, realcost)
                    road.push(finalroad + [action], realcost)
        nowstep = state.pop()  # 이제 현재step은 state에서 pop한 값이다.
        finalroad = road.pop()  # finalroad역시 road에서 pop한 값이다.
        print("nowstep: ", nowstep)  # iteration마다 위치 확인.
        print("direction: ", finalroad[-1])  # iteration마다 방향 확인.
    return finalroad  # 최종적으로 while문을 빠져나온후 finalroad값을 return하면 된다.
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
