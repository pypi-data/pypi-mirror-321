import numpy as np
import pandas as pd
from scipy.stats import binom, norm, poisson
import logging

class HigherCriticism(object):
    """
    Higher Criticism test 

    References:
    [1] Donoho, D. L. and Jin, J., "Higher criticism for detecting sparse
     hetrogenous mixtures", Annals of Stat. 2004
    [2] Donoho, D. L. and Jin, J. "Higher critcism thresholding: Optimal 
    feature selection when useful features are rare and weak", proceedings
    of the national academy of sciences, 2008.
    ========================================================================

    Args:
    -----
        pvals    list of p-values. P-values that are np.nan are exluded.
        stbl     normalize by expected P-values (stbl=True) or observed 
                 P-values (stbl=False). stbl=True was suggested in [2].
                 stbl=False in [1]. 
        gamma    lower fruction of p-values to use.
        normalization    normalization of the ordered P-values. 
                         'donoho-jin2008' is the default normalization used in [2].
                         'beta' is a better normalization that matches the mean and standard deviation of the ordered P-values.
        
    Methods :
    -------
        HC       HC and P-value attaining it
        HCstar   sample adjustet HC (HCdagger in [1])
        HCjin    a version of HC from [3] (Jin & Wang 2016)
    """

    def __init__(self, pvals, stbl=True, normalization='beta'):

        self._N = len(pvals)
        assert (self._N > 0)

        self._EPS = 1 / (1e4 + self._N ** 2)
        self._istar = 0

        self._sorted_pvals = np.sort(np.asarray(pvals.copy()))  # sorted P-values
        
        if normalization == 'donoho-jin2008':
            self._uu = np.linspace(1 / self._N, 1 / self._N, self._N) # this is the default normalization used in [2]
            self._uu[-1] -= self._EPS # to avoide infinity upon standardization
            # we don't use the last P-value in the normalization so this shouldnt't affect the results
        else: # beta normalization
            # this appears to be a better normalization becasue it matches the mean and standard deviation of the ordered P-values
            self._uu = np.linspace(1 / (self._N + 1), 1 - 1 / (self._N + 1) , self._N)

        if stbl:
            denom = np.sqrt(self._uu * (1 - self._uu))
        else:
            denom = np.sqrt(self._sorted_pvals * (1 - self._sorted_pvals))

        self._zz = np.sqrt(self._N) * (self._uu - self._sorted_pvals) / denom

        self._imin_star = np.argmax(self._sorted_pvals > (1 - self._EPS) / self._N)
        self._imin_jin = np.argmax(self._sorted_pvals > np.log(self._N) / self._N)


    def _calculateHC(self, imin, imax) :
        if imin > imax:
            return np.nan
        if imin==imax:
            self._istar = imin
        else: 
            self._istar = np.argmax(self._zz[imin:imax]) + imin
        zMaxStar = self._zz[self._istar]
        return zMaxStar, self._sorted_pvals[self._istar]

    def HC(self, gamma=0.4) : 
        """
        Higher Criticism test statistic

        Args:
        -----
        'gamma' : lower fraction of P-values to consider

        Return:
        -------
        HC test score, P-value attaining it

        """
        imin = 0
        imax = np.maximum(imin, int(gamma * self._N + 0.5))        
        return self._calculateHC(imin, imax)

    def HCjin(self, gamma=0.4) :
        """sample-adjusted higher criticism score from [2]

        Args:
        -----
        'gamma' : lower fraction of P-values to consider

        Return:
        -------
        HC score, P-value attaining it

        """
        
        imin = self._imin_jin
        imax = np.maximum(imin + 1,
                        int(np.floor(gamma * self._N + 0.5)))
        return self._calculateHC(imin, imax)
    
    def HCstar(self, gamma=0.4) :
        """sample-adjusted higher criticism score

        Args:
        -----
        'gamma' : lower fraction of P-values to consider

        Returns:
        -------
        HC score, P-value attaining it

        """

        imin = self._imin_star
        imax = np.maximum(imin + 1,
                        int(np.floor(gamma * self._N + 0.5)))        
        return self._calculateHC(imin, imax)

    def get_state(self):
        return {'pvals' : self._sorted_pvals, 
                'u' : self._uu,
                'z' : self._zz,
                'imin_star' : self._imin_star,
                'imin_jin' : self._imin_jin,
                }


class HC(HigherCriticism):
    """
    For legacy
    """

    
def two_sample_test(smp1, smp2, data_type = 'counts',
                         alt='two-sided', **kwargs) :
    """
    Returns HC score and HC threshold in a two-sample test. 
    =========================================================

    Args:
    ----

    smp1, smp2    dataset representing samples from the identical or different
                  populations.
    data_type     either 'counts' of categorical variables or 'reals'
    alt           how to compute P-values ('two-sided' or 'greater')
    kwargs        additional arguments for the class HC and pvalue computation

    Returns:
    -------
    (HC, HCT)     HC score, HC threshold P-value

    """

    stbl = kwargs.get('stbl', True)
    randomize = kwargs.get('randomize', False)
    gamma = kwargs.get('gamma', 0.2)

    smp1 = np.array(smp1)
    smp2 = np.array(smp2)

    if data_type == 'counts' :
        pvals = two_sample_binomial_test(smp1, smp2, randomize=randomize, alt=alt)
    elif data_type == 'reals' :
        z = (smp1 - smp2) / np.sqrt(2)
        if alt == 'greater' :
            pvals = norm.sf(z)
        else :
            pvals = norm.sf(np.abs(z))

    return HigherCriticism(pvals[~np.isnan(pvals)], stbl).HCstar(gamma)


