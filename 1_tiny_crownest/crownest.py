import argparse

vowel = "aeiouAEIOU"
notLatin = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
cities = ["Adana", "Addis Ababa", "Adelaide", "Accra", "Aktyubinsk Aktobe", "Alexandria", "Algiers", "Almaty", "Amsterdam", "Ankara", "Antalya", "Antananarivo", "Antwerp", "Anshan", "Ahmedabad", "Astana", "Asuncion", "Athens", "Ashgabat", "Baghdad", "Basel", "Baku", "Bangalore", "Bangkok", "Bandung", "Barranquilla", "Barcelona", "Batumi", "Beirut", "Belgrade", "Belo Horizonte", "Berlin", "Birmingham", "Berne", "Bishkek", "Babruysk", "Bobruysk", "Bogota", "Bordeaux", "Brasilia", "Bratislava", "Brest", "Brisbane", "Budapest", "Bukhara", "Bucharest", "Buenos Aires", "Bhopal", "Valencia", "Varna", "Warsaw", "Washington", "Wellington", "Vienna", "Venice", "Vilnius", "Vitebsk", "The Hague", "Havana", "Hamburg", "Kaohsiung", "Guadalajara", "Guatemala", "Gdansk", "Ghent", "Gothenburg", "Jilin", "Glasgow", "Gomel", "Grodno", "Hrodna", "Guangzhou", "Guiyang", "Guayaquil", "Dakar", "Dhaka", "Dacca", "Dallas", "Dalian", "Damascus", "Dar es Salaam", "Delhi", "Jaipur", "Jakarta", "Dnipropetrovsk", "Donetsk", "Dresden", "Dublin", "Douala", "Dushanbe", "Duesseldorf", "Yerevan", "Geneva", "Zhytomyr", "Zagreb", "Zaporizhia", "Jerusalem", "Indore", "Ibadan", "Izmir", "Innsbruck", "Incheon", "Yokohama", "Islamabad", "Esfahan", "Kawasaki", "Cairo", "Santiago de Cali", "Calcutta", "Cannes", "Kanpur", "Caracas", "Karaganda", "Karachi", "Karlovy Vary", "Casablanca", "Kaunas", "Gwangju", "Cologne", "Quezon City", "Kiev", "Kinshasa", "Kyoto", "Quito", "Kishinev", "Klaipeda", "Kobe", "Conakry", "Copenhagen", "Cordoba", "Krakow", "Kuala Lumpur", "Kunming", "Lagos", "Lucknow", "Lanzhou", "Lahore", "Leipzig", "Liverpool", "Lima", "Limassol", "Lyons", "Lisbon", "Lausanne", "London", "Los Angeles", "Luanda", "Lviv", "Luxembourg", "Madrid", "Manaus", "Manila", "Maputo", "Maracaibo", "Marseilles", "Medan", "Medellin", "Melbourne", "Mexico", "Mashhad", "Milan", "Minsk", "Mahilyow", "Montreal", "Montevideo", "Monterrey", "Mumbai", "Munich", "Nagoya", "Nagpur", "Nairobi", "Nanjing", "Nanchang", "Narva", "Naples", "Nicosia", "New York", "Odessa", "Osaka", "Oslo", "Ottawa", "Palembang", "Paris", "Beijing", "Perth", "Poznan", "Porto Alegre", "Potsdam", "Prague", "Pune", "Busan", "Pyongyang", "Recife", "Riga", "Rome", "Rio (de) Janeiro", "Rotterdam", "Salvador", "Samarkand", "San Diego", "Sao Paulo", "San Francisco", "Santo Domingo", "Santiago", "Sapporo", "Sevastopol", "Seoul", "Xi'an", "Sydney", "Simferopol", "Singapore", "Salt Lake City", "Sofia", "Istanbul", "Surabaya", "Surat", "Taipei", "Taiyuan", "Tallinn", "Tangshan", "Tartu", "Tashkent", "Tbilisi", "Tabriz", "Teh(e)ran", "Tel Aviv", "Tiraspol", "Tokyo", "Toronto", "Toulouse", "Daegu", "Taegu", "Daejeon", "Tianjin", "Urumchi", "Utrecht", "Wuhan", "Philadelphia", "Phoenix", "Florence", "Frankfort on the Main", "Frankfort on the Oder", "Fukuoka", "Fushun", "Haifa", "Aleppo", "Hanoi", "Hangzhou", "Harare", "Harbin", "Kharkiv", "Helsinki", "Hiroshima", "Ho Chi Minh", "Houston", "Jinan", "Zibo", "Qingdao", "Qiqihar", "Zurich", "Changchun", "Changsha", "Chicago", "Chittagong", "Chongqing", "Chengdu", "Shanghai", "Shymkent", "Shenyang", "Szczecin", "Eilat", "Eindhoven", "Giza", "Kuwait", "Riyadh", "Jurmala", "Yangon", "Rangoon"]
names = ["Jacob", "Michael", "Joshua", "Matthew", "Ethan", "Andrew", "Daniel", "William", "Joseph", "Christopher", "Anthony", "Ryan", "Nicholas", "David", "Alexander", "Tyler", "James", "John", "Dylan", "Nathan", "Jonathan", "Brandon", "Samuel", "Christian", "Benjamin", "Zachary", "Logan", "Jose", "Noah", "Justin", "Elijah", "Gabriel", "Caleb", "Kevin", "Austin", "Robert", "Thomas", "Connor", "Evan", "Aidan", "Jack", "Luke", "Jordan", "Angel", "Isaiah", "Isaac", "Jason", "Jackson", "Hunter", "Cameron", "Gavin", "Mason", "Aaron", "Juan", "Kyle", "Charles", "Luis", "Adam", "Brian", "Aiden", "Eric", "Jayden", "Alex", "Bryan", "Sean", "Owen", "Lucas", "Nathaniel", "Ian", "Jesus", "Carlos", "Adrian", "Diego", "Julian", "Cole", "Ashton", "Steven", "Jeremiah", "Timothy", "Chase", "Devin", "Seth", "Jaden", "Colin", "Cody", "Landon", "Carter", "Hayden", "Xavier", "Wyatt", "Dominic", "Richard", "Antonio", "Jesse", "Blake", "Sebastian", "Miguel", "Jake", "Alejandro", "Patrick", "Emily", "Emma", "Madison", "Olivia", "Hannah", "Abigail", "Isabella", "Ashley", "Samantha", "Elizabeth", "Alexis", "Sarah", "Grace", "Alyssa", "Sophia", "Lauren", "Brianna", "Kayla", "Natalie", "Anna", "Jessica", "Taylor", "Chloe", "Hailey", "Ava", "Jasmine", "Sydney", "Victoria", "Ella", "Mia", "Morgan", "Julia", "Kaitlyn", "Rachel", "Katherine", "Megan", "Alexandra", "Jennifer", "Destiny", "Allison", "Savannah", "Haley", "Mackenzie", "Brooke", "Maria", "Nicole", "Makayla", "Trinity", "Kylie", "Kaylee", "Paige", "Lily", "Faith", "Zoe", "Stephanie", "Jenna", "Irea", "Riley", "Katelyn", "Angelina", "Kimberly", "Madeline", "Mary", "Leah", "Lillian", "Michelle", "Amia", "Sara", "Sofia", "Jordan", "Alexa", "Rebecca", "Gabrielle", "Caroline", "Vanessa", "Gabriella", "Avery", "Marissa", "Ariana", "Audrey", "Jada", "Autumn", "Evelyn", "Jocelyn", "Maya", "Arianna", "Isabel", "Amber", "Melanie", "Diana", "Danielle", "Sierra", "Leslie", "Aaliyah", "Erin", "Amelia", "Molly", "Claire", "Bailey", "Melissa"]
exeptions = ["sun", "environment", "internet", "French", "English", "Chinese", "Times", "Mayflower", "Guardian", "United States of America", "United Kingdom", "Dominican Republic", "universe", "theatre", "radio", "cinema"]


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input')
    return parser.parse_args()


def crownest(input):
    strInput = str(input)
    if (strInput in cities) or (strInput in names) or (strInput in  exeptions):
        return "Ahoy, Captain, the " + strInput + " off the larboard bow!"
    elif strInput[0] in notLatin:
        return "ERROR: Invalid Input data. Please use only latin alphabet!"
    elif strInput.isalpha():
        if strInput[0] in vowel:
            return "Ahoy, Captain, an " + strInput + " off the larboard bow!"
        else:
            return "Ahoy, Captain, a " + strInput + " off the larboard bow!"
    else: 
        return "ERROR: Invalid Input data. Please use only string!"
        


def main():
    args = get_args()
    print(crownest(args.input)) 


if __name__ == '__main__':
    main()