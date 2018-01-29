# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 20:22:06 2018

@author: Sebastien
"""

#%%
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#%%
browser = webdriver.Chrome()
page = 'https://www.thalys.com/nl/en/'

#%%
browser.get(page)

#%%
link = browser.find_element_by_name('div.rt-el-trains-main btn btn-lg btn-secondary selectorLaterTrains')
#%%
link = browser.find_element_by_xpath('[@id="OutboundTrainSelectionZone"]')
#<div class="rt-el-trains-main btn btn-lg btn-secondary selectorLaterTrains">Later trains <span class="icon-ico-arrow-light-down2"></span></div>

#%%
link.click()


#%%

body = browser.find_element_by_tag_name('body')

#%%
#browser.find_element_by_css_selector('div')
#%%
#css_lnks = [i.get_attribute('href') for i in browser.find_element_by_css_selector('class')]

#%%
test = browser.find_elements_by_css_selector('div.rt-connection-sameday')

#%%
test = browser.find_elements_by_css_selector('div.rt-comfort-button-group btn-group')
#%%
#test = browser.find_elements_by_css_selector('span.text:secondClassButton.priceLabel')
#%%

#        <span class="rt-comfort-button__price sel-label-price" data-bind="text:secondClassButton.priceLabel">€ 59</span>

#%%


#%%
driver = webdriver.Chrome()

driver.get("http://jyotiska.github.io/")
time.sleep(1)
#%%
link = driver.find_elements_by_css_selector('a')
#%%
link[1].click()
#%%
driver.back()
#%%
blog_link = driver.find_element_by_name("stackzed")
blog_link.click()
assert "blog" in driver.current_url
time.sleep(1)
#%%
driver.back()
time.sleep(1)
#%%
github_link = driver.find_element_by_name("Github")
github_link.click()
assert "jyotiska" in driver.current_url
time.sleep(1)
#%%
driver.back()
time.sleep(1)
#%%
all_projects = []
projects = driver.find_element_by_id("projects").find_elements_by_css_selector("li")
for item in projects:
    all_projects.append(item.text)
assert len(all_projects) == 9
time.sleep(1)
#%%
all_talks = []
talks = driver.find_element_by_id("talks").find_elements_by_css_selector("li")
for item in talks:
    all_talks.append(item.text)
assert len(all_talks) == 4
time.sleep(1)
#%%
driver.close()
#%%














#%%
#%%
browser = webdriver.Chrome()
base_url = u'https://twitter.com/search?q='

query_1 = u'iphone%20x%20problem&src=typd'

url_1 = base_url + query_1

browser.get(url = url_1)
time.sleep(1)

body = browser.find_element_by_tag_name('body')

for _ in range(100):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    
tweets_1 = browser.find_elements_by_css_selector('div.content > div.js-tweet-text-container > p')
users_1 = browser.find_elements_by_css_selector("div.content > div.stream-item-header > a > span.username.u-dir.u-textTruncate > b")
replies_1 = browser.find_elements_by_css_selector("div.content > div.stream-item-footer > div.ProfileTweet-actionList.js-actions > div.ProfileTweet-action.ProfileTweet-action--reply > button > span > span")
retweets_1 = browser.find_elements_by_css_selector('div.content > div.stream-item-footer > div.ProfileTweet-actionList.js-actions > div.ProfileTweet-action.ProfileTweet-action--retweet.js-toggleState.js-toggleRt > button.ProfileTweet-actionButton.js-actionButton.js-actionRetweet > span > span')
likes_1 = browser.find_elements_by_css_selector('div.content > div.stream-item-footer > div.ProfileTweet-actionList.js-actions > div.ProfileTweet-action.ProfileTweet-action--favorite.js-toggleState > button.ProfileTweet-actionButton.js-actionButton.js-actionFavorite > span > span')
times_1 = browser.find_elements_by_css_selector('div.stream-item-header > small > a')
#hash_tags = browser.find_elements_by_css_selector('twitter-hashtag pretty-link js-nav')
#permas = browser.find_elements_by_css_selector('div.js-tweet-text-container > p > a')

#driver.find_element_by_css_selector(".test_button4[value='Update']")

tweetss_1 = []
userss_1 = []
repliess_1 = []
retweetss_1 = []
likess_1 = []
timess_1 = []
#permass = []




#for tweet in tweets:
#    tweetss.append(tweet.text)
tweetss_1 = [tweet.text for tweet in tweets_1]

#for user in users:
#    userss.append(user.text)
userss_1 = [user.text for user in users_1]

#for reply in replies:
#    repliess.append(reply.text)
repliess_1 = [reply.text for reply in replies_1]

#for retweet in retweets:
#    retweetss.append(retweet.text)
retweetss_1 = [retweet.text for retweet in retweets_1]

#for like in likes:
#    likess.append(like.text)
likess_1 = [like.text for like in likes_1]
    
#for time in times:
#    timess.append(time.get_attribute("title"))
timess_1 = [time.get_attribute("title") for time in times_1]
    
#for perma in permas:
#    permass.append(perma.text)

#for hash_tag in hash_tags:
#    print (hash_tag.text)



#<strong class="fullname show-popup-with-id u-textTruncate " data-aria-label-part="">TekNotice</strong>
#<span class="username u-dir u-textTruncate" dir="ltr" data-aria-label-part="">@<b>TekNotice</b></span>
#<a href="/TekNotice/status/952962598311313408" class="tweet-timestamp js-permalink js-nav js-tooltip" title="6:56 PM - 15 Jan 2018" data-conversation-id="952962598311313408"><span class="_timestamp js-short-timestamp js-relative-timestamp" data-time="1516038963" data-time-ms="1516038963000" data-long-form="true" aria-hidden="true">2h</span><span class="u-hiddenVisually" data-aria-label-part="last">2 hours ago</span></a>
#<a href="/hashtag/samsungs8?src=hash" data-query-source="hashtag_click" class="twitter-hashtag pretty-link js-nav" dir="ltr"><s>#</s><b><strong>samsungs8</strong></b></a>
#<span class="ProfileTweet-actionCountForAria" id="profile-tweet-action-reply-count-aria-952962598311313408">0 replies</span>
#for tweet in tweets:
#    print(tweet.text)

#%%

#%%
tweetss_1
#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%
