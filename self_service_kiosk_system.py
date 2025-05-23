def session_counter():
    """Simulates a temporary session counter that resets each time it is called."""
    counter = 0
    counter += 1
    print(f"Session visits: {counter}")

def kiosk_usage():
    """Simulates a persistent usage tracker that keeps track of total customers served."""
    if not hasattr(kiosk_usage, "total_users"):
        kiosk_usage.total_users = 0
    kiosk_usage.total_users += 1
    print(f"Total users today: {kiosk_usage.total_users}")

# Simulating three customer sessions
for _ in range(3):
    print("New Customer Session:")
    session_counter()
    kiosk_usage()
    print("-" * 30)

# Demonstrating session counter resets
print("\nDemonstrating session resets:")
for _ in range(5):
    session_counter()

# Showing persistent kiosk usage count
print("\nDemonstrating persistent kiosk usage:")
for _ in range(5):
    kiosk_usage()