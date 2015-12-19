# Compare my current submission with the previous one (the prediction 
# accuracy of the latter is known).

import sys
import csv

new_subm = sys.argv[1]
old_subm = sys.argv[2]

def get_prediction(file_path):
    with open(file_path, 'r') as f:
        result = csv.reader(f, delimiter=',')
        prediction = [(idx, cuisine) for (idx, cuisine) in result]

    return prediction


new_prediction = get_prediction(new_subm)
old_prediction = get_prediction(old_subm)

n = len(new_prediction)
assert n == len(old_prediction)

same = 0
for ((id1, cs1), (id2, cs2)) in zip(new_prediction, old_prediction):
    assert id1 == id2
    if cs1 == cs2:
        same += 1

print "%d/%d = %f" % (same, n, same * 1.0 / n)
