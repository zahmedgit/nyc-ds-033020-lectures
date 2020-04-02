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
    
#albumWithMostTopSongs 
#- returns the name of the artist and album that has that most songs featured on the top 500 songs list Maybe
def mostTopSongs(song_list,album_list):
    count,album=0,''
    for i in album_list:
        x=0
        for song in song_list:
            for track in i['tracks']:
                if song['name']==track:
                    x+=1
                    break

        if x>count:
            count=x
            album=i['album']
    return [album,count]

#albumsWithTopSongs 
#- returns a list with the name of only the albums that have tracks featured on the list of top 500 songs Maybe
def albums_withTopSongs(album_list,song_list):
    albums=[]
    for i in album_list:
        x=0
        for song in song_list:
            for track in i['tracks']:
                if song['name']==track:
                    x+=1
                    break

        if x>0:
            albums.append(i['album'])
    return albums

#songsThatAreOnTopAlbums 
#- returns a list with the name of only the songs featured on the list of top albums
def song_onTopAlbums(album_list, track_list):
    feature_songs=[]
    for data_dict in album_list:
        feature_songs.append(find_name(data_dict['album'],track_list)['tracks'])
    return feature_songs

#topOverallArtist 
#- Artist featured with the most songs and albums on the two lists. This means that if Brittany Spears had 3 of her albums featured on the top albums listed and 10 of her songs featured on the top songs, she would have a total of 13. The artist with the highest aggregate score would be the top overall artist. Easy
def topOverallArtist(song_list, album_list):
    artists_songs = list_artists(song_list)
    artists_albums = list_artists(album_list)
    artists_songs.extend(artists_albums)
    # for artists in artists_list:
    count,top_artist=0,''
    for artist in list(set(artists_songs)):
        if artists_songs.count(artist)>count:
            count,top_artist = artists_songs.count(artist),artist
    # print(top_artist+":",count)
    return top_artist


