from randomuser import RandomUser
import pandas as pd
from datetime import datetime

def get_users(num_users=10):
    """
    Generate random user data.

    Args:
        num_users (int): Number of users to generate.

    Returns:
        pandas.DataFrame: DataFrame containing user information.
    """
    users = []
    try:
        for user in RandomUser.generate_users(num_users):
            dob = user.get_dob()

            # Format DOB if it's a datetime object
            if hasattr(dob, 'strftime'):
                dob = dob.strftime('%Y-%m-%d')
            else:
                # Try parsing ISO8601 string to datetime, then format
                try:
                    dob_obj = datetime.strptime(dob, "%Y-%m-%dT%H:%M:%S.%fZ")
                    dob = dob_obj.strftime('%Y-%m-%d')
                except Exception:
                    # fallback if parsing fails, keep original
                    pass

            users.append({
                "Name": user.get_full_name(),
                "Gender": user.get_gender(),
                "City": user.get_city(),
                "State": user.get_state(),
                "Email": user.get_email(),
                "DOB": dob,
                "Picture": user.get_picture()
            })
    except Exception as e:
        print(f"Error generating users: {e}")
        return pd.DataFrame()  # Return empty DataFrame on error

    return pd.DataFrame(users)


df1 = get_users(num_users=10)
print(df1)