def binom_test(x, n, p, alt='greater') :
    """
    Returns:
    --------
    Prob(Bin(n,p) >= x) ('greater')
    or Prob(Bin(n,p) <= x) ('less')

    Note: for small values of Prob there are differences
    fron scipy.python.binom_test. It is unclear which one is 
    more accurate.
    """
    n = n.astype(int)
    if alt == 'greater' :
        return binom.sf(x, n, p) + binom.pmf(x, n, p)
    if alt == 'less' :
        return binom.cdf(x, n, p)


def poisson_test_random(x, lmd) :
    """Prob( Pois(n,p) >= x ) + randomization """
    p_down = 1 - poisson.cdf(x, lmd)
    p_up = 1 - poisson.cdf(x, lmd) + poisson.pmf(x, lmd)
    U = np.random.rand(x.shape[0])
    prob = np.minimum(p_down + (p_up-p_down)*U, 1)
    return prob * (x != 0) + U * (x == 0)

def binom_test_two_sided(x, n, p) :
    """
    Returns:
    --------
    Prob( |Bin(n,p) - np| >= |x-np| )

    Note: for small values of Prob there are differences
    fron scipy.python.binom_test. It is unclear which one is 
    more accurate.
    """

    n = n.astype(int)

    x_low = n * p - np.abs(x-n*p)
    x_high = n * p + np.abs(x-n*p)

    p_up = binom.cdf(x_low, n, p)\
        + binom.sf(x_high-1, n, p)
        
    prob = np.minimum(p_up, 1)
    return prob * (n != 0) + 1. * (n == 0)


def binom_test_two_sided_random(x, n, p) :
    """
    Returns:
    --------
    pval  : random number such that 
            Prob(|Bin(n,p) - np| >= 
            |InvCDF(pval|Bin(n,p)) - n p|) ~ U(0,1)
    """

    x_low = n * p - np.abs(x-n*p)
    x_high = n * p + np.abs(x-n*p)

    n = n.astype(int)

    p_up = binom.cdf(x_low, n, p)\
        + binom.sf(x_high-1, n, p)
    
    p_down = binom.cdf(x_low-1, n, p)\
        + binom.sf(x_high, n, p)
    
    U = np.random.rand(x.shape[0])
    prob = np.minimum(p_down + (p_up-p_down)*U, 1)
    return prob * (n != 0) + U * (n == 0)

def binom_var_test_df(c1, c2, sym=False, max_m=-1) :
    """ Binmial variance test along stripes. 
        This version returns all sub-calculations
    Args:
    ----
    c1, c2 : list of integers represents count data from two sample
    sym : flag indicates wether the size of both sample is assumed
          identical, hence p=1/2
    """

    df_smp = pd.DataFrame({'n1' : c1, 'n2' : c2})
    df_smp.loc[:,'N'] = df_smp.agg('sum', axis = 'columns')
    
    if max_m > 0 :
        df_smp = df_smp[df_smp.n1 + df_smp.n2 <= max_m]
        
    df_hist = df_smp.groupby(['n1', 'n2']).count().reset_index()
    df_hist.loc[:,'m'] = df_hist.n1 + df_hist.n2
    df_hist = df_hist[df_hist.m > 0]
    
    df_hist.loc[:,'N1'] = df_hist.n1 * df_hist.N
    df_hist.loc[:,'N2'] = df_hist.n2 * df_hist.N

    df_hist.loc[:,'NN1'] = df_hist.N1.sum()
    df_hist.loc[:,'NN2'] = df_hist.N2.sum()

    df_hist = df_hist.join(df_hist.filter(['m', 'N1', 'N2', 'N']).groupby('m').agg('sum'),
                           on = 'm', rsuffix='_m')
    if max_m == -1 :
        df_hist = df_hist[df_hist.N_m > np.maximum(df_hist.n1, df_hist.n2)]

    df_hist.loc[:,'p'] = df_hist['NN1'] / (df_hist['NN1'] + df_hist['NN2'])

    df_hist.loc[:,'s'] = (df_hist.n1 - df_hist.m * df_hist.p) ** 2 * df_hist.N
    df_hist.loc[:,'Es'] = df_hist.N_m * df_hist.m * df_hist.p * (1 - df_hist.p)
    df_hist.loc[:,'Vs'] = 2 * df_hist.N_m *  df_hist.m * (df_hist.m) * ( df_hist.p * (1 - df_hist.p) ) ** 2
    df_hist = df_hist.join(df_hist.groupby('m').agg('sum').s, on = 'm', rsuffix='_m')
    df_hist.loc[:,'z'] = (df_hist.s_m - df_hist.Es) / np.sqrt(df_hist.Vs)
    #df_hist.loc[:,'pval'] = df_hist.z.apply(lambda z : norm.cdf(-np.abs(z)))
    df_hist.loc[:,'pval'] = df_hist.z.apply(lambda z : norm.sf(z))

    # handle the case m=1 seperately
    n1 = df_hist[(df_hist.n1 == 1) & (df_hist.n2 == 0)].N.values
    n2 = df_hist[(df_hist.n1 == 0) & (df_hist.n2 == 1)].N.values
    if len(n1) + len(n2) >= 2 :
        df_hist.loc[df_hist.m == 1, 'pval'] = binom_test_two_sided(n1, n1 + n2 , 1/2)[0]

    return df_hist

