import sys
import json

#TODO: fix
def hw():
    # open sentiment file store words in dictionary
	sent = {}
	with open(sys.argv[1],'r') as s:
		for line in s:
			key,val = line.split('\t')[0],line.split('\t')[1]
			sent[key] = val
   
    data = {}
    with open(sys.argv[2],'r') as t:
    		for line in t:
    			sent_val = 0
    			data = json.loads(line)
    			if 'text' not in data: continue;
     			tweet_string = data['text'].lower()
    			for d in sent.keys():
    				if d in tweet_string:
    					sent_val += float(sent[d])

    			print(sent_val)


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
