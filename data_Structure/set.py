set1 = {'kamal','nimal','amal'}

set1.add('sunimal')
print(set1)

set2 = {'nimali','sunali','kabili'}
set1.update(set2)
print(set1)


print(set1.pop())
print(set1)

set1.remove('kabili')
print(set1)

for x in set1:
    print(x)