def hamming_distance(seq1, seq2):
    '''
    Will count the number of times two sequences do not match. 
    '''

    distance_counter = 0
    result = zip(seq1, seq2)

    for i, j in result:
        if i != j:
            distance_counter += 1

    return distance_counter

