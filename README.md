# Streamlit Database Entry App


## 📌 Project Overview
This Streamlit project is a simple web application that allows users to input personal details such as first name, last name, middle name, age, course, and an "about life" section. The submitted data is stored in a MySQL database with an individual entry ID, timestamp, and date of submission.

## 📂 Project Structure
The project consists of three main Python files:

- **`createdatabase.py`** – Establishes a connection to MySQL, creates the database, and defines the table structure.
- **`databaseinput.py`** – Handles the insertion of user-submitted values into the database.
- **`streamlit.py`** – The main Streamlit application that collects user inputs and submits them to the database via `databaseinput.py`.

## ✨ Features
✅ User-friendly Streamlit UI for data entry.  
✅ MySQL database integration for data storage.  
✅ Automatic recording of submission date and time.  
✅ Unique ID assigned to each entry.  

## 🚀 Installation
To run this project, install the required dependencies:

```sh
pip install streamlit mysql-connector-python pandas
```

## 🛠 How to Run the Project
1. Ensure MySQL is installed and running.
2. Ensure you configure the MySQL connection parameters according to your system.
3. Run the database setup script:
   ```sh
   python createdatabase.py
   ```
4. Start the Streamlit app:
   ```sh
   streamlit run streamlit.py
   ```

## 📦 Dependencies
The project requires the following Python libraries:
- `streamlit` – For creating the web application.
- `mysql-connector-python` – For MySQL database connection and operations.
- `pandas` – For handling data processing and manipulation.

## 🗄 Database Structure
The MySQL table created in `createdatabase.py` has the following structure:

| Column Name       | Data Type             | Description                           |
|------------------|---------------------|---------------------------------------|
| id               | INT (AUTO_INCREMENT) | Unique entry ID (Primary Key)        |
| first_name       | VARCHAR(100)        | User's first name                    |
| middle_name      | VARCHAR(100)        | User's middle name (optional)        |
| last_name        | VARCHAR(100)        | User's last name                     |
| age              | INT                 | User's age                           |
| country          | VARCHAR(12)         | User's country                       |
| phone           | VARCHAR(11)         | User's phone number                  |
| about_life       | TEXT                | User's description of their life     |
| Date_of_birth    | DATE                | User's date of birth                 |
| course           | VARCHAR(19)         | User's course of study               |
| registrationtime | TIMESTAMP DEFAULT CURRENT_TIMESTAMP | Submission date and time |

## 🤝 Contributing
Feel free to contribute by adding features or improving the project. Fork the repository and submit a pull request with your changes.

## 📧 Contact
For any inquiries or support, please reach out to [adelodungbanjubola@gmail.com].

