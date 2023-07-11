import requests


def top():
    response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")
    dic = response.json()
    print(dic)

    numbers_data = []  # 箱の中は空ですよ～
    for number in range(0, 10):
        numbers_data.append(dic[number])  # numbers_data[]という空の箱にnumberをappend(足す)していく
        # print(numbers_data)

    for num in numbers_data:  # ナンバーズデータに10個入っているナンバーを一つずつ取り出す
        response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{num}.json?print=pretty")
        # print(num)
        # タイトルとURLを抜き取る
        dic = response.json()
        title = dic["title"]
        link = dic["url"]

        print(f"'title':{title}, 'link':{link}")


if __name__ == "__main__":
    top()
