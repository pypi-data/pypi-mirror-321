import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
from fake_http_header import FakeHttpHeader
import lxml
import html5lib

session = requests.session()

fake_header = FakeHttpHeader()
# Object to create fake randomized headers for web scraping

league_links = {
  "england": "https://fbref.com/en/comps/9/Premier-League-Stats",
  "spain": "https://fbref.com/en/comps/12/La-Liga-Stats",
  "germany": "https://fbref.com/en/comps/20/Bundesliga-Stats",
  "italy": "https://fbref.com/en/comps/11/Serie-A-Stats",
  "france": "https://fbref.com/en/comps/13/Ligue-1-Stats",
  "netherlands": "https://fbref.com/en/comps/23/Eredivisie-Stats",
  "portugal": "https://fbref.com/en/comps/32/Primeira-Liga-Stats",
  "hungary": "https://fbref.com/en/comps/46/NB-I-Stats",
  "russia": "https://fbref.com/en/comps/30/Russian-Premier-League-Stats",
  "turkey": "https://fbref.com/en/comps/26/Super-Lig-Stats",
}
# Dictionnary with links for the supported leagues

# FBRef URLs for different leagues 

class StatStrings:
  """
  Class with strings for each statistic where leaders are available
  """
  goals = "leaders_goals"
  goals_per_90 = "leaders_goals_per90"
  assists = "leaders_assists"
  assists_per_90 = "leaders_assists_per90"
  ga = "leaders_goals_assists"
  ga_per_90 = "leaders_goals_assists_per90"
  pens_created = "leaders_pens_made"
  non_pen_goals = "leaders_goals_pens"
  non_pen_goals_per90 = "leaders_goals_pens_per90"
  non_pen_ga_per90 = "leaders_goals_assists_pens_per90"
  xg = "leaders_xg"
  xg_per_90 = "leaders_xg_per90"
  non_pen_xg = "leaders_npxg"
  non_pen_xg_per_90 = "leaders_npxg_per90"
  xag = "leaders_xg_assist"
  xag_per_90 = "leaders_xg_assist_per90"
  shots = "leaders_shots"
  shots_per_90 = "leaders_shots_per90"
  shots_on_target = "leaders_shots_on_target"
  shots_on_target_per_90 = "leaders_shots_on_target_per90"
  shots_on_target_percent = "leaders_shots_on_target_pct"
  goals_per_shot = "leaders_goals_per_shot"
  goals_per_shot_on_target = "leaders_goals_per_shot_on_target"
  non_pen_xg_per_shot = "leaders_npxg_per_shot"
  goals_xg_comparision = "leaders_xg_net"
  non_pen_goals_npxg_comparision = "leaders_npxg_net"
  key_passes = "leaders_assisted_shots"
  pass_completion_percent = "leaders_passes_pct"
  progressive_passing_distance = "leaders_passes_progressive_distance"
  passes_into_final_third = "leaders_passes_into_final_third"
  passes_into_penalty_area = "leaders_passes_into_penalty_area"
  crosses_into_penalty_area = "leaders_crosses_into_penalty_area"
  progressive_passes = "leaders_progressive_passes"
  through_balls = "leaders_through_balls"
  xa = "leaders_pass_xa"
  xa_per_90 = "leaders_pass_xa_per90"
  corners = "leaders_corner_kicks"
  crosses = "leaders_crosses"
  throw_ins = "leaders_throw_ins"
  shot_creating_actions = "leaders_sca"
  shot_creating_actions_per_90 = "leaders_sca_per90"
  goal_creating_actions = "leaders_gca"
  goal_creating_actions_per_90 = "leaders_gca_per90"
  tackles = "leaders_tackles"
  tackles_won = "leaders_tackles_won"
  dribblers_tackled = "leaders_challenge_tackles"
  dribblers_tackled_percent = "leaders_challenge_tackles_pct"
  blocks = "leaders_blocks"
  interceptions = "leaders_interceptions"
  clearances = "leaders_clearances"
  touches = "leaders_touches"
  successful_take_ons = "leaders_take_ons_won"
  successful_take_ons_percent = "leaders_take_ons_won_pct"
  progressive_carrying_distance = "leaders_carries_progressive_distance"
  progressive_carries = "leaders_progressive_carries"
  carries_into_penalty_area = "leaders_carries_into_penalty_area"
  progressive_passes_recieved = "leaders_progressive_passes_recieved"

  minutes = "leaders_minutes" ####### Special case as usually many players have equal minutes

  sub_appearances = "leaders_games_subs"
  points_per_game = "leaders_points_per_game"
  plus_minus = "leaders_plus_minus"
  plus_minus_per_90 = "leaders_plus_minus_per90"
  xg_plus_minus = "leaders_xg_plus_minus"
  xg_plus_minus_per_90 = "leaders_xg_plus_minus_per90"
  yellow_cards = "leaders_cards_yellow"
  red_cards = "leaders_cards_red"
  aerials_won = "leaders_aerials_won"
  aerials_won_percent = "leaders_aerials_won_pct"
  fouls_commited = "leaders_fouls"
  fouls_drawn = "leaders_fouled"
  own_goals = "leaders_own_goals"
  clean_sheets = "leaders_gk_clean_sheets"
  clean_sheets_percent = "leaders_gk_clean_sheets_pct"
  saves = "leaders_gk_saves"
  save_percentage = "leaders_gk_save_pct"
  goals_against_per_90 = "leaders_gk_goals_against_per90"
  psxg_ga_comparision = "leaders_gk_psxg_net"
  psxg_ga_comparision_per_90 = "leaders_gk_psxg_net_per90"


