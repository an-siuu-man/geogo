# Geogo

#### Inspiration
After having to travel several times across the globe, it can be tough to navigate the documentation hassle that comes with crossing borders. Therefore, we decided to develop a website with over 100+ destinations that can quickly provide all the legal information you would need for you trip along with useful additional data as well as what to expect to spend on  your trip for an enhanced user experience. 

#### What it does
Picture this, you want to travel abroad, but you're just not too sure about what would be the best country given your budget. Additionally you have not considered visa requirements, requirements that may make some destinations impossible. Geogo is here to help users navigate this tricky proccess eliminating the worst parts of planning a trip. 

#### How we built it
With a lot of caffeine and locking in jokes we persevered to bring Geogo to what it is today by using several common web development techniques along with past knowledge in jss, html, and django. Like any website, a frontend was constructed by using jss, html, and css. We next developed the backend of our code, where a lot of data parsing and error handling was developed for Geogo.

#### Challenges we ran into
Parsing flight data from Google Flights API proved to be harder than expected. In addition, crash-proofing our code also took an unexpected large amount of time. Prior to picking a coding topic, there was also a large amount of time spent deciding which topic we were going to be coding this weekend.

#### Accomplishments that we're proud of
Geogo is able to simplify travel planning worldwide. With comprehensive database and intuitive interface we can proudly state that the user experience is as enhanced as it can be.

#### What we learned
We learned new methods for parsing large data sets from APIs, data acquisition, and of course we further enhanced our development capabilities.

#### What's next for Geogo
We hope to be able to extend our list of countries, airports, enhance our API call response time, and also make the results page much more responsive and attractive. Another major issue is the limit we currently have on the number of API calls in a month, which prevents it
from making the app scalable. We need to look for better API endpoints which have no limits on calls. 


#### Try it out for yourself!
[geogo.tech](http://geogo.tech:8000/geogo)

## If you want to run this on your own...

#### Install all dependencies first
> pip install google-search-results <br>
> pip install openai <br>
> pip install -q -U google-generativeai <br>
> pip install django <br>
> pip install requests <br>

#### Create an "apiKeys.txt" file
1. Create you apiKeys.txt file within the `geogo/geogobackend/geogo/api` folder
2. Generate API keys for
   - Gemini
   - OpenAI
   - SerpAPI
   Note that OpenAI's API charges you a small fee with each API call, so make sure you keep this in mind if you intend on iterating
   the API call a lot of times.
3. Write your API keys in the format below within "apiKeys.txt"
   ```
   serpapi,xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   openai,xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   gemini,xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```
   - Replace the string of x's with the respective API Key

#### Finally launch the server
1. Within the terminal navigate to `geogo/geogobackend`
2. Type `python3 manage.py runserver`
3. Then go to the following url: 127.0.0.1:8000/geogo to see the project!

#### Navigate to your own version of Geogo!
[127.0.0.1:8000/geogo](http://127.0.0.1:8000/geogo) (please note that this link will only work when your local Django server is already running)

