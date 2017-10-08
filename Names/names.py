# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
#
# def names_outputs(dict):
#     for item in dict:
#         name = ""
#         for data in item.iteritems():
#
#             name = "{} {}".format(item['first_name'], item['last_name'])
#         print name
#
# names_outputs(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def users_outputs(dict):
    name = ""
    for key, data in dict.iteritems():
        print key
        count = 0
        for value in data:
            count += 1
            name = "{} {}".format(value['first_name'], value['last_name'])
            print str(count) + " - " + name.upper() + " - " + str(len(name) - 1)

users_outputs(users)
