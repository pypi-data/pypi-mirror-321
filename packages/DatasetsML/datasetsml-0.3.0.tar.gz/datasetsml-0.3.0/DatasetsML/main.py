def d1():
    return("""
Outlook,Temperature,Humidity,Windy,PlayTennis
Sunny,Hot,High,False,0
Sunny,Hot,High,True,0
Overcast,Hot,High,False,1
Rainy,Mild,High,False,1
Rainy,Cool,Normal,False,1
Rainy,Cool,Normal,True,0
Overcast,Cool,Normal,True,1
Sunny,Mild,High,False,0
Sunny,Cool,Normal,False,1
Rainy,Mild,Normal,False,1
Sunny,Mild,Normal,True,1
Overcast,Mild,High,True,1
Overcast,Hot,Normal,False,1
Rainy,Mild,High,True,0

""")

def d2():
    return("""
age,Gender,Family,diet,Lifestyle,cholestrol,heartdisease
0,0,1,1,3,0,1
0,1,1,1,3,0,1
1,0,0,0,2,1,1
4,0,1,1,3,2,0
3,1,1,0,0,2,0
2,0,1,1,1,0,1
4,0,1,0,2,0,1
0,0,1,1,3,0,1
3,1,1,0,0,2,0
1,1,0,0,0,2,1
4,1,0,1,2,0,1
4,0,1,1,3,2,0
2,1,0,0,0,0,0
2,0,1,1,1,0,1
3,1,1,0,0,1,0
0,0,1,0,0,2,1
1,1,0,1,2,1,1
3,1,1,1,0,1,0
4,0,1,1,3,2,0
""")

def q1():
    return("""
data = [
    ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Yes"],
    ["Sunny", "Warm", "High", "Strong", "Warm", "Same", "Yes"],
    ["Rainy", "Cold", "High", "Strong", "Warm", "Change", "No"],
    ["Sunny", "Warm", "High", "Strong", "Cool", "Change", "Yes"],
]

s=data[1][:-1]

for row in data:
    if row[-1].lower() =="yes":
        for i in range(len(s)):
            if row[i]!=s[i]:
                s[i]='?'
    

print("\nFinal specific hypothesis:\n",s)
""")

def q2():
    return("""
data = [
    ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Yes"],
    ["Sunny", "Warm", "High", "Strong", "Warm", "Same", "Yes"],
    ["Rainy", "Cold", "High", "Strong", "Warm", "Change", "No"],
    ["Sunny", "Warm", "High", "Strong", "Cool", "Change", "Yes"],
]

s=data[1][:-1]
g=[['?' for _ in range(len(s))] for __ in range(len(s))]

for row in data:
    if row[-1].lower() == "yes":
        for i in range(len(s)):
            if row[i]!=s[i]:
                s[i]='?'
                g[i][i]='?'
    
    elif row[-1].lower()=="no":
        for i in range(len(s)):
            if row[i]!=s[i]:
                g[i][i]=s[i]
            else:
                g[i][i]="?"

gh=[]
for row in g:
    if not all([row[i] == "?" for i in range(len(row))]):
        gh.append(row)

print("\nFinal specific hypothesis:\n",s)

print("\nFinal general hypothesis:\n",gh)


""")

def q3():
    return("""
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

df = pd.read_csv("data.csv")

df_encoded = df.copy()
for column in df_encoded.columns[:-1]:
    df_encoded[column] = df_encoded[column].astype('category').cat.codes

X = df_encoded.drop('PlayTennis', axis=1)
y = df_encoded['PlayTennis']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

tree_rules = export_text(clf)
print(tree_rules)

""")

