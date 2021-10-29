import numpy

filename = 'pnr_new.csv'

def readcsvfile(fullpath,sep=','):

    with open(fullpath,"r") as f:
        X = []
        h=[]
        for x in f:
            if sep==',': # comma
                xx = x.split(',')
            elif sep==' ': # space
                xx = x.split(' ')
            elif sep==' ': # tab
                xx = x.split('  ')
            acceptline = True
            for xi in xx[2:]:
                try:
                    float(xi)
                except: 
                    acceptline=False
                # X.append([float(xi) for xi in xx])
            if acceptline: 
                X.append(xx[2:])
    return X


def filter_nans(d):
    newd=[]
    for r,line in enumerate(d):
        isnotnan = True
        for c,l in enumerate(line):
            if d[r][c]=='NaN':
                isnotnan=False
            if c==7:
                d[r][c]=l.strip()
        if isnotnan:
            newd.append(numpy.asarray(d[r],dtype=float))
    return newd


# if __name__ == '__main__':

#     x = readcsvfile(filename)

#     print(x[:4])