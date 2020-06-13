my_list = [0, 1, 2, 3, 4]
generated_list = [x for x in range(5)]  # [0,1,2,3,4]

complex_generated_list = [x * 11 for x in range(11)]
print(complex_generated_list)

print(8 % 3)  # 8 / 3 == 6r2, so 8 % 3 give 2 which is the remainder

print(9 % 2)  # Even number 4 % 2 == 0, so it is even

even_numbers = [n for n in range(11) if n % 2 == 0]
print(even_numbers)

people_you_know = ["VIvek", "arti", "VIKASH", "HarSha"]
normalised_names = [person.strip().lower() for person in people_you_know]
print(normalised_names)
