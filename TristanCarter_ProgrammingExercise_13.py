# Tristan Carter 11/30/25
# This program will show the user population growth of a city on Florida

import sqlite3
import random
import matplotlib.pyplot as plt



# Create database and table
def create_database():
    conn = sqlite3.connect("population_TC.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    """)

    # Cities and population
    cities = {
        "Bradenton": 56300,
        "Palmetto": 13400,
        "Sarasota": 58300,
        "Jacksonville": 962000,
        "St. Petersburg": 261000,
        "Hollywood": 153000,
        "Daytona": 76000,
        "Miami": 447000,
        "Gainesville": 144000,
        "Orlando": 312000
    }

    # Insert 2023 data
    for city, pop in cities.items():
        cursor.execute("INSERT INTO population VALUES (?, ?, ?)", (city, 2023, pop))

    conn.commit()
    conn.close()
    print("Database and records created.")



# Simulate growth/decline for 20 years
def simulate_population():
    conn = sqlite3.connect("population_TC.db")
    cursor = conn.cursor()

    # Retrieve 2023 data
    cursor.execute("SELECT city, population FROM population WHERE year=2023")
    data = cursor.fetchall()

    for city, population in data:
        current_pop = population
        for year in range(2024, 2044):  # next 20 years
            growth_rate = random.uniform(-0.02, 0.04)
            current_pop = int(current_pop * (1 + growth_rate))

            cursor.execute(
                "INSERT INTO population VALUES (?, ?, ?)",
                (city, year, current_pop)
            )

    conn.commit()
    conn.close()
    print("Population simulation for 20 years completed.")


# Population growth graph
def show_population_growth():
    cities = [
        "Bradenton", "Palmetto", "Sarasota", "Jacksonville", "St. Petersburg",
        "Hollywood", "Daytona", "Miami", "Gainesville", "Orlando"
    ]

    print("\nFlorida Cities:")
    for c in cities:
        print(" -", c)

    city_choice = input("\nEnter a city name from the list: ")

    conn = sqlite3.connect("population_TC.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT year, population 
        FROM population 
        WHERE city=? 
        ORDER BY year
    """, (city_choice,))

    results = cursor.fetchall()
    conn.close()

    years = [row[0] for row in results]
    populations = [row[1] for row in results]

    plt.figure(figsize=(10, 5))
    plt.plot(years, populations, marker="o", linestyle="-")
    plt.title(f"Population Growth: {city_choice}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.show()



if __name__ == "__main__":
    create_database()
    simulate_population()
    show_population_growth()