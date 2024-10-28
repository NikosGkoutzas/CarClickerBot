# Nick Gkoutzas - Feb 2022 ---------------
# --------------- Last update: Oct 28 2024
# ----------------------------------------

from selenium import webdriver
from datetime import datetime , time , date
import time , datetime , os , sys , smtplib , linecache , socket , imaplib , email , re
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from email.header import decode_header


last_upgrade_version = "v28.10.24"
lines = tuple(open("passwords.txt" , 'r'))
FROM_EMAIL = lines[0].strip() 
FROM_PWD = lines[1].strip()  
ToMe = lines[2].strip()
ToOther = lines[3].strip()
site_username = lines[4].strip()
site_password = lines[5].strip()
PATH_NAME = os.getcwd() + '/'
dailyTotalUpdates = 200



class driver:
    def __init__(self):
        options = Options()
        #options.add_argument('--headless') # hide firefox window
        self.driver = webdriver.Firefox(options=options) # call Firefox

    def openUrl(self , url):
        try:
                self.driver.get(url)
        except Exception as e:
                print(f"Error opening URL: {e}")
        # open URL

    def quit(self):
        self.driver.quit()
        # quit from firefox

    def findElement(self , button_string , case , timeout=10):
        try:
            # Wait for the element to become visible
            element =  WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, button_string)))
            return element
        except:
            email_instance = _email_()
            timer_instance = timer()
            if(case == 'accept'):
                email_instance.send_email("⚠️ Critical situation" , timer_instance.dateAndtime() + "CarClickerBot can't accept cookies due to button code search failure." , ToMe)
                email_instance.send_email("⚠️ Critical situation" , timer_instance.dateAndtime() + "CarClickerBot can't accept cookies due to button code search failure." , ToOther)
                print('CarClickerBot can\'t accept cookies due to\nbutton code search failure.')
            elif(case == 'username'):
                email_instance.send_email("⚠️ Critical situation" , timer_instance.dateAndtime() + "CarClickerBot can't place username due to field code search failure." , ToMe)
                email_instance.send_email("⚠️ Critical situation" , timer_instance.dateAndtime() + "CarClickerBot can't place username due to field code search failure." , ToOther)
                print('CarClickerBot can\'t place username due to\nfield code search failure.')
            if(case == 'password'):
                email_instance.send_email("⚠️ Critical situation" , timer_instance.dateAndtime() + "CarClickerBot can't place password due to field code search failure." , ToMe)
                email_instance.send_email("⚠️ Critical situation" , timer_instance.dateAndtime() + "CarClickerBot can't place password due to field code search failure." , ToOther)
                print('CarClickerBot can\'t place password due to\nfield code search failure.')
            elif(case == 'login'):
                email_instance.send_email("⚠️ Critical situation" , timer_instance.dateAndtime() + "CarClickerBot can't login due to button code search failure." , ToMe)
                email_instance.send_email("⚠️ Critical situation" , timer_instance.dateAndtime() + "CarClickerBot can't login due to button code search failure." , ToOther)
                print('CarClickerBot can\'t login due to\nbutton code search failure.')
            sys.exit(0)
        # driver return the button using the css selector



class initialize:
    def __init__(self , instance):
        self.on_time = datetime.datetime.strptime('07:00:00' , '%H:%M:%S').time()    # start updates at this time
        self.off_time = datetime.datetime.strptime('23:55:00' , '%H:%M:%S').time()   # stop updates at this time
        self.now = datetime.datetime.now()
        self.numOfMachines = instance.read_NumberOfMachines("NumberOfMachines.txt")
        self.machinesEachUpdate = [0] * self.numOfMachines
        self.readUpdateNumberFile = open("updateNumber.txt" , 'r')
        self.currentPosUpdate = int(self.readUpdateNumberFile.read() )
        self.readUpdateNumberFile.close() 
        # initialize:
        #       a list for all machines initializing at 0 (0 updates for all machines so far)
        #       and the current position of the list that driver is updating right now

    @staticmethod
    def clear_geckodriver_log():
        if(os.path.exists(PATH_NAME + "geckodriver.log")):   
            with open("geckodriver.log") as geckodriverLogFile:
                geckodriverLogFile.truncate(0)

    # erase content of 'geckodriver.log' file which is created each time (in order to not be full)



class fileSettings:
    @staticmethod
    def readTotalUpdates():
        read_update = open("totalUpdates.txt" , 'r')
        readMe = read_update.read()
        read_update.close()
        return int( readMe )
        # return the number of total updates


    @staticmethod
    def read_machines_urls(file , line):
        return linecache.getline(file , line).strip("\n")
        # return the specified line (machine) from the file

    @staticmethod
    def write_delay(file_name , writeDelay):    
        delay = open(file_name , 'w')
        delay.write( str(writeDelay) )
        delay.flush()
        delay.close()
        # write a specific delay at the file (initial value: 5 minutes)
        # This means that the duration between updates must take 5 minutes

    @staticmethod
    def read_NumberOfMachines(file):
        machinesNumber = open(file , 'r')
        numberOfMachines = machinesNumber.read()
        machinesNumber.close()
        return int(numberOfMachines)
        # return the number of machines (It reads all the lines of the file)

    @staticmethod
    def update_machines_number(file , number):
        update_nuber = open(file , 'w')
        update_nuber.write( str(number) )
        update_nuber.flush()
        update_nuber.close()
        # update the number of all machines in the file

    @staticmethod
    def replace_line(file , line_num , text):
        lines = open(file , 'r').readlines()
        lines[line_num] = str(text[line_num]) + "\n"
        out = open(file , 'w')
        out.writelines(lines)
        out.flush()
        out.close()
        # replace a specific line of the file with another one
    
    @staticmethod
    def delete_line(file , line_num):
        lines = open(file , 'r').readlines()
        lines[line_num] = ""
        out = open(file , 'w')
        out.writelines(lines)
        out.flush()
        out.close()
        # delete a specific line of the file

    @staticmethod
    def read_GitHubUpdatesNumber(file_name):
        file_ = open(file_name , 'r')
        number = file_.read()
        file_.close()
        return int(number)
        # return the number of github's update the a human being made today
        # Useful when I upload a new version of app on GitHub in order to
        # solve a problem. When I send a specific email to inform system
        # that a new app version is ready, this number is used, so that the
        # human being get informed of how many updaloads are made today

    @staticmethod
    def read_feedbackNumber(file_name):
        file_ = open(file_name , 'r')
        number = file_.read()
        file_.close()
        return int(number)
        # As before, return the feedback number. A human being can send email
        # in order to inform him/her about the app status and the system can
        # show how many feedbacks are made today.

    @staticmethod
    def write_changeUsername_or_password(userOrPassw , index):
        with open('passwords.txt', 'r') as file:
            lines = file.readlines()

        lines[index] = userOrPassw + '\n'
        with open('passwords.txt', 'w') as file:
            file.writelines(lines)
        # write new username or password for login

    @staticmethod
    def read_resetNumber(file_name):
        file_ = open(file_name , 'r')
        number = file_.read()
        file_.close()
        return int(number)
        # return number of app reset

    @staticmethod
    def write_resetNumber(file_name , number):
        file_w = open(file_name , 'w')
        file_w.write(str(number))
        file_w.flush()
        file_w.close()
        # update the number of app reset

    @staticmethod
    def read_imported_removed_machines(file_name):
        f = open(file_name , 'r')
        num = f.read()
        f.close()
        return int(num)
        # return the number of imported/removed machines

    @staticmethod
    def write_imported_removed_machines(file_name , number):
        f = open(file_name , 'w')
        f.write(str(number))
        f.flush()
        f.close()
        # write the number of imported/removed machines

    @staticmethod
    def write_GitHubUpdatesNumber(file_name , number):
        file_w = open(file_name , 'w')
        file_w.write(str(number))
        file_w.flush()
        file_w.close()
        # update the number of new releases from github made this day

    @staticmethod
    def write_FeedbackNumber(file_name , number):
        file_w = open(file_name , 'w')
        file_w.write(str(number))
        file_w.flush()
        file_w.close()
        # update the number of feedbacks made this day

    @staticmethod
    def read_total_errors(file_name):
        errors__ = open(file_name , 'r')
        numOfErrors = errors__.read()
        errors__.close()
        return int(numOfErrors)
        # return the total errors made till now

    @staticmethod
    def write_total_errors(file_name):
        errors__ = open(file_name , 'r')
        numOfErrors = int( errors__.read() ) + 1
        errors__.close()
        errors__ = open(file_name , 'w')
        errors__.write( str(numOfErrors) )
        errors__.flush()
        errors__.close()
        # write the total errors made till now
    
    @staticmethod
    def writeNumOfErrors(file_name , number):
        write_err = open(file_name , 'w')
        write_err.write( str(number) )
        write_err.flush()
        write_err.close()
        # write the number of errors
        # if number of errors == 20 -> sends email to human being and reset this number



