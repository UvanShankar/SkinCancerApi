# SkinCancerApi

This is in backend for the skin cancer is application which is developed using the flask library in python.
It can be directly deployed to the heroku server.
Steps
1.Copy the entire code to your github repository
2.Login to heroku
3.Goto heroku addon and add postgre sql
3.Go to heroko deploy page select the reposiory and click deploy .
4.Enjoy your api

Urls
www.<yourapiurl>/register for registerin new user-POST Method Form with 5 parameters
{
username
password
request
premium
emailId
}

www.<yourapiurl>/auth -authenticate the user eg.login POST Method  with 2 parameters
{
username
password
}

www.<yourapiurl>/model -predict the image  POST Method  with 2 parameters
{
username 
image:"the photo"
}
