
def create_tree(df):
    tree = {'id': 'Root', 'children': []}
    parent_stack = [tree]
    id = 1001

    for _, row in df.iterrows():
        level = len(row['Level'].strip()) - 1  # Correct level calculation

        # Adjust parent stack to the correct level
        while len(parent_stack) > level:  # Adjust condition
            parent_stack.pop()

        # Create the new node
        new_node = {'id': str(id), 'level': level, 'children': []}

        # Add as child to the correct parent
        parent_stack[-1]['children'].append(new_node)

        # Append to parent stack if starting a new level or continuing at the same level
        if level >= len(parent_stack) - 1:
            parent_stack.append(new_node)

        id += 1

    return tree