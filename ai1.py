class FamilyTree:
    def __init__(self):
        self.family = {
            'A': {'father': 'B', 'mother': 'C', 'siblings': ['D'], 'children': ['E', 'F']},
            'D': {'father': 'B', 'mother': 'C', 'siblings': ['A'], 'children': ['G']},
            'E': {'father': 'A', 'mother': 'H', 'siblings': ['F'], 'children': []},
            'F': {'father': 'A', 'mother': 'H', 'siblings': ['E'], 'children': []},
            'G': {'father': 'Info. not available', 'mother': 'D', 'siblings': [], 'children': []},
            'B': {'father': 'Info. not available', 'mother': 'Info. not available', 'siblings': [], 'children': ['A', 'D']},
            'C': {'father': 'Info. not available', 'mother': 'Info. not available', 'siblings': [], 'children': ['A', 'D']},
            'H': {'father': 'Info. not available', 'mother': 'Info. not available', 'siblings': [], 'children': ['E', 'F']}
        }
    def find_relationship(self, name1, name2):
        if name1 not in self.family or name2 not in self.family:
            return "One or both names are not in the family tree."
        if name2 in self.family[name1].get('siblings', []):
            return f"{name2} is {name1}'s sibling."
        if name2 in self.family[name1].get('children', []):
            return f"{name2} is {name1}'s child."
        if self.family[name1].get('father', '') == name2 or self.family[name1].get('mother', '') == name2:
            return f"{name2} is {name1}'s parent."
        if name2 in self.family.get(self.family[name1].get('father', ''), {}).get('children', []) or \
           name2 in self.family.get(self.family[name1].get('mother', ''), {}).get('children', []):
            return f"{name2} is {name1}'s grandparent."
        return "Brothers"
    def print_family_members(self):
        for member, details in self.family.items():
            print(f"{member}:")
            print(f"  Father: {details['father']}")
            print(f"  Mother: {details['mother']}")
            print(f"  Siblings: {', '.join(details['siblings']) if details['siblings'] else 'None'}")
            print(f"  Children: {', '.join(details['children']) if details['children'] else 'None'}")
            print()
family_tree = FamilyTree()
family_tree.print_family_members()
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
relationship = family_tree.find_relationship(name1, name2)
print(relationship)
