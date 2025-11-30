class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
    
    def __repr__(self):
        return f"Person({self.name}, {self.age}, {self.job})"
    
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name

class Group:
    def __init__(self):
        self.people = set()
        self.connections = {}  
    
    def add_person(self, name, age, job):
        person = Person(name, age, job)
        if person in self.people:
            raise ValueError(f"Person {name} already exists in group")
        self.people.add(person)
        return person
    
    def get_person(self, name):
        for person in self.people:
            if person.name == name:
                return person
        return None
    
    def add_connection(self, name1, name2, relation):
        person1 = self.get_person(name1)
        person2 = self.get_person(name2)
        
        if not person1 or not person2:
            raise ValueError("One or both persons not found in group")

        key = tuple(sorted([person1, person2], key=lambda x: x.name))
        self.connections[key] = relation
    
    def forget(self, name1, name2):
        person1 = self.get_person(name1)
        person2 = self.get_person(name2)
        
        if person1 and person2:
            key = tuple(sorted([person1, person2], key=lambda x: x.name))
            self.connections.pop(key, None)
    
    def average_age(self):
        if not self.people:
            return 0
        return sum(person.age for person in self.people) / len(self.people)
    
    def get_connections(self, name):
        person = self.get_person(name)
        if not person:
            return {}
        
        connections = {}
        for (p1, p2), relation in self.connections.items():
            if p1 == person:
                connections[p2.name] = relation
            elif p2 == person:
                connections[p1.name] = relation
        return connections