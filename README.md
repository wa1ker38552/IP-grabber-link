# IP-grabber-link
A IP grabber that grabs IP's upon clicking a link.

**FOR EDUCATIONAL PURPOSES ONLY, I AM NOT RESPONSIBLE FOR ANY MISUSE!**

**Setup:**

To start the program, just run the program and put in your discord webhook on the webhookurl variable. Upon clicking a link from a flask application, the application will view the IP sent through headers and sends it to you via Discord webhook. After processing the IP, the flask application will redirect you to the url of your choice which you can set here: ```return redirect(YOUR_URL_HERE, code = 302)``` 

**REPLIT Hosting**

Open a new Repl and paste in the code. Add your webhook to the webhookurl variable and set a custom link. Change the domain (Freenom recommended) and send to your friends!

**Features:**

Sends location data parsed from https://www.iplocation.net/ip-lookup and OS. Discord webhook embed can be customized as well. 
