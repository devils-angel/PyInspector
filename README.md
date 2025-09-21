# PyInspector

**PyInspector** is a lightweight Python-based vulnerability scanner.  
It performs **banner grabbing** to identify services running on open ports, then checks them against a simple vulnerabilities database.

---

## 📂 Project Structure

- **`banner_grab.py`**  
  Contains the function to connect to a target IP/port and grab the service banner. Some services (e.g., VMware, SSH, FTP) send a banner immediately upon connection, while others (e.g., HTTP) require a probe (`GET / HTTP/1.0`).

- **`vuln_scan.py`**  
  The main scanning script. Iterates over a range of ports, calls the banner grabbing function, and compares results with known vulnerabilities from `vulnerabilities.txt`.

- **`vulnerabilities.txt`**  
  A simple inventory/database of known vulnerable banners. Each line represents a banner string or keyword to match against scanned results.

---

## 🚀 How It Works

1. **Banner Grabbing**  
   - Attempts to connect to a target IP and port.  
   - Reads the response (banner) from the service.  
   - For HTTP-like services (ports 80, 8080), sends a `GET /` request to trigger a response.

2. **Vulnerability Matching**  
   - Scanned banners are compared against `vulnerabilities.txt`.  
   - If a match is found, the scanner reports the service as **potentially vulnerable**.

3. **Reporting**  
   - Prints banners retrieved from each port.  
   - Flags any service that matches an entry in the vulnerabilities list.

---

## 🛠 Usage

### 1. Clone the Repository
```bash
git clone https://github.com/devils-angel/PyInspector.git
cd PyInspector
