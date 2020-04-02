#Find by Name
def find_name(name, data_dicts):
    for data_dict in data_dicts:
        if data_dict['album']==name:
            return data_dict
            
    return None

#Find by Artist
def find_artist(name, data):
    for data_dict in data:
        if data_dict['artist']==name:
            return data_dict
            
    return None


#Find by Rank
def find_rank(rank, datadicts):
    for data_dict in datadicts:
        if data_dict['number']==str(rank):
            return data_dict
            
    return None

#Find by Year
def find_year(year, data_dicts):
    albums = []
    for data_dict in data_dicts:
        if data_dict['year']==str(year):
            albums.append(data_dict)
            
    return albums

#Find by Years
def find_years(start, end, data_dicts):
    albums = []
    for data_dict in data_dicts:
        if int(data_dict['year'])>=int(start) and int(data_dict['year'])<=int(end):
            albums.append(data_dict)
            
    return albums

#Find by Ranks
def find_ranks(start, end, data_dicts):
    albums = []
    for data_dict in data_dicts:
        if int(data_dict['number'])>=int(start) and int(data_dict['number'])<=int(end):
            albums.append(data_dict)
            
    return albums

#All Titles
def list_titles(data_dicts):
    titles=[]
    for data_dict in data_dicts:
        titles.append(data_dict['album'])
    return titles

#All Artists
def list_artists(data_dicts):
    artists=[]
    for data_dict in data_dicts:
        artists.append(data_dict['artist'])
    return artists

#Question: Artists with Most Top Albums
def top_artist(data):
    artists = list_artists(data)
    count,top_artist=0,''
    for artist in set(artists):
        if artists.count(artist)>count:
            count,top_artist = artists.count(artist),artist
    # print(top_artist+":",count)
    return top_artist

def top_artistCount(data):
    artists = list_artists(data)
    count,top_artist=0,''
    for artist in set(artists):
        if artists.count(artist)>count:
            count,top_artist = artists.count(artist),artist
    # print(top_artist+":",count)
    return count

#Question: Most Popular Word in Album Titles
def pop_word(data):
    titles = list_titles(data)
    words=''
    count, top_word = 0,''
    for title in titles:
        title=title.replace('/',' ')
        title=title.replace('[','')
        words= words+' '+title.lower()
    for word in set(words.split()):
        if words.split().count(word)>count:
            count,top_word = words.split().count(word),word
    return top_word

#HIstogram Albums by decade
def hist_decades(data):
    years = []
    for data_dict in data:
        years.append(int(data_dict['year']))
    plt.hist(years, bins=range(1940,2010,10), edgecolor='black')
    plt.show()
    
#HIstogram Albums by genre
def hist_genre(data):
    genres = []
    for data_dict in data:
        genre=data_dict['genre'].title().replace(', ',',').split(',')
    #     genre.replace(', ',',')

        genres.extend(genre)
    fig=plt.figure(figsize=(16,4))
    plt.hist(genres, edgecolor='black')
#     print(set(genres))
    plt.show()

