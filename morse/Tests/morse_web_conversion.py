from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time, sys, os, getpass

def main():
  
  os.system('clear')
    
  print 'Starting Firefox'
  br = webdriver.Firefox()
  # Note: with chrome also works but prints:
  #22848:24292:1104/181539.469:ERROR:gl_surface_egl.cc(538)] EGL Driver message (Error) eglQueryDeviceAttribEXT: Bad attribute.
  #print 'Starting Chrome'
  #br = webdriver.Chrome()
  print 'Loading web page...'
  br.get("https://morsecode.scphillips.com/translator.html")

  print 'feeding information...'
  print 'Typing CustNum and zipCode'
  ele = br.find_element_by_id('input')
  ele.send_keys("SOS SOS")

  try:
    ele = br.find_element_by_id('translate')
    ele.click()
    print 'translate button hit'
  except:
    print 'translate button fail'
    return 1

  print "5 sec delay, then reading output..."	
  time.sleep(5)	
  ele = br.find_element_by_id('output')
  time.sleep(5)
  print "text: "
  #print ele.text # just returns empty string
  print ele.get_attribute("value") # this works!
  
  
main()
