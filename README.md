<h1><b>Application Description for Automated Ad<br>Management on www.car.gr</b></h1>

This application, written in Python, automates the management of ads on www.car.gr, ensuring that ads are regularly refreshed to appear higher in user searches. The application runs daily from 9:00 AM to 11:55 PM, performing a total of 20 refreshes at regular intervals.

Application Features:

1.	Automatic ad refresh:
   The application automatically clicks on ads on www.car.gr to refresh them. The 200 refreshes are distributed evenly throughout the day.
2.	Automatic cookie acceptance and account login:
   Upon startup, the application automatically accepts the cookies on www.car.gr and then logs in using the stored username and password.
3.	Remote management via email:
   You can execute various functions via email, such as:
  
      •	Add or remove ads.

      •	Remotely reset the application.

      •	Change username and password for logging into www.car.gr.
	  
      •	Upgrade the application to a new version.
	  
      •	Upgrade the Geckodriver, the web browser engine the application uses to implement actions in Firefox.

4.	Email notifications and statistics:
	    
      •	Every morning at 9:00 AM, you receive an email notification confirming the application’s startup, ensuring that the process began smoothly.
	
      •	After the application finishes at 11:55 PM, you receive an email with statistics about the ad refreshes.
	
      •	Throughout the day, the application sends email notifications for various processes, such as ad addition/removal, reset, or application upgrade.
	
      •	If an error occurs (e.g., failure to accept cookies, unsuccessful login, or a button press failure), the application immediately sends an email notification and terminates, requiring manual intervention to resolve the issue and restart the program.
	
      •	If there’s an internet connection failure, the application notifies you as soon as the connection is restored, ensuring that the refresh process resumes as normal.

5.	Data security and recovery in case of power failure:
   All application data is logged and stored in files, so in case of a power outage on the server, no information is lost. Once the system is restored, the application can resume from where it left off.
6.	Automatic restart:
   After the daily process ends at 11:55 PM, the application enters a standby mode until 7:00 AM the following day, when it restarts and continues refreshing the ads.

Requirements and Key Technologies:
 
  •	Programming language: The application is written in Python.
 
  •	Email management: All functions of the application are managed remotely via email.
	
  •	Automated clicks for ad refreshes: Targeted ad refreshing to increase visibility.
	
  •	Data storage: All data is securely saved to ensure recovery in case of system failures.

This application provides a comprehensive solution for the automated management of ads on www.car.gr, offering flexible control, real-time monitoring, and secure data handling.