class timer:
    def __init__(self):
        self.sec__ = 0
        self.min__ = 0
        self.hour__ = 0

    def time_correction(self):
        now = datetime.datetime.now()
        if(now.second < 10):
            self.sec__ = str(0) + str(now.second)
        else:
            self.sec__ = str(now.second)
        if(now.minute < 10):
            self.min__ = str(0) + str(now.minute)
        else:
            self.min__ = str(now.minute)
        if(now.hour < 10):
            self.hour__ = str(0) + str(now.hour)
        else:
            self.hour__ = str(now.hour)
        return self.sec__ , self.min__ , self.hour__ , (str(self.hour__) + ":" + str(self.min__) + ":" + str(self.sec__))
        # return the current time

    def dateAndtime(self):
        today = date.today()
        correct_day = '0' if today.day  < 10 else ''
        correct_month = '0' if today.month  < 10 else ''
        correct_year = '0' if today.year  < 10 else ''
        str_date = correct_day + str(today.day) + "/" + correct_month + str(today.month) + "/" + correct_year + str(today.year)

        return str_date + ', ' + self.time_correction()[3] + '<br><br>'
    
    @staticmethod
    def computeDelay(endTimeHours , endTimeMinutes , endTimeSeconds):
        global dailyTotalUpdates
        now = datetime.datetime.now()
        currentTime = datetime.datetime(now.year, now.month , now.day , now.hour , now.minute , now.second)
        finalTime = datetime.datetime(now.year, now.month , now.day , endTimeHours , endTimeMinutes , endTimeSeconds)
        difference = abs(finalTime - currentTime)
        readTotalUpdates___ = open("totalUpdates.txt" , 'r')
        readTotalUpdates____ = readTotalUpdates___.read()
        readTotalUpdates___.close()
        return int ( ( ( ( int(difference.total_seconds() ) / 60 ) / (dailyTotalUpdates - int( readTotalUpdates____ ) ) ) * 60 ) - 10 )
        # return the delay between updates in order to complete 200 updates from 07:00 to 23:55
        # Sometimes, due to errors, the application stop, so this delay must update 

    @staticmethod
    def computeTimeSleep(hour__ , minute__ , second__):
        now = datetime.datetime.now()
        currentTime = datetime.datetime(now.year, now.month , now.day , now.hour , now.minute , now.second)
        startTime = datetime.datetime(now.year, now.month , now.day , hour__ , minute__ , second__)
        difference = abs(currentTime - startTime)
        return int(difference.total_seconds() )
        # return the duration that the application must wait (from 23:55 to 06:59:50)
        # 07:00 is the time that the app starts and 23:55 ends and so on






class internet:
    @staticmethod
    def check_internet_connection():
        try:
            socket.create_connection(("1.1.1.1", 53))
            return True
        except OSError:
            pass
        return False
        # check nternet connection

    @staticmethod
    def error_and_back_to_internet():
        internet_instance = internet()
        if( not internet_instance.check_internet_connection() ):
            fileSettings_instance = fileSettings()
            print("Disconnected from the network. Please wait...")
            fileSettings_instance.write_total_errors("totalErrors.txt")
            fileInternetError = open("internet_error_DATE.txt", "w")
            timer_ = timer()
            timer_.time_correction()
            fileInternetError.write( timer_.hour__ + ":" + timer_.min__ + ":" + timer_.sec__ )
            fileInternetError.flush()
            fileInternetError.close()

            while( not internet_instance.check_internet_connection() ):
                time.sleep(1)
                if( internet_instance.check_internet_connection() ):
                    email_instance = _email_()
                    print("Connection restored.")
                    fileSettings_instance.write_delay("delay.txt" , timer_.computeDelay(23 , 55 , 0) )
                    timer_.time_correction()
                    email_instance.send_email("📶🛜 Unstabled connection" , timer_.dateAndtime() + "A network connection problem<br>occured at " + \
                    str( open("internet_error_DATE.txt" , 'r').read() ) + "<br><br>Possible problems:<br>● Ethernet cable disconnection<br>● Bad Wi-Fi connection" + \
                    "<br>Connection restored.<br><br>" + "Made in Python" , ToMe)
                    email_instance.send_email("📶🛜 Unstabled connection" , timer_.dateAndtime() + "A network connection problem<br>occured at " +\
                    str( open("internet_error_DATE.txt" , 'r').read() ) + "<br><br>Possible problems:<br>● Ethernet cable disconnection<br>● Bad Wi-Fi connection" +\
                    "<br>Connection restored.<br><br>" + "Made in Python" , ToOther)
                    print("Sent email due to network disconnection... > " + timer_.hour__ + ":" + timer_.min__ + ":" + timer_.sec__)
                    open("internet_error_DATE.txt").close()
                    break
        # sleep till wifi is set on






