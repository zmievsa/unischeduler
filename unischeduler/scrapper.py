import requests
from bs4 import BeautifulSoup

from .util import SchedulerError


def scrap_no_school_events(year, term):
    url = f"https://calendar.ucf.edu/{year}/{term}/no-classes/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    raw_events = soup.find_all("tr", {"class": "vevent"})
    scrapped_events = []
    for event in raw_events:
        dtstart = dtend = description = None
        for elem in event.find_all("abbr"):
            class_ = elem['class'] if isinstance(
                elem['class'], str) else elem['class'][0]
            if class_ == "dtstart":
                dtstart = elem['title']
            elif class_ == "dtend":
                dtend = elem['title']
        raw_description = event.find("div", {"class": "more-details"})
        if raw_description is not None:
            description = raw_description.get_text().strip()
        if dtstart is None:
            # Sometimes it has an event with no dtstart and no dtend.
            # I would check back on it later (UCF Cal -> no-school tag -> Study day)
            continue
        scrapped_events.append(dict(
            summary=event.find("span", {"class": "summary"}).get_text(),
            raw_dtstart=dtstart,
            raw_dtend=dtend
        ))
        if description:
            scrapped_events[-1]['description'] = description
    return scrapped_events
