from random import choices
from string import ascii_lowercase
from time import sleep
from selenium import webdriver

try:
    num_of_domains = int (input ('how many domains do you need ?'))
except ValueError:
    print('please enter valid number!\nthe default number is 10')
    num_of_domains = 10

try:
    num_of_domain_characters = int (input ('how many characters yout domain should be have ?'))
except ValueError:
    print('please enter valid number!\nthe default number is 4')
    num_of_domain_characters = 4

def randomain(l):
    return ''.join(choices(ascii_lowercase, k=l)) + '.ir'

wd = webdriver.Firefox()

dom = ''
crcts = 0

while crcts < num_of_domains:
    dom = randomain(num_of_domain_characters)
    wd.get(f'https://iranhost.com/whois/?q={dom}')
    sleep(5)
    try:
        wd.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/whois/div/div/whois-free-result')
        print(dom)
        crcts += 1
    except:
        continue

wd.close()
