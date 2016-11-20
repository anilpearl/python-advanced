from sklearn import tree

#100,0,3,23 => 0(ny)
#120,1,4,45 => 1(sfo)
#200,3,4,65 => 1(sfo)
#3300,3,4,54 => 1(sfo)
#
#300,1,6 => ?  0 (ny) or will the output be 1(sfo)
#300,1,6,10,7 => ?

X = [[0, 0, 3], #nw york (0)
     [1, 1, 4], #sfo (1)
     [2, 3, 4], #sfo (1)
     [3, 3, 4]]  #sfo (1)
     
Y = [0, 1, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

print("{0}".format(clf.predict(
    [[300, 1, 4]])))
     
    
#print("{0}".format(clf.predict_proba(
#    [[2, 2, 4],
#     [0, 0, 3],
#     [2, 3, 4]])))