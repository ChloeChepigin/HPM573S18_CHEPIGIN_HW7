import SurvivalModelClasses as Cls
import scr.SamplePathClasses as SamplePathSupport
import scr.FigureSupport as Fig
import scipy.stats as stat

MORTALITY_PROB = 0.1    # annual probability of mortality
TIME_STEPS = 100        # simulation length
SIM_POP_SIZE = 1000     # population size of the simulated cohort
ALPHA = 0.05            # significance level

# create a cohort of patients
myCohort = Cls.Cohort(id=1, pop_size=SIM_POP_SIZE, mortality_prob=MORTALITY_PROB)

# simulate the cohort
cohortOutcome = myCohort.simulate(TIME_STEPS)

## Question 1 ##
# print the percentage of patients survived beyond 5 years
print('Percentage of patients survived beyond 5 years', myCohort.fiveyearsurvive())


## Question 3 ##
likelihood=stat.binom.pmf(k=400, n=573, p=0.5)
print('the likelihood ration is', stat.binom.pmf(k=400, n=573, p=0.5))