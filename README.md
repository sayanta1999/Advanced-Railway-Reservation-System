# Advanced-Railway-Reservation-System

Advanced Railway Reservation System

It gives an added advantage to the pregnant women and senior citizen to get Lower Berth (if avalaible) and to automate the process of Ticket Checking to some extent with minimal cost.

Process:
- Once a Person Books a ticket, he/she will be given an unique token which depicts his/her seat confirmation. (Note: Berth/Seat number will NOT be given currently).
- Then, before 1 Day of departure of that particular train, Our Algorithm will allocate seats to the passengers and waiting list will be Generated.
- Tatkal will remain same, No change in it.
- Further we have Planned to automate the ticket checking process to some extent with minimal cost.

Algorithm:
1) List of Passengers with their details like Name, Age, Sex, Berth Preference etc will be extracted from the database.
2) Sort the the passengers with respect to date and time.
3) Passengers are divided into 3 categories : 
- Pregnant Women
- Senior Citizen (Male and Female)
- Rest
4) Then First allocate Seats to pregnant women, Senior Citizen (Female), Senior Citizen (Male) and then Rest as per their berth preference (if given) if avalaible.
5) A new list will be generated which depicts final seat alocation and Waiting List.

Automate Ticket Checking: For this We have planned a minimal cost way to automate the the ticket checking process to some extent.
- Every coach of the train will have a device set up with a screen.
- A unique identification code will be sent to every passenger's registered mobile number few minutes before the arrival of the train.
- Passenger needs to enter the code to the device for the confirmation of the berth(s).
- If due to some reasons he/she is not able to recieve the code then that passenger needs to go through the manual ticket checking process.

This helps Passengers to confirm the berth without getting disturbed in the midway.
