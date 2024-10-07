my_dict={'Alex':1948, 'Nick':1958, 'Dick':2004}
print(my_dict)
print(my_dict['Dick'])
my_dict['Den']=2010
print(my_dict)
my_dict.update({'Bob':2008,
                'Smit':1999})
print(my_dict)
a=my_dict.pop('Den')
print(my_dict)
print(a)

my_set={1,1,2,3,4,2,3,'String',True,(1,2,7)}
print(my_set)
my_set.add(7)
my_set.add(9)
print(my_set)
my_set.remove('String')
print(my_set)
