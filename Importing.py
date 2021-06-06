import os

start_dir = input('Starting dir:')
target = input('Target:')
paths = []
dirs_to_search = [start_dir]
while dirs_to_search:
    current_dir = dirs_to_search.pop(0)
    for item in os.listdir(current_dir):
        item_path = os.path.join(current_dir, item)
        if item.split('.')[0] == target:
            paths.append(item_path)
        if os.path.isdir(item_path):
            dirs_to_search.append(item_path)
print(paths)
