# Advanced-Railway-Reservation-System

Advanced Railway Reservation System

It gives an added advantage to the pregnant women and senior citizen to get Lower Berth (if avalaible) and to automate the process of Ticket Checking to some extent at a minimal cost.

Process:
- Once a Person Books a ticket, he/she will be given an unique token which depicts his/her seat confirmation. (Note: Berth/Seat number will NOT be given currently).
- Then,a day before the of departure of that particular train, Our Algorithm will allocate seats to the passengers and the waiting list will be Generated.
- Tatkal Procedures will remain the same.
- Further we have planned to automate the ticket checking process to some extent at a minimal cost.

Algorithm:
1) List of Passengers with their details like Name, Age, Sex, Berth Preference etc will be extracted from the database.
2) The passenger list will be sorted  with respect to date and time.
3) Passengers have been  divided into 3 categories : 
- Pregnant Women
- Senior Citizen (Male and Female)
- Rest
4)First the seats will be allocated to the pregnant women ,then the Senior Citizen (Female) ,followed by the Senior Citizen (Male) and then the rest of the passengers as per their berth preference (if given) if avalaible.
5) A new list will be generated which depicts the final seat alocation list and the Waiting List.

Automate Ticket Checking: With our algorithm we have planned a cost effective way to automate the the ticket checking process to some extent.
- Every coach of the train will have a device set up with a Touchscreen.
- A unique identification code will be sent to every passenger's registered mobile number few minutes before the arrival of the train.
- Passenger needs to enter the code to the device along with his aadhar/PAN number which will be verified for the confirmation of the berth(s).
- If due to some reasons he/she is not able to recieve the code then that passenger needs to go through the manual ticket checking process.

This helps Passengers to confirm the berth without getting disturbed during the journey.
