
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Audio code mapping
audio_code = {
            "captcha_voice/b6589fc6ab0dc82cf12099d1c2d40ab994e8410c.mp3": '0',
            "captcha_voice/356a192b7913b04c54574d18c28d46e6395428ab.mp3": '1',
            "captcha_voice/da4b9237bacccdf19c0760cab7aec4a8359010b0.mp3": '2',
            "captcha_voice/77de68daecd823babbb58edb1c8e14d7106e83bb.mp3": '3',
            "captcha_voice/1b6453892473a467d07372d45eb05abc2031647a.mp3": '4',
            "captcha_voice/ac3478d69a3c81fa62e60f5c3696165a4e5e6ac4.mp3": '5',
            "captcha_voice/c1dfd96eea8cc2b62785275bca38ac261256e278.mp3": '6',
            "captcha_voice/902ba3cda1883801594b6e1b452790cc53948fda.mp3": '7',
            "captcha_voice/fe5dbbcea5ce7e2988b8c69bcfdfde8904aabc1f.mp3": '8',
            "captcha_voice/0ade7c2cf97f75d009975f4d720d1fa6c19f4897.mp3": '9',
}
class CourseBot:
    def __init__(self, uid, pwd) -> None:
        self.chrome_options = Options()
        ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
        self.chrome_options.add_argument('user-agent={}'.format(ua))
        self.uid, self.pwd = uid, pwd
        self.chrome = None
        self.target = 'https://www.ais.tku.edu.tw/EleCos_English/loginE.aspx'

 
    def __run_driver(self) -> None:
        self.chrome = webdriver.Chrome(options=self.chrome_options)
        self.chrome.get(self.target)

    def is_exist(self, by,value) -> bool:
        try:
            self.chrome.find_element(by,value)
            return True
        except:
            return False

    # Get audio code and map to number
    def passVidCode(self) -> list:
        try:
            vid = self.chrome.execute_script('readyAudio();return playlist')
            return ''.join(map(audio_code.get, vid))
        except:
            self.chrome.quit()
            input('Currently it is not course selection time. Please try again later.')
            exit()


    def drop_course_code(self, drop_list:list,log=False) -> None:
        if drop_list == None or len(drop_list) == 0:
            return
        for i in drop_list:
            self.chrome.execute_script(
                f"""
                document.getElementById('txtCosEleSeq').value = '{i}';
                __doPostBack('btnDel','');
                """
            )
            if log:print('drop success: ', i)


    def add_course_code(self, add_list:list,log=False) -> None:
        _add_list = add_list.copy()
        for c in add_list:
            self.chrome.execute_script(
                f"""
                document.getElementById('txtCosEleSeq').value = '{c}';
                __doPostBack('btnAdd','');
                """
            )
   
            if self.is_exist(By.XPATH,
                        f"//table[@id='GridView1']//td[text()='{c}']"):
                if log:print('add success: ', c)
                _add_list.remove(c)
            else:
                if log:print('add failed: ', c)
        return _add_list

 
    def login(self) -> bool:
        self.chrome.execute_script(
        f"""
            document.getElementById('txtStuNo').value = '{self.uid}';
            document.getElementById('txtPSWD').value = '{self.pwd}';
            document.getElementById('txtCONFM').value = '{self.passVidCode()}';
            __doPostBack('btnLogin','');
        """
        )
        # if login failed, return False
        if 'login' in self.chrome.current_url:
            if self.is_exist(By.XPATH,
                    "//*[text()='password error']"):
                exit('password error')
            return False
        else:
            return True
       

    def main(self, add_list:list, drop_list=None) -> None:
        self.__run_driver()
        while len(add_list)>0:
            count = 0
            # if login failed, try again
            while not self.login():
                continue

            if drop_list != None:
                self.drop_course_code(drop_list)
                drop_list = None
            
            while len(add_list)>0:
                count+=len(add_list)
                add_list=self.add_course_code(add_list) 
                if count >= 30:
                    self.chrome.execute_script('__doPostBack("btnLogout","")')
                    break
            
        self.chrome.quit()
        input('Success! press Enter to exit')
        exit()


if __name__ == '__main__':
    # Change to your own student number and password
    bot = CourseBot('stdNo', 'pwd')

    # Example:
    # drop_list = ['0991','3076']
    # add_list = ['2336','2337']
    drop_list=[]
    add_list = ['2336']

    bot.main(add_list=add_list, drop_list=drop_list)
