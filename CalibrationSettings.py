import scipy.stats as stat


SIM_POP_SIZE = 1000       # population size of simulated cohorts
TIME_STEPS = 1000        # length of simulation
ALPHA = 0.05             # significance level for calculating confidence intervals
NUM_SIM_COHORTS = 500   # number of simulated cohorts used to calculate prediction intervals

# details of a clinical study estimating the mean survival time
OBS_N = 573        # number of patients involved in the study
OBS_alive = 400    # estimated mean survival time
OBS_HL = 1.5      # half-length
OBS_ALPHA = 0.05   # significance level
# the standard deviation of the mean survival time reported in the clinical study
# assumes that the reported confidence interval in this study is a t-confidence interval
OBS_STDEV = OBS_HL / stat.t.ppf(1 - OBS_ALPHA / 2, OBS_N-1)

# how to sample the posterior distribution of mortality probability
# minimum, maximum and the number of samples for the mortality probablity
POST_L, POST_U, POST_N = 0.05, 0.25, 1000


## Question 4 ##
SIM_POP_SIZE = 1000       # population size of simulated cohorts
TIME_STEPS = 1000        # length of simulation
ALPHA = 0.05             # significance level for calculating confidence intervals
NUM_SIM_COHORTS = 1000   # number of simulated cohorts used to calculate prediction intervals

print()POST_L, POST_U, POST_N = 0.05, 0.25, 1000


calibration = Calibration()
calibration.sample_posterior()

# Estimate of mortality probability and the posterior interval
print('Estimate of mortality probability ({:.{prec}%} credible interval):'.format(1-ALPHA, prec=0),
      calibration.get_mortality_estimate_credible_interval(ALPHA, 4))
# effective sample size
txtEff = 'Effective sample size: {:.1f}'.format(calibration.get_effective_sample_size())
print(txtEff)


## Question 5 and 6 - honestly, I was very confused from Question 3 on, I've tried my best organize the code
# but wasn't sure how to continue

# Question 5
calibration = Calibration()
calibration.sample_posterior()
print('Mean survival time and {:.{prec}%} projection interval:'.format(1 - P.ALPHA, prec=0),
      calibrated_model.get_mean_survival_time_proj_interval(P.ALPHA, deci=4))


