# def who_do_you_know():
#     people = input("Input the name of people you know, separated by commas!")  # Vivek,Aarti,Harsha,Raj,Vikash
#     people_list = people.split(',')  # ["Vivek", "Aarti", "Harsha", "Raj", "Vikash"]
#     people_without_list = []
#     for person in people_list:
#         people_without_list.append(person.strip())
#     return people_without_list


def who_do_you_know():
    people = input("Input the name of people you know, separated by commas!")  # Vivek,Aarti,Harsha,Raj,Vikash
    people_list = people.split(',')  # ["Vivek", "Aarti", "Harsha", "Raj", "Vikash"]
    people_without_list = [person.strip() for person in people_list]
    return people_without_list


def ask_user():
    person = input("Enter the name of person you know!")
    if person in who_do_you_know():
        print("You know {}!".format(person))


ask_user()
