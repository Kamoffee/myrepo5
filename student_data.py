def get_student_data(last_name: str, first_name: str, student_id: int) -> tuple:
    """ 
    Creating a function that return user name, first name and student.

    Parameters:
    a (str) : name
    b (str) : first name
    c (int) : student id


    returns :
    tuple : a touple with name, first name and student id 
    """

    return last_name, first_name, student_id

# asking for user input
a = input("Please enter name: ")
b = input("Please enter your first name: ")
c = input("Please enter your student_id: ")

# calling the function
student_data = get_student_data(a, b, c)
print(student_data)