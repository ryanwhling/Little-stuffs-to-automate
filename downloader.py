import requests, m3u8 #if error then do "pip3 install requests m3u8"
### change this for every download ##############
# master list =  press F12, navigate to network, search for "m3u8", reload tab, right click "index.m3u8", copy url
master_list =r"https://s-cloudfront.cdn.ap.panopto.com/sessions/6e6c5bbc-fd02-4883-b8c5-ac4200dfb1cf/068c06c7-bb98-4709-8ee1-ac4200dfb1d8-59ac1b1d-907a-4322-8385-ac4200ee12f3.hls/1500000/index.m3u8"
# the absolute path of the file location you want to save e.g. /Users/nico/Documents/FINA3290/lecture \vids/
flocation = ""
# how u want to name the file , must end at .ts unless u want me to make it mp4
file_name = "Chapter_3_P5.ts"
############## end of chenge this ####################

###### DO NOT EDIT ANYTHING BELOW ######
base_url = ""
for elm in master_list.split('/')[:-1]:
    base_url += (elm+'/')

r= requests.get(master_list)
playlist = m3u8.loads(r.text)

with open(flocation+file_name, 'wb') as f:
    for block in playlist.data["segments"]:

        fname = block["uri"]
        print(f"downloading {fname}")
        snap = requests.get(base_url+fname)
        f.write(snap.content)
