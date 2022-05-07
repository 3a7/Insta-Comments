import requests,sys,json,secrets
from time import sleep
from colorama import Fore,init
from instabot import Bot
from os import system
from random import choice,randint
from instascrape import Profile,Hashtag,exceptions
try:
    if not sys.warnoptions:
        import warnings
        warnings.simplefilter("ignore")
    init(autoreset=True)
except:
    pass
cokie  = secrets.token_hex(8)*2

bot = Bot

# https://www.instagram.com/web/search/topsearch/?context=blended&query=web  searchs in profiles 'web'

system('title WELCOME TO INSTA COMMENTS BY @A7.ACC')
accounts = dict()
sessions = []
cook = []
clear = lambda: system("cls")

# COLORS
g = lambda x : Fore.GREEN+x+Fore.WHITE
rod = lambda x : Fore.RED+x+Fore.WHITE
b = lambda x : Fore.BLUE+x+Fore.WHITE
y = lambda x : Fore.YELLOW+x+Fore.WHITE
c = lambda x : Fore.CYAN+x+Fore.WHITE
m = lambda x : Fore.MAGENTA+x+Fore.WHITE

# MARKS
exl = '['+rod('!')+']'
ques = '['+m('?')+']'
ha  ='['+g('#')+']'
mult = '['+c('*')+']'

clear()
def logo():
    lo = y('''
 _                           _______                                        
| |             _           (_______)                              _        
| |____   ___ _| |_ _____    _       ___  ____  ____  _____ ____ _| |_  ___ 
| |  _ \ /___|_   _|____ |  | |     / _ \|    \|    \| ___ |  _ (_   _)/___)
| | | | |___ | | |_/ ___ |  | |____| |_| | | | | | | | ____| | | || |_|___ |
|_|_| |_(___/   \__)_____|   \______)___/|_|_|_|_|_|_|_____)_| |_| \__|___/ 
                                                                            
''')
    print(lo+m('                                       CopyRight: instagram.com/a7.acc         \n'))
    print(mult+' This program is not for sale!! If you bought this program please notify me '+m('instagram.com/a7.acc')+' or '+m('https://t.me/a7_acc '))
    print(mult+f' This program is completely {g("FREE")} and located on GitHub with both .exe and .py file format!\n')
    
logo()
def generate_user_agent():
    useragents = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2828.31 Safari/537.36'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2643.44 Safari/537.36'
        'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
        'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'
        'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.3; Trident/4.0)'
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2965.63 Safari/537.36'
        'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2862.69 Safari/537.36'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:45.0) Gecko/20100101 Firefox/45.0'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2950.18 Safari/537.36'
        'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; WOW64; Trident/6.0)'
        'Mozilla/5.0 (X11; Linux i686; rv:49.0) Gecko/20100101 Firefox/49.0'
        'Mozilla/5.0 (Windows NT 5.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'
        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2690.91 Safari/537.36'
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.3; WOW64; Trident/5.0)'
        'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2777.66 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2898.2 Safari/537.36'
        'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2801.53 Safari/537.36'
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Trident/5.0)'
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2694.39 Safari/537.36'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2703.73 Safari/537.36'
        'Mozilla/5.0 (X11; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
        'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; WOW64; Trident/4.0)'
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2800.88 Safari/537.36'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2646.45 Safari/537.36'
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0'
        'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:47.0) Gecko/20100101 Firefox/47.0'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0'
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0'
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2646.73 Safari/537.36'
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'
        'Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2760.49 Safari/537.36'
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2834.2 Safari/537.36'
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2833.13 Safari/537.36'
        'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2799.34 Safari/537.36'
        'Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:48.0) Gecko/20100101 Firefox/48.0'
        'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2845.18 Safari/537.36'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2889.10 Safari/537.36'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:47.0) Gecko/20100101 Firefox/47.0'
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.89 Safari/537.36'
        'Mozilla/5.0 (Windows NT 5.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'
        'Mozilla/5.0 (X11; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2770.77 Safari/537.36'
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2760.44 Safari/537.36'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2751.15 Safari/537.36'
    ]
    return choice(useragents)


                                #    GETS INSTAGRAM ACCOUNTS 
