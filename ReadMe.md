# ComicPub

ComicPub, a.k.a Comic Publish is a Django based comic hosting web app. It is unique because you do not need to host the comic's chapter's images on your own web server. You can utilize Imgur's album embeds. This is completely deployable after making little changes.

## Table of Content

* [Features](#Features)
* [Screenshots](#Screenshots)
* [Dependencies](#Dependencies)
* [Installation](#Installation)
* [Problems](#Problems)
* [Development](#Development)
* [Mockups](#Mockups)
* [Contributors](#Contributors)
* [Changelog](#Change-Log)
* [Donations](#Donations)

### Features

  - Django Based Web App.
  - No need to store Images on your own server.
  - Images are served fast.
  - Integrated Disqus comment system.
  - Simple, yet powerful and secure admin panel (with csrf tokens).
  - Bootstrap based (for the most part).
  - Supports Python 2.7 and 3.5.
  - Users don't have to browse to completely new pages to see the About, Recruitment or Contact section.
  - Easy to navigate UI.
  - Open Source.
  - Many more features coming.

### Screenshots

Coming Soon...

### Dependencies

You do not need anything special to run this. Just Python and Django. That is all!

### Installation

Nothing special is needed in general. You just need to make a few setting changes and BOOM, you can go live without a hiccup. Follow these instructions and you should not face any errors.

1.) Browse to the `ComicPub/ComicPub` directory. You should see 4 `.py` files in this directory. Open `settings.py` in any text editor (please don't use Notepad, pls just don't).

2.) Scroll to the very end of this `settings.py` file and you should see these two lines :

```
"""
DO NOT MAKE CHANGES ABOVE THIS LINE IF YOU DON'T KNOW WHAT YOU'RE DOING!.
EDIT THE LINES BELOW AND PLACE THE ONES YOU WANT.
AFTER MAKING ALL THE CHANGES, MAKE "DEBUG=FALSE" ON LINE 26.
"""

# Your website's name
WEBSITE_NAME = "My Comic Website"

# Ex : https://username.disqus.com/embed.js <-- Should be something like this.
# You might have to make a shortname.
DISQUS_URL = "https://YourUserName.disqus.com/embed.js"
```

Replace `My Comic Website` with the name of your website (what you want your website to be called). And then, if you want a comment section (powered by Disqus) on your website, then sign up on disqus and replace `YourUserName` with your app's name on disqus. I guess you need to make some sort of app or something on disqus, for you to be able to integrate into your website.

Now, look for `DEBUG = True` (on line 26) and change it to `DEBUG = False` (this is case sensitive).

This should set your website up. Now, we need to create an admin account. The account that is the boss of all accounts.
So, open up your Terminal or Command Prompt and browse to the `/ComicPub/` directory and you should see `manage.py` file.
When you're in that directory, you need to execute this command :

```
python manage.py createsuperuser
```

Then it'll ask you for a username, email ID and password. This is going to be an admin account, so be VERY careful while setting these values. Because, if someone was to get access to these credentials, then they can do anthing (literally) with your website.

After this, you're good to go. To test the website on your localhost, just open up your Command Prompt/Terminal and browse to the same directory that you browsed to in previous step. And type :

```
python manage.py runserver 8000
```

It doesn't have to be 8000, it's just a port. But, you need to specify a port that is not being used by any other application. It should show something like this :

```
Performing system checks...

System check identified no issues (0 silenced).
June 26, 2017 - 22:26:57
Django version 1.11.2, using settings 'ComicPub.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

If you see this, then your website is running and you could see it by visiting `http://127.0.0.1:8000/`. Remember that this is running just on your computer and is NOT being accessed by the rest of the world. You need a web host that supports Django.

After running the website, you can click on "About" (form the top Menu) and check out the list of some web hosts that support Django (both, paid and free).

### Problems

* Since this is my FIRST Django project, the code might not be the best and could be cleaned and refined more. But, the website is not rendered slow or laggy. It works just fine.

* I suck at CSS and Bootstrap and hence, you can see some weird "Image going out of DIVs" on smaller devices (phones only). The website looks fine on Desktops, laptops and even iPads.

* Currently, the chapters listed on Homepage aren't ordered by their upload dates. The chapter that was uploaded first appears to be on top. Need to fix this.

* Contact Us form doesn't work right now. Should be easy to whip up some PHP code.

These were the only points I remember that could pose as "problems". But, I hope to fix them as time goes by.

### Development

Want to contribute? Great! Few things that you should keep in mind while sending the PR.

* Please do NOT send PR for things like "Indentation Fix", "Typo Fix". Just open an Issue.
* Everytime you update something, do make sure that you go to the `ComicPub/comics/templates/header.html` and at the very end of this file, update the "Current Version". The format is YY.MM.DD. (Do prepend '0', if the date/month is a single integer).
* Please do write a comment or two around the changes you've made, so that the other developers, people and I can understand what is happening and why it is happening.
* I have used `FileField()` for uploading the Cover images. The reason is that I wanted to avoid `PIL` library dependency and please let's keep it that way.
* Please also update the changelog and follow the syntax.

That's all, at least for now. This might sound like I'm imposing a lot of rules, but believe me, I just want to punch people when I see a complex code without any trace of comments and decent explanation. I guess a lot of people do too.

### Mockups

You can take a look at [Mockups] and see where we wanted to head. Help us fix this crappy Bootstrap and CSS.

### Contributors

Thank you everyone who helped and made this repo amazing!
Check out the list of contributors [Here](https://github.com/Xonshiz/ComicPub).

### Change Log

You can find it here [Here](https://github.com/Xonshiz/ComicPub).

### Donations
You can always send some money over from this :

Paypal : [![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.me/xonshiz)

Patreon Link : https://www.patreon.com/xonshiz

PayUMoney :

<div class="pm-button">
  <a href="https://www.payumoney.com/paybypayumoney/#/04EE508CD699DDFA8F7E827E1CB98B85">
    <img src="https://www.payumoney.com/media/images/payby_payumoney/new_buttons/22.png" />
  </a>
</div>

Any amount is appreciated :)
