import numpy as np

school_scores = [{"school_class": "4a", "scores":[3,3,5,4,2,5]},{"school_class":"4b", "scores": [2,2,4,5,3]},{"school_class":"4c", "scores":[5,5,5,4,5,5]}]    

midle_rating = None
for school_class in school_scores:
    class_midle_rating = sum(school_class["scores"])/len(school_class["scores"])
    if midle_rating is None:
        midle_rating = class_midle_rating
    else:
        midle_rating = (midle_rating + class_midle_rating)/2.0  
print(midle_rating)
   
for scores in school_scores:
    print(np.mean(scores["scores"]))