def get_accounts():
    while True:
        try:
            c1 = input(f'{ques} How do you want to get your instagram accounts to start commenting using them? >> \n[{c("1")}] from accounts.txt\n[{c("2")}] I will enter my instagram account\n  >> ')
            if c1 == '1' or c1 == '2':
                break
        except:
            print(exl+' Please enter one option! 1 or 2 only')
            sleep(3)
        
    if c1 == '1':
        with open('accounts.txt','r',encoding='utf-8') as file:
            for line in file.readlines():
                try:
                    line = line.split(':')
                    accounts[line[0].strip('\n')] = line[1].strip('\n')
                except:
                    pass
        print(ha+' '+g(str(len(accounts)))+' accounts found in accounts.txt file!')
        sleep(2)
        return
    else:
        while True:
            try:
                ac = input(ques+' Enter your accounts in this sequence mail:pass or username:pass >> ')
                ac = ac.split(':')
                if len(ac) == 2:
                    accounts[ac[0]] = ac[1]
                    break
            except:
                print(exl+' Make sure you are putting mail:pass or username:pass!\n')
                sleep(3)
get_accounts()

#'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
def logins():
    for username in accounts.keys():
        cokie  = secrets.token_hex(8)*2
        password = accounts[username]
        r = requests.session()
        url_login = 'https://www.instagram.com/accounts/login/ajax/'
        headers_login = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': str(randint(300,400)),
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': cokie,
            'origin': 'https://www.instagram.com',
            'x-csrftoken':'missing',
            'referer': 'https://www.instagram.com/accounts/login/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': str(generate_user_agent),
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-instagram-ajax': '0edc1000e5e7',
            'x-requested-with': 'XMLHttpRequest'}
        data_login = {'username': f'{username}','enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}'}
        logged = False
        r1 = ''
        for _ in range(3):
            try:
                r1 = r.post(url_login, headers=headers_login, data=data_login,timeout=5)
                logged = True
                break
            except:
                pass
        if '@' in username and '.' in username:
            pass
        else:
            username = '@'+username

        if '"authenticated":true' in r1.text and logged:
            print(f"[{g('+')}] Logged In >> {username}")
            sessions.append(r)
            cook.append(r1.cookies)
        elif '"authenticated":false' in str(r1.text) or '"message":"checkpoint_required"' in str(r1.text):
            print(f"[{rod('-')}] Failed Login >> {username} "+rod('|Secured account|'))
        else:
            print(f"[{rod('-')}] Failed Login >> {username}")
            print(exl+' Error message: \n-------------------------------------\n'+r1.text+'\n-------------------------------------')
    print()

