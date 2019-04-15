from flask import Flask, render_template
app = Flask(__name__)
exc =[{
    'Name' : 'Toe touching',
    'Link' : 'https://www.youtube.com/'
},
{
    'Name' : 'push ups',
    'Link' : 'https://www.youtube.com/watch?v=IODxDxX7oi4'
},
]

@app.route("/")
def home():
    return '''<!DOCTYPE HTML>
<html>
	<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>Stamina &mdash; Free Website Template, Free HTML5 Template by freehtml5.co</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="description" content="Free HTML5 Website Template by freehtml5.co" />
	<meta name="keywords" content="free website templates, free html5, free template, free bootstrap, free website template, html5, css3, mobile first, responsive" />
	<meta name="author" content="freehtml5.co" />



  	<!-- Facebook and Twitter integration -->
	<meta property="og:title" content=""/>
	<meta property="og:image" content=""/>
	<meta property="og:url" content=""/>
	<meta property="og:site_name" content=""/>
	<meta property="og:description" content=""/>
	<meta name="twitter:title" content="" />
	<meta name="twitter:image" content="" />
	<meta name="twitter:url" content="" />
	<meta name="twitter:card" content="" />

	<link href="https://fonts.googleapis.com/css?family=Work+Sans:300,400,500,700,800" rel="stylesheet">

	<!-- Animate.css -->
	<link rel="stylesheet" href="css/animate.css">
	<!-- Icomoon Icon Fonts-->
	<link rel="stylesheet" href="css/icomoon.css">
	<!-- Bootstrap  -->
	<link rel="stylesheet" href="css/bootstrap.css">

	<!-- Magnific Popup -->
	<link rel="stylesheet" href="css/magnific-popup.css">

	<!-- Owl Carousel  -->
	<link rel="stylesheet" href="css/owl.carousel.min.css">
	<link rel="stylesheet" href="css/owl.theme.default.min.css">

	<!-- Theme style  -->
	<link rel="stylesheet" href="css/style.css">

	<!-- Modernizr JS -->
	<script src="{{ url_for('static',filename = 'modernizr-2.6.2.min.js')}}"></script>
	<!-- FOR IE9 below -->
	<!--[if lt IE 9]>
	<script src="js/respond.min.js"></script>
	<![endif]-->

	</head>
	<body>
		<button><a href="fresh_tomatoes.html">Press me</button>

	<div class="fh5co-loader"></div>

	<div id="page">
	<nav class="fh5co-nav" role="navigation">
		<div class="top">
			<div class="container">
				<div class="row">
					<div class="col-xs-12 text-right">
						<p class="num">Call: +01 123 456 7890</p>
						<ul class="fh5co-social">
							<li><a href="#"><i class="icon-twitter"></i></a></li>
							<li><a href="#"><i class="icon-dribbble"></i></a></li>
							<li><a href="#"><i class="icon-github"></i></a></li>
						</ul>
					</div>
				</div>
			</div>
		</div>
		<div class="top-menu">
			<div class="container">
				<div class="row">
					<div class="col-xs-2">
						<div id="fh5co-logo"><a href="index.html">DO RIGHT<span>.</span></a></div>
					</div>
					<div class="col-xs-10 text-right menu-1">
						<ul>
							<li class="active"><a href="index.html">Home</a></li>
							<li><a href="gallery.html">Gallery</a></li>
							<li><a href="about.html">Trainer</a></li>
							<li><a href="pricing.html">Pricing</a></li>
							<li class="has-dropdown">
								<a href="blog.html">Blog</a>
								<ul class="dropdown">
									<li><a href="#">Web Design</a></li>
									<li><a href="#">eCommerce</a></li>
									<li><a href="#">Branding</a></li>
									<li><a href="#">API</a></li>
								</ul>
							</li>
							<li><a href="contact.html">Contact</a></li>
						</ul>
					</div>
				</div>

			</div>
		</div>
	</nav>

	<header id="fh5co-header" class="fh5co-cover" role="banner" style="background-image:url(images/img_bg.jpg);" data-stellar-background-ratio="0.5">
		<div class="overlay"></div>
		<!-- <div class="container">
			<div class="row">
				<div class="col-md-8 col-md-offset-2 text-center">
					<div class="display-t">
						<div class="display-tc animate-box" data-animate-effect="fadeIn">
							<h1>Make it a lifestyle, not a duty</h1>
							<h2>Free html5 templates Made by <a href="http://freehtml5.co/" target="_blank">freehtml5.co</a></h2>
							<p><a href="https://vimeo.com/channels/staffpicks/93951774" class="btn btn-primary popup-vimeo">Watch Our Video</a></p>
						</div>
					</div>
				</div>
			</div>
		</div> -->
	</header>

	<div id="fh5co-services" class="fh5co-bg-section">
		<div class="container">
			<div class="row">
				<div class="col-md-4 text-center animate-box">
					<div class="services">
						<span><img class="img-responsive" src="images/dumbbell.svg" alt=""></span>
						<h3>Weight Lifting</h3>
						<p>Weight training is a type of strength training that uses weights for resistance.Weight training provides a stress to the muscles that causes them to adapt and get stronger.You can also increase your strength. </p>
						<p><a href="#" class="btn btn-primary btn-outline btn-sm">More <i class="icon-arrow-right"></i></a></p>
					</div>
				</div>
				<div class="col-md-4 text-center animate-box">
					<div class="services">
						<span><img class="img-responsive" src="images/exercise.svg" alt=""></span>
						<h3>Stamina</h3>
						<p>"Stamina" is the strength and energy needed to exert oneself for an extended period of time. The word most commonly refers to the exertion needed for physical activities like exercise and sports.		</p>
						<p><a href="#" class="btn btn-primary btn-outline btn-sm">More <i class="icon-arrow-right"></i></a></p>
					</div>
				</div>
				<div class="col-md-4 text-center animate-box">
					<div class="services">
						<span><img class="img-responsive" src="images/yoga-carpet.svg" alt=""></span>
						<h3>Yoga</h3>
						<p>Practicing yoga results in the union of individual consciousness with universal consciousness, bringing about a perfect harmony between the mind and the body and man and nature.</p>
						<p><a href="#" class="btn btn-primary btn-outline btn-sm">More <i class="icon-arrow-right"></i></a></p>
					</div>
				</div>
			</div>
		</div>
	</div>

	<div id="fh5co-trainer">
		<div class="container">
			<div class="row animate-box">
				<div class="col-md-8 col-md-offset-2 text-center fh5co-heading">
					<h2>Diet Plans</h2>
					<p>A healthy diet chart helps you regulate your calorie intake. By specifying your activities and calorie intake during the day, the list gives you a good idea of what you must eat to be on track. You may also use a diet chart for weight loss given by an expert</p>
				</div>
			</div>
			<div class="row">
				<div class="col-md-4 col-sm-4 animate-box">
					<div class="trainer">
						<a href="#"><img class="img-responsive" src="images/d1.jpg" alt="trainer"></a>

					</div>
				</div>
				<div class="col-md-4 col-sm-4 animate-box">
					<div class="trainer">
						<a href="#"><img class="img-responsive" src="images/d2.png" alt="trainer"></a>

					</div>
				</div>
				<div class="col-md-4 col-sm-4 animate-box">
					<div class="trainer">
						<a href="#"><img class="img-responsive" src="images/d3.png" alt="trainer"></a>
					</div>
				</div>
			</div>
		</div>
	</div>

	<div id="fh5co-schedule" class="fh5co-bg" style="background-image: url(images/img_bg_1.jpg);">
		<div class="container">
			<div class="row">
				<div class="col-md-8 col-md-offset-2 text-center fh5co-heading animate-box">
					<h2>Exercise Plans</h2>
				</div>
			</div>

			<div class="row animate-box">

				<div class="fh5co-tabs">
					<ul class="fh5co-tab-nav">
						<li class="active"><a href="#" data-tab="1"><span class="visible-xs">S</span><span class="hidden-xs">Sunday</span></a></li>
						<li><a href="#" data-tab="2"><span class="visible-xs">M</span><span class="hidden-xs">Monday</span></a></li>
						<li><a href="#" data-tab="3"><span class="visible-xs">T</span><span class="hidden-xs">Tuesday</span></a></li>
						<li><a href="#" data-tab="4"><span class="visible-xs">W</span><span class="hidden-xs">Wednesday</span></a></li>

						<li><a href="#" data-tab="5"><span class="visible-xs">Th</span><span class="hidden-xs">Thursday</span></a></li>
						<li><a href="#" data-tab="6"><span class="visible-xs">F</span><span class="hidden-xs">Friday</span></a></li>
						<li><a href="#" data-tab="7"><span class="visible-xs">S</span><span class="hidden-xs">Saturday</span></a></li>
					</ul>

					<!-- Tabs -->
					<div class="fh5co-tab-content-wrap">
						<div class="fh5co-tab-content tab-content active" data-tab-content="1">
							<ul class="class-schedule">
								<li class="text-center">
									<span><img src="images/exercise.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Cardio</h4>

								</li>
								<li class="text-center">
									<span><img src="images/dumbbell.svg" class="img-responsive" alt=""></span>
									<span class="time">9:00 AM - 11AM</span>
									<h4>Body Building</h4>

								</li>
								<li class="text-center">
									<span><img src="images/yoga-carpet.svg" class="img-responsive" alt=""></span>
									<span class="time">6:00 AM - 7AM</span>
									<h4>Yoga</h4>

								</li>
								<li class="text-center">
									<span><img src="images/two-boxing-gloves.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Boxing</h4>

								</li>
								<li class="text-center">
									<span><img src="images/ballet.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Ballet Dance</h4>

								</li>
								<li class="text-center">
									<span><img src="images/dumbbell.svg" class="img-responsive" alt=""></span>
									<span class="time">9:00 AM - 11AM</span>
									<h4>Body Building</h4>

								</li>
								<li class="text-center">
									<span><img src="images/yoga-carpet.svg" class="img-responsive" alt=""></span>
									<span class="time">6:00 AM - 7AM</span>
									<h4>Yoga</h4>

								</li>
								<li class="text-center">
									<span><img src="images/exercise.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Cardio</h4>

								</li>
							</ul>
						</div>

						<div class="fh5co-tab-content tab-content active" data-tab-content="2">
							<ul class="class-schedule">
								<li class="text-center">
									<span><img src="images/exercise.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Cardio</h4>

								</li>
								<li class="text-center">
									<span><img src="images/dumbbell.svg" class="img-responsive" alt=""></span>
									<span class="time">9:00 AM - 11AM</span>
									<h4>Body Building</h4>

								</li>
								<li class="text-center">
									<span><img src="images/yoga-carpet.svg" class="img-responsive" alt=""></span>
									<span class="time">6:00 AM - 7AM</span>
									<h4>Yoga</h4>

								</li>
								<li class="text-center">
									<span><img src="images/two-boxing-gloves.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Boxing</h4>

								</li>
								<li class="text-center">
									<span><img src="images/ballet.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Ballet Dance</h4>

								</li>
								<li class="text-center">
									<span><img src="images/dumbbell.svg" class="img-responsive" alt=""></span>
									<span class="time">9:00 AM - 11AM</span>
									<h4>Body Building</h4>

								</li>
								<li class="text-center">
									<span><img src="images/yoga-carpet.svg" class="img-responsive" alt=""></span>
									<span class="time">6:00 AM - 7AM</span>
									<h4>Yoga</h4>

								</li>
								<li class="text-center">
									<span><img src="images/exercise.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Cardio</h4>

								</li>
							</ul>
						</div>

						<div class="fh5co-tab-content tab-content active" data-tab-content="3">
							<ul class="class-schedule">
								<li class="text-center">
									<span><img src="images/exercise.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Cardio</h4>

								</li>
								<li class="text-center">
									<span><img src="images/dumbbell.svg" class="img-responsive" alt=""></span>
									<span class="time">9:00 AM - 11AM</span>
									<h4>Body Building</h4>

								</li>
								<li class="text-center">
									<span><img src="images/yoga-carpet.svg" class="img-responsive" alt=""></span>
									<span class="time">6:00 AM - 7AM</span>
									<h4>Yoga</h4>

								</li>
								<li class="text-center">
									<span><img src="images/two-boxing-gloves.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Boxing</h4>

								</li>
								<li class="text-center">
									<span><img src="images/ballet.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Ballet Dance</h4>

								</li>
								<li class="text-center">
									<span><img src="images/dumbbell.svg" class="img-responsive" alt=""></span>
									<span class="time">9:00 AM - 11AM</span>
									<h4>Body Building</h4>

								</li>
								<li class="text-center">
									<span><img src="images/yoga-carpet.svg" class="img-responsive" alt=""></span>
									<span class="time">6:00 AM - 7AM</span>
									<h4>Yoga</h4>

								</li>
								<li class="text-center">
									<span><img src="images/exercise.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Cardio</h4>

								</li>
							</ul>
						</div>

						<div class="fh5co-tab-content tab-content active" data-tab-content="4">
							<ul class="class-schedule">
								<li class="text-center">
									<span><img src="images/exercise.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Cardio</h4>

								</li>
								<li class="text-center">
									<span><img src="images/dumbbell.svg" class="img-responsive" alt=""></span>
									<span class="time">9:00 AM - 11AM</span>
									<h4>Body Building</h4>

								</li>
								<li class="text-center">
									<span><img src="images/yoga-carpet.svg" class="img-responsive" alt=""></span>
									<span class="time">6:00 AM - 7AM</span>
									<h4>Yoga</h4>

								</li>
								<li class="text-center">
									<span><img src="images/two-boxing-gloves.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Boxing</h4>

								</li>
								<li class="text-center">
									<span><img src="images/ballet.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Ballet Dance</h4>

								</li>
								<li class="text-center">
									<span><img src="images/dumbbell.svg" class="img-responsive" alt=""></span>
									<span class="time">9:00 AM - 11AM</span>
									<h4>Body Building</h4>

								</li>
								<li class="text-center">
									<span><img src="images/yoga-carpet.svg" class="img-responsive" alt=""></span>
									<span class="time">6:00 AM - 7AM</span>
									<h4>Yoga</h4>

								</li>
								<li class="text-center">
									<span><img src="images/exercise.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Cardio</h4>

								</li>
							</ul>
						</div>

						<div class="fh5co-tab-content tab-content active" data-tab-content="5">
							<ul class="class-schedule">
								<li class="text-center">
									<span><img src="images/exercise.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Cardio</h4>

								</li>
								<li class="text-center">
									<span><img src="images/dumbbell.svg" class="img-responsive" alt=""></span>
									<span class="time">9:00 AM - 11AM</span>
									<h4>Body Building</h4>

								</li>
								<li class="text-center">
									<span><img src="images/yoga-carpet.svg" class="img-responsive" alt=""></span>
									<span class="time">6:00 AM - 7AM</span>
									<h4>Yoga</h4>

								</li>
								<li class="text-center">
									<span><img src="images/two-boxing-gloves.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Boxing</h4>

								</li>
								<li class="text-center">
									<span><img src="images/ballet.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Ballet Dance</h4>

								</li>
								<li class="text-center">
									<span><img src="images/dumbbell.svg" class="img-responsive" alt=""></span>
									<span class="time">9:00 AM - 11AM</span>
									<h4>Body Building</h4>

								</li>
								<li class="text-center">
									<span><img src="images/yoga-carpet.svg" class="img-responsive" alt=""></span>
									<span class="time">6:00 AM - 7AM</span>
									<h4>Yoga</h4>

								</li>
								<li class="text-center">
									<span><img src="images/exercise.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Cardio</h4>

								</li>
							</ul>
						</div>

						<div class="fh5co-tab-content tab-content active" data-tab-content="6">
							<ul class="class-schedule">
								<li class="text-center">
									<span><img src="images/exercise.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Cardio</h4>

								</li>
								<li class="text-center">
									<span><img src="images/dumbbell.svg" class="img-responsive" alt=""></span>
									<span class="time">9:00 AM - 11AM</span>
									<h4>Body Building</h4>

								</li>
								<li class="text-center">
									<span><img src="images/yoga-carpet.svg" class="img-responsive" alt=""></span>
									<span class="time">6:00 AM - 7AM</span>
									<h4>Yoga</h4>

								</li>
								<li class="text-center">
									<span><img src="images/two-boxing-gloves.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Boxing</h4>

								</li>
								<li class="text-center">
									<span><img src="images/ballet.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Ballet Dance</h4>

								</li>
								<li class="text-center">
									<span><img src="images/dumbbell.svg" class="img-responsive" alt=""></span>
									<span class="time">9:00 AM - 11AM</span>
									<h4>Body Building</h4>

								</li>
								<li class="text-center">
									<span><img src="images/yoga-carpet.svg" class="img-responsive" alt=""></span>
									<span class="time">6:00 AM - 7AM</span>
									<h4>Yoga</h4>

								</li>
								<li class="text-center">
									<span><img src="images/exercise.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Cardio</h4>

								</li>
							</ul>
						</div>

						<div class="fh5co-tab-content tab-content active" data-tab-content="7">
							<ul class="class-schedule">
								<li class="text-center">
									<span><img src="images/exercise.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Cardio</h4>

								</li>
								<li class="text-center">
									<span><img src="images/dumbbell.svg" class="img-responsive" alt=""></span>
									<span class="time">9:00 AM - 11AM</span>
									<h4>Body Building</h4>

								</li>
								<li class="text-center">
									<span><img src="images/yoga-carpet.svg" class="img-responsive" alt=""></span>
									<span class="time">6:00 AM - 7AM</span>
									<h4>Yoga</h4>

								</li>
								<li class="text-center">
									<span><img src="images/two-boxing-gloves.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Boxing</h4>

								</li>
								<li class="text-center">
									<span><img src="images/ballet.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Ballet Dance</h4>

								</li>
								<li class="text-center">
									<span><img src="images/dumbbell.svg" class="img-responsive" alt=""></span>
									<span class="time">9:00 AM - 11AM</span>
									<h4>Body Building</h4>

								</li>
								<li class="text-center">
									<span><img src="images/yoga-carpet.svg" class="img-responsive" alt=""></span>
									<span class="time">6:00 AM - 7AM</span>
									<h4>Yoga</h4>

								</li>
								<li class="text-center">
									<span><img src="images/exercise.svg" class="img-responsive" alt=""></span>
									<span class="time">7:00 AM - 8AM</span>
									<h4>Cardio</h4>

								</li>
							</ul>
						</div>

					</div>

				</div>
			</div>
		</div>
	</div>



	


	<div id="fh5co-started" class="fh5co-bg" style="background-image: url(images/img_bg_3.jpg);">
		<div class="overlay"></div>
		<div class="container">
			<div class="row animate-box">
				<div class="col-md-8 col-md-offset-2 text-center">
					<h2>Fitness Classes this Summer <br> <span> Pay Now and <br> Get <span class="percent">35%</span> Discount</span></h2>
				</div>
			</div>
			<div class="row animate-box">
				<div class="col-md-8 col-md-offset-2 text-center">
					<p><a href="#" class="btn btn-default btn-lg">Become a Member</a></p>
				</div>
			</div>
		</div>
	</div>

	<div id="fh5co-blog" class="fh5co-bg-section">
		<div class="container">
			<div class="row">
				<div class="col-md-8 col-md-offset-2 text-center fh5co-heading animate-box">
					<h2>Recent Blog</h2>
					<p>Achieving and maintaining fitness is a common problem. Because most of us tend to fall off the track every once in a while. That’s why fitness enthusiasts like you and me need the help of experts to stay focused and motivated. And to do that, follow the best fitness blogs on the internet – like I do. </p>
			</div>
			</div>
			<div class="row row-bottom-padded-md">
				<div class="col-lg-4 col-md-4">
					<div class="fh5co-blog animate-box">
						<a href="#"><img class="img-responsive" src="images/b1.png" alt=""></a>
						<div class="blog-text">
							<h3><a href=""#>45 Minimal Worksspace Rooms for Web Savvys</a></h3>
							<span class="posted_on">Sep. 15th</span>
							<span class="comment"><a href="">21<i class="icon-speech-bubble"></i></a></span>
							<p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.</p>
							<a href="#" class="btn btn-primary">Read More</a>
						</div>
					</div>
				</div>
				<div class="col-lg-4 col-md-4">
					<div class="fh5co-blog animate-box">
						<a href="#"><img class="img-responsive" src="images/b1.png" alt=""></a>
						<div class="blog-text">
							<h3><a href=""#>45 Minimal Worksspace Rooms for Web Savvys</a></h3>
							<span class="posted_on">Sep. 15th</span>
							<span class="comment"><a href="">21<i class="icon-speech-bubble"></i></a></span>
							<p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.</p>
							<a href="#" class="btn btn-primary">Read More</a>
						</div>
					</div>
				</div>
				<div class="col-lg-4 col-md-4">
					<div class="fh5co-blog animate-box">
						<a href="#"><img class="img-responsive" src="images/b1.png" alt=""></a>
						<div class="blog-text">
							<h3><a href=""#>45 Minimal Worksspace Rooms for Web Savvys</a></h3>
							<span class="posted_on">Sep. 15th</span>
							<span class="comment"><a href="">21<i class="icon-speech-bubble"></i></a></span>
							<p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.</p>
							<a href="#" class="btn btn-primary">Read More</a>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>

	<footer id="fh5co-footer" class="fh5co-bg" style="background-image: url(images/img_bg_1.jpg);" role="contentinfo">
		<div class="overlay"></div>
		<div class="container">
			<div class="row row-pb-md">
				<div class="col-md-4 fh5co-widget">
					<h3>A Little About Stamina.</h3>
					<p>Facilis ipsum reprehenderit nemo molestias. Aut cum mollitia reprehenderit. Eos cumque dicta adipisci architecto culpa amet.</p>
					<p><a class="btn btn-primary" href="#">Become A Member</a></p>
				</div>
				<div class="col-md-8">
					<h3>Classes</h3>
					<div class="col-md-4 col-sm-4 col-xs-6">
						<ul class="fh5co-footer-links">
							<li><a href="#">Cardio</a></li>
							<li><a href="#">Body Building</a></li>
							<li><a href="#">Yoga</a></li>
							<li><a href="#">Boxing</a></li>
							<li><a href="#">Running</a></li>
						</ul>
					</div>

					<div class="col-md-4 col-sm-4 col-xs-6">
						<ul class="fh5co-footer-links">
							<li><a href="#">Boxing</a></li>
							<li><a href="#">Martial Arts</a></li>
							<li><a href="#">Karate</a></li>
							<li><a href="#">Kungfu</a></li>
							<li><a href="#">Basketball</a></li>
						</ul>
					</div>

					<div class="col-md-4 col-sm-4 col-xs-6">
						<ul class="fh5co-footer-links">
							<li><a href="#">Badminton</a></li>
							<li><a href="#">Body Building</a></li>
							<li><a href="#">Teams</a></li>
							<li><a href="#">Advertise</a></li>
							<li><a href="#">API</a></li>
						</ul>
					</div>
				</div>
			</div>

			<div class="row copyright">
				<div class="col-md-12 text-center">
					<p>
						<small class="block">&copy; 2016 Free HTML5. All Rights Reserved.</small>
						<small class="block">Designed by <a href="http://freehtml5.co/" target="_blank">FreeHTML5.co</a> Demo Images: <a href="http://unsplash.co/" target="_blank">Unsplash</a></small>
					</p>
					<p>
						<ul class="fh5co-social-icons">
							<li><a href="#"><i class="icon-twitter"></i></a></li>
							<li><a href="#"><i class="icon-facebook"></i></a></li>
							<li><a href="#"><i class="icon-linkedin"></i></a></li>
							<li><a href="#"><i class="icon-dribbble"></i></a></li>
						</ul>
					</p>
				</div>
			</div>

		</div>
	</footer>
	</div>

	<div class="gototop js-top">
		<a href="#" class="js-gotop"><i class="icon-arrow-up"></i></a>
	</div>
	<!-- jQuery -->
	<script src="{{ url_for('static',filename = 'jquery.min.js') }}"></script>
	<!-- jQuery Easing -->
	<script src="{{ url_for('static',filename = 'jquery.easing.1.3.js') }}"></script>
	<!-- Bootstrap -->
	<script src="{{ url_for('static',filename = 'bootstrap.min.js') }}"></script>
	<!-- Waypoints -->
	<script src="{{ url_for('static',filename = 'jquery.waypoints.min.js') }}"></script>
	<!-- Stellar Parallax -->
	<script src="{{ url_for('static',filename = 'jquery.stellar.min.js') }}"></script>
	<!-- Carousel -->
	<script src="{{ url_for('static',filename = 'owl.carousel.min.js') }}"></script>
	<!-- countTo -->
	<script src="{{ url_for('static',filename = 'jquery.countTo.js') }}"></script>
	<!-- Magnific Popup -->
	<script src="{{ url_for('static',filename = 'jquery.magnific-popup.min.js')}}"></script>
	<script src="{{ url_for('static',filename = 'magnific-popup-options.js')}}"></script>
	<!-- Main -->
	<script src="{{url_for('static',filename = 'main.js')}}"></script>



	</body>
</html>
'''
@app.route("/v")
def trynow():
    return render_template('fresh_tomatoes.html')

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')




