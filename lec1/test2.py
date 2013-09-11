import shelve 
import ex1lib

documents = {0: 'breakthrough drug for schizophrenia',1: 'new schizophrenia drug',2: 'new approach to treatment of schizophrenia',3: 'new hope for schizophrenia patients'}

ex1lib.print_documents(documents)

s = shelve.open('ex1');
try:
	s['documents'] = documents
finally:
	s.close()

