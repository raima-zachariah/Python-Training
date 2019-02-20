if __name__ == "__main__":
    filename = "captains.txt"
    captain_info = list()
    with open(filename) as fh:
        headers = next(fh)
        data = fh.read().split('\n')
        
    for line in data:
        details = dict()
        details['name'] = line.split(',')[0]
        details['match'] = int(line.split(',')[2])
        details['won'] = int(line.split(',')[3])
        details['lost'] = int(line.split(',')[4])
        captain_info.append(details)

    for captain in captain_info:
        captain['winPerc'] = (captain['won'] * 100)/ captain ['match']
        
    print(captain_info)
    print("-----------------------------------")

    
    sort_winPerc = sorted(captain_info, key=lambda x: x['winPerc'], reverse=True)
    print("Captain with heighest Win Percentage is:", sort_winPerc[0]['name'])
    print("-----------------------------------")
    print("Top 5")
    print("-----------------------------------")
    for cap in sort_winPerc[:5]:
        print(cap['name'])
        
    print("Top 5 who playe d more than 5 matches")
    print("-----------------------------------")
    cap_5 = [ cap for cap in captain_info if cap['match'] > 5]
    
    exp_captains = sorted(cap_5, key = lambda x: x['winPerc'], reverse=True)
    for cap in exp_captains[:5]:
        print(cap['name'])
    #captain_info = []
    #key_headers = ['name', 'match', 'won', 'lost']
    #for line in data:
    #    ld = line.split(',')
    #    name, match, won, lost = ld[0],ld[2],ld[3],ld[4]
    #    det = [name,match,won,lost]
    #    captain_info.append(dict(zip(key_headers,det)))
    #print("####")  
    #print(captain_info)
