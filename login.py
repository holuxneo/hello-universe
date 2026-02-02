def login(username, password):
    """
    Simple login function with hardcoded credentials.
    
    Args:
        username: User's username
        password: User's password
        
    Returns:
        True if credentials match, False otherwise
    """
    # Hardcoded credentials (use database in production)
    valid_users = {
        "admin": "Holux$&O",
        "user": "holuxneo"
    }
    
    if username in valid_users and valid_users[username] == password:
        return True
    return False


def main():
    """Main login interface"""
    attempts = 3
    
    while attempts > 0:
        print("=== Login System ===")
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if login(username, password):
            print("✓ Login successful!")
            return
        else:
            attempts -= 1
            print(f"✗ Invalid credentials. Attempts remaining: {attempts}\n")
    
    print("✗ Login failed. Too many attempts!")


if __name__ == "__main__":
    main()