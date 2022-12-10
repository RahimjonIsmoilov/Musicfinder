import requests

def getmusic(word):
    n=1
    url=f'https://api.deezer.com/search?q={word}'
    r=requests.get(url)
    res=r.json()
    if 'error' in res.keys():
        return False
    output={}
    senses=res['data']
    music=[]
    for sense in senses:
        music.append(f"{n}.{sense['title']}")
        n+=1
    output['title']="\n".join(music)
    if res['data'][0].get('preview'):
        output['preview']=res['data'][0]['preview']
    return output

if __name__ =='__main__':
    from pprint import pprint as print
    print(getmusic("eminem"))