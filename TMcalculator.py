#TM sequence 
#Thesis
#Carrie Padula


def TM(n):
	#this computes the sequence to 2^(input integer)
	if n % 2 != 0: 
		raise Exception("sorry, convergence only works for even n!")
		#we're just ignoring odd n
		# we could just make it compute the sequence by removing
		#this if stmnt if we so desire
	else: 
		j = 1
		i = '0'
		t = i + negator(i) #start here
		while j <= n:#note this means we loop n+1 times, could change it? 
			t = t + str(neg_loop(t))#we take the negation of the string and attach it to the string to make a new string
			j = j+1
		return str(t) 
		#returns the whole thing as a string so we can remove pieces off
		#with the parser

def neg_loop(s):#this does the bulk of the work, it translates all of the 0's in a string into 1's and vice versa.
	intab = "01"
	outtab = "10"
	hh = str.maketrans(intab,outtab) 
	return s.translate(hh)



def negator(s): #negates the first thing!
	if s == '0':
		return '1'
	elif s == '1':
		return '0'
	elif s!= '0' or '1':
		raise Exception('must be 0 or 1, not ' + s) 

def test():
	print(TM(2))
	#generates 01101001! 

test()


#runtime analysis (loose)
#modding check takes t time
#negator takes t1 time
#negloop takes t3 + t4 time (t3 is maketrans, t4 is translate)
#so tm calculator takes ((n)(t3+t4)) + t + t1 time. 

