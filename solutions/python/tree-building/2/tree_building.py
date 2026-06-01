"""tree building"""
class Record:
    """record"""
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id

    def validate(self):
        if (self.record_id == 0 and self.parent_id != 0) or (self.record_id < self.parent_id):
            raise ValueError('Node parent_id should be smaller than its record_id.')
        if self.record_id == self.parent_id and self.record_id != 0:
            raise ValueError('Only root should have equal record and parent id.')

class Node:
    """node"""
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    """builds tree from records"""
    records.sort(key=lambda x: x.record_id)
    if not records:
        return None
    ordered_id = [i.record_id for i in records]
    if records and ((ordered_id[0] != 0) or (ordered_id[-1] != len(ordered_id) - 1)):
        raise ValueError('Record id is invalid or out of order.')

    for record in records:
        record.validate()
        
    trees = [Node(record.record_id) for record in records]
    
    for record, node in zip(records[1:], trees[1:]):
        trees[record.parent_id].children.append(node)

    return trees[0]