def q4():
    return("""
import numpy as np
X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)
X = X/np.amax(X, axis=0)
y = y/100

class Neural_Network(object):
    def __init__(self):
        self.inputSize = 2
        self.outputSize = 1
        self.hiddenSize = 3
        self.W1 = np.random.randn(self.inputSize, self.hiddenSize)
        self.W2 = np.random.randn(self.hiddenSize, self.outputSize)

    def forward(self, X):
        self.z = np.dot(X, self.W1)
        self.z2 = self.sigmoid(self.z)
        self.z3 = np.dot(self.z2, self.W2)
        o = self.sigmoid(self.z3) 
        return o 

    def sigmoid(self, s):
        return 1/(1+np.exp(-s))

    def sigmoidPrime(self, s):
        return s * (1 - s)
    
    def backward(self, X, y, o):
        self.o_error = y - o
        self.o_delta = self.o_error*self.sigmoidPrime(o)

        self.z2_error = self.o_delta.dot(self.W2.T)
        self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2)

        self.W1 += X.T.dot(self.z2_delta)
        self.W2 += self.z2.T.dot(self.o_delta)

    def train (self, X, y):
        o = self.forward(X)
        self.backward(X, y, o)

NN = Neural_Network()
for i in range(1000):
       print ("\nPredicted Output: \n" + str(NN.forward(X)))
       print ("\nLoss: \n" + str(np.mean(np.square(y - NN.forward(X)))))
       NN.train(X, y)

print ("\nInput: \n" + str(X))
print ("\nActual Output: \n" + str(y))
""")

def q5():
    return("""
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score

df = pd.read_csv("data.csv")

df_encoded = df.copy()
for column in df_encoded.columns[:-1]:
    df_encoded[column] = df_encoded[column].astype('category').cat.codes

X = df_encoded.drop('PlayTennis', axis=1)
y = df_encoded['PlayTennis']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

clf = MultinomialNB()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')

""")

def q6():
    return("""
import pandas as pd
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination
data = pd.read_csv("data2.csv")
heart_disease = pd.DataFrame(data)
model = BayesianNetwork([
 ('age', 'Lifestyle'),
 ('Gender', 'Lifestyle'),
 ('Family', 'heartdisease'),
 ('diet', 'cholestrol'),
 ('Lifestyle', 'diet'),
 ('cholestrol', 'heartdisease'),
 ('diet', 'cholestrol')])
model.fit(heart_disease, estimator=MaximumLikelihoodEstimator)
HeartDisease_infer = VariableElimination(model)
print("\nCPDs for each variable:")
for cpd in model.get_cpds():
    print(cpd)

""")

def q7():
    return("""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

np.random.seed(0)
X = np.vstack((
    np.random.normal([2, 2], 0.5, size=(50, 2)),
    np.random.normal([8, 3], 0.5, size=(50, 2)),
    np.random.normal([5, 8], 0.5, size=(50, 2))
))

k = 3
kmeans = KMeans(n_clusters=k, random_state=0)
kmeans.fit(X)

centers = kmeans.cluster_centers_
labels = kmeans.labels_

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], marker='X', c="red")
plt.savefig('7_plot.png')

""")

def q8():
    return("""
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np

dataset=load_iris()
X_train,X_test,y_train,y_test=train_test_split(dataset["data"], dataset["target"])

kn=KNeighborsClassifier(n_neighbors=1)
kn.fit(X_train,y_train)

for i in range(len(X_test)):
    x=X_test[i]
    x_new=np.array([x])
    prediction=kn.predict(x_new)
    print("TARGET:\t",y_test[i],dataset["target_names"] [y_test[i]],"\tPREDICTED:",prediction,dataset["target_names"][prediction])

print(f"Score: {kn.score(X_test,y_test)}")
""")

def q9():
    return("""
import numpy as np
import matplotlib.pyplot as plt

def locally_weighted_regression(x_train, y_train, x_query, bandwidth):
    weights = np.exp(-((x_train - x_query) ** 2) / (2 * bandwidth ** 2))
    theta = np.sum(weights * y_train) / np.sum(weights)
    return theta

x_train = np.linspace(0, 10, 100)
y_train = np.sin(x_train) + np.random.normal(0, 0.1, len(x_train))

x_query = np.linspace(0, 10, 200)
y_predicted = [locally_weighted_regression(x_train, y_train, x, bandwidth=0.5) for x in x_query]

plt.scatter(x_train, y_train, s=10, label="Training Data")
plt.plot(x_query, y_predicted, color="red", label="LWR Prediction")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.title("Simple Locally Weighted Regression")
plt.savefig('9_plot.png')

""")