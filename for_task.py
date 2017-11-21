import numpy as np

school_scores = [{"school_class": "4a", "scores":[3,3,5,4,2,5]},{"school_class":"4b", "scores": [2,2,4,5,3]},{"school_class":"4c", "scores":[5,5,5,4,5,5]}]


for scores in school_scores:
    print (np.mean(scores["scores"]))