"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import numpy
import thinkbayes2
import thinkplot


class Bus(thinkbayes2.Suite):
    """Represents hypotheses about."""

    def Likelihood(self, data, hypo):
        """Computes the likelihood of the data under the hypothesis.

        hypo: value of lam, bus/#minutes
        data: time arrive after last bus left, minutes
        """
        # lam=hypo
        # t=data/90 #portion of a game that has gone by
        # like = thinkbayes2.EvalExponentialPdf(t, lam)
        return 1#like

    def DistWaiting(self, low, high ):
        """Plots the predictive distribution for waiting time of uniformlly distributed
        bus waiting times.

        low: minimum interval buses come in
        high: maximum interval buses
        """
        lam=range(low,high)
        metapmf=thinkbayes2.Pmf()
        for lam, prob in self.Items():
            lamt=lam*rem_time/90
            pmf=thinkbayes2.MakePoissonPmf(lamt, 12)
            #thinkplot.Pdf(pmf)
            metapmf[pmf]=prob
        #make mixture
        mix=thinkbayes2.MakeMixture(metapmf)
        mix+=score
        thinkplot.Hist(mix)
        thinkplot.Show()


def main():
    hypos = numpy.linspace(10, 30, 21)
    suite = Bus(hypos)

    thinkplot.Pdf(suite, label='prior')
    print('prior mean', suite.Mean())

    suite.Update(69)
    thinkplot.Pdf(suite, label='prior 2')
    print('Pseudo Obs Prior', suite.Mean())

    suite.Update(11)
    thinkplot.Pdf(suite, label='posterior 1')
    print('after goal', suite.Mean())

    suite.Update(12)
    thinkplot.Pdf(suite, label='posterior 2')
    print('after another', suite.Mean())

    thinkplot.Show()

    suite.PredRemaining((90-23), 2)


if __name__ == '__main__':
    main()