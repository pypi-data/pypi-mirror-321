import random
import pandas as pd
import os

def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}
    return user_preference

def generate_parsi_names(n, user_preference=None, seed=None):

    # parsi Male First Names
    male_parsi_firstname= [
        'Zia', 'Faramarz', 'Ravshan', 'Javad', 'Ramin', 'Soroush', 'Dastan', 'Kian', 'Shapour', 'Shahin', 'Zohar', 'Arian', 'Parsa', 'Bardia', 
        'Sohrab', 'Reza', 'Yousef', 'Dariush', 'Omid', 'Shapur', 'Roham', 'Zain', 'Benyamin', 'Aryan', 'Darius', 'Farhan', 'Kambiz', 'Kaveh', 
        'Niroo', 'Peyman', 'Yazdan', 'Ashkan', 'Sina', 'Bahram', 'Mehrdad', 'Fariborz', 'Moeen', 'Iraj', 'Ferydoun', 
        'Houshang', 'Vahid','Vera', 'Taraz', 'Saeed', 'Sadegh', 'Mihan', 'Zubin', 'Amin', 'Shahram', 'Rashid', 'Yashar', 'Boman',
        'Arman', 'Farid', 'Kourosh', 'Nadim', 'Koroush', 'Arda', 'Cyrus', 'Aditya', 'Nader', 'Behzad', 'Ebrahim', 'Bahman', 'Farzad', 'Adar', 
        'Arash', 'Hossein', 'Giv', 'Zaman', 'Kamran', 'Shahin']
