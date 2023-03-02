import node as N

def to_string(node_chain):
    """
    Purpose:
        Create a string representation of the node chain. E.g.,
        [ 1 | *-]-->[2 | *-]-->[3 | / ]
    Pre-conditions:
        :param node_chain: A node-chain, possibly empty(None)
    Post-conditions:
        None
    Return: A string representation of the nodes.
    """
    # special case: empty node chain
    if node_chain == None:
        result = 'EMPTY'

    else:
        # walk along the chain
        walker = node_chain
        value = walker.get_data()
        # print the data
        result = '[ {} |'.format(str(value))

        """
            until there is no more nodes left in the chain, which is when we reach the last node.
            As the walker is moved to the next node inside the loop and then the data of the node is collected, 
            if we check for walker to be None, then when the walker reaches the end node of the chain it will create error.
            As a result, when the chain's last node is reached by the walker, the following node will 
            be None and devoid of the method get data, resulting in an error. Since the first node is 
            already added to the result, check for the next node to be None
        """
        while walker.get_next() is not None:
            # move walker to the next node in the chain
            walker = walker.get_next()
            # get the value of the walker
            value = walker.get_data()

            # represent the next with an arrow-like figure
            result += ' *-]-->[ {} |'.format(str(value))

            # at the end of the chain, use '/'
        result += ' / ]'
    return result

