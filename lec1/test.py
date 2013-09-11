import shelve
import ex1lib

s = shelve.open('ex1');
try:
	documents = s['documents']
finally:
	s.close

m = ex1lib.calc_term_document_matrix(documents)
print(documents)
