from django.core.management.base import BaseCommand, CommandError
from Movies.models import Movie

from django.core.files.base import ContentFile
import shelve
import urllib.request, urllib.parse, urllib.error
from django.conf import settings

class Command(BaseCommand):

    def handle(self,*arg,**options):
        SFile=shelve.open(settings.MOVIEDATA_FILE)
        Shelf=shelve.open(settings.PATHS_FILE)
        for (movie,path) in zip(SFile['Movies'],Shelf['Paths']):
            mov=Movie()
            try:
                ex = Movie.objects.filter(Name=movie['title']).exists()
            except Exception as fault:
                self.stdout.write("Got:fault {0} for {1}:{2}: \n path:{3}".format(str(fault), str(mov), str(movie), str(path)))
                continue

            if not ex:
                try:
                    mov.Name=movie['title']
                except:
                    mov.Name="Not Available"
                try:
                    mov.Year=movie['year']
                except:
                    mov.Year="Not Available"
                try:
                    mov.Plot=''.join(movie['plot'])
                    mov.Plot_outline=''.join(movie['plot outline'])
                except:
                    mov.Plot="Not Available"
                    mov.Plot_outline="Not Available"
                try:
                    mov.Genre=' '.join(movie['genres'])
                except:
                    mov.Genre="Not Available"
                try:
                    mov.Imdb_rating=movie['rating']
                except:
                    mov.Imbd_rating=0.0
                d=''
                try:
                    for name in movie['director']:
                        d+=','+str(name)
                        mov.Director=d.strip(',')
                except:
                    mov.Director="Not Available"
                try:
                    url=movie['full-size cover url']
                    mov.Poster.save(movie['title']+'.jpg',ContentFile(urllib.request.urlopen(url).read()))
                except:
                    mov.Poster=None
                if mov.Name =="Not Available" or 'TV' in mov.Genre or 'Show' in mov.Genre:
                    SFile['Movies'].remove(movie)
                else:
                    mov.Path=path
                    mov.save()
                    self.stdout.write(mov.Name)
            self.stdout.write(movie['title'])
        Shelf.close()
        SFile.close()
