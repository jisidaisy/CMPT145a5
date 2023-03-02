"""
Assuming node class contains the below methods to set and get the data and next node values.
get_data() returns the value of the node
set_data(value) updates the value of the node
get_next() returns the next node in the chain (None if last node)
set_next(n) sets the next node of the node to n
"""

def sumnc(node_chain):
    """
    Purpose:
        Given a node chain with numeric data value, calculate
        the sum of the data values.
    Pre-conditions:
        : param node_chain: a node-chain, possibly empty, containing
                                numeric data values
    Post-condition:
        None
    Return
        :return: the sum of the data values in the node chain
    """

    # initialize total to 0
    total = 0
    # set curr to first node of the chain
    curr = node_chain
    # loop over the chain
    while curr is not None:
        total += curr.get_data()  # add the value of curr to total
        curr = curr.get_next()  # move curr to next node

    return total