class _email_:
    def __init__(self):
        self.SMTP_SERVER = "imap.gmail.com" 
        self.SMTP_PORT = 993

    
    def send_email(self , SUBJECT , message , send_to):
        global FROM_EMAIL , FROM_PWD , PATH_NAME

        FROM = FROM_EMAIL
        TO = send_to
        MESSAGE = MIMEMultipart('alternative')
        MESSAGE['subject'] = SUBJECT
        MESSAGE['To'] = TO
        MESSAGE['From'] = FROM
        HTML_BODY = MIMEText(message, 'html')
        MESSAGE.attach(HTML_BODY)
        server = smtplib.SMTP("smtp.gmail.com:587")    
        password = FROM_PWD
        server.starttls()
        server.login(FROM,password)
        server.sendmail(FROM , TO , MESSAGE.as_string() )
        server.quit()
        # send an email to a specific address (2 people)


    def read_email(self):
        global FROM_EMAIL , FROM_PWD , site_username , site_password , last_upgrade_version
        try:
            timer_instance = timer()
            fileSettings_instance = fileSettings()
            mail = imaplib.IMAP4_SSL(self.SMTP_SERVER)
            mail.login(FROM_EMAIL , FROM_PWD)
            mail.select('inbox')

            data = mail.search(None, 'ALL')
            mail_ids = data[1]
            id_list = mail_ids[0].split()   
            latest_email_id = int(id_list[-1])
            check_last_N_emails = 11
            for e in range(latest_email_id , latest_email_id - check_last_N_emails , -1):
                data = mail.fetch(str(e), '(RFC822)' )
                for response_part in data:
                    arr = response_part[0]
                    if isinstance(arr, tuple):
                        msg = email.message_from_string(str(arr[1],'utf-8'))
                        email_subject = msg['subject'].strip()
                        email_date = msg['Date']

                for part in msg.walk():
                    if(email_subject == "delete" or email_subject == "Delete"):
                        now = datetime.datetime.now()
                        listOfMonths = ["Jan" , "Feb" , "Mar" , "Apr" , "May" , "Jun" , "Jul" , "Aug" , "Sep" , "Oct" , "Nov" , "Dec"]
                        dateOfToday = str(now.day) + " " + listOfMonths[int(now.month) - 1] + " " + str(now.year)
                        date_of_email_update = ''

                        for _string_ in range(5 , 16):
                            date_of_email_update += str(email_date[_string_])
                        
                        date_of_email_update = "".join(date_of_email_update.split())
                        dateOfToday = "".join(dateOfToday.split())
                        
                        if(date_of_email_update == dateOfToday):
                            for part in msg.walk():
                                body = 0
                                try:
                                    # get the email body
                                    body = part.get_payload(decode=True).decode()
                                    body = str( body.strip() )
                                except:
                                    pass
                            
                            pattern = r'<a href="(.*?)">.*?</a>'
                            match = re.search(pattern, body)
                            if(match):
                                body = match.group(1)
                            else:
                                return
                            listOfURLs = []
                            readMe = open("URL_machines.txt" , 'r')
                            for s in range(fileSettings_instance.read_NumberOfMachines("NumberOfMachines.txt") ):
                                readMeValue = readMe.readline().replace("\n" , "")
                                listOfURLs.append( str(readMeValue) )
                            readMe.close()

                            
                            for s in range(fileSettings_instance.read_NumberOfMachines("NumberOfMachines.txt") ):
                                if( body == listOfURLs[s] ):
                                    fileSettings_instance.delete_line("MachinesEachUpdate.txt" , s)
                                    fileSettings_instance.delete_line("URL_machines.txt" , s)
                                    text = body.split('-')[1:]
                                    if('zitiste' in text):
                                        text = text[:text.index('zitiste')]
                                    elif('wwwelectronordgr\n' in text):
                                        text = text[:text.index('wwwelectronordgr\n')]
                                    elif('wwwelectronord' in text):
                                        text = text[:text.index('wwwelectronord')]
                                    elif('electronord') in text:
                                        text = text[:text.index('electronord')]
                                        
                                    name_text = ''
                                    for i in range(len(text)):
                                        name_text += text[i] + ' '
                                    name_text.strip()
                                    display = f'<a href="{body}">{name_text}</a>'
                                    fileSettings_instance.write_imported_removed_machines('removed_machines.txt' , fileSettings_instance.read_imported_removed_machines('removed_machines.txt') + 1)
                                    self.send_email("⤴️ Machine removed" , timer_instance.dateAndtime() + display + " deleted successfully.<br>List of machines updated.<br><br>" + "Made in Python" , ToMe)
                                    self.send_email("⤴️ Machine removed" , timer_instance.dateAndtime() + display + " deleted successfully.<br>List of machines updated.<br><br>" + "Made in Python" , ToOther)
                                    fileSettings_instance.update_machines_number("NumberOfMachines.txt" , fileSettings.read_NumberOfMachines("NumberOfMachines.txt") - 1 )
                                    open("URL_machines.txt").close()
                                    print("====================================================")
                                    print("A machine just removed.")
                                    print("====================================================")
                                    break
                            
                            listOfURLs.clear()


                    if(email_subject == "insert" or email_subject == "Insert"):
                        now = datetime.datetime.now()
                        listOfMonths = ["Jan" , "Feb" , "Mar" , "Apr" , "May" , "Jun" , "Jul" , "Aug" , "Sep" , "Oct" , "Nov" , "Dec"]
                        dateOfToday = str(now.day) + " " + listOfMonths[int(now.month) - 1] + " " + str(now.year)
                        date_of_email_update = ''

                        for _string_ in range(5 , 16):
                            date_of_email_update += str(email_date[_string_])
                        
                        date_of_email_update = "".join(date_of_email_update.split())
                        dateOfToday = "".join(dateOfToday.split())

                        if(date_of_email_update == dateOfToday):
                            for part in msg.walk():
                                body = 0
                                try:
                                    # get the email body
                                    body = part.get_payload(decode=True).decode()
                                    body = str( body.strip() )
                                except:
                                    pass
                            
                            now = datetime.datetime.now()
                            timer_instance.time_correction()
                            pattern = r'<a href="(.*?)">.*?</a>'
                            match = re.search(pattern, body)
                            if(match):
                                body = match.group(1)
                            else:
                                pass
                            
                            if(not body in open("URL_machines.txt" , 'r').read() ):
                                fileSettings_instance.update_machines_number("NumberOfMachines.txt" , fileSettings_instance.read_NumberOfMachines("NumberOfMachines.txt") + 1 )
                                with open("URL_machines.txt", "a") as __file__:
                                    __file__.write(str(body) + "\n")
                                with open("MachinesEachUpdate.txt", "a") as __file:
                                    __file.write(str(0) + "\n")

                                open("URL_machines.txt").close()
                                open("MachinesEachUpdate.txt").close()
                                fileSettings_instance.write_imported_removed_machines('imported_machines.txt' , fileSettings_instance.read_imported_removed_machines('imported_machines.txt') + 1)
                                
                                text = body.split('-')[1:]
                                if('zitiste' in text):
                                    text = text[:text.index('zitiste')]
                                elif('wwwelectronordgr\n' in text):
                                    text = text[:text.index('wwwelectronordgr\n')]
                                elif('wwwelectronord' in text):
                                    text = text[:text.index('wwwelectronord')]
                                elif('electronord') in text:
                                    text = text[:text.index('electronord')]
                                    
                                name_text = ''
                                for i in range(len(text)):
                                    name_text += text[i] + ' '
                                name_text.strip()
                                display = f'<a href="{body}">{name_text}</a>'
                                self.send_email("⤵️ Machine inserted" , timer_instance.dateAndtime() + display + " inserted successfully.<br>List of machines updated.<br><br>" + "Made in Python" , ToMe)
                                self.send_email("⤵️ Machine inserted" , timer_instance.dateAndtime() + display + " inserted successfully.<br>List of machines updated.<br><br>" + "Made in Python" , ToOther)
                                print("====================================================")
                                print("New machine just inserted.")
                                print("====================================================")


                    if(email_subject == "update" or email_subject == "Update"):
                        now = datetime.datetime.now()
                        listOfMonths = ["Jan" , "Feb" , "Mar" , "Apr" , "May" , "Jun" , "Jul" , "Aug" , "Sep" , "Oct" , "Nov" , "Dec"]
                        dateOfToday = str(now.day) + " " + listOfMonths[int(now.month) - 1] + " " + str(now.year)
                        date_of_email_update = ''

                        for _string_ in range(5 , 16):
                            date_of_email_update += str(email_date[_string_])
                        
                        date_of_email_update = "".join(date_of_email_update.split())
                        dateOfToday = "".join(dateOfToday.split())
                        
                        if(date_of_email_update == dateOfToday):
                            body = 0
                            try:
                                # get the email body
                                body = part.get_payload(decode=True).decode()
                                body = int( body.strip() )
                            except:
                                pass
                            
                            if(body == fileSettings_instance.read_GitHubUpdatesNumber("GitHubUpdatesNumber.txt") + 1):
                                timer_instance.time_correction()
                                fileSettings_instance.write_GitHubUpdatesNumber("GitHubUpdatesNumber.txt" , fileSettings_instance.read_GitHubUpdatesNumber("GitHubUpdatesNumber.txt") + 1 ) # increase 'update' number (GitHub upates) by 1
                                print("====================================================")
                                print("The app stopped running for the next 7 minutes.\nA new version will be automatically\ndownloaded from GitHub. Do not interrupt operation.\nTime: " + str(timer_instance.hour__) + ":" + str(timer_instance.min__) + ":" + str(timer_instance.sec__) )
                                self.send_email("🛠️ New release version" , timer_instance.dateAndtime() + "CarClickerBot stopped running for the next 7 minutes. The old version<b> " + last_upgrade_version + "</b> removed<br>and the new one will be automatically<br>downloaded from GitHub.<br>Do not interrupt operation.<br>Number of update version" + \
                                                ": " + str(fileSettings_instance.read_GitHubUpdatesNumber("GitHubUpdatesNumber.txt")) + "<br><br>" + "Made in Python", ToMe)
                                self.send_email("🛠️ New release version" , timer_instance.dateAndtime() + "CarClickerBot stopped running for the next 7 minutes. The old version<b> " + last_upgrade_version + "</b> removed<br>and the new one will be automatically<br>downloaded from GitHub.<br>Do not interrupt operation.<br>Number of update version" + \
                                                ": " + str(fileSettings_instance.read_GitHubUpdatesNumber("GitHubUpdatesNumber.txt")) + "<br><br>" + "Made in Python", ToOther)

                                print("====================================================")
                                time.sleep(7 * 60)  # sleep for 7 minutes
                                print("The new version will be run at a moment...")
                                print("====================================================")
                                os.system("wget 'https://github.com/NikosGkoutzas/CarClickerBot/raw/main/carClickerBot.py' && mv carClickerBot.py.1 carClickerBot.py")
                                driver_instance.quit()   # quit firefox
                                os.execv(sys.executable, ["python3"] + sys.argv) 


                    if(email_subject == "feedback" or email_subject == "Feedback"):
                        now = datetime.datetime.now()
                        
                        listOfMonths = ["Jan" , "Feb" , "Mar" , "Apr" , "May" , "Jun" , "Jul" , "Aug" , "Sep" , "Oct" , "Nov" , "Dec"]
                        dateOfToday = str(now.day) + " " + listOfMonths[int(now.month) - 1] + " " + str(now.year)
                        date_of_email_update = ''

                        for _string_ in range(5 , 16):
                            date_of_email_update += str(email_date[_string_])
                        
                        date_of_email_update = "".join(date_of_email_update.split())
                        dateOfToday = "".join(dateOfToday.split())

                        if(date_of_email_update == dateOfToday):
                            body = 0
                            try:
                                # get the email body
                                body = part.get_payload(decode=True).decode()
                                body = int( body.strip() )
                            except:
                                pass

                            if(body == fileSettings_instance.read_feedbackNumber("read_feedbackNumber.txt") + 1):
                                fileSettings_instance.write_FeedbackNumber("read_feedbackNumber.txt" , fileSettings_instance.read_feedbackNumber("read_feedbackNumber.txt") + 1)
                                print("====================================================")
                                print("Sending email feedback due to request.")
                                print("====================================================")
                                imported_machines = fileSettings_instance.read_imported_removed_machines('imported_machines.txt')
                                removed_machines = fileSettings_instance.read_imported_removed_machines('removed_machines.txt')

                                self.send_email("ℹ️ Check feedback" , timer_instance.dateAndtime() + "Number of machines: " + str(fileSettings_instance.read_NumberOfMachines("NumberOfMachines.txt")) + "<br>Current number of updates: " + str( fileSettings_instance.readTotalUpdates() ) + "<br>Number of errors: " + str( fileSettings_instance.read_total_errors("totalErrors.txt") ) + \
                                "<br>Imported machines: " + str(imported_machines) + "<br>" + "Removed machines: " + str(removed_machines)+ "<br>" + \
                                "New releases: " + str(fileSettings_instance.read_GitHubUpdatesNumber("GitHubUpdatesNumber.txt")) + "<br>" + "Number of app resets: " + str(fileSettings_instance.read_resetNumber("read_resetNumber.txt")) + "<br>" + \
                                "Number of feedbacks: " + str(fileSettings_instance.read_feedbackNumber("read_feedbackNumber.txt")) + \
                                "<br><br>App is currently running normally.<br><br>" + "Made in Python", ToMe)
                                                    
                                self.send_email("ℹ️ Check feedback" , timer_instance.dateAndtime() + "Number of machines: " + str(fileSettings_instance.read_NumberOfMachines("NumberOfMachines.txt")) + "<br>Current number of updates: " + str( fileSettings_instance.readTotalUpdates() ) + "<br>Number of errors: " + str( fileSettings_instance.read_total_errors("totalErrors.txt") ) + \
                                "<br>Imported machines: " + str(imported_machines) + "<br>" + "Removed machines: " + str(removed_machines) + "<br>" + \
                                "New releases: " + str(fileSettings_instance.read_GitHubUpdatesNumber("GitHubUpdatesNumber.txt")) + "<br>" + "Number of app resets: " + str(fileSettings_instance.read_resetNumber("read_resetNumber.txt")) + "<br>" + \
                                "Number of feedbacks: " + str(fileSettings_instance.read_feedbackNumber("read_feedbackNumber.txt")) + \
                                "<br><br>App is currently running normally.<br><br>" + "Made in Python", ToOther)
                                

                    if(email_subject == "reset" or email_subject == "Reset"):
                        now = datetime.datetime.now()
                        
                        listOfMonths = ["Jan" , "Feb" , "Mar" , "Apr" , "May" , "Jun" , "Jul" , "Aug" , "Sep" , "Oct" , "Nov" , "Dec"]
                        dateOfToday = str(now.day) + " " + listOfMonths[int(now.month) - 1] + " " + str(now.year)
                        date_of_email_update = ''

                        for _string_ in range(5 , 16):
                            date_of_email_update += str(email_date[_string_])
                        
                        date_of_email_update = "".join(date_of_email_update.split())
                        dateOfToday = "".join(dateOfToday.split())
                        if(date_of_email_update == dateOfToday):
                            body = 0
                            try:
                                # get the email body
                                body = part.get_payload(decode=True).decode()
                                body = int( body.strip() )
                            except:
                                pass

                            

                            if(body == fileSettings_instance.read_resetNumber("read_resetNumber.txt") + 1):
                                fileSettings_instance.write_resetNumber("read_resetNumber.txt" , fileSettings_instance.read_resetNumber("read_resetNumber.txt") + 1)
                                print("====================================================")
                                print("All files have been reset.\nCarClickerBot restart.")
                                print("====================================================")

                                self.send_email("🔁 App restart" , timer_instance.dateAndtime() + "All files have been reset due to request.<br>The app will automatically launch again.<br><br>" + "Made in Python", ToMe)
                                self.send_email("🔁 App restart" , timer_instance.dateAndtime() + "All files have been reset due to request.<br>The app will automatically launch again.<br><br>" + "Made in Python", ToOther)

                                reset.reset_files(False)

                                driver_instance.quit()   # quit firefox
                                os.execv(sys.executable, ["python3"] + sys.argv)    # run again from the top


                    if(email_subject == 'username' or email_subject == 'Username' or email_subject == 'password' or email_subject == 'Password'):
                        listOfMonths = ["Jan" , "Feb" , "Mar" , "Apr" , "May" , "Jun" , "Jul" , "Aug" , "Sep" , "Oct" , "Nov" , "Dec"]
                        now = datetime.datetime.now()
                        dateOfToday = str(now.day) + " " + listOfMonths[int(now.month) - 1] + " " + str(now.year)
                        date_of_email_update = ''
                        for _string_ in range(5 , 16):
                            date_of_email_update += str(email_date[_string_])
                        
                        date_of_email_update = "".join(date_of_email_update.split())
                        dateOfToday = "".join(dateOfToday.split())

                        if(date_of_email_update == dateOfToday):
                            for part in msg.walk():
                                body = 0
                                try:
                                    # get the email body
                                    body = part.get_payload(decode=True).decode()
                                    body = str( body.strip() )
                                except:
                                    pass

                            pattern = r'<a href="(.*?)">.*?</a>'
                            match = re.search(pattern, body)
                            if(match):
                                body = match.group(1)
                            else:
                                pass

                            if(email_subject == 'username' or email_subject == 'Username'):
                                if(body != site_username):
                                    site_username = body
                                    fileSettings_instance.write_changeUsername_or_password(str(body) , 4)
                                    print("====================================================")
                                    print("Username successfully changed!")
                                    print("====================================================")
                                    self.send_email("⚙ Username changed" , timer_instance.dateAndtime() + "Username changed due to request.<br>The new username will be<br>used for the next login.<br><br>" + "Made in Python", ToMe)
                                    self.send_email("⚙ Username changed" , timer_instance.dateAndtime() + "Username changed due to request.<br>The new username will be<br>used for the next login.<br><br>" + "Made in Python", ToOther)

                            else:
                                if(body != site_password):
                                    site_password = body
                                    fileSettings_instance.write_changeUsername_or_password(str(body) , 5)
                                    print("====================================================")
                                    print("Password successfully changed!")
                                    print("====================================================")
                                    self.send_email("⚙ Password changed" , timer_instance.dateAndtime() + "Password changed due to request.<br>The new Password will be<br>used for the next login.<br><br>" + "Made in Python", ToMe)
                                    self.send_email("⚙ Password changed" , timer_instance.dateAndtime() + "Password changed due to request.<br>The new Password will be<br>used for the next login.<br><br>" + "Made in Python", ToOther)
                        return
                    

                    if(email_subject == 'engine' or email_subject == 'Engine'): # change geckodriver version (FILE)
                        now = datetime.datetime.now()

                        listOfMonths = ["Jan" , "Feb" , "Mar" , "Apr" , "May" , "Jun" , "Jul" , "Aug" , "Sep" , "Oct" , "Nov" , "Dec"]
                        dateOfToday = str(now.day) + " " + listOfMonths[int(now.month) - 1] + " " + str(now.year)
                        date_of_email_update = ''

                        for _string_ in range(5 , 16):
                            date_of_email_update += str(email_date[_string_])
                        
                        date_of_email_update = "".join(date_of_email_update.split())
                        dateOfToday = "".join(dateOfToday.split())
                        if(date_of_email_update == dateOfToday):
                            filename = None
                            
                            if part.get_content_disposition() == 'attachment':
                                # Get the filename of the attachment
                                filename = part.get_filename()
                                version = filename.split('geckodriver-')[1].split(('-linux64'))[0]
                                numberOfVersion = version.split('.')[1].split('.')[0]
                                numberOfPreviousVersion = None
                                for filename__ in os.listdir(PATH_NAME):
                                    if("geckodriver" in filename__):
                                        version__ = filename__.split('geckodriver-')[1].split(('-linux64'))[0]
                                        numberOfPreviousVersion = version__.split('.')[1].split('.')[0]
                                
                                if(filename and numberOfPreviousVersion != None and int(numberOfVersion) > int(numberOfPreviousVersion)):
                                    for filename__ in os.listdir(PATH_NAME):
                                        if("geckodriver" in filename__):
                                            os.remove(filename__)  # Remove the previous version
                                    print("====================================================")
                                    print("New engine will be used in a few minutes.")
                                    print("====================================================")
                                    # Decode the filename (sometimes it's encoded)
                                    filename = decode_header(filename)[0][0]
                                    if isinstance(filename, bytes):
                                        filename = filename.decode()

                                    # Save the file to the current directory
                                    filepath = os.path.join(".", filename)
                                    with open(filepath, "wb") as f:
                                        f.write(part.get_payload(decode=True))

                                    self.send_email("⚙️🛠️ New engine installation" , timer_instance.dateAndtime() + "A new version <b>" + version + "</b> of the Geckodriver web browser engine has been downloaded and is ready for installation.<br>CarClickerBot will run again.<br><br>" + "Made in Python", ToMe)
                                    self.send_email("⚙️🛠️ New engine installation" , timer_instance.dateAndtime() + "A new version <b>" + version + "</b> of the Geckodriver web browser engine has been downloaded and is ready for installation.<br>CarClickerBot will run again.<br><br>" + "Made in Python", ToOther)
                                    os.system('tar -xvzf ' + str(filename))
                                    os.system('sudo mv geckodriver /usr/local/bin')
                                    os.system('export PATH=$PATH:/usr/local/bin/geckodriver')
                                    time.sleep(5)
                                    driver_instance.quit()
                                    os.execv(sys.executable, ["python3"] + sys.argv)    # run again from the top
                                return
                        

        except:
            driver_instance.quit()   # quit firefox
            os.execv(sys.executable, ["python3"] + sys.argv)    # run again from the top





