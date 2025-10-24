import urllib.request
import ssl
import time
# common practice is to put imports at the beginning

data = { # it might be a better idea to put this in a separate file
    "iPod1,1": { # device identifier
        "2.0": { # "category" / major version
            "beta3": "https://archive.org/download/Apple_iPod_Firmware/Apple%20iPod%20Touch%201.1%20Firmware%202.0%20%282.0.5A240d%29%20%28beta3%29/media_ipsw.rar/iPod1%2C1_2.0_5A240d_Restore.ipsw" # specific version (which i refer to later in code as "minor version") and download link
        },
        "3.0": {
            "beta1": "https://archive.org/download/Apple_iPod_Firmware/Apple%20iPod%20Touch%201.1%20Firmware%203.0%20%283.0.7A238j%29%20%28beta%29/media_ipsw.rar/iPod1%2C1_3.0_7A238j_Restore.ipsw",
            "beta2": "https://archive.org/download/Apple_iPod_Firmware/Apple%20iPod%20Touch%201.1%20Firmware%203.0%20%283.0.7A259g%29%20%28beta%29/media_ipsw.rar/iPod1%2C1_3.0_7A259g_Restore.ipsw",
            "beta3": "https://archive.org/download/Apple_iPod_Firmware/Apple%20iPod%20Touch%201.1%20Firmware%203.0%20%283.0.7A280f%29%20%28beta%29/media_ipsw.rar/iPod1%2C1_3.0_7A280f_Restore.ipsw",
            "beta4": "https://archive.org/download/Apple_iPod_Firmware/Apple%20iPod%20Touch%201.1%20Firmware%203.0%20%283.0.7A280f%29%20%28beta%29/media_ipsw.rar/iPod1%2C1_3.0_7A300g_Restore.ipsw",
            "beta5": "https://archive.org/download/Apple_iPod_Firmware/Apple%20iPod%20Touch%201.1%20Firmware%203.0%20%283.0.7A312g%29%20%28beta5%29/media_ipsw.rar/iPod1%2C1_3.0_7A312g_Restore.ipsw"
        },
        "3.1": {
            "beta1": "https://archive.org/download/Apple_iPod_Firmware/Apple%20iPod%20Touch%201.1%20Firmware%203.1%20%283.1.7C97d%29%20%28beta%29/media_ipsw.rar/iPod1%2C1_3.1_7C97d_Restore.ipsw",
            "beta2": "https://archive.org/download/Apple_iPod_Firmware/Apple%20iPod%20Touch%201.1%20Firmware%203.1%20%283.1.7C106c%29%20%28beta2%29/media_ipsw.rar/iPod1%2C1_3.1_7C106c_Restore.ipsw",
            "beta3": "https://archive.org/download/Apple_iPod_Firmware/Apple%20iPod%20Touch%201.1%20Firmware%203.1%20%283.1.7C116a%29%20%28beta3%29/media_ipsw.rar/iPod1%2C1_3.1_7C116a_Restore.ipsw"
        }
    }
}

print(""" *** iOS Beta Downloader ***
         Version 0.3
           Turlum25
-----------------------------
Supported:""")
for device in data: # this iterates over the data dictionary, printing each device identifier
    print(device)
print("More coming soon")

awaiting_valid_input = True

while awaiting_valid_input:
    try:
        device = input("Enter a device (Example: iPod1,1) >>> ")

        if device in data:
            print("Versions:")
            for major_version in data[device]: # we're getting the device and iterating over the major versions
                print(major_version)
                for minor_version in data[device][major_version]: # now we're getting the major version for the device and iterating over the minor versions
                    print(f" {minor_version}")
            print("----")
            awaiting_valid_input = False # this will allow the loop to exit
        else:
            print("Not a supported device, try again or Ctrl+C to exit.")
    except KeyboardInterrupt:
        exit() # exit gracefully
    except Exception as exception:
        raise exception # if there's an exception that isn't a keyboardinterrupt, raise it (usual behavior of an exception)

print("Download speed may be very slow as it is taken from the Internet Archive")

awaiting_valid_input = True

while awaiting_valid_input:
    try:
        raw_ios_input = input("Enter version (example: 3.0 beta1) >>> ")
        ios_input = raw_ios_input.split(" ") # !!!!!!!!! this is designed with the assumption that the ONLY space should be between the "major version" and "minor version"!!!!!!!!
        if len(ios_input) != 2: # if there are more or less than two items in the split
            print("Couldn't find that iOS version, are you sure you typed it correctly? Ctrl+C to exit.")
        elif ios_input[0] not in data[device]: # if the major version is not in the device dictionary
            print("Couldn't find that iOS version, are you sure the device supports it? Ctrl+C to exit.")
        elif ios_input[1] not in data[device][ios_input[0]]: # if the minor version is not in the major version's dictionary in the device dictionary
            print("Couldn't find that iOS version, are you sure the device supports it? Ctrl+C to exit.")
        else:
            awaiting_valid_input = False # we have determined our version, exit the loop
    except KeyboardInterrupt:
        exit()
    except Exception as exception:
        raise exception

ssl._create_default_https_context = ssl._create_unverified_context # what does this do?

def safe_download(url, filename, retries=5): # what's this unused function?
    for i in range(retries):
        try:
            urllib.request.urlretrieve(url, filename)
            print("Finished downloading")
            return
        except Exception as e:
            print(f"download failed ({e}), retrying... {i+1}/{retries}")
            time.sleep(3)
    print("failed after retries")

url = data[device][ios_input[0]][ios_input[1]]
print("Downloading from", url)
urllib.request.urlretrieve(url, url.split('/')[-1])
print("Finished downloading!")
