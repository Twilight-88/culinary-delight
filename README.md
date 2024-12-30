# culinary-delight

## Culinary Delight - Web Project

### Youtube video url : https://youtu.be/Q_hYmA0mK8Y

### Overview
Culinary Delight is a restaurant website that allows users to register, log in, explore various menus, reserve tables, and send messages. The website features a navigation bar containing sections such as Home, Our Story, Menu, Reservation, Services, and Contact Us. The Menu page includes dining options, drink menu, happy hours, and dessert menu, with specific country menus for India, Australia, Japan, Italy, France, Spain, Korea, and China.

### Table of Contents
<ul>
  <li>Features</li>
  <li>Technologies Used</li>
  <li>Setup and Installation</li>
  <li>Usage</li>
  <li>Screenshots</li>
</ul>

### Features
<ul>
  <li><bold>User Registration and Login:</bold> Users can create an account and log in to access personalized features.</li>
  <li><bold>Navigation Bar:</bold> Home, Our Story, Menu, Reservation, Services, Contact Us.</li>
  <li><bold>Table Reservation:</bold> Users can reserve a table through the Reservation section.</li>
  <li><bold>Message Contact:</bold> Users can send messages through the Contact Us section.</li>
  <li><bold>Menu Sections:</bold> Includes dining menu, drink menu, happy hours, and dessert menu.</li>
  <li><bold>Country-Specific Menus:</bold> Separate menus for India, Australia, Japan, Italy, France, Spain, Korea, and China.</li>
</ul>


#### Technologies Used
<ul>
  <li>Front End: HTML, CSS, JavaScript</li>
  <li>Back End: Python, Flask, Werkzeug</li>
  <li>Database: SQLite</li>
  <li>Libraries and Tools: Flask-SQLAlchemy, Jinja2, pip</li>
</ul>

#### Setup and Installation
<ul>
  <li><h5>Clone the Repository:</h5> </li>
  git clone https://github.com/Twilight-88/culinary-delight.git <br>
  cd culinary-delight

  <li><h5>Create a Virtual Environment:</h5> </li>
  python -m venv restaurant_env <br>
  source restaurant_env/bin/activate  # For Linux/macOS <br>
  restaurant_env\Scripts\activate  # For Windows <br>

  <li><h5>Install Dependencies:</h5> </li>
  pip install -r requirements.txt

  <li><h5>Install Dependencies:</h5> </li>
  python app.py

#### Notes
  Ensure you have Python and pip installed.
  Access the website at http://127.0.0.1:5000/


#### Screenshot
<p>The below page will open for this url (http://127.0.0.1:5000/) </p>

![Screenshot 2024-12-30 221136](https://github.com/user-attachments/assets/a92dff05-d3ca-4884-8621-8746f8106973)

  <li><h5>Exiting SQLite Command Line</h5> </li>
  .exit
</ul>


#### Additional Information
<ul>
  <li>**User Registration and Login:** The user registration process is straightforward. Users can sign up by providing their name, email, and password. After registering, they can log in using their credentials. This feature ensures that users have a personalized experience on the website, such as viewing their reservation history and sending messages.<li>
  ![Screenshot_31-12-2024_21746_127 0 0 1](https://github.com/user-attachments/assets/90e21550-1db1-46d5-b3b9-8d5b407dca8d)

  <li>**Table Reservation System:** The table reservation system allows users to select the date, time, and number of guests for their reservation. Once submitted, the system checks for availability and confirms the reservation. This feature is integrated with the back-end to manage table availability and ensure a smooth booking process.</li>

  <li>**Challenges Faced:** Developing a user-friendly and responsive design was one of the main challenges. Ensuring that the website works seamlessly across various devices required extensive testing and adjustments. Another challenge was integrating the various country-specific menus, which involved managing multiple datasets and ensuring that the correct menu is displayed based on the user's selection.</li>

  <li>**Country-Specific Menus:** The website offers distinct menus for different countries. This feature is managed by storing the menu data in SQLite and dynamically loading the relevant menu based on the user's selection. This allows users to explore a variety of dining options tailored to their preferences and regional tastes.</li>
</ul>


