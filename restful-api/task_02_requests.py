import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()

        for post in data:
            print(post["title"])


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Convert into required format
        posts = []
        for post in data:
            posts.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        # Write to CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts)
