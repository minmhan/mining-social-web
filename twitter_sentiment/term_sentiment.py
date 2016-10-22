import sys
import json

def hw():
    sent = {}
    with open(sys.argv[1],'r') as s:
        for line in s:
            key,val = line.split('\t')[0], line.split('\t')[1]
            sent[key] = val

    data = {}
    sent_new = {}
    with open(sys.argv[2],'r') as t:
        for line in t:
            sent_sum = 0
            data = json.loads(line)
            if 'text' not in data: continue;
            tweet_string = data['text']
            tweet_words = tweet_string.split()
            for t in tweet_words:
                if t in sent:
                    sent_sum += float(sent[t])

            if sent_sum == 0: continue;
            for tw in tweet_words:
                if tw not in sent:
                    if tw not in sent_new:
                        sent_new[tw] = sent_sum
                    else:
                        sent_new[tw] += sent_sum

    for ns in sent_new.keys():
        print(ns,":", sent_new[ns])


def lines(fp):
    print(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
