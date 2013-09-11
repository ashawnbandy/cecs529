import numpy as np

def print_documents(docs):
	print r"\begin{itemize}"
	for doc in docs:
		print r"\item \textbf{Doc " + str(doc+1) + ": } " + docs[doc]
	print r"\end{itemize}"

def format_term_document_matrix(m,docs):
	header = "\\begin{tabular}{| l"
	firstline = "word"
	dn = len(docs) + 1;
	for d in docs:
		header += "| l"
		dn -= 1
		firstline += "&" + str(dn)
		
	header += "|} \\hline"
	firstline += "\\\\ \\hline"
	rows = dict()
	for word in m:
		a = "{0:0" + str(len(docs)) + "b}"
		b = a.format(m[word])
		rows[word] = '&'.join([b[i:i+1] for i in range(0, len(b), 1)]) + "\\\\"
	footer = "\\hline \\end{tabular}"
	return (header,firstline,rows,footer)
	

def calc_term_document_matrix(docs):
	m = dict();
	for doc in docs:
        	words = docs[doc].split()
        	for word in words:
                	i = 0
                	for d in docs:
                        	if word in docs[d].split():
                                	i += pow(2,d)
                	m[word] = i
	return m
