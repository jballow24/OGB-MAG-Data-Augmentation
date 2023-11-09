def add_related_edges(graph):
    citation_map = {}

    for i, val in enumerate(graph['edge_index_dict'][('paper','cites','paper')][0]):
        if val not in citation_map:
            citation_map[val] = []

        if graph['edge_index_dict'][('paper', 'cites', 'paper')][1][i] not in citation_map[val]:
            citation_map[val].append(graph['edge_index_dict'][('paper', 'cites', 'paper')][1][i])

    result = [[],[]]

    for key in citation_map.keys():
        i = 0
        while i < len(citation_map[key]) - 1:
            j = i + 1
            while j < len(citation_map[key]):
                result[0].append(citation_map[key][i])
                result[1].append(citation_map[key][j])
                j += 1
            i += 1

    array1 = result[0]
    array2 = result[1]

    # Create an empty set to store unique value pairs
    unique_pairs = set()

    # Initialize new arrays to store the filtered values
    filtered_array1 = []
    filtered_array2 = []

    # Iterate through the arrays
    for i in range(len(array1)):
        # Create a tuple with the values from both arrays at the same index
        pair = (array1[i], array2[i])
    
        # Check if the pair is not in the set (not seen before)
        if pair not in unique_pairs:
            # Add the pair to the set to mark it as seen
            unique_pairs.add(pair)
        
            # Append the values to the filtered arrays
            filtered_array1.append(array1[i])
            filtered_array2.append(array2[i])

    result[0] = filtered_array1
    result[1] = filtered_array2

    i = 0
    length = len(result[0])
    while i < length:
        result[0].append(result[1][i])
        result[1].append(result[0][i])
        i += 1

    return result
        
