from fsds.imports import *

def plot_sample_rug(male_sample):
    """Plots a rugplot of the sample"""
    ## Plot Male Heights
    ax = sns.rugplot(male_sample,height=0.5)
    ax.get_figure().set_size_inches(10,3)
    ax.set(title='Observed Male Heights', xlabel='Height (inches)')
    
    sides = ['top','left','right']
    [ax.spines[side].set_visible(False) for side in sides] 
    ax.yaxis.set_visible(False)
    return ax


from scipy import stats

def plot_sample_dist(male_sample,mean,std):
    """Plots the sample vs a pdf generated using the mean and std 
    provided. 
    """
    ## Make even number of observations
    xs = np.linspace(male_sample.min(),
                     male_sample.max(),
                     len(male_sample))
    
    ## Get PDF of guessed mean and std
    pdf = stats.norm.pdf(xs,loc=mean,scale=std)
    

    ## Plot Results
    fig,ax = plt.subplots(figsize=(10,3))
    sns.rugplot(male_sample,ax=ax,height=0.2)
    ax.plot(xs,pdf,label='PDF')
    
    ## Annotate input mean and std
    ax.axvline(mean,color='k',ls=':',
              label=f"Mean={mean}")
    
    ## Set labels, title
    ax.set(ylabel='Density', 
          title=f"Normal Distribution with Mean={mean}, std={std}")
     
    ## Final aesthetic tweaks
    sides = ['top','right']
    [ax.spines[side].set_visible(False) for side in sides] 
    ax.legend()
    
    return fig,ax