posts_shortcodes = set()
def scrape_posts():    
    def scrape_profiles(amn):
        for profileN in amn:
            ok = True
            if profileN.startswith('@'):
                profileN = profileN[1:]

            profile = Profile(profileN)
            try:
                profile.scrape(headers={'user-agent':str(generate_user_agent()),'cookie':str(secrets.token_hex(8)*2)})
                posts = list(profile.get_recent_posts(amt=12))
            except ValueError:
                ok = False
                print(exl+' The account is banned or does not exist! >> '+c('@'+profileN))
                sleep(2)
            except:
                ok = False
                print(f'\n{exl} Error while scraping from the profile! >> '+c('@'+profileN))
                print(exl+' If you are using a VPN service please disable it!')
                print(exl+' If you are not using any VPN service try any other instagram account')
                sleep(5)
                sys.exit()
            if ok:
                for post in posts:
                    shortcode = post.json_dict['shortcode']
                    posts_shortcodes.add(shortcode)
                if len(posts) == 0:
                    print(exl+' Error while scraping posts from '+c('@'+profileN)+'. The profile is either private or does\'nt exist.')
                    sleep(2)
                else:
                    print(ha+' Done Scraping '+str(len(posts))+' posts from '+c('@'+profileN))
                    sleep(2)
    
    def scrape_hashtags(amn,amnt):
        for hashy in amn:
            ok = True
            if hashy.startswith('#'):
                hashy = hashy[1:]
            _hashtag = Hashtag(f'https://www.instagram.com/explore/tags/{hashy}/')

            try:
                _hashtag.scrape()
            except exceptions.exceptions.InstagramLoginRedirectError:
                _hashtag.scrape(headers={'user-agent':str(generate_user_agent()),'cookie':str(secrets.token_hex(8)*2)})
            except ValueError:
                print(exl+' Hashtag >> '+c('#'+hashy)+' Does not exist or have 0 posts!')
                ok = False
                sleep(2)
            except Exception as er:
                ok = False
                print(exl+' Error while scraping posts from '+c('#'+hashy)+' !')
            
            if ok:
                try:
                    v = _hashtag.get_recent_posts(amt=amnt)
                except:
                    ok = False
                    print(exl+' Error while scraping from the hashtag! >> '+c('#'+hashy))
                    print(exl+' If you are using a VPN service please disable it!')
                    print(exl+' If you are not using any VPN service try any other instagram account')
                    sleep(5)
                    sys.exit()
                
                if amnt != len(v):
                    print('\n'+mult+' Maximum amount of posts can be scraped in '+c('#'+hashy)+' is '+str(len(v)))
                for post in v:
                    shortcode = post.json_dict['shortcode']
                    posts_shortcodes.add(shortcode)
                print(ha+' Done Scraping '+c(str(len(v)))+' posts from '+c('#'+hashy))

            
    
    def asky():            #         ASKING FOR POSTS
        while True:
            print(f'\n{ques} Currently there is '+c(str(len(list(posts_shortcodes))))+' posts. Do you want to scrape more?',end='')
            ans = input(f'''
[{c("1")}] Yes (from a profile/s)
[{c("2")}] Yes (from a Hashtag/s)
[{c("3")}] Yes (from a profile/s and hashtag/s)
[{c("4")}] Yes (from hashtags_and_profiles.txt file)
[{c("5")}] No
    >> ''')
            try:
                ans = int(ans)
                return ans
            except:
                print(exl+' Please enter the number of the option! (1,2,3 or 4)')
                sleep(5)

        #                                     ACTUAL CODE IS HERE    
    ans = asky()

    while True:
        if ans == 1:
            ans2 = input(f'''{ques} How many profiles do you want to scrape?
[{c("1")}] One profile (max 12 posts)
[{c("2")}] several profiles
    >> ''')
            try:
                assert int(ans2)
                if int(ans2) == 1:   #        PROFILE       ONE PROFILE
                    clear()
                    profileN = [input(ques+" Enter profile's username >> ")]
                    scrape_profiles(profileN)
                    
                elif int(ans2) == 2:    #     PROFILE        SEVERAL PROFILES
                    clear()
                    profiless = input(ques+' Enter the usernames seperating them with a space like this >> @google @dell @instagram ...\n >> ').split(' ')
                    profiless = [i[1:] if i.startswith('@') else i for i in profiless]
                    print()
                    scrape_profiles(profiless)
                else:
                    raise AssertionError          
            except AssertionError:
                clear()
                print(exl+' Please enter the number of the option! (1 or 2) only!')
                sleep(5)

        elif ans == 2:
            ans2 = input(f'''{ques} How many Hashtags do you want to scrape posts from ?
[{c('1')}] One hashtag
[{c('2')}] several Hashtags
    >> ''')
            try:
                assert int(ans2)
                if int(ans2) == 1:  #         HASHTAG     ONE HASHTAG
                    clear()
                    hashy = [input('Enter the hashtag you want to scrape posts from >> ')]
                    amnt = int(input(ques+' How many posts do you want to scrape from the hashtag? >> '))
                    scrape_hashtags(hashy,amnt)
                    
                    
                elif int(ans2) == 2: #         HASHTAG       SEVERAL HASHTAGS
                    clear()
                    hashtags = input(ques+' Enter the hashtags seperating them with a space like this >> #sun #love #vacation ...\n >> ').split(' ')
                    amnt = int(input(ques+' How many posts do you want to scrape from every hashtag? >> '))
                    hashtags = [i[1:] if i.startswith('#') else i for i in hashtags]
                    print()
                    scrape_hashtags(hashtags,amnt)

            except AssertionError:
                print(exl+' Please enter the number of the option! (1 or 2)!')
                sleep(5)
        elif ans == 3 or ans == 4:       #     HASHTAGS AND PROFILES !!
            clear()
            profiles = []
            hashtags = []

            if ans == 4:
                hashtags_and_profiles = ''
                try:
                    file = open('hashtags_and_profiles.txt','r',encoding='utf-8')
                    for i in file.readlines():
                        hashtags_and_profiles += i.strip('\n')+' '
                except Exception as er:
                    print(exl+' Error while openning hashtags_and_profiles.txt !! >> '+y(str(er)))
                    sleep(5)

            else:
                hashtags_and_profiles = input(f'\n{ques} Enter the hashtags and the profiles that you want to scrape seperating them with a space like this >> @instagram #ok #hashtag @a7.acc  >>> ')
            hashtags_and_profiles = hashtags_and_profiles.split(' ')
            if ans == 4:
                hashtags_and_profiles = hashtags_and_profiles[:-1]
            for tag in hashtags_and_profiles:
                if tag[0] == '@':
                    profiles.append(tag[1:])
                elif tag[0] == '#':
                    hashtags.append(tag[1:])
            print(mult+' Found '+c(str(len(hashtags)))+' hashtags and '+c(str(len(profiles)))+' profiles!')
            amnt = 0
            if len(hashtags) > 0:
                amnt = int(input(ques+' How many posts do you want to scrape from the hashtag? >> '))
            print(mult+' scraping ..')
                
            scrape_profiles(profiles)
            scrape_hashtags(hashtags,amnt)

        elif ans == 5:
            break
        ans = asky()

    # Scrape from a profile MAX 12

