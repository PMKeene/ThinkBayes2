import thinkbayes2
import thinkplot
from random import random, sample
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

	Bandits=[B1,B2,B3]
	hiddenRates=[.85, .6, .75]
	#thinkplot.Pmf(B1, label='Uniform Prior')

	NumPulls=500
	for i in range(0,NumPulls):
		#Sample Random Var Xb for each bandit
		RandHypo=[]
		for pmf in Bandits:
			RandHypo.append(pmf.Random())
		#RandHypo=sample(hypos, len(hiddenRates))
		print(RandHypo)
		#Eval our beliefs in hypotheses for each bandit
		ProbHypo=[]
		for j in range(len(RandHypo)):
			ProbHypo.append(Bandits[j].Prob(RandHypo[j]))
		print(ProbHypo)
		#choose one with highest belief and simulate a pull
		MaxBelief=max(ProbHypo)
		BestBanditIndex=ProbHypo.index(MaxBelief)
		print(MaxBelief, BestBanditIndex)
		data=SimPull(hiddenRates[BestBanditIndex])
		print(data)
		#update belief about that bandit's probability distribution
		Bandits[BestBanditIndex].Update(data)

		# if i%25==0:
		# 	thinkplot.Pmf(B1, label='B1 Posterior')
		# 	thinkplot.Pmf(B2, label='B2 Posterior')
		# 	thinkplot.Pmf(B3, label='B3 Posterior')
		# 	thinkplot.Show()
	Ex1=Bandit(hypos)
	Ex2=Bandit(hypos)
	data1=[True, True,True, False,True, False,True, False,True, False,True, False,True, False,True, False,True, False,True, False]
	data2=[True,True,True,False,False, True,True,True,False,False]
	for data in data1:
		Ex1.Update(data)
		Ex1.Update(data)
	for data in data2:
		Ex2.Update(data)
	thinkplot.Pmf(Ex1, label='Set 1, 40 pts')
	thinkplot.Pmf(Ex2, label='Set 2, 10 pts')
	thinkplot.Show()
	# thinkplot.Pmf(B1, label='B1 Posterior')
	# thinkplot.Pmf(B2, label='B2 Posterior')
	# thinkplot.Show()

if __name__ == '__main__':
	main()