# ICT340 - Application Analysis and Design

# ICT340 End-of-Course Assessment (ECA01) - January Semester 2024

### Question 1
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

3. Ambiguous Vehicle Selection:

It is ambiguous because the requirements excerpt mentions that customers can choose a destination and wait for a taxi to arrive which is ambiguous because the information in the appendix stated that PickMeNow offers customers 3 different types of vehicles for their ride which are cars, vans and excursion buses. Meanwhile, the requirements excerpt does not clarify if taxi referred to all vehicle types or 1 of the 3 vehicle types that customers can choose from. 


### Question 2

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

**ANS:**

<img width="510" alt="image" src="https://github.com/user-attachments/assets/b535fc5f-b322-498c-a3d3-ba483a9c3c89" />


### Question 3

Analysis on the requirements for the driver give rise to an updated class diagram which allows a driver to accept a ride and update the ride status to "Driver Assigned", part of which is shown in Figure Q3 below.

Note that this may not be applicable to Question 2 above.

<img width="700" alt="Screenshot 2024-12-28 at 5 07 08 PM" src="https://github.com/user-attachments/assets/8f5868a3-327d-4c4b-838a-9f4bf4c184e7" />

**Question 3a (8 marks)**

Develop the dynamic model for the application function, by drawing the sequence diagram for the walkthrough to accept a ride so that a driver is assigned.

**ANS:**

<img width="490" alt="image" src="https://github.com/user-attachments/assets/40ee904a-b1fb-4f6d-9cfb-323f9bba3f6a" />

**Question 3b**

Implement the method in the following classes that is responsible for accepting a ride
and assigning a driver:

**Question 3b(i) (4 marks)**

the orchestrating class

**ANS:**

<img width="771" alt="Screenshot 2024-12-28 at 5 09 28 PM" src="https://github.com/user-attachments/assets/58b90813-8130-4eda-8cfb-f2384c81c5f1" />
<img width="771" alt="Screenshot 2024-12-28 at 5 09 39 PM" src="https://github.com/user-attachments/assets/f1902dc2-8e16-4046-b64f-0cfdbfdf74a3" />

**Question 3b(ii) (4 marks)**

the Ride class

**ANS:**

<img width="771" alt="Screenshot 2024-12-28 at 5 10 17 PM" src="https://github.com/user-attachments/assets/4334548f-098c-4dbe-907f-0a230103d479" />


### Question 4 (14 marks)

Demonstrate the construction of a component in the PickMeNow system by submitting your answers to the following:

Draw the state diagram for a Ride object as it passes through the system.

**ANS:**

<img width="504" alt="image" src="https://github.com/user-attachments/assets/6296dc1f-3915-40ca-bbe0-3dafa0899e13" />


### Question 5

Demonstrate the application of the observer pattern in the PickMeNow system by submitting your answers to the following:

**Question 5a (8 marks)**

Develop a structural model of the system that uses the observer pattern by constructing the class association diagram that allows an administrator to register interest in receiving feedback and as soon as a customer gives a feedback, the administrator will be informed to process the feedback.

**ANS:**

<img width="437" alt="image" src="https://github.com/user-attachments/assets/44e538cc-74ab-419e-8094-77d1349602e8" />

**Question 5b (10 marks)**

Implement the concrete classes for the structural model in Question 5(a).

**ANS:**

<img width="771" alt="Screenshot 2024-12-28 at 5 09 28 PM" src="https://github.com/user-attachments/assets/5781a1ee-1395-4ce9-986b-439c2a0c4d88" />
<img width="771" alt="Screenshot 2024-12-28 at 5 09 39 PM" src="https://github.com/user-attachments/assets/357bcb7d-fd29-4ea0-8a6c-b9588d19a806" />
<img width="771" alt="Screenshot 2024-12-28 at 5 10 17 PM" src="https://github.com/user-attachments/assets/8033a88a-44d6-4091-9d4d-38a8101c3445" />
<img width="771" alt="Screenshot 2024-12-28 at 5 16 24 PM" src="https://github.com/user-attachments/assets/c7079567-5829-4583-86b9-793e0f8e8e7c" />
<img width="771" alt="Screenshot 2024-12-28 at 5 16 34 PM" src="https://github.com/user-attachments/assets/c11eda88-61c6-40ae-ab00-445f300950f4" />
<img width="771" alt="Screenshot 2024-12-28 at 5 16 56 PM" src="https://github.com/user-attachments/assets/f60df48e-e332-4f88-807d-d89b87dedde3" />
<img width="771" alt="Screenshot 2024-12-28 at 5 17 06 PM" src="https://github.com/user-attachments/assets/5e5f396e-989e-4634-90cf-66f39baacd09" />


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

