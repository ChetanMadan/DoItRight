import media
import fresh_tomatoes
toy_story = media.Movie("Push Up","Story about a boy whose toys come to life","https://www.mumslounge.com.au/wp-content/uploads/2012/07/push%20ups%20exercise.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
avatar = media.Movie("Plank","Marine on alien planet","https://life-cdn.global.ssl.fastly.net/life/wp-content/uploads/2016/05/Are-You-Planking-All-Wrong_StraightBack.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()
alvin = media.Movie("Crunches","Chipmunks who can sing","https://health.clevelandclinic.org/wp-content/uploads/sites/3/2016/04/SitUp.jpg","https://www.youtube.com/watch?v=xA6cOSEZhzM")
school_of_rock = media.Movie("Toe Touch","Using rock music to learn","https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/wm-0807-toe-touch-1441032989.jpg","https://www.youtube.com/watch?v=3PsUJFEBC74")
harry_potter = media.Movie("Burpees","Magic school","http://risetoit.co.za/wp-content/uploads/2013/04/Burpees.jpg","https://www.youtube.com/watch?v=PbdM1db3JbY")
movies = [toy_story,avatar,alvin,school_of_rock,harry_potter]
fresh_tomatoes.open_movies_page(movies)
