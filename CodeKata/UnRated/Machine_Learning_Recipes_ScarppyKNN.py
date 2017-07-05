#import random
from scipy.spatial import distance

def euc(a,b):
    return distance.euclidean(a,b)


class ScarppyKNN():

    def fit(self , X_train, Y_train):
        self.X_train = X_train
        self.Y_train = Y_train

    def predict(self, X_Test):
        predictions = []
        for row in X_Test:
            #label = random.choice(self.Y_train)
            label = self.closest(row)
            predictions.append(label)
        return predictions

    def closest(self, row):
        best_dist = euc(row, self.X_train[0])
        best_index = 0
        for i in range(1, len(self.X_train)):
            dist = euc(row, self.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.Y_train[best_index]



from sklearn import datasets
iris = datasets.load_iris()

x = iris.data
y = iris.target

from sklearn.cross_validation import train_test_split

X_train, X_Test ,Y_train, Y_test = train_test_split(x, y, test_size = .5)

#from sklearn import tree
#myclassifier  = tree.DecisionTreeClassifier()

#from sklearn.neighbors import KNeighborsClassifier
#myclassifier = KNeighborsClassifier()

myclassifier = ScarppyKNN()

myclassifier.fit(X_train, Y_train)

predictions = myclassifier.predict(X_Test)


from sklearn.metrics import accuracy_score


print (accuracy_score(Y_test , predictions) )



