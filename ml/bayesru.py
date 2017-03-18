# http://habrahabr.ru/post/120194/
# http://bazhenov.me/blog/2012/06/11/naive-bayes.html

from __future__ import division
from collections import defaultdict
from math import log

def train(samples):
    classes, freq = defaultdict(lambda:0), defaultdict(lambda:0)
    for feats, label in samples:
        classes[label] += 1                 # count classes frequencies
        for feat in feats:
            freq[label, feat] += 1          # count features frequencies

    for label, feat in freq:                # normalize features frequencies
        freq[label, feat] /= classes[label]
    for c in classes:                       # normalize classes frequencies
        classes[c] /= len(samples)

    return classes, freq                    # return P(C) and P(O|C)

def classify(classifier, feats):
    classes, prob = classifier
    return min(classes.keys(),              # calculate argmin(-log(C|O))
        key = lambda cl: -log(classes[cl]) + \
            sum(-log(prob.get((cl,feat), 10**(-7))) for feat in feats))


def test(classifier, test_set):
    hits = 0
    for feats, label in test_set:
        if label == classify(classifier, feats):
            hits += 1
    return hits/len(test_set)

def get_features(sample): return (
        'll: %s' % sample[-1],          # get last letter
        'fl: %s' % sample[1],           # get first letter
        'sl: %s' % sample[0],           # get second letter
        )

if __name__ == '__main__':
    samples = (line.decode('utf-8').split() for line in open('names.txt'))

    features = [(get_features(feat), label) for feat, label in samples]
    N_REC= 20  # in names.txt file?
    #train_set, test_set = features[:-100], features[-100:]
    train_set, test_set = features[:-N_REC], features[-N_REC:]

    print "len(features)=", len(features)
    print "len(train_set)=", len(train_set)
    print "train_set=", train_set
    print "len(test_set)=", len(test_set)
    print "test_set=", test_set
    classifier = train(train_set)
    print 'Accuracy: ', test(classifier, test_set)
