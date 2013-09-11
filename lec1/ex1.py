import numpy as n

documents = {0:'pea soup hot',1:'pea soup cold',2:'pea soup in the pot',
        3:'nine days old',4:'some like it hot',5:'some like it cold'}

m = dict();
for doc in documents:
        words = documents[doc].split()
        for word in words:
                i = 0
                for d in documents:
                        if word in documents[d].split():
                                i += pow(2,d)
                m[word] = i

print('\\begin{tabular}{| l | l | l | l | l | l | l |}')
print('\\hline word&6&5&4&3&2&1\\\\ \\hline');
for word in m:
        row = word + '&'
        b = '{0:0' + str(len(docs) + 'b}'.format(m[word])
        row += '&'.join([b[i:i+1] for i in range(0, len(b), 1)])
        row += '\\\\'
        print(row)
print('\\hline \\end{tabular}')

print('\\\\ \n:');
print('soup: ' + '{0:06b}'.format(m['soup']) + '\\\\')
print('hot: ' + '{0:06b}'.format(m['hot']) + '\\\\')
print('soup \& hot: ' + '{0:06b}'.format((m['hot'] & m['soup'])) + '\\\\')
print('soup or cold not pot: ' + '{0:06b}'.format(((m['soup'] | m['cold']) &~m['pot'])) + '\\\\') 
