# viewbot
increase youtube view 

edit the first few lines of mini_T.py by changing the CAPITALIZED variables values as desired.
those variables are self-explanatory e.g.

self.PROXY=True if you want to use proxy
or 
self.PROXY=False if you don't want to

        self.MAX_WAIT = 30                      # page load timeout
        self.MAX_ERROR = 200                    # 200 errors will stop the script
        self.NUM_OF_VIEWS = 300                 # view the video 300 times
        self.HEADLESS = False                   # unused 
        self.WATCH_TIME_LIMIT = 300             # watch the video for 300 seconds
        self.SHUTDOWN_WHEN_FINISHED = False     # unused
        self.BROWSER = 'chrome'                 #no need to edit the
        self.DEBUG = False                      #unused     
        self.PROXY = True                       # you should leave this true
        self.PROXY_LIST = []                    # you don't need to edit this
        self.CONSUMED_PROXIES = 200             #you don't need to edit the
        self.PROXY_TIMEOUT = 3 #
        
        #visited when DEBUG is set true
        self.CUSTOM_URL = 'https://www.youtube.com/watch?v=d64hfj4'    # additionally you can use debug mode by self.DEBUG=True and visit this url everytime
        
        ####replace these with your desired strings####
        #the title of targetted video
        self.VIDEO_TITLE = 'Joker song 2019'                           # the script will click the video with this title
        
        #after roaming this is searched
        self.SEARCH_BY = "Muhammad fahim joker"                        #the script will search for this in youtube searchbar
        #this is used for finding channel from search list
        self.CHANNEL_DESCRIPTION='hi.'                                 # the script will click the channel with this description







(do this if you are lazy enough)you can run rat_T.py and let it do everything for you. rat_T.py needs sudo permission. It will automatically download chrome , chromedriver and mini_T.py and run mini_T.py all the requirements canbe installed using rat_T.py. to install requirements simply run rat_T.py as sudo. It is recommended to use a cloud server that is running ubuntu. And you should already have python3.7 installed

Know this, same results can be achieved without rat_T.py.
rat_T.py installs a lot of things. so If you don't trust the script,
please don't run it. 



Just install the dependencies manually.

## xvfb is essential for headless chrome.
so do  this 

## sudo apt install xvfb

## then install google chrome, 

## download chromedriver and put chromedriver in '/usr/bin/'

change permission of chromedriver: 

## sudo chmod +rx /usr/bin/chromedriver



then pip install the modules used.

modules used:

## requests
## selenium
## fake-useragent
## pyvirtualdisplay


wala! you are good to go. Now edit the CAPITALIZED variables in mini_T.py
## The 'T' in mini_T.py stands for treasure 😌
