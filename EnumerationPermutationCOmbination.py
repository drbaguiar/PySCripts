def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    """
    
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp
    return ans

def gen_permutations(outcomes, length):
    '''
    iterative function that generates set of permutations of outcomes of length num_trials,
    repeated outcomes allowed
    '''  
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                if item not in new_seq:
                    new_seq.append(item)              
                    temp.add(tuple(new_seq))
        ans = temp
    return ans
    
def gen_sorted_sequences(outcomes, length):
    """
    Function that creates all sorted sequences via gen_all_sequences
    """    
    all_sequences = gen_all_sequences(outcomes, length)
    sorted_sequences = [tuple(sorted(sequence)) for sequence in all_sequences]
    return set(sorted_sequences)

def gen_sorted_permutations(outcomes, length):
    """
    Function that creates all sorted sequences via gen_all_sequences
    """    
    all_sequences = gen_permutations(outcomes, length)
    sorted_sequences = [tuple(sorted(sequence)) for sequence in all_sequences]
    return set(sorted_sequences)
    
def run_example1():
    """
    Example of all sequences
    """   
    seq_outcomes = gen_all_sequences(outcomes, length)
    print "Computed", len(seq_outcomes), "sequences of", str(length), "outcomes"
    print "Sequences were", seq_outcomes


def run_example2():
    """
    Examples of sorted sequences of outcomes
    """
    seq_outcomes = gen_sorted_sequences(outcomes, length)
    print "Computed", len(seq_outcomes), "sorted sequences of", str(length) ,"outcomes"
    print "Sequences were", seq_outcomes
    
def run_example3():
    """
    Examples of permutations
    """
    seq_outcomes = gen_permutations(outcomes, length)
    print "Computed", len(seq_outcomes), "permutations of", str(length) ,"outcomes"
    print "Sequences were", seq_outcomes

def run_example4():
    """
    Examples of sorted sequences of outcomes
    """
    seq_outcomes = gen_sorted_permutations(outcomes, length)
    print "Computed", len(seq_outcomes), "combinations of", str(length) ,"outcomes"
    print "Sequences were", seq_outcomes
     
   
#outcomes = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#outcomes = set(["Red", "Green", "Blue"])
#outcomes = set(["Sunday", "Mondy", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
outcomes = set(["Red", "Green", "Blue","Yellow","Black","White"])
length = 3

run_example1() #All enurmations
run_example2() #Ordered enurmations
run_example3() #Permutations
run_example4() #Combinations