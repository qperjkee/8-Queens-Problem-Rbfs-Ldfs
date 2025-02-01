import random, math, time

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.conflicts = count_conflicts(state)

def generate_random_queens_positions(size):
    return [random.randint(0, size - 1) for _ in range(size)]

def print_board(queens):
    wrong_spots = find_wrong_spots(queens)
    for i in range(len(queens)):
        for j in range(len(queens)):
            if queens[i] == j:
                if queens[i] not in wrong_spots:
                    print("Q ", end="")
                else:
                    print("q ", end="")
            else:
                print("x ", end="")
        print()

def find_wrong_spots(board):
        wrong_spots = []
        for i in range(len(board)):
            for j in range(i + 1, len(board)):
                if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                    if board[i] not in wrong_spots:
                        wrong_spots.append(board[i])
                    if board[j] not in wrong_spots:
                        wrong_spots.append(board[j])
        return wrong_spots 

def count_conflicts(queens_positions):
    conflicts = 0
    size = len(queens_positions)
    for i in range(size):
        for j in range(size):
            if i != j:
                if queens_positions[i] == queens_positions[j] or abs(queens_positions[i] - queens_positions[j]) == abs(i - j):
                    conflicts += 1
    return conflicts // 2

def is_solution(node):
    return count_conflicts(node.state) == 0

def ldfs(node, depth, max_depth, root, start_time):
    if depth > max_depth:
        return None  

    if is_solution(node):
        return node.state

    if time.time() - start_time > 120:
        return None

    if depth != max_depth:
        for child in find_child_states(node.state, node.parent, root.state):
            child_node = Node(child, node.state)
            result = ldfs(child_node, depth + 1, max_depth, root, start_time)
            if result:
                return result
        
    return None

def find_child_states(queens_positions, parent_positions=None, root=None):
    child_states = []
    size = len(queens_positions)

    for i in range(size):
        for j in range(size):
            child_board = queens_positions.copy()
            child_board[i] = j
            if child_board != queens_positions and child_board != parent_positions and child_board != root:
                child_states.append(child_board)

    return child_states

def rbfs_nqueens(queens_positions):
    initial_node = Node(queens_positions)
    conflicts_limit = math.inf
    res = []
    max_depth = 100

    if rbfs(initial_node, conflicts_limit, res, max_depth) == -1:
        queens_positions.clear()
        queens_positions.extend(res)
        return True

    return False

def rbfs(node, conflicts_limit, res, max_recursion_depth=100):
    if max_recursion_depth <= 0:
        return math.inf

    if is_solution(node):
        res.extend(node.state)
        return -1

    successors = find_successors(node)

    if not successors:
        return math.inf

    min_conflicts_successors = find_min_conflincts_successor(successors)

    alternative_conflicts_amount = min(successor.conflicts for successor in min_conflicts_successors)

    successors.clear()

    if alternative_conflicts_amount > conflicts_limit:
        conflicts_limit = alternative_conflicts_amount
    else:
        for successor in min_conflicts_successors:
            result = rbfs(successor, min(conflicts_limit, alternative_conflicts_amount), res, max_recursion_depth - 1)
            if result == -1:
                return -1
            conflicts_limit = result

    return conflicts_limit

def find_successors(node):
    size = len(node.state)
    successors = []
    for col in range(size):
        for row in range(size):
            if node.state[row] != col:
                child = Node(node.state.copy())
                child.state[row] = col
                child.conflicts = count_conflicts(child.state)
                successors.append(child)
    
    return successors

def find_min_conflincts_successor(successors):
    min_conflicts_successors = []
    min_conflicts_amount = math.inf
    for successor in successors:
        if successor.conflicts < min_conflicts_amount:
            min_conflicts_amount = successor.conflicts
            min_conflicts_successors.clear()
        if successor.conflicts == min_conflicts_amount:
            min_conflicts_successors.append(successor)
    return min_conflicts_successors

def get_size():
    while True:
        try:
            size = int(input("Enter nqueens from 4 to 8: "))
            if size < 4:
                raise ValueError("No nqueens solution for such board")
            if size > 8:
                raise ValueError("Too large amount of queens")
            break
        except ValueError as e:
            print(f"Error: {e}. Try again!") 
    
    return size

def get_depth(size):
    while True:
        try:
            size = int(input(f"Enter max depth of LDFS for {size}-queens: "))
            if size < 2:
                raise ValueError("The depth is too small")
            if size > 10:
                raise ValueError("Too large depth")
            break
        except ValueError as e:
            print(f"Error: {e}. Try again!") 
    
    return size

def get_decision():
    try:
        dec = int(input("Choose algorithm - (1 - LDFS, 2 - RBFS, 3 - BOTH): "))
        return dec
    except ValueError as e:
            print(f"Error: {e}.") 
            return 0

def ldfs_method_nqueens_solver(queens_positions_copy, size):
    depth = get_depth(size)
    initial_node = Node(queens_positions_copy)
    start_time = time.time()
    ldfs_queens = ldfs(initial_node, 0, depth, initial_node, start_time)

    if ldfs_queens:
        print("LDFS solution:")
        print_board(ldfs_queens)
    else:
        print("LDFS algorithm couldn't find solution.")

    print(f"Time: {time.time() - start_time:.2f}")

def rbfs_method_nqueens_solver(queens_positions):
    start_time = time.time()
    if rbfs_nqueens(queens_positions):
        print("RBFS solution:")
        print_board(queens_positions)
    else:
        print("RBFS algorithm couldn't find solution.")
    print(f'Time: {time.time() - start_time:.2f}')

def main():
    size = get_size()

    queens_positions = generate_random_queens_positions(size)
    queens_positions_copy = queens_positions.copy()

    print(f"\nStart(random) placment of {size}-queens: ")
    print_board(queens_positions)
    print() 

    dec = get_decision()

    if dec == 1:
        ldfs_method_nqueens_solver(queens_positions_copy, size)

    elif dec == 2:
        rbfs_method_nqueens_solver(queens_positions)
    
    elif dec == 3:
        ldfs_method_nqueens_solver(queens_positions_copy, size)
        print()
        rbfs_method_nqueens_solver(queens_positions)

if __name__ == "__main__":
    main()