# 📚 **Blog_LLM_AI_DATA** - A Personal Blog Web Application Built with Python Flask ⚡

This is a **dynamic and interactive blog** web application developed using the **Python Flask framework**. The project allows users to **log in**, **create posts**, and **view blog posts**. It's powered by an **SQLite database**, offering a seamless experience with efficient data storage and retrieval. 

With a clean, modern design powered by **HTML** and **CSS**, this project serves as a foundation for anyone interested in building **full-stack web applications**. It’s an ideal solution for bloggers, content creators, and learners looking to dive into **web development** with Flask.

---

## 🛠️ **Technologies Used**

- **Python**: The primary language used to develop the backend logic.
- **Flask**: A lightweight web framework used to build the blog's backend and routing.
- **SQLite**: A lightweight, file-based database used to store user data and blog posts.
- **HTML**: Used for creating the structure and content of the web pages.
- **CSS**: Provides the styling and design, making the blog responsive and visually appealing.

---

## 📂 **Project Structure**

This project follows a modular structure, making it easier to navigate and maintain. Here’s the breakdown of the core files and directories:

- **app.py**: Main Python script where the Flask routes and logic are implemented.
- **templates/**:
  - **index.html**: The homepage that displays all the blog posts.
  - **login.html**: User authentication page for login.
  - **post.html**: Allows users to create new blog posts.
- **static/**:
  - **css/**: Contains CSS files that style the web pages.
- **database/**: Stores the SQLite database containing user and blog post information.

---

## 🔍 **Project Description**

### **Objective**
The aim of this project is to build a **simple, functional blog platform** where users can create, view, and manage blog posts. The system features **user authentication** to ensure that only registered users can create posts. It demonstrates the power of Flask in building web applications, **SQLite** for lightweight data management, and front-end skills with HTML and CSS.

### **Key Features**
- 🔑 **User Authentication**: Secure login page for user authentication.
- 📝 **Blog Creation**: Create, edit, and manage posts easily through a clean interface.
- 📚 **Dynamic Content**: Automatically displays the latest blog posts on the homepage.
- 🔒 **Security**: Simple user authentication to ensure data integrity.

---

## 🧑‍💻 **How It Works**

### 1. **User Login**
   - Users log in through the **login.html** page. The system uses basic authentication to verify credentials stored in the **SQLite database**.

### 2. **Blog Post Management**
   - Once logged in, users are redirected to **index.html** to see the list of available blog posts.
   - To create a new post, users are directed to **post.html**, where they can add content. The new posts are stored in the **SQLite database**.

### 3. **Displaying Posts**
   - The **index.html** page fetches all the blog posts from the database and displays them in a user-friendly layout.

### 4. **Database Integration**
   - The **SQLite database** stores **user data** (for authentication) and **blog post details** (title, content, timestamp).

---

## 💻 **Features & Capabilities**

### **1. User Authentication**
   - Secure login page to authenticate users.
   - User credentials are stored and verified using **SQLite**.

### **2. Dynamic Blog Management**
   - Users can create new posts, which are automatically displayed on the homepage.
   - Each post includes a **title**, **content**, and **date**.

### **3. Clean & Responsive Design**
   - Aesthetic design with simple, effective CSS for a seamless user experience.
   - The layout is fully responsive, ensuring the blog looks great on all devices.

---

## 📊 **How to Run the Project Locally**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/prabhatadvait/Blog_LLM_AI_DATA.git
