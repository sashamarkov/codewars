import json
from preloaded import print_tree
​
def find_seventh_sons_of_seventh_sons(jstring: str) -> set:
    def dfs(node, parent_seventh=False):
        result = set()
        if 'children' in node:
            sons = 0
            for child in node['children']:
                if child['gender'] == 'male':
                    sons += 1
                    if sons == 7:
                        if parent_seventh:
                            result.add(child['name'])
                        result |= dfs(child, True)
                else:
                    sons = 0
                result |= dfs(child, False)
        return result
    return dfs(json.loads(jstring))