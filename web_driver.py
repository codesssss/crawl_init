from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/uas/login")
elem_name= driver.find_element_by_id("username")
elem_name.send_keys("xuhang.shi@outlook.com")


elem_psw=driver.find_element_by_id("password")
elem_psw.send_keys("200831sxh")
elem_login=driver.find_element_by_xpath("//*[@id='app__container']/main/div/form/div[3]/button")
elem_login.click()
#-*-coding:utf-8-*-

# #此处为用户所要登陆的网站链接
# url = 'https://www.linkedin.com/uas/login'
# #浏览器访问网站的cookie信息
# cookie = {"Cookie":'"v=2&8c72485c-a44d-4344-81e7-12ca5de779e7"; bscookie="v=1&2020020118082174c9e036-300c-4a4f-8bef-d67bb4360caaAQFd1TzjQ5_pNcqdTjYFuzFqhrYEykyN"; lissc=1; lissc1=1; lissc2=1; sl=v=1&w7vHW; li_at=AQEDAS81I88AS9N3AAABcAHwgR0AAAFwJf0FHVEAuYiCjQIOrn6EfI8mYquqpAfnRHsdhT_TB9TxtOtJ5gQTbZ-sFO9MmlS07OuyjgkdpvoToE4c04oDr0d-DV4DT-vVPMELn96Baj1xi0FVlCCCnvE9; liap=true; li_cc=AQEKJuq7E539EQAAAXAB8IKfhWxdpGIQ1PZqJEnf3vZUuS-Am8uFXzILJ9vJKJR1xwHR6NUxkQ7f; lang=v=2&lang=zh-cn; _lipt=CwEAAAFwAfCUKUuwDYuWAapunIJt20G6O_bLYuKeItZr2bGb3kRV-URIw4i9Lnu9ucyQaB1m7NpR72ikBDchfObTtKKN9iMSsBO3yH7hOKz3C3j2EUhkgHI; _guid=e1175cd5-d7df-48b0-8eb8-1518dc55a174; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; aam_uuid=72925580792500894570984962441494028389; li_sugr=60a21930-40f7-45cd-a829-56eda805c217; UserMatchHistory=AQJDG3rdWmIB7gAAAXAB8KODfYTPkjrmziLTF8gdTXpg6qBbj_Xq8pvSw3vk4bzcpVoQ30HrVL-2-JtNizkkj0uIQSFhbc4jXrcH-y-TnOR4au7z-Hi_QJ66S07e-PxxlMJsnn_5QxsCORFozYA63A364vIVMkW5inqgJhxiCqzpRluin5ADcCq0xnzX0TzO9I4b01fATTPO9c60enufVzCius5KUmnu; li_oatml=AQG9CbMseDMLtgAAAXAB8KP05l-3WlxMVTVPGB9dFguWEOtMJPl5Ws38E3eeaeKxaVxBCJk_gPIY0l_1SacmdbZWQyuYDTzh; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-1303530583%7CMCIDTS%7C18294%7CMCMID%7C73485923713491738180965007423421584302%7CMCAAMLH-1581185315%7C11%7CMCAAMB-1581185315%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1580587712s%7CNONE%7CMCCIDH%7C-1475695649%7CvVersion%7C3.3.0; lidc="b=SGST00:g=8:u=1:i=1580605031:t=1580664971:s=AQF54d3YbvB919Ef1mffxYr_GzIu2ayB"'}
# #requests请求，获取登录网站页面
# driver.add_cookie(cookie)
# html = requests.get(url,cookies=cookie).content
# print (html)

