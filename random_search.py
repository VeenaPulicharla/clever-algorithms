import numpy as np

"""Implementing random search in python
Input: NumIterations, ProblemSize, SearchSpace
Output: Best cost and candidate

"""



def objective_function(candidate_vector):
    cost = 0
    # objective function x^2 - 5.0 
    for x in candidate_vector:
        cost += (x ** 2) - 5.0
    return cost

def select_candidate(problem_size):
    list_cand = []
    for val in range(problem_size):
        #here [-5,5] is the search space
        candidate = np.random.uniform(-5, 5)
        list_cand.append(candidate)

    vector = np.array(list_cand)
    return vector
    


def search(no_of_iterations, problem_size):
    best_cost = None
    best_candidate = None
    for i in range(no_of_iterations):
        candidate_vector=select_candidate(problem_size)
       # print "candidate : ",candidate_vector
        cost = objective_function(candidate_vector)
        if not best_cost:
            best_cost = cost
            best_candidate = candidate_vector
        elif cost < best_cost:
            best_cost = cost
            best_candidate = candidate_vector
    return best_candidate, best_cost

if __name__ == '__main__':
    problem_size=2
    search_space=[-5,5]
    no_of_iter=10
    best_candidate, best_cost = search(no_of_iter,problem_size)
    print ("best_cost:"+ str(best_cost) , "best_candidate :" + str(best_candidate))

