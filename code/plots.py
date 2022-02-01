from matplotlib import pyplot
import numpy

#plots for the paper are created using the ecdf and cdf
#this function will return the ecdf of the data
def ecdf(data):
    x1 = numpy.sort(data)
    x = x1.tolist()
    n = len(x)
    p = 1/n
    pvalues = list(numpy.linspace(p,1,n))
    return x, pvalues
#to get the staircase plot for ecdf 
def stairs(data):
    def stepdata(x,y): # x,y must be python list
        xx,yy = x*2, y*2
        xx.sort()
        yy.sort()
        return xx, [0.]+yy[:-1]
    x, p = ecdf(data)
    x, y = stepdata(x,p)
    return x, y


def binit(x,m_range,r_range):
    M = x[:,1]
    R = x[:,2]
    m_to_keep = (M>m_range[0]) & (M<=m_range[1])
    r_to_keep = (R>r_range[0]) & (R<=r_range[1])
    index_to_keep = m_to_keep & r_to_keep
    return x[index_to_keep,:]


def plot_figure_ranking(X_arr,Mw_ranges,Rh_ranges):
    binned_datasets=[]
    for mwrange in Mw_ranges:
        for rhrange in Rh_ranges:
            binned_datasets.append(binit(X_arr,mwrange,rhrange))

    M_range = [r'$M_w \in [-0.25,1]$', r'$M_w \in [1,2]$', r'$M_w \in [2,3]$', r'$M_w \in [-0.25,3]$']
    R_range = [r'$R \in [0,10]$', r'$R \in [10,25]$', r'$R \in [0,25]$']


    fig,ax = pyplot.subplots(nrows=4+1,ncols=3+1,figsize=(16,16))
    colors = numpy.linspace(0, 1, 10)

    k=0
    for i in range(4+1):
        for j in range(3+1):
            if i == 0:
                ax[i,j].set_xticks([])
                ax[i,j].set_yticks([])
                ax[i,j].axis('off')
                if j>0:
                    ax[i,j].text(0.25,0.2,R_range[j-1],fontsize=18)
            elif j == 0:
                ax[i,j].set_xticks([])
                ax[i,j].set_yticks([])
                ax[i,j].axis('off')
                if i>0:
                    ax[i,j].text(0.15,0.5,M_range[i-1],fontsize=18)
            else:
                if k<12:
                    X_ij = binned_datasets[k]
                    x,y = stairs(list(numpy.log10(X_ij[:,5])))
                    ax[i,j].plot(x,y,label='Observed data')
                    ax[i,j].grid()
                    ax[i,j].tick_params(grid_alpha=0.5)
                    ax[i,j].legend(fontsize=12)
            #         if i == 0:
            #             ax[i,j].set_xlabel(M_range[j],fontsize=20)
            #         if j == 0:
            #             ax[i,j].set_ylabel(R_range[i],fontsize=20)
                    k+=1
            if i==4:
                ax[i,j].set_xlabel(r'$\log10 (PGA \ $cm$^2$/s)',fontsize=14)
            if j==1:
                ax[i,j].set_ylabel('Probability',fontsize=14)
                
            

    # .xticks([0.5], [0.5])

    pyplot.tight_layout(pad=1.3)                            
