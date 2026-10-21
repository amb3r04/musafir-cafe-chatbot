"""
Musafir Cafe AI Chatbot - CS-2 Interactive Server & CLI Demo
School of Computer Science - Computing Projects

Usage:
  1. Web App: python server.py --web    (launches http://localhost:8080)
  2. CLI Bot: python server.py --cli    (runs terminal chatbot conversation)
"""

import sys
import os
import http.server
import socketserver
import webbrowser

PORT = 8080

KNOWLEDGE_BASE = {
    "name": "Musafir Café",
    "location": "Upper Mall Road (Near Picture Palace), Mussoorie, Uttarakhand",
    "hours": "8:00 AM – 10:00 PM (Kitchen cutoff: 9:15 PM)",
    "menu": {
        "Doon Valley Espresso": 140,
        "Americano": 160,
        "Musafir Mountain Cappuccino": 210,
        "Himalayan Honey Cinnamon Latte": 240,
        "Himalayan Cold Brew (18-hr)": 220,
        "Pahadi Masala Chai": 110,
        "Walnut & Dark Chocolate Brownie": 210,
        "Truffle Mushroom Toast": 280,
    },
    "policies": {
        "delivery": "Dine-in and takeaway ONLY. No home delivery.",
        "pets": "Welcome on outdoor terrace only. Not permitted indoors.",
        "allergens": "Walnuts in brownies; gluten in breads. Cannot guarantee 100% cross-contamination safety."
    }
}

def run_web():
    directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(directory)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"============================================================")
        print(f"  Musafir Cafe Chatbot Web Server running at:")
        print(f"  http://localhost:{PORT}")
        print(f"  Press Ctrl+C to stop.")
        print(f"============================================================")
        try:
            webbrowser.open(f"http://localhost:{PORT}")
        except:
            pass
        httpd.serve_forever()

def run_cli():
    print("="*60)
    print("  Musafir Café CLI Chatbot — Mall Road, Mussoorie")
    print("  Type 'quit' or 'exit' to end conversation.")
    print("="*60)
    print("\nBarista: Namaste! Welcome to Musafir Café on Mall Road, Mussoorie.")
    print("Barista: How may I help you today?\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ['quit', 'exit']:
                print("\nBarista: Phir milenge! Safe travels in the mountains.\n")
                break
                
            lower = user_input.lower()
            if "hour" in lower or "time" in lower or "open" in lower:
                print("\nBarista: We are open Monday to Sunday from 8:00 AM to 10:00 PM (kitchen closes at 9:15 PM).\n")
            elif "menu" in lower or "price" in lower or "coffee" in lower:
                print("\nBarista: Our favorites include the Doon Valley Espresso (₹140), Mountain Cappuccino (₹210), and Himalayan Cold Brew (₹220).\n")
            elif "location" in lower or "where" in lower or "address" in lower:
                print("\nBarista: We are on Upper Mall Road, near Picture Palace, Mussoorie, overlooking the Doon Valley!\n")
            elif "allergy" in lower or "nut" in lower or "celiac" in lower or "gluten" in lower:
                print("\nBarista: WARNING: Our kitchen handles real tree nuts (walnuts) and wheat gluten. We cannot guarantee 100% zero cross-contamination for severe allergies.\n")
            elif "delivery" in lower or "deliver" in lower:
                print("\nBarista: We do not offer delivery in the hills. We are dine-in and takeaway only.\n")
            else:
                print("\nBarista: I'm here to help with Musafir Café's menu, hours, or directions on Mall Road. Feel free to ask!\n")
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        run_cli()
    else:
        run_web()
