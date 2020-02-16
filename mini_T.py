from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from time import sleep,time,ctime
from random import randint
from fake_useragent import UserAgent
ua = UserAgent()
from pyvirtualdisplay import Display

import random
import os
import subprocess
import re
import requests




class YouViewer:


    def __init__(self):

        #LOG INFO TITLE
        self.log_info(f'.......event started.....local TIME : {ctime()}')
        
        # CONFIGURABLE variables
        self.MAX_WAIT = 30
        self.MAX_ERROR = 200
        self.NUM_OF_VIEWS = 300
        self.HEADLESS = False
        self.WATCH_TIME_LIMIT = 300
        self.SHUTDOWN_WHEN_FINISHED = False
        self.BROWSER = 'chrome'
        self.DEBUG = False        
        self.PROXY = True
        self.PROXY_LIST = []
        self.CONSUMED_PROXIES = 200
        self.PROXY_TIMEOUT = 3
        
        #visited when DEBUG is set true
        self.CUSTOM_URL = 'https://www.youtube.com/watch?v=d64hfj4'
        
        ####replace these with your desired strings####
        #the title of targetted video
        self.VIDEO_TITLE = 'Joker song 2019'
        
        #after roaming this is searched
        self.SEARCH_BY = "Muhammad fahim joker"
        #this is used for finding channel from search list
        self.CHANNEL_DESCRIPTION='hi.'


        #this variable is used for counting how much time has passed
        self.time_counter = time()

     
        #starting everything
        if self.PROXY:
            self.get_proxy()
            
####################################

        self.NUM_OF_ERRORS = 0    
        for i in range(self.NUM_OF_VIEWS):
            try:
                self.starting_preparation()
                self.main_func()
                self.end_operation()
                
                
            except Exception as e: 
                try: 
                    self.end_operation() 
                except: 
                    pass
                
                
                self.NUM_OF_ERRORS += 1
                print(str(e))
                self.log_info(str(e))
                print(f'Time passed :{self.count_time()}')
                
         
                if self.NUM_OF_ERRORS > self.MAX_ERROR:
                    self.log_info('maximum error limit exceded')
                    
                    #shutdown
                    if self.SHUTDOWN_WHEN_FINISHED:
                        self.shutdown_computer()
                        
                    raise SystemExit

        

############## __init__ method ends here ###############
    def main_func(self):

        if not self.DEBUG:

            roaming = self.roam_randomly_to(what_to_search = self.SEARCH_BY)
            #customize this sector for best results
            if roaming:
                element2 = self.view_xpath(f'//div[text()="{self.CHANNEL_DESCRIPTION}"]/preceding-sibling::h3/a')
                element2.click()
                sleep(1)
                element3= self.view_xpath(f'//*[text()="{self.VIDEO_TITLE}"]')
                element3.click()
                sleep(1)
                print('sleeping for watchtime')
                element6 = self.view_xpath('//div[@class="watch-view-count"]')
                views= element6.text
                print('successfully loaded page with '+ views)
                self.log_info(f'SUCCESS-> TIME:{self.count_time()} counting: '+ views)
                
                sleep(randint(70,self.WATCH_TIME()))
                
            else:
                print('View did not complete')
                self.log_info(f'ERROR-> TIME:{self.count_time()}')
                
            
###############loging info##########

            
            print(f'time passed : {self.count_time()}')
            if roaming:
                self.roam_randomly_to()
                
            
##################################_______WHEN_DEBUG_IS_SET_TRUE________##########################this is run
        if self.DEBUG:
            roaming = self.roam_randomly_to(what_to_search = self.SEARCH_BY)
            if roaming:
                
                
                self.driver.get(self.CUSTOM_URL)
                sleep(self.WATCH_TIME())
            
            else:
                print('View did not complete')



            





            ##### finished DEBUGGING
            print(f'len of proxy list: {len(self.PROXY_LIST)}')
            print(f'finished in {self.count_time()}')
            print(f'No of errors :{self.NUM_OF_ERRORS}')
            
        
        
        
        
        
        
        
        
####################    methods start here    ################################        

    #this method is used in starting_preparation
    
    
    def get_proxy(self):
        try:        
            self.driver = webdriver.Chrome()
            self.driver.get('https://www.proxy-list.download/HTTPS')
            elem = self.driver.find_element_by_xpath('//*[@id="txta1"]')
            unfiltered = elem.get_attribute('value')
            filtered = re.findall(r'(\d+\.\d+\.\d+\.\d+:\d+)\n', unfiltered)
            self.PROXY_LIST = filtered
            self.end_operation()
            return self.PROXY_LIST
            
        except Exception as e:
            self.end_operation()
            print('ERROR AT GET PROXY')
            print(str(e))
            raise e
    
