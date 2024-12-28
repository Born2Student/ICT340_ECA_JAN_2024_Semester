# ICT340 - Application Analysis and Design

# ICT340 End-of-Course Assessment (ECA01) - January Semester 2024

**Question 1**
Read the system requirements of PickMeNow in the Appendix and submit answers to
the following:

**Question 1a** 

**Question 1(a)(i) (5 marks)**

Identify the Actors in the system.

**ANS:**

Primary Actors:
Drivers, Customers, Administrator, Premium Customers (Inherited From Customers)

Supporting Actors:
Bank System


**Question 1(a)(ii) (13 marks)**

Formulate a use case diagram to depict the PickMeNow system design.

Your use case diagram should show the actors, the use cases and their relationships.

**ANS**

<img width="417" alt="image" src="https://github.com/user-attachments/assets/e363c650-ff82-4856-aa73-5e1cc17707cd" />


**Question 1(b) (4 marks)**

The following is an extract of the requirements of the PickMeNow system:

"PickMeNow is a unique taxi-booking experience that allows
customers to access drivers. Customers can just select a destination
and then wait for his taxi to arrive. Payment is also easy with a
choice of cash or credit card. If the customer changes his mind, he
can always cancel without any penalty."

Analyse the above requirements to identify and explain any TWO (2) ambiguous, incorrect, incomplete or inconsistent inadequacies of the system design.

Note that in your answers, you are not supposed to use imagination to add anything not mentioned in the requirements. 

Further, do not include general commentaries in your answer.

**ANS**

The system design is inconsistent and ambiguous.

1. Inconsistent Cancellation Policy:
It is inconsistent because the requirements excerpt mentions that customers can always cancel without any penalty which contradicts the information in the appendix which stated that customers would be penalized with a $4 surcharge fee for cancelling after 5 minutes of car bookings.

2. Ambiguous Vehicle Selection:
It is ambiguous because the requirements excerpt mentions that customers can choose a destination and wait for a taxi to arrive which is ambiguous because the information in the appendix stated that PickMeNow offers customers 3 different types of vehicles for their ride which are cars, vans and excursion buses. Meanwhile, the requirements excerpt does not clarify if taxi referred to all vehicle types or 1 of the 3 vehicle types that customers can choose from. 


**Question 2**
Develop a structural model for the food ordering system design, by submitting your answers to the following:

**Question 2a (15 marks)**
Complete the class description by identifying classes, their attributes and any hierarchical relationship(s) that would be required for the application.

**ANS:**

<img width="826" alt="Screenshot 2024-12-28 at 5 01 32 PM" src="https://github.com/user-attachments/assets/12fb5a1c-fba0-482a-9a07-090b29f9e438" />
<img width="826" alt="Screenshot 2024-12-28 at 5 01 45 PM" src="https://github.com/user-attachments/assets/8822e883-701b-42f7-af32-1638dba2798a" />
<img width="826" alt="Screenshot 2024-12-28 at 5 02 00 PM" src="https://github.com/user-attachments/assets/258ea971-755c-4b71-a46d-bcfce0daabd2" />
<img width="826" alt="Screenshot 2024-12-28 at 5 02 11 PM" src="https://github.com/user-attachments/assets/e1a06f9b-1c26-47a2-8372-788a3f117af8" />

**Question 2b (15 marks)**

Appraise the associations among the classes and hierarchical relationship(s) that would
be required for the application. Construct the class association diagram in UML as your
answer. Ensure that you do not include any derived or redundant association in your
diagram.


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

