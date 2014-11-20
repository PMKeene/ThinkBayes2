import thinkbayes2
import thinkplot
from random import random
import numpy

class Bandit(thinkbayes2.Suite):
	"""Suite of hypotheses of rates of success getting reward"""
	def Likelihood(self, data, hypo):
		"""Computes the likelihood of the data under the hypothesis.

		hypo: value of x, the probability of success (0-100)
		data: True or False, result of a simulated pull
		"""
		x = hypo / 100.0
		if data == True:
		    return x
		else:
		    return 1-x

def SimPull(hidden):
	return random()< hidden

def main():
	hypos=numpy.linspace(0,100,250)
	B1=Bandit(hypos)
	B2=Bandit(hypos)
	B3=Bandit(hypos)
	B4=Bandit(hypos)

	Bandits=[B1,B2,B3, B4]
	hiddenRates=[.85, .60, .75, .45]
	#thinkplot.Pmf(B1, label='Uniform Prior')

	NumPulls=1000
	for i in range(1,NumPulls+1












		):
		#Sample Random Var Xb for each bandit
		RandHypo=[]
		for pmf in Bandits:
			RandHypo.append(pmf.Random())
		
		#Choose highest randomly sampled hyposthesis and simulate a pull on that bandit
		OptimisticHypo=max(RandHypo)
		BestBanditIndex=RandHypo.index(OptimisticHypo)
		print(BestBanditIndex)
		data=SimPull(hiddenRates[BestBanditIndex])
		
		#update belief about that bandit's probability distribution
		Bandits[BestBanditIndex].Update(data)


		if i%25==0:
			thinkplot.Pmf(B1, label='B1 Posterior')
			thinkplot.Pmf(B2, label='B2 Posterior')
			thinkplot.Pmf(B3, label='B3 Posterior')
			thinkplot.Pmf(B4, label='B4 Posterior')
			thinkplot.Show( title='Bandit Distributions after %d pulls'%i, xlabel='Success Rate Hypotheses', ylabel='Degree of Belief')

if __name__ == '__main__':
	main()