def binom_var_test(c1, c2, sym=False, max_m=-1) :
    """ Binmial variance test along stripes
    Args:
    ----
    c1, c2 : list of integers represents count data from two sample
    sym : flag indicates wether the size of both sample is assumed
          identical, hence p=1/2
    """
    df_hist = binom_var_test_df(c1, c2, sym=sym, max_m=max_m)
    return df_hist.groupby('m').pval.mean()

def two_sample_pvals(c1, c2, randomize=False, sym=False, alt='two-sided'):
    logging.warning("two_sample_pvals is deprecated. Use two_sample_binomial_test instead")
    return two_sample_binomial_test(c1, c2, randomize=randomize, sym=sym, alt=alt)

def two_sample_binomial_test(c1, c2, randomize=False,
     sym=False, alt='two-sided', ret_p=False):

    """ two-sample binomial allocation test

    Args:
    ----
    c1, c2 : list of integers represents count data from two sample
    randomize : flag indicate wether to use randomized P-values
    sym : flag indicates wether the size of both sample is assumed
          identical, hence p=1/2
    alt :  how to compute P-values. 
    """

    T1 = c1.sum()
    T2 = c2.sum()

    den = (T1 + T2 - c1 - c2)
    if den.sum() == 0 :
        return c1 * np.nan

    p = ((T1 - c1) / den)*(1-sym) + sym * 1./2

    if alt == 'greater' or alt == 'less' :
        pvals = binom_test(c1, c1 + c2, p, alt=alt)
    elif randomize :
        pvals = binom_test_two_sided_random(c1, c1 + c2, p)
    else :
        pvals = binom_test_two_sided(c1, c1 + c2, p)

    if ret_p :
        return pvals, p
    return pvals

def two_sample_test_df(c1, c2, gamma=0.2, min_cnt=0,
                stbl=True, randomize=False, 
                alt='two-sided', HCtype='HCstar'):
    """
    Same as two_sample_test but returns all information for computing
    HC score of the two samples as a pandas data DataFrame. 
    Requires pandas.

    Args: 
    -----
    c1, c2       lists of integers of equal length
    gamma      parameter of HC statistic
    stbl       parameter of HC statistic
    randomize  use randomized or not exact binomial test
    alt        type of test alternatives: 'two-sided' or 'one-sided'
    HCtype     either 'HCstar' (default) or 'standard'. Determine
               different variations of HC statistic 

    Returns:
    -------
    counts : DataFrame with fields: 
            n1, n2, p, T1, T2, pval, sign, HC, thresh
            Here: 
            -----
            'n1' <- X
            'n2' <- Y
            'T1' <- sum(X)
            'T2' <- sum(Y)
            'p' <- (T1 - n1) / (T1+ T2 - n1 - n2)
            'pval' <- binom_test(n1, n1 + n2, p) (P-value of test)
            'sign' :    indicates whether a feature is more frequent 
                    in sample X (+1) or sample Y (-1)
            'HC' :      is the higher criticism statistic applies to the
                    column 'pval'
            'thresh' :  indicates whether a feature is below the HC 
                        threshold (True) or not (False)
    """
    assert len(c1) == len(c2)

    counts = pd.DataFrame()
    counts['n1'] = c1
    counts['n2'] = c2
    T1 = counts['n1'].sum()
    T2 = counts['n2'].sum()
    
    counts['T1'] = T1
    counts['T2'] = T2

    counts['pval'], counts['p'] = two_sample_binomial_test(
        counts['n1'], counts['n2'],
        randomize=randomize, alt=alt, ret_p=True)

    counts['sign'] = np.sign(counts.n1 - (counts.n1 + counts.n2) * counts.p)

    counts.loc[counts.n1 + counts.n2 < min_cnt, 'pval'] = np.nan
    pvals = counts.pval.values
    hc = HigherCriticism(pvals[~np.isnan(pvals)], stbl=stbl)

    if HCtype == 'standard' :
        hc, p_val_thresh = hc.HC(gamma=gamma)
    else:
        hc, p_val_thresh = hc.HCstar(gamma=gamma)

    counts['HC'] = hc

    counts['thresh'] = True
    counts.loc[counts['pval'] >= p_val_thresh, ('thresh')] = False
    counts.loc[np.isnan(counts['pval']), ('thresh')] = False
    
    return counts