class LeagueScraper:
  """
  A class for scraping data from different leagues on FBRef
  Instantiate a LeagueScraper by passing the country name of the league you wish to scrape into the 'league' argument.
  """

  def __init__(self, league):
    self.league = league

    try:
      self.url = league_links[league]
    except:
      raise ValueError(f"Invalid league: {league}")

    response = session.get(self.url, headers=fake_header.as_header_dict())
    # gets the raw HTML from self.url

    splitter = '<!-- 	<div class="data_grid" id="div_leaders" data-entry-type="Leaderboards">'
    # splits the raw HTML after a specific comment so that the code can read a commented-out section which includes league leaders in different stats
    #print(splitter in response.text) # Prints the split HTML, used for testing when the splitting isn't working
    leader_tables_html = response.text.split(splitter)[1]
    # this variable stores the SECOND PART (hence the [1]) of the split text so BeautifulSoup doesn't see that it's a comment

    # two BeautifulSoup objects. self.soup for the main tables, and self.leaders_soup for the league leaders in different stats
    self.soup = BeautifulSoup(response.text, "html.parser")
    self.leaders_soup = BeautifulSoup(leader_tables_html, "html.parser")

  def getLeagueLeaders(self, stat_id):
    """
    Returns a list containing league leader(s) in the category specified by stat_id, as well as the value of the statistic
    """
    if (stat_id == StatStrings.minutes): # Minute leaders
      playerRows = self.leaders_soup.find("div", id=stat_id).findAll("tr") # Returns all the rows

      highestMinutes = playerRows[0].find("td", {"class":"value"}).text.split(" ")[1]
      # Gets the minute value of the first row in the table

      leaders = [] # Creates the leaders list to return to the user

      for i in playerRows: # Loops through all the rows
        if i.find("td", {"class": "value"}).text == " " + highestMinutes:
          leaders.append(i.find("td", {"class": "who"}).find("a").text)

        # if the current row's minute value is the same as highestMinutes:
        # append the player name to the leaders list

      leaders.append(int(highestMinutes))

    else: # Any stat other than minutes
      firstPlacePlayersRows = self.leaders_soup.find("div", id=stat_id).findAll("tr",{"class":"first_place"})
      # Scrapes the table rows with the class "first_place" (as there may be more than one)
      leaders = [i.find("td", {"class":"who"}).find("a").text for i in firstPlacePlayersRows]
      # Scrapes the player names from each entry in firstPlacePlayers
      leaderValue = float(firstPlacePlayersRows[0].find("td", {"class": "value"}).text)
      # Scrapes the amount of of the stat value by the top keeper(s)
      leaders.append(leaderValue)
      # Appends the leaderValue to leaders[] so that it can be returned to the user

    return leaders

  def getTeams(self):
    """
    Returns a list containing strings of all the names of the teams in the league, in alphabetical order
    """
    table = self.soup.findAll('table')[2] # 3rd table on the website
    league_rows = table.find('tbody').findAll('tr') # Finds all rows
    teams = [team.find('th', {'data-stat':'team'}).find('a').text for team in league_rows] # Adds the teams to the teams list

    return teams

  def getLeagueTable(self):
    """
    Returns a pandas dataframe of the league table
    """

    league_table = self.soup.findAll('table')[0] # Gets the league table HTML
    pandas_table = pd.read_html(StringIO(str(league_table)))[0] # Reads the HTML table as a pandas dataframe
    return pandas_table

  def getSquadStats(self):
    """
    Returns a pandas dataframe of the squad stats
    """

    squad_stats = self.soup.findAll('table')[2] # Gets the squad stats HTML
    pandas_table = pd.read_html(StringIO(str(squad_stats)))[0] # Reads the HTML table as a pandas dataframe
    return pandas_table


