import pandas as pd
import numpy as np

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('F:/DataScience/DataScience-Python3/ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv('F:/DataScience/DataScience-Python3/ml-100k/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)

userRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')

corrMatrix = userRatings.corr()

x=int(input('Enter the minimum numbers of users who have rated the movies ....'))
corrMatrix = userRatings.corr(method='pearson', min_periods=x)


y= np.random.randint(944)
myRatings = userRatings.loc[y].dropna()
#myRatings

rdmovies = pd.Series()
for i in range(0, len(myRatings.index)):
    print ("Adding movies for " + myRatings.index[i] + "...")
    # Retrieve similar movies to this one that I rated
    movies= corrMatrix[myRatings.index[i]].dropna()
    # Now scale its similarity by how well I rated this movie
    movies = movies.map(lambda x:(x * myRatings[i]))
    # Add the score to the list of recommended movies
    rdmovies = rdmovies.append(movies)
    

rdmovies.sort_values(inplace = True, ascending = False)
#print (rdmovies.head(10))


rdmovies = rdmovies.groupby(rdmovies.index).sum()

rdmovies.sort_values(inplace = True, ascending = False)
#size=len(myRatings.index)

'''if('Return of the Jedi (1983)' in rdmovies.index):
    print('working')
'''
lis=[]
for j in myRatings.index:
    if(j in rdmovies.index):
        lis.append(j)
        #rdmvies=rdmovies.drop([str(j)])
#rdmovies=rdmovies.drop(['Empire Strikes Back, The (1980)'])

filtermovies = rdmovies.drop(lis)
print("Recommended movies for the given user :         ")
print(filtermovies.head(10))


