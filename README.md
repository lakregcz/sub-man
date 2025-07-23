

# Subscription Manager 💎  

![App Banner](https://lakiup.com/wp-content/uploads/2025/07/1.png)  

A modern, user-friendly application for managing premium subscriptions with MySQL database integration.  

---

## ✨ Features  

<div align="center">
  <img src="https://lakiup.com/wp-content/uploads/2025/07/2.png" width="45%" alt="Dashboard Preview">
  <img src="https://lakiup.com/wp-content/uploads/2025/07/3.png" width="45%" alt="Subscription Plans">
</div>  

| Feature | Description |
|---------|-------------|
| 🔐 **Secure Auth** | Login/registration with password protection |
| 💳 **Subscription Plans** | Monthly/Quarterly/Annual billing options |
| 📅 **Auto-Expiry** | Tracks subscription end dates |
| 🎨 **Dark Theme UI** | Sleek Flet-based interface |
| 🗃️ **MySQL Backend** | Persistent user data storage |

---

## 🛠️ Tech Stack  

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)  
![Flet](https://img.shields.io/badge/Flet-0.9.0-green)  
![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange?logo=mysql)  

---

## 🚀 Installation  

### Prerequisites  
- Python 3.9+  
- MySQL Server 8.0+  

1. **Clone the repo**:  
   ```bash
   git clone https://github.com/lakregcz/sub-man.git
   cd sub-man
   ```

2. **Install dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up MySQL**:  
   ```sql
   CREATE DATABASE premium_manager;
   USE premium_manager;
   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(50) UNIQUE NOT NULL,
       email VARCHAR(100) UNIQUE NOT NULL,
       password VARCHAR(100) NOT NULL,
       subscription_end DATE NULL
   );
   ```

---

## ⚙️ Configuration  

1. Edit the database connection in the Python file:  
   ```python
   self.db = mysql.connector.connect(
       host='localhost',      # Your MySQL host
       database='premium_manager',  # Database name
       user='your_username', # MySQL username
       password='your_password' # MySQL password
   )
   ```

2. **Run the app**:  
   ```bash
   python "premium manager by lakiup.py"
   ```

---

## 📸 Screenshots  

| Login Screen | Subscription Plans |  
|--------------|--------------------|  
| <img src="https://lakiup.com/wp-content/uploads/2025/07/2.png" width="400"> | <img src="https://lakiup.com/wp-content/uploads/2025/07/3.png" width="400"> |  

---

## 📜 License  
MIT © 2025 [lakiup](https://cv.lakiup.com)  

---

### Key Improvements:  
1. **Fixed all typos** (e.g., `sub-ma` → `sub-man`)  
2. **Added clear MySQL setup instructions**  
3. **Specified exact configuration steps**  
4. **Improved formatting** for better readability  
5. **Added badges** for tech stack visibility  

Let me know if you'd like any further adjustments! 🚀