# parsi Female First Names
    female_parsi_firstname = [
        'Avan', 'Laleh', 'Banu', 'Shadmehr', 'Giti', 'Arya', 'Mahinaz', 'Piroja', 'Darayus', 'Aria', 'Maryam', 'Mahtab', 'Saba', 'Behnaz', 
        'Roya', 'Roxane', 'Roshanak', 'Behzad', 'Nazish', 'Vahid', 'Setayesh', 'Shokouh', 'Shahnaz', 'Avan', 'Laleh', 'Banu', 'Shadmehr', 'Giti', 'Arya', 'Mahinaz', 'Piroja', 'Darayus', 'Aria', 'Maryam', 'Mahtab', 'Saba', 'Behnaz', 
        'Roya', 'Roxane', 'Roshanak', 'Behzad', 'Nazish', 'Vahid', 'Setayesh', 'Shokouh', 'Shahnaz', 'Kamran', 'Razieh', 'Chandana', 
        'Tanaz', 'Mohini', 'Daryan', 'Sanaz', 'Shadi', 'Shahla', 'Naaz', 'Shahin', 'Yazdan', 'Vali', 'Durren', 'Shamsi', 'Zeynab', 
        'Parnaz', 'Pirooz', 'Shahidah', 'Jameela', 'Manzar', 'Soheila', 'Soraya', 'Sahar', 'Manizheh', 'Sheida', 'Farnaz', 'Zohreh', 'Nagma', 
        'Nasrin', 'Anousha', 'Golsheri', 'Elham', 'Mohsen', 'Mitra', 'Ladan', 'Shirin', 'Edal', 'Khadija', 'Kambiz', 'Niloofar', 'Shideh', 
        'Arameh', 'Nahal', 'Forough', 'Zarina', 'Marjan', 'Taraneh', 'Zari', 'Anahita', 'Niloufar', 'Shahram', 'Sheyda', 'Arzoo', 'Feroze', 
        'Roshan', 'Mehrdad', 'Benazir', 'Asgar', 'Masoumeh', 'Roshni', 'Ashna', 'Firoza', 'Navaz', 'Mehrnaz', 'Yasaman', 'Tahmineh', 'Parvin', 
        'Shayan', 'Zahra', 'Nahid', 'Fereshteh', 'Moharram', 'Anousheh', 'Mahsa', 'Mahshid', 'Roudabeh', 'Simin', 'Farahnaz', 'Nooshin', 
        'Mandana', 'Roxan', 'Homai', 'Negin', 'Mariam', 'Farah', 'Afsheen', 'Shakila', 'Mahboubeh', 'Kiana', 'Jasmin', 'Dena', 'Fariha', 
        'Mahoor', 'Chahna', 'Shabnam', 'Shahrzad', 'Mahin', 'Roxana', 'Golnaz', 'Yasmin', 'Nasreen', 'Hasti', 'Pari', 'Homa', 
        'Dinaz', 'Eshita', 'Parastoo', 'Roshin', 'Khushnuma', 'Mahnoosh', 'Samira', 'Najmeh', 'Parsa', 'Afsana', 'Atash', 'Farida', 'Khorshid', 
        'Nazanin', 'Nilofer', 'Marzieh','Razieh', 'Chandana', 'Tanaz', 'Mohini', 'Daryan', 'Sanaz', 'Shadi', 'Shahla', 'Naaz', 'Yazdan', 'Vali',
        'Durren', 'Shamsi', 'Zeynab','Parnaz', 'Pirooz', 'Shahidah', 'Jameela', 'Manzar', 'Soheila', 'Soraya', 'Sahar', 'Manizheh', 'Sheida', 'Farnaz', 'Zohreh', 'Nagma', 
        'Nasrin', 'Anousha', 'Golsheri', 'Elham', 'Mohsen', 'Mitra', 'Ladan', 'Shirin', 'Edal', 'Khadija', 'Kambiz', 'Niloofar', 'Shideh', 
        'Arameh', 'Nahal', 'Forough', 'Zarina', 'Marjan', 'Taraneh', 'Zari', 'Anahita', 'Niloufar', 'Shahram', 'Sheyda', 'Arzoo', 'Feroze', 
        'Roshan', 'Mehrdad', 'Benazir', 'Asgar', 'Masoumeh', 'Roshni', 'Ashna', 'Firoza', 'Navaz', 'Mehrnaz', 'Yasaman', 'Tahmineh', 'Parvin', 
        'Shayan', 'Zahra', 'Nahid', 'Fereshteh', 'Moharram', 'Anousheh', 'Mahsa', 'Mahshid', 'Roudabeh', 'Simin', 'Farahnaz', 'Nooshin', 
        'Mandana', 'Roxan', 'Homai', 'Negin', 'Mariam', 'Farah', 'Afsheen', 'Shakila', 'Mahboubeh', 'Kiana', 'Jasmin', 'Dena', 'Fariha', 
        'Mahoor', 'Chahna', 'Shabnam', 'Shahrzad', 'Mahin', 'Roxana', 'Golnaz', 'Yasmin', 'Nasreen', 'Hasti', 'Pari', 'Homa', 
        'Dinaz', 'Eshita', 'Parastoo', 'Roshin', 'Khushnuma', 'Mahnoosh', 'Samira', 'Najmeh', 'Parsa', 'Afsana', 'Atash', 'Farida', 'Khorshid', 
        'Nazanin', 'Nilofer', 'Marzieh']
    parsi_surname = [
        "Adajania", "Albless", "Anjaria", "Banaji", "Baria", "Behram", "Bhansali", "Billimoria", 
        "Chawda", "Choksy", "Daruwalla", "Davar", "Dastur", "Desai", "Dinshaw", "Faredia", 
        "Firoze", "Gilla", "Hathi", "Irani", "Jafari", "Jamshedji", "Kambata", 
        "Kharas", "Khorshed", "Khatri", "Khoras", "Mistry", "Mogrelia", "Navroji", "Noshirwani", "Patel", "Pishor", 
        "Rangoonwala", "Rustomji", "Vakharia", "Vaswani", "Wadia", "Wolfe", "Vaze", "Zaveri", "Zangeneh", 
        "Zodhi", "Jamshedwala", "Jamshidwala", "Pardiwala", "Randerwala", "Sorabji", "Tata", "Shahji", 
        "Hormaiz", "Mota", "Mavani", "Poonawala", "Mehta", "Manekji", "Motwani", "Dasturwala", "Wadiawala", "Zarwani", 
        "Malian", "Zartosht", "Bhandara", "Brombaria", "Bulsara", "Chinoy", "Cama", "Dinshawwala", "Erachwala",
        "Fletcher", "Hirjee", "Iraniwala", "Kama", "Kholwalia", "Nadri",  "Shahnaaz", "Worley", "Tayabji", "Tatawala",
        "Nariman", "Mistrywala", "Navrojiwala", "Kundranwala", "Minoo", "Vahidi", "Zarirani", "Wadiawala", "Ishmailwala",
        "Mumtazwala", "Dhanjiwala", "Gandhiwala"]
    # Set the random seed if provided
    if seed is not None:
        random.seed(seed)

    # Initialize user preferences
    preferences = init(user_preference)

    # Create a list to store names and their genders
    names = []

    # Generate names
    for i in range(n // 2):  # Generate half male and half female names
        # Male Name Generation
        first_name_male = random.choice(male_parsi_firstname)
        last_name_male = random.choice(parsi_surname)

        if preferences.get('name_type') == 'first':
            name_male = first_name_male  # Only first name
        else:
            name_male = first_name_male + " " + last_name_male  # Full name

        # Female Name Generation
        first_name_female = random.choice(female_parsi_firstname)
        last_name_female = random.choice(parsi_surname)
       
        if preferences.get('name_type') == 'first':
            name_female = first_name_female  # Only first name
        else:
            name_female = first_name_female + " " + last_name_female  # Full name

        # Append names with gender information
        names.append((name_male, "Male"))
        names.append((name_female, "Female"))

    # Create a DataFrame
    df = pd.DataFrame(names, columns=["Name", "Gender"])

    # Write to CSV file
    file_path = 'generated_parsi_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Names have been written to '{file_path}' successfully.")
    return df
