![image](https://github.com/user-attachments/assets/a321beb7-c4fd-400b-b266-5d981e6ed5df)# ICT340 - Application Analysis and Design

# ICT340 End-of-Course Assessment (ECA01) - January Semester 2024

**Question 1**
Read the system requirements of PickMeNow in the Appendix and submit answers to
the following:

**Question 1a (5 marks)** 

Identify the Actors in the system.

Primary Actors:
Drivers, Customers, Administrator, Premium Customers (Inherited From Customers)

Supporting Actors:
Bank System



**Appendix:**

PickMeNow is a new taxi company which has started its operations recently. In order
to meet the transportation needs of their customers, PickMeNow has decided to invest
in an IT solution to connect their customers and support their drivers. Some key features
and business requirements of PickMeNow are described below.

Drivers and customers are required to register with PickMeNow by providing: a name,
contact number and an email address. PickMeNow assigns an identification number to
each registered driver and customer. In addition, each driver is required to provide the
details of his bank account (account number and bank name) and vehicle details as
described in the next paragraph. Drivers can choose to transfer any amount in his
PickMeNow account to his bank account.

Customers need to key in their pick-up and drop-off locations to obtain an estimated
fare before booking. If the customer accepts, a driver who wishes to provide the ride
would accept the booking. The driver’s location and arrival time will be then be
displayed in real time to the customer.

PickMeNow allows customers to choose from three types of vehicle: cars, vans and
excursion buses. For each vehicle, it is required to capture the licence plate number,
brand and model. When a customer books a car, he can choose to cancel. If he or she
cancels after 5 minutes of booking, a $4 surcharge will apply. When a customer books
an excursion bus or a van, he or she has to make an upfront deposit amount. The deposit
will be returned to the customer if the booking is not cancelled by the customer. For
vans, there is a booking fee on top of the trip fare. Although a customer can cancel a
booking for an excursion bus or a van, the deposit is forfeited if the cancellation is
received 3 days before the date of the ride.

The data to be kept for each ride include: reference number, driver and customer details
(identification number and name), fare, pick-up point, destination, distance, date, start
time and end time of the ride. At the end of each ride an e-receipt is created and sent
to the customer’s email address. At the same time, the driver’s account will be credited
with the amount of the fare minus any fee due to PickMeNow.

A ride can go through the following states during its lifecycle: Ride Requested, Driver
Assigned, Customer Cancelled, Driver Cancelled, Customer Waiting, Driver Arrived,
Ride Started, Payment Done, Ride Done, Rated.

After completing a ride, customers can accumulate points. After completing rides
worth a total of $500, the customer will become a Premium customer. Only Premium
customers can redeem their points to pay their bill in full. Points may be used to offset
a customer’s bill and if there are insufficient points, the rest of the bill must be paid
using a credit card.

After each ride, drivers and customers can rate each other from 1 to 5 stars based on
their ride experience. Customers can also give compliments or complaints about the
drivers by writing a short review. An administrator of the system reviews the ratings
and feedback and records the follow-up action taken.

