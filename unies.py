import requests
from bs4 import BeautifulSoup

def get_top_universities():
    url = "https://www.topuniversities.com/university-rankings/university-subject-rankings/2022/computer-science-information-systems"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        universities = []
        for row in soup.select("div.rankingsData"):
            university = row.select_one("div.uniTitle > a").text.strip()
            rank = row.select_one("div.rank").text.strip()
            universities.append({"Rank": rank, "University": university})
        return universities
    else:
        print("Failed to fetch data from the website.")
        return None

if __name__ == "__main__":
    top_universities = get_top_universities()
    if top_universities:
        print("Top Universities for MS in Computer Science:")
        for uni in top_universities:
            print(f"{uni['Rank']}. {uni['University']}")
    else:
        print("No data available.")
