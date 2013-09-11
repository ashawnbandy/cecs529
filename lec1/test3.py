import shelve
import ex1lib

s = shelve.open('ex1');
try:
        documents = s['documents']
finally:
        s.close

m = ex1lib.calc_term_document_matrix(documents)
(header,firstline,rows,footer) = ex1lib.format_term_document_matrix(m,documents)
print header
print firstline
for word in rows:
	print word + "&" + rows[word]
print footer
