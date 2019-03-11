import requests

badgeCount = 0

# type in your acclaim badges url
# url = "https://www.youracclaim.com/user/robert-mapstead"
print("\nThis program lists your badges from the Acclaim Badges Platform \n")
name = input("Enter user name. Example: robert-mapstead >>> ")
url = "https://www.youracclaim.com/users/"+name

# Getting the webpage, creating a Response object.
response = requests.get(url)

# Extracting the source code of the page.
#if response == 200:
urlx = url+"/badges.json?api=api&page="+str(1).strip()
response = requests.get(urlx)
jdata = response.json()
j_pcount = jdata['metadata']['total_pages']
j_tcount = jdata['metadata']['total_count']
print(urlx)

badges = []
for k in range(j_pcount):
    j = k + 1
    if j > 1:
        urlx = jdata['metadata']['next_page_url']
        print(urlx) 
        response = requests.get(urlx)
        jdata = response.json()
    j_count = jdata['metadata']['count']
    i = 0
    for i in range(j_count):
        j_name = jdata['data'][i]['badge_template']['name']
        badges.append(j_name)

# Extracting text from the the <a> tags, i.e. class badges.
print()
print("Copy all of this text below OR copy the text from the badges.txt file on the left sidebar for use in your resume, CV, or Social Media Profiles: \n")

fobj = open('badges.txt', 'a')
#fobj.write(url+"\n")
fobj.write(url + "\n")
print("\nmy Badges:")
for badge in badges:
    #print(badge.text)
    print(badge.rstrip())
    with open('badges.txt','a') as f: 
        fobj.write(badge.rstrip() + "\n")
    badgeCount = badgeCount + 1

print()

print("Total Badges Earned: " + str(badgeCount))
with open('badges.txt','a') as f:
    fobj.write("\ntotalBadges: " + str(badgeCount) + "\n")
print()
print("How many badges do you have?  https://bit.ly/uc-mybadges\n")
print("Source: "+url+"\n")

fobj.close()
