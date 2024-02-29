# import sqlite3
# import os
# import sys

# def get_chrome_history():
#     # Change the path accordingly if Chrome is installed in a different directory
#     if sys.platform.startswith('win'):
#         history_db = os.path.join(os.environ['LOCALAPPDATA'], 'Google\\Chrome\\User Data\\Default', 'History')
#     elif sys.platform.startswith('linux'):
#         history_db = os.path.expanduser('~/.config/google-chrome/Default/History')
#     elif sys.platform.startswith('darwin'):
#         history_db = os.path.expanduser('~/Library/Application Support/Google/Chrome/Default/History')
#     else:
#         print("Unsupported operating system")
#         return

#     if not os.path.isfile(history_db):
#         print("Google Chrome history database not found.")
#         return

#     conn = sqlite3.connect(history_db)
#     cursor = conn.cursor()

#     try:
#         cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls")
#         rows = cursor.fetchall()
#         print("URL\tTitle\tVisit Count\tLast Visit Time")
#         for row in rows:
#             url = row[0]
#             title = row[1]
#             visit_count = row[2]
#             # Converting last visit time from Chrome's format to a human-readable format
#             last_visit_time = chrome_time_to_human(row[3])
#             print(f"{url}\t{title}\t{visit_count}\t{last_visit_time}")
#     except sqlite3.OperationalError as e:
#         print("Error:", e)

#     conn.close()

# def chrome_time_to_human(chrome_time):
#     # Chrome time is in microseconds since January 1, 1601 (UTC)
#     # Converting it to seconds since January 1, 1970 (Unix time)
#     unix_time = chrome_time / 1000000 - 11644473600
#     # Converting Unix time to a human-readable format
#     return str(datetime.datetime.fromtimestamp(unix_time))

# if __name__ == "__main__":
#     get_chrome_history()

import os

def power_off():
    if os.name == 'posix':  # For Unix-based systems
        os.system('sudo shutdown -h now')  # Execute the shutdown command with superuser privileges
    elif os.name == 'nt':  # For Windows
        os.system('shutdown /s /t 1')  # Execute the shutdown command
    else:
        print("Power off command is not supported on this platform.")

if __name__ == "__main__":
    power_off()

