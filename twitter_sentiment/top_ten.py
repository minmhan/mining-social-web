import sys
import json

def hw():
    hashtag = {}
    with open(sys.argv[1],'r') as t:
        for line in t:
            data = json.loads(line)
            if 'entities' not in data: continue;
            if len(data['entities']['hashtags']) == 0: continue;
            for dic in data['entities']['hashtags']:
                if not dic['text'] in hashtag:
                    hashtag[dic['text']] = 1
                else:
                    hashtag[dic['text']] += 1

    #print hashtag
    top_10_list = sorted(hashtag,key=hashtag.get,reverse=True)[:10]
    for ht in top_10_list:
        print(ht, '%.1f' % hashtag[ht])
            
            
# usage: happiest_state.py sentiment.txt twitter_stream.txt
def main():
    hw()

if __name__ == '__main__':
    main()

