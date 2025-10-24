print(" *** iOS Beta Downloader *** ")
print("         Version 0.2")
print("           Turlum25")
print("-----------------------------")
print("Supported:")
print("iPod1,1 (iPod touch 1)")
print("More coming soon")

user_input = input("Enter a device (Example: iPod1,1) >>> ")

if user_input == "iPod1,1":
    print("Versions:")
    print("2.0")
    print(" beta3")
    print("----")
    print("3.0")
    print(" beta1")
    print(" beta2")
    print(" beta3")
    print(" beta4")
    print(" beta5")
    print("-----")
    print("3.1")
    print(" beta1")
    print(" beta2")
    print(" beta3")
    print("Download speed may be very slow as it is taken from the Internet Archive")
    ios_input = input("Enter version (example: 3.0 beta1) >>> ")

import urllib.request
import ssl
import time

ssl._create_default_https_context = ssl._create_unverified_context

def safe_download(url, filename, retries=5):
    for i in range(retries):
        try:
            urllib.request.urlretrieve(url, filename)
            print("Finished downloading")
            return
        except Exception as e:
            print(f"download failed ({e}), retrying... {i+1}/{retries}")
            time.sleep(3)
    print("failed after retries")

if ios_input == "2.0 beta3":
    url1 = "https://archive.org/download/Apple_iPod_Firmware/Apple%20iPod%20Touch%201.1%20Firmware%202.0%20%282.0.5A240d%29%20%28beta3%29/media_ipsw.rar/iPod1%2C1_2.0_5A240d_Restore.ipsw"
    print("Downloading from", url1)
    urllib.request.urlretrieve(url1, url1.split('/')[-1])
    print("Finished downloading")

elif ios_input == "3.0 beta1":
    url2 = "https://archive.org/download/Apple_iPod_Firmware/Apple%20iPod%20Touch%201.1%20Firmware%203.0%20%283.0.7A238j%29%20%28beta%29/media_ipsw.rar/iPod1%2C1_3.0_7A238j_Restore.ipsw"
    print("Downloading from", url2)
    urllib.request.urlretrieve(url2, url2.split('/')[-1])
    print("Finished downloading")

elif ios_input == "3.0 beta2":
    url3 = "https://archive.org/download/Apple_iPod_Firmware/Apple%20iPod%20Touch%201.1%20Firmware%203.0%20%283.0.7A259g%29%20%28beta%29/media_ipsw.rar/iPod1%2C1_3.0_7A259g_Restore.ipsw"
    print("Downloading from", url3)
    urllib.request.urlretrieve(url3, url3.split('/')[-1])
    print("Finished downloading")

elif ios_input == "3.0 beta3":
    url4 = "https://archive.org/download/Apple_iPod_Firmware/Apple%20iPod%20Touch%201.1%20Firmware%203.0%20%283.0.7A280f%29%20%28beta%29/media_ipsw.rar/iPod1%2C1_3.0_7A280f_Restore.ipsw"
    print("Downloading from", url4)
    urllib.request.urlretrieve(url4, url4.split('/')[-1])
    print("Finished downloading")

elif ios_input == "3.0 beta4":
    url5 = "https://archive.org/download/Apple_iPod_Firmware/Apple%20iPod%20Touch%201.1%20Firmware%203.0%20%283.0.7A280f%29%20%28beta%29/media_ipsw.rar/iPod1%2C1_3.0_7A300g_Restore.ipsw"
    print("Downloading from", url5)
    urllib.request.urlretrieve(url5, url5.split('/')[-1])
    print("Finished downloading")

elif ios_input == "3.0 beta5":
    url6 = "https://archive.org/download/Apple_iPod_Firmware/Apple%20iPod%20Touch%201.1%20Firmware%203.0%20%283.0.7A312g%29%20%28beta5%29/media_ipsw.rar/iPod1%2C1_3.0_7A312g_Restore.ipsw"
    print("Downloading from", url6)
    urllib.request.urlretrieve(url6, url6.split('/')[-1])
    print("Finished downloading")

elif ios_input == "3.1 beta1":
    url7 = "https://archive.org/download/Apple_iPod_Firmware/Apple%20iPod%20Touch%201.1%20Firmware%203.1%20%283.1.7C97d%29%20%28beta%29/media_ipsw.rar/iPod1%2C1_3.1_7C97d_Restore.ipsw"
    print("Downloading from", url7)
    urllib.request.urlretrieve(url7, url7.split('/')[-1])
    print("Finished downloading")

elif ios_input == "3.1 beta2":
    url8 = "https://archive.org/download/Apple_iPod_Firmware/Apple%20iPod%20Touch%201.1%20Firmware%203.1%20%283.1.7C106c%29%20%28beta2%29/media_ipsw.rar/iPod1%2C1_3.1_7C106c_Restore.ipsw"
    print("Downloading from", url8)
    urllib.request.urlretrieve(url8, url8.split('/')[-1])
    print("Finished downloading")

elif ios_input == "3.1 beta3":
    url9 = "https://archive.org/download/Apple_iPod_Firmware/Apple%20iPod%20Touch%201.1%20Firmware%203.1%20%283.1.7C116a%29%20%28beta3%29/media_ipsw.rar/iPod1%2C1_3.1_7C116a_Restore.ipsw"
    print("Downloading from", url9)
    urllib.request.urlretrieve(url9)
    print("Finished downloading")

else:
  print("ERROR: Device name or iOS beta version name is incorrect")
