def get_val(x):
    #return game[x]
    return game.get(x)

if __name__ == "__main__":
    filename = "captains.txt"
    game = dict()
    with open(filename) as fh:
        headers = next(fh)
        data = fh.read()

    data = data.split('\n')
    #create a dictionary
    for item in data:
        name = item.split(',')[0]
        matches = int(item.split(',')[2])
        game[name] = matches

    # sort based on names
    sorted_keys = sorted(game)
    for keys in sorted_keys:
        print(keys, game[keys])

    print('-'*100)
    #sort based on number of matches
    for keys in sorted(game, key=get_val, reverse=True)[:5]:
        print(keys, game[keys])
