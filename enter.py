import media
import fresh_tomatoes


push_ups = media.Movie("Push_Up","Story about a boy whose toys come to life","file:///home/dexter/Desktop/projects/ml/DoItRight/msgifs/icon1.jpg","file:///home/dexter/Desktop/DoIt/msgifs/Push_Up.gif")
#print(toy_story.storyline)
plank = media.Movie("Plank","Marine on alien planet","file:///home/dexter/Desktop/projects/ml/DoItRight/msgifs/icon2.png","file:///home/dexter/Desktop/DoIt/msgifs/Plank.gif")
#print(avatar.storylinfew we)
#avatar.show_trailer()
crunches = media.Movie("Crunches","Chipmunks who can sing","file:///home/dexter/Desktop/projects/ml/DoItRight/msgifs/icon3_new.jpg","file:///home/dexter/Desktop/DoIt/msgifs/Crunches.gif")
toe_touch = media.Movie("Toe_Touch","Using rock music to learn","file:///home/dexter/Desktop/projects/ml/DoItRight/msgifs/icon4_new.jpg","file:///home/dexter/Desktop/DoIt/msgifs/Toe_Touch.gif")
exercises = [push_ups,plank,crunches,toe_touch]
fresh_tomatoes.open_movies_page(exercises)