count = 0           # keep track of all the comments (sent or unsent)
bad = 0             # keep track of unsent comments
good = 0            # keep track of sent comments
#accoo = 0           # keep track of current commenting account
#ercount = 0         # keep track of the errors in each account
ertotal = 0         # keep track of all the errors in all the accounts
acban = 0           # keep track of the banned accounts
change = False
#chnge_acc_co = 0    # keep track of comments in each account
def comment(url,comm):
    global count,bad,good,ertotal,acban,cook,change
    system(f'title SENT:{str(good)}       BAD:{str(bad)}       ERROR:{str(ertotal)}       ACCOUNTS REMAINING:{str(len(cook))}')
    try:
        if len(cook) == 1 and change:
            print(exl+' This is the last account! ending the program..')
            return 'er1'
        current_acc = choice(cook)
    except:
        return 'er1'
    post_id = bot.get_media_id_from_link(self='',link=f'https://www.instagram.com/p/{url}/')
    url_comment = f'https://www.instagram.com/web/comments/{post_id}/add/'
    headers_comment = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-length': str(randint(30,40)),
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': f'ig_did=D37E2F4F-6193-4E76-B7C6-6FDBE4A0C230; mid=X_3LtAALAAFAdQMURlFUf_U68Q6H; ig_nrcb=1; csrftoken={current_acc["csrftoken"]}; shbid=11548; shbts=1615465726.6437705; rur=ASH,ds_user_id={current_acc["ds_user_id"]}; sessionid='+current_acc["sessionid"],
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/p/CMRSs2uhpUQ/',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': str(generate_user_agent()),
        'x-csrftoken': current_acc["csrftoken"],
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR1Y1dEsDcV-xq-u_7U0XISuyjCpWSS-VvmOhVU2N6rp9-nm',
        'x-instagram-ajax': '181fef01fd26',
        'x-requested-with': 'XMLHttpRequest'
            }

    data_comment = {
        'comment_text': f'{comm}',
        'replied_to_comment_id': ''
    }
    
    commenty = ''
    try:
        commenty = requests.post(url_comment,headers=headers_comment,data=data_comment,timeout=5).text
    except Exception as fv:
        ertotal += 1
        count += 1
        print(f"[{rod(str(count))}] Error While Commenting ! error message >> "+str(fv))
        sleep(5)


    if '"status":"ok"' in commenty:
        count += 1
        good += 1
        print(f"[{g(str(count))}] Comment Sent!")
        system(f'title SENT:{str(good)}       BAD:{str(bad)}       ERROR:{str(ertotal)}       ACCOUNTS REMAINING:{str(len(cook))}')
        data = json.loads(commenty)
        sleep(3)
    elif 'Please wait a few minutes before you try again.' in commenty:
        print(f'[{rod(str(count))}] An account banned temporarily from commenting.. changing the account..')
        bad += 1
        count += 1
        change = True
        sleep(2)
    else:
        count += 1
        bad += 1
        ertotal += 1
        if '"Unable to post comment."' in commenty:
            print(f"[{rod(str(count))}] Unable to post the comment >> "+y(commenty)+" the post owner probably closed the comments or the comments are limited.")
            print(f'https://www.instagram.com/p/{url}/')
        elif "Sorry, this media is not available." in commenty:
            print(f"[{rod(str(count))}] Error while commenting >> "+y(commenty)+f" post url >> https://www.instagram.com/p/{url}/")
        else:
            print(f"[{rod(str(count))}] Uknown error! comment message >> "+y(commenty)+'.. removing the account from the loop')
            acban += 1
            cook.remove(current_acc)
        sleep(5)        
    


