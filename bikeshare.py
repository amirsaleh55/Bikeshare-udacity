import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city= input("\nEnter the city you want to explore from chicago,new york city,washington \n").lower()
        if city not in CITY_DATA:
            print("Invalid input please follow the instructions and Try again")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month= input("\nWould you like to filter by month if yes enter the month as follows: january, february,...june \n if no enter all \n").lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("Invalid input please follow the instructions and Try again")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input("\nWould you like to filter by day if yes enter the day as follows: sunday, monday,... saturday \n if no enter all  \n").lower()
        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            print("Invalid input please follow the instructions and Try again")
            continue
        else:
            break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
   #reading data from csv file by city name
    df = pd.read_csv(CITY_DATA[city])
    
    
    # convert the Start Time column to datetime to access the months and days of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #new columns for month and day of week to filter with 
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    
    #filter by month
    if month != "all":
        list_months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = list_months.index(month) + 1
        df = df[df['month'] == month]
    
    #filter by day
    if day!= "all":
        df = df[df['day_of_week'] == day.title()]
    
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_popular_month = df['month'].mode()[0]
    print("\nThe most popular month is:",most_popular_month,"\n")

    # TO DO: display the most common day of week
    most_popular_day = df['day_of_week'].mode()[0]
    print("\nThe most popular day is:",most_popular_day,"\n")

    # TO DO: display the most common start hour
    
    #new coulmn for hours
    df['hours']=df['Start Time'].dt.hour
    
    most_popular_hour = df['hours'].mode()[0]
    print("\nThe most popular hour is:",most_popular_hour,"\n")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_popular_start_station=df['Start Station'].value_counts().idxmax()
    print("\nThe most popular start station is:", most_popular_start_station,"\n" )

    # TO DO: display most commonly used end station
    
    most_popular_end_station=df['End Station'].value_counts().idxmax()
    print("\nThe most popular end station is:", most_popular_end_station,"\n" )

    # TO DO: display most frequent combination of start station and end station trip
    
    combined_trip = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print("\nThe most combination of start station and end station trips is:",combined_trip)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    Total_travel_time = sum(df['Trip Duration'])
    print('\nTotal travel time in minutes:', Total_travel_time/60, " Minutes")
    print('\nTotal travel time in hours:', Total_travel_time/3600, " Hours")
    print('\nTotal travel time in days:', Total_travel_time/86400, " Days")

    # TO DO: display mean travel time

    print("\nThe mean travel time in minutes is :",(df['Trip Duration'].mean())/60)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    count_of_user_types = df['User Type'].value_counts()
    print(count_of_user_types)

    if city != "washington":
        # TO DO: Display counts of gender
        
        count_of_genders = df['Gender'].value_counts()
        print(count_of_genders)

        # TO DO: Display earliest, most recent, and most common year of birth
    
        print("The earliest year of birth is :",df['Birth Year'].min())
   
        print("The most recent year of birth is :",df['Birth Year'].max())
    
        print("The most common year of birth is :",df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data form the dataframe."""
    index_start=0
    
    while True:
        #taking input from user to detrmine he want to see data or no
        
        input_choice = input("/nDo you want to display Raw data if yes enter 'yes' if no enter 'no' ").lower()
        
        #checking for input choice
        if input_choice == "yes":
            print(df.iloc[index_start:index_start+5])
            index_start+=5
            continue
        elif input_choice == "no":
            break
        else :
            print("\nInvalid input please follow the instruction and try again")

            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
