import numpy as np
from bs4 import BeautifulSoup
import urllib
import pandas as pd

myurl = "http://www.hsquizbowl.org/db/tournaments/5076/stats/all_games_%28w_packet_names%29/teamdetail/"
page = urllib.request.urlopen(myurl)
#get the html page
soup = BeautifulSoup(page,'html.parser')
#example of getting team names from html
teamnames = [list(x.stripped_strings)[0] for x in soup.find_all('h2')[1:]]
#get the numerical stats, and pair them with team names
rawtabs = pd.read_html(myurl,header=0)
teamstats = [rawtabs[i] for i in np.arange(0,len(teamnames*2),2)+1]
teamstats_dict = dict(zip(teamnames,teamstats))
#example of getting a single stat (PPB for each game, for each team)
team_ppb = dict(zip(teamnames, [teamstats_dict[namei]['P/B'][:-1] for namei in teamnames]))
