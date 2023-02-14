import imdb
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# # Create your views here.
moviesDB = imdb.IMDb()


# fetching top movies

def index(request):
    # top = moviesDB.get_top250_movies()  
    # args = {}  
    # args['movies'] = top[0:14]     
    return render(request, 'stream/home.html')


# view more button
# def More(request):
#     top = moviesDB.get_top250_movies()
#     args = {}  
#     args['movies'] = top[14:29]
#     return render(request, 'stream/home.html',args)


#  1) Search for a title
@csrf_exempt
def search_name(request):
    name = request.POST['name']
    searched = moviesDB.search_movie(name)
    print(searched[0].data, "P")
    args = {}
    args['movies'] = searched[0:9]
    for m in args['movies']:
        m['img'] = m['cover url']
    #    print(searched[0].data)
    #    if (searched.data):
    return render(request, 'stream/searchedout.html', args)


# playing page

def movie_details(request, id):
    movie = moviesDB.get_movie(id)
    args = {}
    args['movie'] = movie

    return render(request, 'stream/moviedetails.html', args)


# passing data
def season_episode(request):
    # season=1
    # args = {}
    ep = 'you'
    return render(request, 'stream/seriesdetails.html', context={'episode': ep})


def series_details(request, id):
    series = moviesDB.get_movie(id)
    moviesDB.update(series, 'episodes')
    # getting episodes of the series
    episodes = series.data['episodes']
    # print(episodes)
    # for i in episodes.keys():
    #     n = len(episodes[i])
    #     print("Total Episodes in Season " + str(i) + " : " + str(n))
    args = {}
    args['movie'] = series
    args['episodes'] = episodes
    return render(request, 'stream/seriesdetails.html', args)


# buttons

def top_movies(request):
    top = moviesDB.get_top250_movies()
    args = {}
    args['movies'] = top[0:20]
    return render(request, 'stream/TopMoviesSearch.html', args)


def bottom_movies(request):
    bottom = moviesDB.get_bottom100_movies()
    args = {}
    args['movies'] = bottom[0:20]
    return render(request, 'stream/BottomMoviesSearch.html', args)


def series_page(request):
    top = moviesDB.get_top250_movies()
    args = {}
    args['movies'] = top[0:20]
    return render(request, 'stream/SeriesSearch.html', args)
