from datetime import datetime, timedelta
import webbrowser

# Get the start and end dates from the user
start_date_str = input("Enter the start date (YYYY-MM-DD): ")
end_date_str = input("Enter the end date (YYYY-MM-DD): ")

# Convert user input to datetime objects
start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

# Loop through the date range and open URLs in the web browser
current_date = start_date
while current_date <= end_date:
    date_str = current_date.strftime("%d%b%Y").upper()
    year = current_date.strftime("%Y")
    month = current_date.strftime("%b").upper()
    
    # Generate the dynamic URL
    url = f"https://nsearchives.nseindia.com/content/historical/EQUITIES/{year}/{month}/cm{date_str}bhav.csv.zip"
    
    # Open the URL in the web browser
    webbrowser.open(url)
    
    # Move to the next date
    current_date += timedelta(days=1)
