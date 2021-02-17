from bs4 import BeautifulSoup
import requests

class Main:
  score_page = "https://www.cricbuzz.com/live-cricket-scorecard/32257/ind-vs-eng-2nd-test-england-tour-of-india-2021"

  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}

  page = requests.get(score_page, headers = headers).text
  soup = BeautifulSoup(page, 'html.parser')

  def validate_score_card_url(self):
    if self.score_page.find('/live-cricket-scorecard/') == -1:
      print('please enter valid cricbuzz scorecard url')
      return False
    return True

  def print_match_header(self):
    match_header = self.soup.find('h1', itemprop="name")
    if match_header is not None:
      print(match_header.get_text().split('-')[0])

  def print_match_summary(self):

    score_details = self.soup.findAll('div', {"class":"cb-scrd-hdr-rw"})

    score_details.pop()

    for item in score_details:
      print(item.select('span')[0].get_text(), "-", item.select('span')[1].get_text())

  def print_match_result(self):

    result = self.soup.find('div', {"class": "cb-scrcrd-status"})

    print(result.get_text())


main = Main()

if main.validate_score_card_url():
  main.print_match_header()
  main.print_match_summary()
  main.print_match_result()