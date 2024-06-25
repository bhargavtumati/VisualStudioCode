# Define the ThroneInheritance class
from typing import List


class ThroneInheritance:
    def __init__(self, kingName: str):
        self.dead = set()
        self.graph = {kingName: []}
        self.root = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.graph.setdefault(parentName, []).append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        def dfs(n):
            """Pre-order traverse the graph."""
            if n not in self.dead:
                ans.append(n)
            for nn in self.graph.get(n, []):
                dfs(nn)

        ans = []
        dfs(self.root)
        return ans

# Example usage:
if __name__ == "__main__":
    # Create an instance of the ThroneInheritance class
    obj = ThroneInheritance("king")

    # Perform births
    obj.birth("king", "andy")
    obj.birth("king", "bob")
    obj.birth("king", "catherine")
    obj.birth("andy", "matthew")
    obj.birth("bob", "alex")
    obj.birth("bob", "asha")

    # Perform deaths
    obj.death("bob")

    # Get the inheritance order
    inheritance_order = obj.getInheritanceOrder()
    print(inheritance_order)  # Output: ['king', 'andy', 'matthew', 'catherine', 'asha']
