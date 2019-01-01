import media
import fresh_tomatoes
push_ups = media.Movie("Push Up","Story about a boy whose toys come to life","file:///home/dexter/Desktop/projects/ml/DoItRight/msgifs/icon1.jpg","file:///home/dexter/Desktop/projects/ml/DoItRight/msgifs/icon1.gif")
#print(toy_story.storyline)
plank = media.Movie("Plank","Marine on alien planet","file:///home/dexter/Desktop/projects/ml/DoItRight/msgifs/icon2.png","file:///home/dexter/Desktop/projects/ml/DoItRight/msgifs/icon2.gif")
#print(avatar.storyline)
#avatar.show_trailer()
alvin = media.Movie("Crunches","Chipmunks who can sing","file:///home/dexter/Desktop/projects/ml/DoItRight/msgifs/icon3_new.jpg","file:///home/dexter/Desktop/projects/ml/DoItRight/msgifs/icon4.gif")
school_of_rock = media.Movie("Toe Touch","Using rock music to learn","file:///home/dexter/Desktop/projects/ml/DoItRight/msgifs/icon4_new.jpg","file:///home/dexter/Desktop/projects/ml/DoItRight/msgifs/icon3.gif")
movies = [push_ups,plank,alvin,school_of_rock]
fresh_tomatoes.open_movies_page(movies)
