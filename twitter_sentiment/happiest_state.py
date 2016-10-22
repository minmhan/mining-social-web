import sys
import json

def hw():
    sent = {}
    with open(sys.argv[1],'r') as s:
        for line in s:
            key,val = line.split('\t')[0], line.split('\t')[1]
            sent[key] = val
    
    data = {}
    state_sentiment = {}
    print(sys.argv[1])
    with open(sys.argv[2],'r') as t:
        for line in t:
            sent_val = 0
            data = json.loads(line)
            #if 'user' not in data: continue;
            #print data['user']['location']

            if 'text' not in data: continue;
            if 'place' not in data: continue;
            if data['place'] is None: continue;
            if data['place']['country_code'] != 'US': continue;
            if data['place']['full_name'] is None: continue;
            if len(data['place']['full_name'].split(',')) != 2: continue;
            state = data['place']['full_name'].split(',')[1].strip()
            if not state in state_sentiment:
                state_sentiment[state] = 0
            
            
            #if 'coordinates' not in data: continue;
            #if data['coordinates'] is None: continue;
            #print data['coordinates']

            tweet_string = data['text']
            for d in sent.keys():
                if d in tweet_string:
                    sent_val += float(sent[d])    

            state_sentiment[state] += sent_val
            

        #for v in state_sentiment.keys():
        #   print '{0} {1}'.format(v,state_sentiment[v])
        #highest = max(state_sentiment.values())
        #print [k for k,v in state_sentiment.items() if v== highest][0]
      
        print(max(state_sentiment, key=lambda x: state_sentiment.get(x)))
        

def main():
    hw()


if __name__ == '__main__':
    main()
