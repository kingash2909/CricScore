import requests
from datetime import datetime
class ScoreGet():
    def __init__(self):
        """
        Declaring the endpoints, apikey
        """
        self.url_get_all_matches = "http://cricapi.com/api/matches"
        self.url_get_score="http://cricapi.com/api/cricketScore"
        self.api_key = "gxwN6bPkAZN4AzBbuGEWREgco5r2"
        self.unique_id = ""  # unique to every match

    def get_unique_id(self):
        """
        Returns Indian cricket teams match id, if the match is Live
        :return:
        """
        uri_params = {"apikey": self.api_key}
        resp = requests.get(self.url_get_all_matches, params=uri_params)
        resp_dict = resp.json()
        uid_found=0
        for i in resp_dict['matches']:
            if (i['team-1'] == "India" or i['team-2'] == "India") and i['matchStarted']:
                todays_date = datetime.today().strftime('%Y-%m-%d')
                todays_date = "2020-02-12"
                if todays_date == i['date'].split("T")[0]:
                    uid_found=1
                    self.unique_id=i['unique_id']
                    # print(self.unique_id)
                    break
        if not uid_found:
            self.unique_id=-1

        send_data=self.get_score(self.unique_id)
        return send_data
    def get_score(self,unique_id):
        data="" #stores the cricket match data
        if unique_id == -1:
            data="No matches today"
        else:
            uri_params = {"apikey": self.api_key, "unique_id": self.unique_id}
            resp=requests.get(self.url_get_score,params=uri_params)
            data_json=resp.json()
            #print(data_json)
            try:
                data="Here's the score : "+ "\n" + data_json['stat'] +'\n' + data_json['score']
            except KeyError as e:
                data="Something went wrong"
        return data



if __name__ == "__main__":
    match_obj=ScoreGet()
    send_message=match_obj.get_unique_id()
    print(send_message)

    from twilio.rest import Client
    account_sid = 'ACfea9d74ba9a6da7f1ba912307d5b47f0'
    auth_token = '79e2d72e5daee15124ef9b5f8021f4e5'
    client = Client(account_sid, auth_token)

    def msg():
        message = client.messages.create(
            body=send_message,
            from_='whatsapp:+14155238886',
            to='whatsapp:+917303019154'
        )

        print(message.sid)
    a=msg()
