# culinary-delight

## Culinary Delight - Web Project

### Youtube video url : https://youtu.be/Q_hYmA0mK8Y
### Website url : https://teja88.pythonanywhere.com/
```
Username : guest_access
Password : welcome123
```

### Overview
Culinary Delight is a restaurant website that allows users to register, log in, explore various menus, reserve tables, and send messages. The website features a navigation bar containing sections such as Home, Our Story, Menu, Reservation, Services, and Contact Us. The Menu page includes dining options, drink menu, happy hours, and dessert menu, with specific country menus for India, Australia, Japan, Italy, France, Spain, Korea, and China.

### Table of Contents
<ul>
  <li>Project Architecture</li>
  <li>Features</li>
  <li>Technologies Used</li>
  <li>Setup and Installation</li>
  <li>Usage</li>
  <li>Screenshots</li>
</ul>

### Project Architecture
```
culinary-delight/
|_RESTAURENT
| |_static
| |_templates
| |_app.py
| |_requirements.txt
| |_restaurant.db
|_README.md
```
<ul>
  <li>culinary-delight/: The root directory of your project.</li>
  
  <li>RESTAURENT/: The main directory containing all the essential files and subdirectories for your project.</li>
  
  <li>static/:<br>
  This directory holds all the static files such as CSS, JavaScript, and images. <br>
  
  Example contents: CSS files for styling your web pages, JavaScript files for client-side scripts, and images used on the site.</li>

  <li>templates/: <br>
  This directory contains all the HTML templates for rendering the web pages.<br>

  Example contents: HTML files like index.html, menu.html, reservation.html, etc., which define the structure and layout of your web pages.</li>

  <li>app.py:<br>
  The main Python file for your Flask application.<br>
  
  This file includes the application setup, routes, and any backend logic required for handling requests and responses.</li>

  <li>requirements.txt:<br>
A text file listing all the dependencies and libraries required for your project.<br>

  This file is used to install all the necessary packages using pip.
  </li>

  <li>restaurant.db: <br>
  The SQLite database file storing all the data for your application.<br>
  
  This includes user information, menu details, reservations, and any other data relevant to your project.</li>

  <li>README.md: <br>
  A markdown file providing a detailed overview of your project.<br>
  
  This file includes the project description, setup instructions, usage guidelines, features, technologies used, and any additional information to help users understand and work with your project.
  </li>
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
  
  ```
  git clone https://github.com/Twilight-88/culinary-delight.git 
  cd culinary-delight
  ```

  <li><h5>Create a Virtual Environment:</h5> </li>

  ```
  python -m venv restaurant_env <br>
  source restaurant_env/bin/activate  # For Linux/macOS <br>
  restaurant_env\Scripts\activate  # For Windows <br>
  ```

  <li><h5>Create a Virtual Environment:(In Anaconda Prompt)</h5> </li>

  ```
  conda create --name restaurant_env python=3.8 <br>
  conda activate restaurant_env <br> #Activate the Environment
  ```

  <li><h5>Install Dependencies:</h5> </li>
  
  ```
  pip install -r requirements.txt
  ```

  <li><h5>Install Dependencies:</h5> </li>

  ```
  python app.py
  ```

#### Notes
  Ensure you have Python and pip installed.
  Access the website at http://127.0.0.1:5000/

  ![Screenshot 2024-12-31 024240](https://github.com/user-attachments/assets/90fd92ff-124d-463e-abc0-82b41b252dad)


#### Screenshot
<p>The below page will open for this url (http://127.0.0.1:5000/) </p>

![Screenshot 2024-12-30 221136](https://github.com/user-attachments/assets/a92dff05-d3ca-4884-8621-8746f8106973)

  <li><h5>Exiting SQLite Command Line</h5> </li>

  ```
  .exit
  ```
</ul>


#### Additional Information
<ul>
  <li><bold>User Registration and Login:</bold> The user registration process is straightforward. Users can sign up by providing their name, email, and password. After registering, they can log in using their credentials. This feature ensures that users have a personalized experience on the website, such as viewing their reservation history and sending messages.<li>
    
  ![Screenshot_31-12-2024_21746_127 0 0 1](https://github.com/user-attachments/assets/90e21550-1db1-46d5-b3b9-8d5b407dca8d)

  <li><bold>Table Reservation System:</bold> The table reservation system allows users to select the date, time, and number of guests for their reservation. Once submitted, the system checks for availability and confirms the reservation. This feature is integrated with the back-end to manage table availability and ensure a smooth booking process.</li>
  
  ![Screenshot 2024-12-31 022216](https://github.com/user-attachments/assets/e4e297b5-4fa7-40c9-b7ed-e8131b7b9866)

  <li><bold>Challenges Faced:</bold> Developing a user-friendly and responsive design was one of the main challenges. Ensuring that the website works seamlessly across various devices required extensive testing and adjustments. Another challenge was integrating the various country-specific menus, which involved managing multiple datasets and ensuring that the correct menu is displayed based on the user's selection.</li>
  
  ![Screenshot 2024-12-31 022701](https://github.com/user-attachments/assets/2ced6de8-397e-417e-9b53-2b86ce89dc97)

  <li>**Country-Specific Menus:** The website offers distinct menus for different countries. This feature is managed by storing the menu data in SQLite and dynamically loading the relevant menu based on the user's selection. This allows users to explore a variety of dining options tailored to their preferences and regional tastes.</li>
  
  ![Screenshot 2024-12-31 022837](https://github.com/user-attachments/assets/af5546f9-ec67-4505-8a20-214d102e2ba5)
</ul>


