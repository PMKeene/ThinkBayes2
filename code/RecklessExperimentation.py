from thinkbayes2 import Pmf

def ch2():
    pmf1=Pmf()
    for x in [1,2,3,4,5,6]:
    	pmf1.Set(x,1/6.0) #Setting Probablities directly

    pmf2=Pmf()
    word_list=['hello', 'world']
    for word in word_list:
    	pmf2.Incr(word, 1) #incrementing a count of a thing, 
    	pmf2.Normalize() # then turn a count into a prob

    print pmf2.Prob('hello') #getting actual probs out

def Odds(p):
	return p/(1-p)
def Probability(o):
	return o/(o+1)
def Probability2(yes,no):
	return yes/(yes+no)

def PmfProduct(self, other):
	'''
	PMF of the product. 
	other: another pmf
	returns: new pmf
	'''
	pmf = Pmf()
	for v1, p1 in self.Items():
		for v2, p2 in other.Items():
			pmf.Incr(v1 * v2, p1 * p2)
	return pmf

def PmfProbSumGreater(pmf1, pmf2, pmf3):
	'''
	akes three distributions and returns the probability 
	that the sum of values from the first two distributions 
	exceeds a value drawn from the third. 

	Distribution of a maxima in section 5.5
	'''

	return 0
##Mixtures! HOW DO?

def ComboED(pmf_e,pmf_d):
	joint=Joint()
	suite=Suite()
	for v1,p1 in pmf_e.Items():
		for v2,p2 in pmf_d.Items():
			joint.Set((v1,v2),p1*p2)
	for pair, prob in joint.Items():
		suite.Set(pair,prob)
	return suite


if __name__ == '__main__':
	print 'Bayes'
	pmf1=Pmf()
	pmf2=Pmf()
	InitJointSuite=ComboED(pmf1,pmf2)
	