class reset:
    @staticmethod
    def reset_files(allFiles):
        fileSettings_instance = fileSettings()
        initializer_instance = initialize(fileSettings_instance)
        initializer_instance.clear_geckodriver_log()

        file = open("updateNumber.txt", "w")    # open the file
        file.write(str(0))   # write the number in the file
        file.flush() 
        file.close()

        fileTotal = open("totalUpdates.txt", "w")    # open the file
        fileTotal.write(str(0))   # write the number in the file
        fileTotal.flush()
        fileTotal.close()

        fileEach = open("MachinesEachUpdate.txt" , "w")
        for i in range(0 , fileSettings_instance.read_NumberOfMachines("NumberOfMachines.txt")):
            fileEach.write(str(0) + "\n")
        fileEach.close()

        fileSettings_instance.writeNumOfErrors("reached_20_errors.txt" , 0)
        fileSettings_instance.write_delay("delay.txt" , 5)

        errors__ = open("totalErrors.txt" , 'w')
        errors__.write( str(0) )
        errors__.flush()
        errors__.close()

        internet_err_DATE_file = open("internet_error_DATE.txt" , 'w')
        internet_err_DATE_file.write( str(0) )
        internet_err_DATE_file.flush()
        internet_err_DATE_file.close()

        if(allFiles):
            fileGitHub = open("GitHubUpdatesNumber.txt" , 'w')
            fileGitHub.write( str(0) )
            fileGitHub.flush()
            fileGitHub.close()

            fileGitHub = open("read_feedbackNumber.txt" , 'w')
            fileGitHub.write( str(0) )
            fileGitHub.flush()
            fileGitHub.close()
            
            filereset = open("read_resetNumber.txt" , 'w')
            filereset.write( str(0) )
            filereset.flush()
            filereset.close()

            file_removed_machines = open("removed_machines.txt" , 'w')
            file_removed_machines.write( str(0) )
            file_removed_machines.flush()
            file_removed_machines.close()

            file_imported_machines = open("imported_machines.txt" , 'w')
            file_imported_machines.write( str(0) )
            file_imported_machines.flush()
            file_imported_machines.close()