def scraping_comments():
    while True:
        asky = input(f'''\n{ques} Do you want to scrape comments from comments.txt file or type one comment only??
[{c('1')}] Scrape comments from comments.txt 
[{c('2')}] Type only one comment
  >> ''')
        try:
            asky = int(asky)
            break
        except:
            print(exl+' Please enter one digit, 1 or 2 only')
            sleep(5)
            clear()
    comments = []
    if asky == 1:
        try:
            fil = open('comments.txt','r',encoding='utf-8')
        except Exception as er:
            print(exl+' Error while openning comments.txt file '+y(str(er)))
            sleep(5)
            exit()
        for i in fil.readlines():
            comments.append(i.strip('\n'))
        print(f'{ha} {c(str(len(comments)))} comments found in comments.txt!')
        sleep(2)
        return comments
    elif asky == 2:
        comment = input(ques+' Enter your comment >> ')
        comments.append(comment)
        return comments


logins()
total_acc = len(cook.copy())
if len(sessions) > 0:
    global ertype
    print(f'\n{g(str(len(sessions)))} accounts successfully logged in!')
    sleep(3)
    scrape_posts()
    links = list(posts_shortcodes)
    comments = scraping_comments()
    print('\n'+ha+' There are '+c(str(len(links)))+' posts.')
    sleep(5)

    for i in links:
        commy = choice(comments)
        ertype = comment(i,commy)
        system(f'title SENT:{str(good)}       BAD:{str(bad)}       ERROR:{str(ertotal)}       ACCOUNTS REMAINING:{str(len(cook))}')
        print()
        if ertype == 'er1':
            break
else:
    print(exl+' There is 0 accounts logged in! Change the accounts and try again.')
    sleep(5)
    sys.exit()
if ertype == 'er1':
    print(exl+' All accounts got banned from commenting!')
    sleep(3)
if good+bad == len(links):
    print(ha+' All comments sent !')

print(f'''
[{b('%')}] Results! :

[{y('!')}] accounts banned from commenting > {y(str(acban))}
[{g('#')}] comments sent successfully      > {g(str(good))}
[{rod('!')}] comments sent unsuccessfully    > {rod(str(bad))}
[{c('*')}] total comments                  > {c(str(len(links)))}
[{b('*')}] total accounts                  > {c(str(total_acc))}
[{y('!')}] Errors                          > {y(str(ertotal))}

''')
input('\nClick enter to exit the program!'.upper())
sys.exit()