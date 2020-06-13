import json

f = open('../data/employees.json')

# print(json.load(f))              # reads the json file

# Only used to read json data, not for json string
data = json.load(f)
# print(type(json_data))
student_list = data['students']

for student in student_list:
    print(student)

for std in student_list:
    print(std['name'], std['city'])

# Reading Json String
json_string = """
{
  "students": [
    {
      "age": 32,
      "name": "Vivek",
      "city": "Pune",
      "developer": true
    },
    {
      "age": 33,
      "name": "Aarti",
      "city": "Pune",
      "developer": false
    },
    {
      "age": 29,
      "name": "Harsh",
      "city": "Pune",
      "developer": false
    },
    {
      "age": 35,
      "name": "Raj",
      "city": "Pune",
      "developer": true
    },
    {
      "age": 22,
      "name": "DoubleDigit",
      "city": "Germany",
      "developer": false
    }
  ]
}
"""
data = json.loads(json_string)

print(data)

student_data = data['students']
print(student_data)

for s in student_data:
    print(s['name'], s['age'])

# Convert dict to string
json_string_from_dict = json.dumps(data, indent=2)
print(json_string_from_dict)
print(type(json_string_from_dict))

# Sort data based on keys in dict
json_string_sorted_by_keys = json.dumps(data, indent=2, sort_keys=True)
print(json_string_sorted_by_keys)

# Write data in a file
f = open('../data/output_students.json', 'w')
json.dump(json_string_from_dict, f, indent=2)
f_2 = open('../data/output_2_students.json', 'w')
json.dump(data, f_2, indent=4)


