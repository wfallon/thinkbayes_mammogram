from thinkbayes import Suite

class mammogram(Suite):
    
    #redefine init to account for probability of cancer within population
    def __init__(self, hypos):
        Suite.__init__(self)
        for hypo in hypos:
            if(hypo == 'No_Cancer'):
                self.Set(hypo, .99)
            else:
                self.Set(hypo, .01)

    mixes = {
        #define the probability of mammogram giving positive result for both patients with
        #no cancer and patients with cancer
        'No_Cancer':dict(positive=0.07),
        'Yes_Cancer':dict(positive=0.87),
    }

    #Define likelihood as the data entry in mixes for each hypo
    def Likelihood(self, data, hypo):
        mix = self.mixes[hypo]
        like = mix[data]
        return like

def main():
    #define hypos
    hypos = ['No_Cancer', 'Yes_Cancer']
    
    #initialize mammogram object
    mam = mammogram(hypos)
    
    #call update
    mam.Update('positive')
    
    for hypo, prob in mam.Items():
        print hypo, prob


if __name__ == '__main__':
    main()
