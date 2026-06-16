# 🏧 ATM Management System

A Python-based ATM simulation system with MySQL backend, developed as a Computer Science project for the AISSCE examination at Indian Educational School, Kuwait.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Database Design](#database-design)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Limitations](#limitations)

---

## 📌 Overview

This ATM System automates core banking operations, making bank administration easier and more accessible. It enables users to open accounts, check balances, deposit/withdraw funds, transfer money, and close accounts — all through a simple command-line interface.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🆕 Open Account | Create a new bank account with auto-generated account & PIN numbers |
| 💸 Withdrawal | Withdraw funds with balance validation |
| 💰 Deposit | Deposit funds into an existing account |
| 🔁 Transfer | Transfer money between two accounts |
| 📊 Balance Enquiry | View current account balance |
| ❌ Close Account | Close an account after withdrawing all funds |

---

## 🛠 Tech Stack

- **Frontend / Logic:** Python 3.x
- **Backend / Database:** MySQL
- **Modules Used:**
  - `mysql.connector` — connects Python to the MySQL server
  - `random` — generates unique account and PIN numbers (`randint()`)

---

## 🗄 Database Design

**Database:** `BANK`

### Table 1: `Bank_Acc_Info` (Parent)

| Column | Type | Constraint |
|---|---|---|
| AccountNo | BIGINT(20) | PRIMARY KEY |
| SocSecNo | INT(10) | |
| FirstName | VARCHAR(20) | |
| LastName | VARCHAR(20) | |
| PhoneNo | BIGINT(12) | UNIQUE |
| PinNo | INT(4) | |
| DOB | DATE | |

### Table 2: `Bank_Balance` (Child)

| Column | Type | Constraint |
|---|---|---|
| AccountNo | BIGINT(20) | FOREIGN KEY → Bank_Acc_Info |
| Balance | FLOAT(15,4) | |
| PinNo | INT(4) | |

---

## 💻 System Requirements

**Recommended:**
- Processor: Intel® Core i5 or higher
- RAM: 4GB – 8GB
- Storage: 256GB
- OS: Windows XP or above

**Minimum:**
- Processor: Intel Core i5
- RAM: 2GB – 4GB
- Storage: 15GB

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Redanaz/ATM-Simulator.git
   cd ATM-Simulator
   ```

2. **Install MySQL Connector for Python**
   ```bash
   pip install mysql-connector-python
   ```
   > Note: Ensure Python is added to your system's PATH before installing.

3. **Set up the MySQL database**
   - Start your MySQL server and log in as root.
   - Run the database setup script:
     ```bash
     python create_db.py
     ```
   This will create the `BANK` database and both tables automatically.

4. **Run the main program**
   ```bash
   python atm.py
   ```

---

## 🖥 Usage

On launch, the following menu is displayed:

```
         ATM FUNCTIONS
1. Open a New Account          2. Close your Account
3. Withdraw Money              4. Deposit Money
5. Transfer Money              6. Bank Balance
7. Exit
Enter your option:
```

### Account Creation Requirements
- Valid 10-digit phone number (must be unique)
- Valid 8-digit social security number
- Must be 18 years or older
- Minimum initial deposit: ₹300

### Validation & Error Handling
- Duplicate phone numbers are rejected
- Invalid/non-existent account numbers are caught
- Wrong PIN entries are flagged
- Overdraft attempts (withdraw/transfer beyond balance) are blocked
- Account closure requires a zero balance

---

## 📁 Project Structure

```
atm-project/
│
├── create_db.py       # Script to create the BANK database and tables
├── atm.py             # Main ATM program with all functions
└── README.md
```

### Key Functions

**Checklist Functions (validators)**
- `Exists(acc)` — checks if an account number exists
- `Pin_No(pin, acc)` — validates the entered PIN
- `exists_phoneno(no)` — ensures phone number uniqueness
- `Amm(acc, amount)` — checks sufficient balance before debit

**ATM Functions (operations)**
- `Create_Acc()` — opens a new bank account
- `Deposit(acc, amount)` — deposits money
- `Witham(acc, amount)` — withdraws money
- `Transfer(acc, acc2, amount)` — transfers between accounts
- `Balance_Enquiry(acc)` — displays current balance
- `Close_Acc(acc)` — closes an account with zero balance

---

## ⚠️ Limitations

- Offline only — no internet or networked banking support
- No account number or PIN recovery mechanism
- Reports are produced in a fixed, pre-designed format only
- No time limit on sessions (unlike real ATMs)
- A restricted number of users can modify database records

---

## 👩‍💻 Author

**Reda Naz Zia**
Class XII-B | Indian Educational School, Kuwait
Examination: AISSCE | Year: 2023–2024
Guided by: Ms. Anjali Nair (Computer Science Teacher)
