# Create a School class  to handle classroom assignments:

# The constructor should create the following attributes: a list of classroom objects. See the description of the Room class in the next paragraph.
# A function called  assign_room(class_name, num_of_students) should look for available rooms and ensure that there is enough space for that number of students. If the class_name is already assigned with the classroom, change the number of students to reflect the new value. If no matching classroom can be found, the relevant error message should be displayed.
# A function called print_assigned_room() is used to print a list of assigned classrooms, containing details like room number and capacity. class_name and the number of students enrolled.
# A function called unassign_room(room_id) that removes the room assignment by resetting the target room object’s attributes related to the assignment. The function will free up the room so that a new class can be assigned to it.
# Create a Room class that has the following attributes:

# Room id, assigned (boolean), and room capacity, which indicates the maximum number of students that can fit in that room, the class_name, as well as the number of students who are currently enrolled in that class.
# Create a main function to test all the functionalties of your classes.

print("Program to assign room to students")
print("__________________________________")

#School class to handle classroom assignments
class School:
    def __init__(self):
        self.classroom = []
    
    #function to assign room
    def assign_room(self, class_name, num_of_students):
        for room in self.classroom:
            if room.class_name == class_name:
                room.num_of_students = num_of_students
                return
        
        #if class_name is not assigned to any room
        for room in self.classroom:
            if room.assigned == False and room.capacity >= num_of_students:
                room.assigned = True
                room.class_name = class_name
                room.num_of_students = num_of_students
                return
        print("Sorry, no available room")
    
    #function to print assigned room
    def print_assigned_room(self):
        for room in self.classroom:
            if room.assigned == True:
                print("Room number: ", room.room_id)
                print("Room capacity: ", room.capacity)
                print("Class name: ", room.class_name)
                print("Number of students: ", room.num_of_students)
                print("Assigned: ", room.assigned)
                print(" ")
    
    #function to unassign room
    def unassign_room(self, room_id):
        for room in self.classroom:
            if room.room_id == room_id:
                room.assigned = False
                room.class_name = ""
                room.num_of_students = 0
                return
        print("Sorry, room not found")

#Room class
class Room:
    def __init__(self, room_id, capacity):
        self.room_id = room_id
        self.capacity = capacity
        self.assigned = False
        self.class_name = " "
        self.num_of_students = 0
        
#main function to test all the functionalities of the classes
def main():
    school = School()
    school.classroom.append(Room(1, 15))
    school.classroom.append(Room(2, 25))
    school.classroom.append(Room(3, 35))
    school.assign_room("Mathematics", 25)
    school.assign_room("Engineering", 35)
    school.assign_room("Chemisty", 45)
    school.print_assigned_room()
    school.unassign_room(2)
    school.print_assigned_room()

if __name__ == "__main__":
    main()
    
    