class GeneralScraper:
  """
  A GENERAL Scraper, not tied to any specific league. All methods in this class are static.
  """

  @staticmethod
  def getPlayerLink(inputted_player_name):
    """
    Returns a list with the stats page for the player inputted.
    If more than one player has that name, it will return all their links in a list.
    """
    returned_players = []

    player_name_list = inputted_player_name.split(" ")

    searchbar_link = "https://fbref.com/en/search/search.fcgi?search="
    for i in player_name_list:
        searchbar_link += i + "+"
    # This is the search URL that will be scraped to find the player page

    search_html = session.get(searchbar_link, headers=fake_header.as_header_dict())
    search_soup = BeautifulSoup(search_html.text, "html.parser")
    # returns HTML of the search bar page
    
    try:
      search_h3 = search_soup.find('h3').text
      # The first h3 tag on the website
    except:
      raise ValueError("Input unable to be processed") from None
      # Error if the h3 cannot be found

    if (search_h3 == "About FBref.com"):
      # The player has been found and we're on his page. Now we need the URL
      player_link = "https://fbref.com" + search_soup.find('div', {'id': 'bottom_nav_container'}).find('a')['href']
      # Finds a div (id: bottom_nav_container) and finds the first link inside it, which contains a link back to the same page we're on (for some reason). We can use this to find the URL of our player and return it in our function
      returned_players.append(player_link)

    elif (search_h3 == 'Players from Leagues Covered by FBref.'):
      # If the search returns more than one player
      player_divs = search_soup.findAll('div', {'class': 'search-item-name'})
      # finds all the players
      for i in player_divs:
        returned_players.append("https://fbref.com" + i.find('a')['href'])

    else:
      print("Input unable to be processed")

    return returned_players

  @staticmethod
  def getPlayerPosition(player_link):
    """Returns a string of the position(s) of the player whose URL is in the player_link argument"""

    player_html = session.get(player_link, headers=fake_header.as_header_dict())
    player_soup = BeautifulSoup(player_html.text, "html.parser")
    # Scrapes the player_link URL
    
    try:
      position_text = player_soup.find(text='Position:').parent.parent
      # Finds the "position" text on the page, and
      # gets its parent (the <strong> tag) and the parent of that (the <p> tag)
    
    except:
      return "N/A"
      # Error if the position text cannot be found

    position_text = position_text.text.split("\xa0▪\xa0 ")[0]
    # Splits the text into a list, and gets the first item in the list (the position)
    position_text = position_text.split("Position: ")[1]
    # Removes the "Position: " text
    
    return position_text

  @staticmethod
  def getPlayerFootedness(player_link):
    """Returns a string of the footedness of the player whose URL is in the player_link argument"""

    player_html = session.get(player_link, headers=fake_header.as_header_dict())
    player_soup = BeautifulSoup(player_html.text, "html.parser")
    # Scrapes the player_link URL

    try:
      footedness_text = player_soup.find(text='Footed:').parent.parent
      # Finds the "position" text on the page, and
      # gets its parent (the <strong> tag) and the parent of that (the <p> tag)

    except:
      return "N/A"
      # Error if the position text cannot be found

    footedness_text = footedness_text.text.split("\xa0▪\xa0 ")[1]
    # Splits the text into a list, and gets the second item in the list (the footedness)
    footedness_text = footedness_text.split("Footed: ")[1]
    # Removes the "Footed: " text
    return footedness_text
  
  @staticmethod
  def getPlayerClub(player_link):
    """Returns a string the club of the player whose URL is in the player_link argument"""

    player_html = session.get(player_link, headers=fake_header.as_header_dict())
    player_soup = BeautifulSoup(player_html.text, "html.parser")
    # Scrapes the player_link URL

    try:
      club_text = player_soup.find(text='Club:').parent.parent.find('a').text
      # Finds the "Club:" text on the page, and
      # gets its parent (the <strong> tag) and the parent of that (the <p> tag)
      # then gets its child which is a link (the club) and gets its text

    except:
      return "N/A"
      # Error if the club text cannot be found  

    return club_text

  @staticmethod
  def getPlayerNationalTeam(player_link):
    """Returns a list containing the national team(s) or citizenship of the player whose URL is in the player_link argument"""

    player_html = session.get(player_link)
    player_soup = BeautifulSoup(player_html.text, "html.parser")
    # Scrapes the player_link URL

    try: # If the player has listed NATIONAL TEAM(S)
      player_stat_paragraph = player_soup.find(string='National Team:').parent.parent
      # Finds the "National Team:" text on the page, and
      # gets its parent (the <strong> tag) and the parent of that (the <p> tag)
      nation_links = player_stat_paragraph.findAll('a')
      for i in range(len(nation_links)): nation_links[i] = nation_links[i].text
      # Finds all the links under this paragraph, which is/are the national team(s) the player represents
      # It then loops through the list and gets only the text from the <a> tags

      return nation_links
      # Returns the list containing the NATIONAL TEAMS of the player
    
    except: # If the player has listed CITIZENSHIP(S) instead of NATIONAL TEAM(S)
      player_stat_paragraph = player_soup.find(string='Citizenship:').parent.parent
      # Finds the "Citizenship:" text on the page, and
      # gets its parent (the <strong> tag) and the parent of that (the <p> tag)
      citizenship_links = player_stat_paragraph.findAll('a')
      for i in range(len(citizenship_links)): citizenship_links[i] = citizenship_links[i].text
      # Finds all the links under this paragraph, which is/are the national team(s) the player represents
      # It then loops through the list and gets only the text from the <a> tags

      return citizenship_links
      # Returns the list containing the CITIZENSHIP of the player

  @staticmethod
  def getPlayerAwards(player_link):
    """Returns a list containing the award(s) of the player whose URL is in the player_link argument"""

    player_html = session.get(player_link)
    player_soup = BeautifulSoup(player_html.text, "html.parser")
    # Scrapes the player_link URL

    try:
      awards_text = player_soup.find("ul", id="bling").findAll("li")
      # Finds the <ul> with ID "bling" and gets all the <li> tags within it
      for i in range(len(awards_text)): awards_text[i] = awards_text[i].find('a').text
      # Loops through the <li> tags and finds the text within the children of the <li> tags, which are <a> tags

    except:
      return "N/A"
      # Error if the awards cannot be found

    return awards_text

  @staticmethod
  def getSimilarPlayers(player_link):
    """Returns a dictionary containing one or more pandas dataframes of similar players to player_link."""

    # We can use the id similar_ then the position, so GK, CB, FB, MF, AM, FW

    player_html = session.get(player_link)
    player_soup = BeautifulSoup(player_html.text, "html.parser")
    # Scrapes the player_link URL

    try:
      similar_tables = {
        "GK": player_soup.find("table", id="similar_GK"), # Gets the goalkeeper table, and reads it as a pandas dataframe
        "CB": player_soup.find("table", id="similar_CB"), # Gets the centreback table, and reads it as a pandas dataframe
        "FB": player_soup.find("table", id="similar_FB"), # Gets the fullback table, and reads it as a pandas dataframe
        "MF": player_soup.find("table", id="similar_MF"), # Gets the midfielder table, and reads it as a pandas dataframe
        "AM": player_soup.find("table", id="similar_AM"), # Gets the att. midfielder table, and reads it as a pandas dataframe
        "FW": player_soup.find("table", id="similar_FW"), # Gets the forward table, and reads it as a pandas dataframe
      }
      # Dictionary containing scraped tables of the Similar Players table for all the positions
      # If the table exists on the website, it is stored in the value associated with its position key
      # If no table is found, the value will be None

      output_dict = {} # Initializes output dictionary
      
      for key in similar_tables: # Iterates through the dictionary
        if similar_tables[key] != None: # If the dictionary entry is NOT equal to None
          output_dict[key] = pd.read_html(StringIO(str(similar_tables[key])))[0] # Add the key and its value in a pandas dataframe to the ouput dict.
      
      return output_dict # Returns the dataframe
      
    except:
      return "N/A" # Returns N/A if the dataframe is not found, or if an error occurs

  @staticmethod
  def getScoutingReport(player_link):
    """Returns a dictionary containing one or more pandas dataframes of the scouting report of player_link."""

    # We can use the id scout_summary_ then the position, so GK, CB, FB, MF, AM, FW

    player_html = session.get(player_link)
    player_soup = BeautifulSoup(player_html.text, "html.parser")
    # Scrapes the player_link URL

    try:
      similar_tables = {
        "GK": player_soup.find("table", id="scout_summary_GK"), # Gets the goalkeeper table, and reads it as a pandas dataframe
        "CB": player_soup.find("table", id="scout_summary_CB"), # Gets the centreback table, and reads it as a pandas dataframe
        "FB": player_soup.find("table", id="scout_summary_FB"), # Gets the fullback table, and reads it as a pandas dataframe
        "MF": player_soup.find("table", id="scout_summary_MF"), # Gets the midfielder table, and reads it as a pandas dataframe
        "AM": player_soup.find("table", id="scout_summary_AM"), # Gets the att. midfielder table, and reads it as a pandas dataframe
        "FW": player_soup.find("table", id="scout_summary_FW"), # Gets the forward table, and reads it as a pandas dataframe
      }
      # Dictionary containing scraped tables of the Scout Summary table for all the positions
      # If the table exists on the website, it is stored in the value associated with its position key
      # If no table is found, the value will be None

      output_dict = {} # Initializes output dictionary
      
      for key in similar_tables: # Iterates through the dictionary
        if similar_tables[key] != None: # If the dictionary entry is NOT equal to None
          output_dict[key] = pd.read_html(StringIO(str(similar_tables[key])))[0] # Add the key and its value in a pandas dataframe to the ouput dict.
      
      return output_dict # Returns the dictionary
      
    except:
      return "N/A" # Returns N/A if the dataframe is not found, or if an error occurs
