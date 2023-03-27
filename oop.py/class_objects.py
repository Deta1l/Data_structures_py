#связный список

class full_grade:
    def __init__(self, data):
        full_grade.data = data
        self.next = None

    def append(self, val):
        end = full_grade(val)
        n = self
        while (n.next):
            n = n.next
        n.next = end


class school_class:
    def __init__(self, name, grade, mark):
        self.name = name
        self.grade = grade
        self.mark = mark
        self.next = None
    
    def append(self, name, grade, mark):
        end = school_class(name, grade, mark)
        n = self
        while (n.next):
            n = n.next
        n.next = end

    def __del__(self):
        print('Object destroyed')



        
    


class_11A = school_class("Maxim Pyankov", "11A", 5)
class_11A.append("Popov", "11A", 3)
class_11A.append("Krasnov", "11A", 4)
class_11A.append("Lapin", "11A", 5)
class_11B = school_class("Maxim Pyankov", "11A", 5)
class_11B.append("Popov", "11A", 3)
class_11B.append("Lapin", "11A", 5)
class_11C = school_class("Maxim Pyankov", "11A", 5)
class_11C.append("Popov", "11A", 3)
class_11C.append("Lapin", "11A", 5)

full_11grade = full_grade(class_11A)
full_11grade.append(class_11B)
full_11grade.append(class_11C)


node = full_11grade
print(node.data)
while node.next:
    node = node.next
    print(node.data)

print("\n")

node = class_11A
print(node.name, node.grade, node.mark)
while node.next:
    node = node.next
    print(node.name, node.grade, node.mark) 


print("\n")