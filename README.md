Application for Automated Listing Management on car.gr

This Python-based application automates the management of listings on car.gr, ensuring that specific listings are regularly refreshed to appear higher in user searches. The application operates daily from 7:00 a.m. to 11:55 p.m., performing a total of 200 refreshes distributed evenly throughout the day.
Application Features:

1.	Automated Listing Refresh:
The application automatically clicks on listings on car.gr to refresh them. The 200 refreshes are evenly distributed during the day to maximize the visibility of each listing.

2.	Remote Management via Email:
    The application can be managed remotely by sending emails to a specified address. The following actions can be performed via email:
	•	Add or delete listings.
	•	Remotely reset the application.
	•	Change the username and password used to log in to car.gr.
	•	Upgrade the application to a newer version.

3.	Email Notifications and Reporting:
	•	Every day at 7:00 a.m., you receive an email notification confirming the application has started, ensuring that the process begins smoothly.
	•	After the application completes its cycle at 11:55 p.m., you receive an email containing detailed statistics about the refreshed listings.
	•	During the day, the application sends real-time email notifications for important actions, such as listing additions/deletions, resets, or upgrades.
	•	In the event of an internet outage, the application sends an email notification once the connection is restored, ensuring the refresh process resumes without issues.

4.	Data Security and Recovery in Case of Power Failure:
    All application data is logged and saved to files, ensuring that no information is lost in the event of a power failure on the server. Once the server is back online, the application can continue its operations from where it left off.

5.	Automatic Restart:
    After the end of the day’s operations at 11:55 p.m., the application enters standby mode until 7:00 a.m. the next day, when it automatically restarts to begin the refresh process again.

Requirements and Key Technologies:
Programming Language: The application is written in Python.
Email-Based Management: All operations can be controlled remotely by sending commands via email.
Automated Click Refresh: Targeted clicks on listings to boost visibility in user searches.
Data Persistence: The data is securely stored in files to ensure recovery after unexpected shutdowns.

This application provides a comprehensive solution for automated listing management on car.gr, offering flexible remote control, real-time monitoring, and secure data handling to ensure continuous operations and maximized listing visibility.