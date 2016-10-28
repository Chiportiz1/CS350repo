class agent(object):
    def __init__(self, n, l, g, o): # init is global to the class
        self.speech = n
        self.lists = l
        self.name = g
        self.quote = o
    def check(self, speech, series):
        votes = "vot";kind = "plan";topic = "";topic1 = "";count = 0;
        for i in range(len(speech)):
            if speech[i] == "v":
                for j in range(len(votes)):
                    if speech[i+j] == votes[j]:
                        count  += 1
                        if count == 3:
                            if (topic == "vote" or topic == ""):
                                topic = "vote"
                            else:
                                if (topic != "vote" and topic1 == ""):
                                    topic1 = "vote"
            count  = 0
            if speech[i] == "p":
                for k in range(len(kind)):
                    if speech[i+k] == kind[k]:
                        count  += 1
                        if count == 4:
                            if (topic == "plan" or topic == ""):
                                topic = "plan"
                            else:
                                if (topic != "plan" and topic1 == ""):
                                    topic1 = "plan"
            count = 0
        if topic == "":
            print ("Please select one of the topics to discuss.")
            series = [3]
            return series
        else:
            if ((topic == "plan" and topic1 == "vote") or (topic == "vote" and topic1 == "plan")):
                series = [0,1]

            if (topic == "plan" and topic1 == ""):
                series = [2]
            if (topic == "vote" and topic1 == ""):
                series = [1]
            return series
    def what(self, name, quote, lists):
        try:
            lists[1]
            print (name + ": My goal is to "+ quote[lists[0]] +" by " + quote[lists[1]] + ".")
        except:
            if series[0] == 3:
                print ("What??")
            else:
                print (name + ": My plan is to " + quote[lists[0]] + ".")





x = 1;question = 1;
while x == 1:
    while question == 1:
        locas = raw_input("Do you want to  ask an agent questions? (y)es or ((n)o or just anything else). >> ")
        if (locas == "y" or locas == "yes" or locas == "yeah" or locas == "1"):
            print("Alright")
        else:
            x = 0; question = 0;
            break
        who = raw_input("Pick one of the agents, Hillary(1) of Trump(2)? >> ")
        if (who == "Hillary" or who == "hillary" or who == "1"):
            one = "Hillary"
            two = ['supporting womans equality & rights', 'gain the support of parents and business owners', 'try a series of new bills to improve the economy','strong public education is the key to preparing our children for the future' 'improve the quality of education']
        else: 
            one = "Trump"
            two = ['make america great again', 'gain the support of business owners & improve education', 'stop giving other contries our jobs','promises to get rid of Common Core']
        print("We have come with answers to your question about Donald Trump and Hillary Clinton.")
        print("These questions are about United State's 'voters' and 'plans'.")
        test = raw_input("What is your question? (One question at a time plz.) >> ")
        series = []
        t = agent(test, one,two, series)
        t.check(test,series)
        series = t.check(test, series)
        t.what(one, two, series)
