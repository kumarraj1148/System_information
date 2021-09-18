from selenium import webdriver
import time


class Cricbuzz():

    def Summary_and_Scorecard(url):

        Url="https://www.cricbuzz.com/"
        driver = webdriver.Chrome('/usr/local/bin/chromedriver')
        driver.get(Url)
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='teamDropDown']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='page-wrapper']/div[5]/div[1]/div[2]/div[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='page-wrapper']/span[2]/span/div[2]/nav/a[3]").click()
        time.sleep(2)
        summary = driver.find_element_by_xpath("//*[@id='series-matches']/div[3]").text
        print("================ Summary ==============="
                       '\n',summary,'\n',
          "================*********==============")
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='series-matches']/div[3]/div/a[2]").click()
        time.sleep(2)
        results = driver.find_element_by_xpath("//*[@id='matchCenter']/div[3]/div[2]/div[2]").text

        print("================ Results ==============="
              '\n', results, '\n',
              "================*********==============")

        driver.find_element_by_xpath("//*[@id='matchCenter']/div[2]/nav/a[2]").click()
        time.sleep(2)


        details = driver.find_elements_by_xpath("//*[@class='cb-col cb-col-100 cb-scrd-itms']")
        details = details[:100]

        Fetch_Details = []
        i=0
        for a in details:
            #print(i.text)
            Fetch_Details.append(a.text)
        for a in Fetch_Details:
            a = a.split('\n')
            if a[0].find('Pant') >= 0:
                i=i+1
                print('Player {}st Innings score'.format(i))
                print('{} scored {} runs for {} balls and {} fours {} sixes with {} strike rate'.format(a[0], a[2] ,a[3] ,a[4] ,a[5] ,a[6]))
                print("****************************************")



result=Cricbuzz()
result.Summary_and_Scorecard()


