class Influencer:
    def __init__(self,name,followers,earnings):
        self.name = name
        self.followers = followers
        self.earnings = earnings
    def post_content(self):
        print(f"{self.name} posted content.")
    def __update_earnings(self,amount):
        self.earnings += amount
    def getinfo(self):
        print(self.__str__())
    def __str__(self):
        return f'''Influencer Profile: {self.name}
Followers: {self.followers}
Earnings: P{self.earnings:.2f}'''
class InfluencerWithAds(Influencer):
    def __init__(self,name,followers,earnings):
        super().__init__(name,followers,earnings)
        self.ads_created = 0
    def create_ad(self):
        earned = 5000
        self.ads_created += 1
        self._Influencer__update_earnings(earned)
        print(f'''{self.name} Creates an ad! Earnings increase by {earned}
{self.name}'s Total earnings after ad creation: P{self.earnings}''')
Alice = Influencer("Alice", 100000,2000)
Zoe = InfluencerWithAds("Zoe",300000, 25000)
Alice.post_content()
Zoe.post_content()
Zoe.create_ad()
Zoe.getinfo()