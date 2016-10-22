import sys
import json

def hw():
    data = {}
    sent_new = {}
    
    with open(sys.argv[1],'r') as t:
        for line in t:
            data = json.loads(line)
            if 'text' not in data: continue;
            tweet_string = data['text']
            tweet_words = tweet_string.split()
            for w in tweet_words:
                if w in sent_new:
                    sent_new[w] = sent_new[w]+1
                else:
                    sent_new[w] = 1


    keycount = len(sent_new)
    for w in sent_new.keys():
        print(w, ': %1.4f' % (sent_new[w]/float(keycount)))

#usage: frequency.py twitter_stream.txt 
def main():
    tweet_file = open(sys.argv[1])
    hw()
    

if __name__ == '__main__':
    main()