########### Only call this function if you already called get_proxy

    def random_proxy(self):
        
        for i in range(self.CONSUMED_PROXIES + 1):
            try:
                x = random.choice(self.PROXY_LIST)
                print('TRYING PROXY: '+x)
                
                proxies= {
                        'http':'http://'+ x,
                        'https':'https://'+ x,
                        }
                r = requests.get('https://www.google.com/humans.txt',
                                 timeout = self.PROXY_TIMEOUT,
                                 proxies = proxies
                                 )
                
                if r.status_code == 200:
                    return x
            
            except Exception as e:
                #removing invalid proxy
                self.PROXY_LIST.remove(x)
                
                if not i < self.CONSUMED_PROXIES:
                    print('NO VALID PROXY ERROR')
                    raise e
                
                print(f'TRYING ANOTHER PROXY....PROXY NO.{i+1}')

    


######other functions######

    def WATCH_TIME(self):
        return randint(self.WATCH_TIME_LIMIT, self.WATCH_TIME_LIMIT+5)
    
    def count_time(self):
        return time()-self.time_counter

    def shutdown_computer(self):
        print('shutting down computer')
        self.log_info('shutting down computer')
        subprocess.run('shutdown/s',shell=True)

    #configure the chrome        
    def starting_preparation(self):
        #applies when running chrome
        if self.BROWSER == 'chrome':
            self.chrome_options = webdriver.ChromeOptions()
            self.chrome_options.add_argument('--no-sandbox')
            self.chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            self.chrome_options.add_argument("disable-infobars")
            self.chrome_options.add_argument("--start-maximized")
            self.chrome_options.add_argument("--allow-running-insecure-content")
            self.chrome_options.add_experimental_option('useAutomationExtension', False)
            self.chrome_options.add_argument(f'--user-agent={ua.random}')

            if self.PROXY:
                #feed proxy to the chrome
                rando_prox = self.random_proxy()
                self.chrome_options.add_argument(f'--proxy-server={rando_prox}')
                
            
            

            self.driver = webdriver.Chrome(chrome_options = self.chrome_options)
            self.driver.get('https://www.youtube.com')    

#log_info for later use
    def log_info(self,comment):
        with open('YTlog.txt',mode='a') as writer:
            writer.write(comment+'\n')

    def end_operation(self):
        self.driver.quit()
        
    #customised for setting timeout   
    def view_xpath(self,xpath_pattern):
        start_time = time()
        while True:
            try:
                self.element = self.driver.find_element_by_xpath(xpath_pattern)
                return self.element
                
            except WebDriverException as e:
                
                if (time() - start_time) > self.MAX_WAIT:
                    print('ERROR AT VIEW_XPATH')
                    raise e
                sleep(0.5)
                
    #randomly browses youtube   
    def roam_randomly_to(self,roam_permit=1,what_to_search = None, each_watch_len=3): 
        current_url = self.driver.execute_script('return window.location.href')
        #check if its a mobile site
        if current_url.startswith('https://www.'):
            try:
                sleep(randint(2,3))
                return_to_home= self.driver.find_element_by_xpath('//a[text()="Remind me later"]')
                return_to_home.click()
                
            except Exception:
                print('did not tell me to update my browser!')
            
            try:
                sleep(randint(2,3))
                prompt = self.driver.find_element_by_xpath('//*[@id="text" and text()="Ok"]')
                prompt.click()
                print('prompt clicked')
            except Exception:
                print('prompt not found')

            for i in range(randint(roam_permit, roam_permit+3)):
                sleep(randint(2,6))
                #this l is used for getting out of a loophole in youtube
                l=0
                while True:
                    l+=1
                                    
                    sleep(.5)
                    inp = '//span[@class="video-time"]/preceding-sibling::img[contains(@src,"https://i.ytimg.com")]'
                    x = self.driver.find_elements_by_xpath(inp)
                    
                    print(f"site roam {i}")
                    try:
                        x = random.choice(x)
                        x.click()
                        break
                    except Exception as e:
                        print('cannot click, moving to another object')
                        print(str(e))
                        
                        if l>10:
                            raise ValueError('went to a loophole')                    
                        elif l>6:
                        	continue                    	
                        elif l>5:
                            self.driver.execute_script("window.history.go(-1)")
                                        
                        
                wait=randint(0,3)
                if wait:
                    sleep(randint(each_watch_len,each_watch_len+30))
                    
            #now we search
            if what_to_search != None:
                srch_elem = self.view_xpath('//input[@placeholder="Search"]')
                srch_elem.send_keys(what_to_search)
                srch_elem.send_keys(Keys.ENTER)
                print('searched.......')
                sleep(randint(1,3))
                
            
            print('everything completed')
            return True
        else:
            print('went to a mobile version of youtube')
            return False



if __name__ == '__main__':
    display = Display(visible=0, size=(1024, 768))
    display.start()
    runner = YouViewer()
    display.stop()
