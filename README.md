# Sentinels-Mobile-Application
Developing doctor mobile application by using kivy library

# Mobile Application for the Doctors
We implemented a doctor mobile application using Kivy. It is an open-source Python library for rapid development of applications that make use of innovative user interfaces, such as multi-touch apps. Kivy is selected because it runs on Linux, Windows, OS X, Android, iOS, and Raspberry Pi. You can run the same code on all supported platforms. The android application has 5 main activities (Sign up, log in, Main Page, connecting with patient’s database, and Videocall). We move from one to another by starting new intent. The doctor can sign up if he doesn’t have any account or can move to login activity if he already has an account. Then, the android Application will take him to the main page where the app services will be available to the doctor to use. The doctor can user the video call conference feature to communicate with the patient form any place. The doctor can also view patient’s measures from the main page by using patient details button and then by entering the patient id he can view any patient specific measurements.

![image](https://user-images.githubusercontent.com/100867843/180037244-30fed5ac-3d9e-48f3-9d16-6fad738e24c6.png)
![image](https://user-images.githubusercontent.com/100867843/180037276-36a038cf-49b2-4744-8959-5f95388a5a09.png)
![image](https://user-images.githubusercontent.com/100867843/180037746-cdc1949e-5d8b-4bfe-9038-85dff59f0bb3.png)


# Database connection with the android app
As mentioned before MySQL database is used to store the patient’s measures which comes from our GUI Tkinter interface in the robot. When the doctor presses the patient details button and enters the patient id The android application connects with the database and retrieves the data from it and the data will be presented in the android app for the doctor to see and review.

![image](https://user-images.githubusercontent.com/100867843/180040471-cace7ddd-6f8b-42e6-adaa-64b3d703d80f.png)
![image](https://user-images.githubusercontent.com/100867843/180040485-ef4241bc-f1fd-4f61-b46d-fa40888bbbf5.png)
![image](https://user-images.githubusercontent.com/100867843/180040496-d7926ac9-81b9-4419-8bc5-0501157aa902.png)


# Video call Feature
We implemented the video call feature in the app to allow the doctor to communicate efficiently with the patients. The main-Page of the android application has also video call button which starts new intent to video-call activity if the robot is ready which means that it arrived at the room and the patient has initiated the video call. 
Our video call feature depends on the patient initiation of the video call as when the patient is in front of the robot, he will press the video call button in the GUI then the GUI with direct the patient to a video call room in which he will communicate with doctor and then an email will be send to the doctor to tell him that a patient wants to call him. After that the doctor will go to the android application and press the video call button to join the room with the patient.
![image](https://user-images.githubusercontent.com/100867843/180037532-47eaff07-81c8-43dd-8f21-3dbadf21f437.png)
