def making_tuples(dict):
    new_list = []
    for data in dict.iteritems():
        new_list.append(data)
    return new_list

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

print making_tuples(my_dict)
