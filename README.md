# JioFi Battery Notifier 

This is a simple python script which checks JioFi battery every 2 Minutes and notifies if level is lower than desired value. You can also run script jiofi_once.py for check battery level once. This Script works on both Linux and Windows.
If you want you can also include max desired level in script for notify on battery full.

## Python Version:
Python 3

## Prerequisite:
pip install requests

pip install py-notifier

#### Additional Installation only for Windows
pip install win10toast

## Parameters
-> url - JioFI's gateway address ( Use route -n for find ) (Most Probably 192.168.225.1 or 192.168.255.1)

-> min - Minimum Percentage Required

## Usage
**Simple Use**

	python jiofi_battery_notifier.py
	
**Check Once**

	python jiofi_once.py
**Auto Start at Boot**

	Follow guidelines for your operating system for running python scripts at startup.

## YouTube Tutorial
https://www.youtube.com/watch?v=_FRg6Q0JLlk

## Troubleshooting
####  Gateway Url Wrong
	Change default gateway Url of your JioFi
#### Unable to find percentage from requests
	Print response using using print(response.text) and find out what pattern is used for your device
#### Others
	Debug your code and find out what is going wrong and if you need my help reach me at "git.hrca@gmail.com"

## Liked my work?
<a href="https://www.buymeacoffee.com/parveshmonu" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

## Websites
https://github.com/Parveshdhull
<br />https://twitter.com/ParveshMonu
<br />https://youtube.com/right2trick





