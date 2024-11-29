# 🌐 Domain Information Retrieval

A Python script to retrieve detailed information about a domain, including its WHOIS server, expiration date, organization details, and location. This tool helps you check whether a domain is available or already registered.

---

## ✨ Features

- ✅ Check if a domain is registered or available for purchase.
- 🛠️ Retrieve detailed domain registration information:
  - WHOIS server
  - Expiration date
  - Domain name
  - Organization
  - Geographic details (state, city, country)

---

## 📋 Prerequisites

Ensure Python is installed on your system. You'll also need the `whois` library.

Install the required library using:

```bash
pip install python-whois
```

---

## 🚀 How to Use

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-repo-name
   ```

3. Run the script:

   ```bash
   python domain_info.py
   ```

4. Enter a domain URL (e.g., `example.com`) when prompted. The script will display whether the domain is registered and its information if available.

---

## 🖥️ Code Overview

```python
import whois

def Domain_Info(link):
    domain = whois.whois(url)
    print(f"Server : {domain.whois_server}")
    print(f"Exp Date : {domain.expiration_date}")
    print(f"Name : {domain.name}")
    print(f"Organization : {domain.org}")
    print(f"State : {domain.state}")
    print(f"City : {domain.city}")
    print(f"Country : {domain.country}")

url = input("Enter URL with .com or anything\n")

try:
    domain = whois.whois(url)
except:
    print("Domain is available")

else:
    print("Domain is already purchased\n")
    print("Domain Info is as follow:-\n")
    Domain_Info(url)
```

---

## 🛠️ Example Usage

### Registered Domain
```bash
Enter URL with .com or anything
example.com
Domain is already purchased

Domain Info is as follow:-
Server : whois.verisign-grs.com
Exp Date : 2026-01-01
Name : Example Domain
Organization : Example Inc.
State : California
City : Los Angeles
Country : US
```

### Available Domain
```bash
Enter URL with .com or anything
newdomainexample123.com
Domain is available
```

---

## 🤝 Contributing

Contributions are welcome! 🎉 If you have suggestions for improvements or find a bug, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## ✍️ Author

- **Dhairya Vora**  
  - GitHub: [DR-Vora](https://github.com/DR-Vora)  
  - LinkedIn: [Dhairya Vora](https://www.linkedin.com/in/dhairya-vora-475577275)  

---

## 📞 Contact Me

If you have any questions or feedback, feel free to reach out!  
📧 **Email**: voradhairya22@gmail.com  
