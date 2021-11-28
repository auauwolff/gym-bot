# Gym Booking Bot

<img src="https://user-images.githubusercontent.com/36112125/113499920-e8431a00-94e7-11eb-977a-0f0810a3a0e8.png" alt="Your image title" width="120"/>

:muscle: I wrote a Python script that automates my gym time bookings at specific times.

I had to wake up at 5AM, to not miss a spot in my favorite classes, due to that I have created this bot, that does the job for me!

### Tools/Technologies: ###  
* [Selenium WebDriver](https://www.selenium.dev/documentation/en/webdriver/)  

### How I built it: ###  
:arrow_right:	I web scraped my gym's website by inspecting its **HTML** elements.  
:arrow_right:	I used [**Selenium**](https://www.selenium.dev/) to automate the booking process, more specifically, 
I used [**ChromeDriver**](https://chromedriver.chromium.org/) which is a standalone server that is used by [Selenium WebDriver](https://www.selenium.dev/documentation/en/webdriver/) to control tests on Chrome.  

### To use: ###  
:arrow_right:	Clone this repo and set up your local copy of the repository.  
:arrow_right:	Download [**ChromeDriver**](https://chromedriver.chromium.org/) so you can run the automated script on Chrome.  
:arrow_right:	You can set up a task scheduler (Windows only) and it will run the script only if your machine is turned on