class launch:
    @staticmethod
    def launch_program():
        global initialize_instance , last_upgrade_version
        try:
            fileSettings_instance = fileSettings()
            reset_instance = reset()
            email_instance = _email_()
            internet_instance = internet()
            internet_instance.error_and_back_to_internet()
            print('====================================================')
            print("              CarClickerBot launched!\n====================================================\n" + \
            "                  Made in Python\n" + "                     " + last_upgrade_version + "\n====================================================\n")
            print("Step 1: Checking emails")
            email_instance.read_email()
            link_site = "https://www.car.gr"
            internet_instance.error_and_back_to_internet()
            driver_instance.openUrl(link_site)  
            print("Step 2: Open 'https://www.car.gr' page")      
            cookies = None

            try:
                cookies = driver_instance.findElement(".css-ofc9r3" , '') 
            except:
                cookies = driver_instance.findElement(".css-ofc9r3 > span:nth-child(1)" , 'accept')      # accept cookies

            cookies.click()
            print("Step 3: Accept cookies")
            time.sleep(1)
            internet_instance.error_and_back_to_internet()
            driver_instance.openUrl("https://www.car.gr/login/")
            print("Step 4: Go to login page")
            internet_instance.error_and_back_to_internet()
            username_input = None
            password_input = None
            log_in_button = None
            try:
                username_input = driver_instance.findElement("#ui-id-2 > div:nth-child(2) > div:nth-child(2) > input:nth-child(1)" , '')     # give username
                username_input.send_keys(site_username)
            except:
                username_input = driver_instance.findElement("#input-username" , 'username')     # give username
                username_input.send_keys(site_username)
                
            print("Step 5: Enter username")
            internet_instance.error_and_back_to_internet()
            try:
                password_input = driver_instance.findElement("#ui-id-2 > div:2nth-child(3) > div:nth-child(2) > input:nth-child(1)" , '')     # give password
                password_input.send_keys(site_password)
            except:
                password_input = driver_instance.findElement("#current-password" , 'password')     # give password
                password_input.send_keys(site_password)

            print("Step 6: Enter password")
            time.sleep(1)
            internet_instance.error_and_back_to_internet()
            try:
                log_in_button = driver_instance.findElement(".submit-btn > span:nth-child(1)" , '')   # press login button
            except:
                log_in_button = driver_instance.findElement(".submit-btn" , 'login')   # press login button
            internet_instance.error_and_back_to_internet()
            
            log_in_button.click()
            print("Step 7: Press login button")
            time.sleep(5)
            current_time = datetime.datetime.now().time()   # get current time
            if(not current_time < initialize_instance.on_time and not current_time >= initialize_instance.off_time):
                print("\nUpdates will start soon...\n====================================================") 
            else:
                print("\nUpdates will start at 07:00:00 in the morning.\n====================================================\n") 
            time.sleep(1)  
            internet_instance.error_and_back_to_internet()

            with open("MachinesEachUpdate.txt") as fileEach:
                for i in range(0 , fileSettings_instance.read_NumberOfMachines("NumberOfMachines.txt") ):
                    initialize_instance.machinesEachUpdate[i] = int(fileEach.readline())
                    line = linecache.getline("MachinesEachUpdate.txt" , i+1)
            line = linecache.getline("MachinesEachUpdate.txt" , 0)

            with open("totalUpdates.txt") as fileTotal:
                totalUpdates = int(fileTotal.read())
                fileTotal.close()
            open("MachinesEachUpdate.txt").close()


            # main loop
            while(True):    
                current_time = datetime.datetime.now().time()   # get current time
                if(not current_time < initialize_instance.on_time and not current_time >= initialize_instance.off_time):
                    
                    if( fileSettings_instance.readTotalUpdates() < dailyTotalUpdates ):
                        email_instance.read_email()
                        timer_instance = timer()
                        fileSettings_instance.write_delay("delay.txt" , timer_instance.computeDelay(23 , 55 , 0) )

                        with open("updateNumber.txt") as file:
                            currentPosUpdate = int(file.read())  # read the number from file
                            driver_instance.openUrl( fileSettings_instance.read_machines_urls("URL_machines.txt" , currentPosUpdate + 1) )
                        open("updateNumber.txt").close()

                        internet_instance.error_and_back_to_internet()
                        updateMachine = None
                        
                        for loops in range(5):
                            try:
                                updateMachine = driver_instance.findElement("div.c-list-group-item:nth-child(1) > div:nth-child(1)" , '')     # find the update button
                                updateMachine.click()       # press the "update" button
                                break
                            except:
                                try:
                                    updateMachine = driver_instance.findElement("div.list-group-item:nth-child(1)" , '')     # find the update button
                                    updateMachine.click()       # press the "update" button
                                    break
                                except:
                                    time.sleep(3)
                                    if(loops == 4): # go to the next machine
                                        loops = 0   # and go at the beginning
                                        if(currentPosUpdate == fileSettings_instance.read_NumberOfMachines("NumberOfMachines.txt")):  # if update of all machines finished
                                            currentPosUpdate = 0                    # start again
                                            file = open("updateNumber.txt", "w")    # open the file
                                            file.write(str(currentPosUpdate))       # write the number in the file
                                            file.flush() 
                                            file.close()
                                        else:
                                            currentPosUpdate += 1       # increase current position of machine update
                                            with open("updateNumber.txt" , 'w') as file:
                                                file.write(str(currentPosUpdate))   # write the number in the file
                                                file.flush()    
                                                file.close()
                                        with open("updateNumber.txt") as file:
                                            currentPosUpdate = int(file.read()) # read the number from file
                                            driver_instance.openUrl( fileSettings_instance.read_machines_urls("URL_machines.txt" , currentPosUpdate + 1) )
                                        open("updateNumber.txt").close()
                        internet_instance.error_and_back_to_internet()
                        
                        
                        
                        initialize_instance.machinesEachUpdate[currentPosUpdate] += 1
                        with open("updateNumber.txt" , 'r') as file:
                            fileSettings_instance.replace_line("MachinesEachUpdate.txt" , int( file.read() ) , initialize_instance.machinesEachUpdate)
                        open("updateNumber.txt").close()
                        
                        totalUpdates += 1
                        with open("totalUpdates.txt" , 'w') as fileTotal:
                            fileTotal.write(str(totalUpdates))   # write the number in the file
                            fileTotal.flush() 
                            fileTotal.close()
                        
                        with open("totalUpdates.txt" , 'r') as fileTotal_R:
                            timer_instance = timer()
                            timer_instance.time_correction()
                            if( int(fileTotal_R.read()) == 1):
                                actions = 'Insert a new machine or delete an existing<br>one, update to the latest version of app,<br>receive a feedback, reset the app, change<br>the username/password or set a new<br>geckodriver web browser engine.<br>Do all these stuff by sending an email.<br><br>'
                                email_instance.send_email("✅ Launch" , timer_instance.dateAndtime() + "<b>About</b>:<br>Developer/Programmer: Nikos Gkoutzas<br>Email: nickgkoutzas@gmail.com<br>App creation date: Feb 2022<br>App version: " + last_upgrade_version + "<br>Number of machines: " + \
                                                    str(fileSettings_instance.read_NumberOfMachines("NumberOfMachines.txt")) + \
                                                    "<br><br><b>Actions</b>:<br>" + actions + "● &nbsp;Send an email to " + str(FROM_EMAIL) + "<br>" + "&nbsp;" * 4 + "     with subject: 'Insert'" + "<br>" + "&nbsp;" * 4 + \
                                                    "     and message: The link-machine" + "<br>" + "&nbsp;" * 4 + " you want to add.<br><br> \
                                                    ● &nbsp;Send an email to " + str(FROM_EMAIL) + "<br>" + "&nbsp;" * 4 + "     with subject: 'Delete'" + "<br>" + "&nbsp;" * 4 + \
                                                    "     and message: The link-machine" + "<br>" + "&nbsp;" * 4 + " you want to delete.<br><br>" \
                                                    "● &nbsp;Send an email to " + str(FROM_EMAIL) + "<br>" + "&nbsp;" * 4 + "     with subject: 'Update'" + "<br>" + "&nbsp;" * 4 + \
                                                    "     and message: The current number<br>" + "&nbsp;" * 5 +  "of changes made in GitHub today.<br><br>" \
                                                    "● &nbsp;Send an email to " + str(FROM_EMAIL) + "<br>" + "&nbsp;" * 4 + "     with subject: 'Feedback'" + "<br>" + "&nbsp;" * 4 + \
                                                    "     and message: The current number<br>" + "&nbsp;" * 5 + "of feedback request.<br><br>" \
                                                    "● &nbsp;Send an email to " + str(FROM_EMAIL) + "<br>" + "&nbsp;" * 4 + "     with subject: 'Reset'" + "<br>" + "&nbsp;" * 4 + \
                                                    "     and message: The current number<br>" + "&nbsp;" * 5 + "of reset request.<br><br>" \
                                                    "● &nbsp;Send an email to " + str(FROM_EMAIL) + "<br>" + "&nbsp;" * 4 + "     with subject: 'Username'" + "<br>" + "&nbsp;" * 4 + \
                                                    "     and message: The new username.<br><br>" \
                                                    "● &nbsp;Send an email to " + str(FROM_EMAIL) + "<br>" + "&nbsp;" * 4 + "     with subject: 'Password'" + "<br>" + "&nbsp;" * 4 + \
                                                    "     and message: The new password.<br><br>" \
                                                    "● &nbsp;Send an email to " + str(FROM_EMAIL) + "<br>" + "&nbsp;" * 4 + "     with subject: 'Engine'" + "<br>" + "&nbsp;" * 4 + \
                                                    "     and message: Import the file.<br><br>" \
                                                "A notification will be sent.<br><br>" + "Made in Python" , ToMe)
                                
                                email_instance.send_email("✅ Launch" , timer_instance.dateAndtime() + "<b>About</b>:<br>Developer/Programmer: Nikos Gkoutzas<br>Email: nickgkoutzas@gmail.com<br>App creation date: Feb 2022<br>App version: " + last_upgrade_version + "<br>Number of machines: " + \
                                                    str(fileSettings_instance.read_NumberOfMachines("NumberOfMachines.txt")) + \
                                                    "<br><br><b>Actions</b>:<br>" + actions + "● &nbsp;Send an email to " + str(FROM_EMAIL) + "<br>" + "&nbsp;" * 4 + "     with subject: 'Insert'" + "<br>" + "&nbsp;" * 4 + \
                                                    "     and message: The link-machine" + "<br>" + "&nbsp;" * 4 + " you want to add.<br><br> \
                                                    ● &nbsp;Send an email to " + str(FROM_EMAIL) + "<br>" + "&nbsp;" * 4 + "     with subject: 'Delete'" + "<br>" + "&nbsp;" * 4 + \
                                                    "     and message: The link-machine" + "<br>" + "&nbsp;" * 4 + " you want to delete.<br><br>" \
                                                    "● &nbsp;Send an email to " + str(FROM_EMAIL) + "<br>" + "&nbsp;" * 4 + "     with subject: 'Update'" + "<br>" + "&nbsp;" * 4 + \
                                                    "     and message: The current number<br>" + "&nbsp;" * 5 +  "of changes made in GitHub today.<br><br>" \
                                                    "● &nbsp;Send an email to " + str(FROM_EMAIL) + "<br>" + "&nbsp;" * 4 + "     with subject: 'Feedback'" + "<br>" + "&nbsp;" * 4 + \
                                                    "     and message: The current number<br>" + "&nbsp;" * 5 + "of feedback request.<br><br>" \
                                                    "● &nbsp;Send an email to " + str(FROM_EMAIL) + "<br>" + "&nbsp;" * 4 + "     with subject: 'Reset'" + "<br>" + "&nbsp;" * 4 + \
                                                    "     and message: The current number<br>" + "&nbsp;" * 5 + "of reset request.<br><br>" \
                                                    "● &nbsp;Send an email to " + str(FROM_EMAIL) + "<br>" + "&nbsp;" * 4 + "     with subject: 'Username'" + "<br>" + "&nbsp;" * 4 + \
                                                    "     and message: The new username.<br><br>" \
                                                    "● &nbsp;Send an email to " + str(FROM_EMAIL) + "<br>" + "&nbsp;" * 4 + "     with subject: 'Password'" + "<br>" + "&nbsp;" * 4 + \
                                                    "     and message: The new password.<br><br>" \
                                                    "● &nbsp;Send an email to " + str(FROM_EMAIL) + "<br>" + "&nbsp;" * 4 + "     with subject: 'Engine'" + "<br>" + "&nbsp;" * 4 + \
                                                    "     and message: Import the file.<br><br>" \
                                                "A notification will be sent.<br><br>" + "Made in Python" , ToOther)
                                print("Updates started at " + timer_instance.dateAndtime() + '\b'*8 + ". Emails sent.")
                                fileTotal_R.close()

                            timer_instance.time_correction()
                            print("Total updates until now, (" + str(timer_instance.hour__) + ":" + str(timer_instance.min__) + ":" + str(timer_instance.sec__) + "): " , end = "" , flush = True)
                            if( int (open("totalUpdates.txt").read() ) <= 9):
                                print("0" + open("totalUpdates.txt").read())
                            else:
                                print(open("totalUpdates.txt").read())
                            open("totalUpdates.txt").close()
                        
                        currentPosUpdate += 1       # increase current position of machine update
                        with open("updateNumber.txt" , 'w') as file:
                            file.write(str(currentPosUpdate))   # write the number in the file
                            file.flush()    
                            file.close()

                    if(currentPosUpdate == fileSettings_instance.read_NumberOfMachines("NumberOfMachines.txt")):  # if update of all machines finished
                        currentPosUpdate = 0                    # start again
                        file = open("updateNumber.txt", "w")    # open the file
                        file.write(str(currentPosUpdate))       # write the number in the file
                        file.flush() 
                        file.close()
                    
                    
                    if(fileSettings_instance.readTotalUpdates() == dailyTotalUpdates ):
                        print("====================================================")
                        print( str(dailyTotalUpdates) + " updates have been performed before 23:55:00.\nSleeping till 23:55:00 ...")
                        print("====================================================")
                        timer_instance = timer()
                        sleep__ = timer_instance.computeTimeSleep(23 , 55 , 0)
                        time.sleep(sleep__)
                    

                    elif (fileSettings_instance.readTotalUpdates() < dailyTotalUpdates ):
                        for i in range( 1 , int( open("delay.txt").read() ) ):   # sleeping... & checking for network disconnection      
                            time.sleep(1)
                            internet_instance.error_and_back_to_internet()
                        open("delay.txt").close()
                    

                elif(current_time > initialize_instance.off_time):
                    print("====================================================")
                    print('Last step: Extracting statistical results')
                    with open("totalUpdates.txt") as fileTotal , open("MachinesEachUpdate.txt") as fileEach , open('URL_machines.txt') as machines:
                        machine_display = []
                        for line in machines.readlines():
                            text = line.split('-')[1:]
                            if('zitiste' in text):
                                text = text[:text.index('zitiste')]
                            elif('wwwelectronordgr\n' in text):
                                text = text[:text.index('wwwelectronordgr\n')]
                            elif('wwwelectronord' in text):
                                text = text[:text.index('wwwelectronord')]
                            elif('electronord') in text:
                                text = text[:text.index('electronord')]
                                
                            name_text = ''
                            for i in range(len(text)):
                                name_text += text[i] + ' '
                            
                            name_text.strip()
                            cut_off = 25
                            if(len(name_text) <= cut_off):
                                machine_display.append(f'<a href="{line}">{name_text}</a>')
                            else:
                                if(len(name_text[cut_off:]) > cut_off):
                                    temp_1 = name_text[cut_off:]
                                    temp_2 = temp_1[:cut_off].strip()
                                    temp_3 = temp_1[cut_off:].strip()
                                    temp = name_text[:cut_off].strip() + '<br>' + "&nbsp;" * len('0 updates for') + "&nbsp;" * 7 + temp_2 + '<br>' + "&nbsp;" * len('0 updates for') + "&nbsp;" * 7 + temp_3
                                else:
                                    temp = name_text[:cut_off].strip() + '<br>' + "&nbsp;" * len('0 updates for') + "&nbsp;" * 7 + name_text[cut_off:].strip()
                                machine_display.append(f'<a href="{line}">{temp}</a>')
                        
                        all_machines_updates_number = ''
                        k = 0
                        for line in fileEach.readlines():
                            all_machines_updates_number += str(line) + " updates for" + "&nbsp;" + machine_display[k] + "<br>"
                            k += 1
                        successful_updates_of_day = str(fileTotal.read().strip())
                        analytics_link = "https://www.car.gr/analytics/overview?date-from=1644962400&date-to=1644993347&fbclid=IwAR0PP4jRq9XOQROeGJIRON7gSMOO4RPUDBAEiJXrPPhg44pTBiZNRsS6vz4"
                        analytics_name_display = 'analytics'
                        analytics = f'<a href="{analytics_link}">{analytics_name_display}</a>'
                        s = 's' if int(fileSettings_instance.read_total_errors("totalErrors.txt")) != 1 else ''
                        email_instance.send_email("📊 Statistical results" , timer_instance.dateAndtime() + "Check out " + analytics + "<br><br>" + successful_updates_of_day + "/" + str(dailyTotalUpdates) + " successful updates for " + \
                        str(fileSettings.read_NumberOfMachines("NumberOfMachines.txt")) + "<br>machines in total with " + str(fileSettings_instance.read_total_errors("totalErrors.txt")) + " error" + s + ".<br><br>" + all_machines_updates_number + " <br><br>" + "Made in Python" , ToMe)
                        email_instance.send_email("📊 Statistical results" , timer_instance.dateAndtime() + "Check out " + analytics + "<br><br>" + successful_updates_of_day + "/" + str(dailyTotalUpdates) + " successful updates for " + \
                        str(fileSettings.read_NumberOfMachines("NumberOfMachines.txt")) + "<br>machines in total with " + str(fileSettings_instance.read_total_errors("totalErrors.txt")) + " error" + s + ".<br><br>" + all_machines_updates_number + "<br><br>" + "Made in Python" , ToOther)
                        print("Emails just sent...\n" + successful_updates_of_day + "/200 updates were performed successfully.")
                        print("====================================================")
                        fileTotal.close()
                        fileEach.close()

                        # reset all files for the new day    
                        reset_instance.reset_files(True)

                        # executes only once per day...
                        print("Waiting till 06:59:50 pm ...")
                        time.sleep(10*60)
                        timer_instance = timer()
                        timer_instance.time_correction()
                        time.sleep( timer_instance.computeTimeSleep(6 , 59 , 50) )  # sleep till tomorrow morning at 7pm                
                        
                        driver_instance.quit()   # quit firefox
                        os.execv(sys.executable, ["python3"] + sys.argv)    # run again from the top
                        


        except:
            print("====================================================\\nAn error occured. Trying again...\n====================================================\\n")
            initialize_instance = initialize(fileSettings_instance)
            timer_instance = timer()
            email_instance = _email_()
            email_instance.send_email("🚨 Unknown error" , timer_instance.dateAndtime() + "App stopped running due to an unknown exception. Trying to restart app.<br>You may need to manually fix the problem if this remains.<br><br>" + "Made in Python" , ToMe)
            email_instance.send_email("🚨 Unknown error" , timer_instance.dateAndtime() + "App stopped running due to an unknown exception. Trying to restart app.<br>You may need to manually fix the problem if this remains.<br><br>" + "Made in Python" , ToOther)
            current_time = datetime.datetime.now().time()   # get current time
            if(not current_time < initialize_instance.on_time and not current_time >= initialize_instance.off_time):
                email_instance.read_email()

            # close all files...
            open("delay.txt").close()
            open("internet_error_DATE.txt").close()
            open("read_feedbackNumber.txt").close()
            open("reached_20_errors.txt").close()
            open("MachinesEachUpdate.txt").close()
            open("NumberOfMachines.txt").close()
            open("totalErrors.txt").close()
            open("totalUpdates.txt").close()
            open("updateNumber.txt").close()
            open("URL_machines.txt").close()
            open("GitHubUpdatesNumber.txt").close()
            open("passwords.txt").close()

            fileSettings_instance = fileSettings()
            fileSettings_instance.writeNumOfErrors("reached_20_errors.txt" , 0)
            fileSettings_instance.write_total_errors("totalErrors.txt")
            fileSettings_instance.writeNumOfErrors("reached_20_errors.txt" , fileSettings_instance.read_total_errors("reached_20_errors.txt") + 1)
            
            driver_instance.quit()   # quit firefox
            os.execv(sys.executable, ["python3"] + sys.argv)    # run again from the top
        






        
if(__name__ == '__main__'):
    driver_instance = driver()
    fileSettings_instance = fileSettings()
    initialize_instance = initialize(fileSettings_instance)
    launcher = launch()
    launcher.launch_program()