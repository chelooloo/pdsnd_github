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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington?: ").lower()
        if city not in ('chicago', 'new york city', 'washington', 'all'):
            print("{} is not a valid input.".format(city))
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month? January, February, March, April, May, or June?: ").lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("{} is not a valid input.".format(month))
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day?: ").title()
        if day not in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All'):
            print("{} is not a valid input.".format(day))
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

    # Load data file into a dataframe
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month, day of week and start hour from the Start Time column to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['start_hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print("Most popular month: {}".format(popular_month))

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("Most popular day of week: {}".format(popular_day))

    # display the most common start hour
    popular_hour = df['start_hour'].mode()[0]
    print("Most popular start hour: {}".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("Most popular start station: {}".format(start_station))

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("Most popular end station: {}".format(end_station))

    # display most frequent combination of start station and end station trip
    print("Most popular end station: {}".format(df.groupby(['Start Station', 'End Station']).size().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("total travel time: {}".format(df['Trip Duration'].sum()))

    # display mean travel time
    print("mean travel time: {}".format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    try:
        print("counts of user types: {}".format(df['User Type'].value_counts()))
    except KeyError:
        print("No data is available")

    # Display counts of gender
    try:
        print("counts of gender: {}".format(df['Gender'].value_counts()))
    except KeyError:
        print("No data is available")

    # Display earliest, most recent, and most common year of birth
    try:
        print("earliest year of birth: {}".format(df['Birth Year'].min()))
    except KeyError:
        print("No data is available")

    try:
        print("most recent year of birth: {}".format(df['Birth Year'].max()))
    except KeyError:
        print("No data is available")

    try:
        print("most common year of birth: {}".format(df['Birth Year'].mode()[0]))
    except KeyError:
        print("No data is available")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """Display users some rows of data upon request"""

    display1 = input("Do you want to see 5 rows of data? ")
    if display1.lower() == 'yes':
        print(df.iloc[:5])

    row_start = 5
    row_end = 10
    while True:
        display2 = input("Do you want to see the next 5 rows of data? ")
        if display2.lower() != 'yes':
            break
        print(df.iloc[row_start: row_end])
        row_start = row_end
        row_end = row_end + 5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
