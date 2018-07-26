# Simple script used to turn report list from twiki into markdown.
# Input taken from all-reports.twiki
#
# Arie van Deursen, July 2018.

import re

def wikiURL(text):
	text = re.sub(r'\[\[(.*?/.*?)\]\[(.*?)\]\]', r'[\2](\1)', text)
	text = re.sub(r'%ATTACHURL%/', 'http://swerl.tudelft.nl/twiki/pub/Main/TechnicalReports/', text)
	return text

def wikiWord(text):
	text1 = re.sub(r'\[\[([\w\s]+)\]\]', r'\1', text)
	text2 = re.sub(r'\[\[([\w\.\s]+)\]\[(.*?)\]\]', r'\2', text1)
	return text2

def doEntry(line):
	entryPattern = re.compile(r'\|(.*TUD-SERG.*)\|(.*)\|(.*)\|(.*)\|')
	entryMatch = entryPattern.match(line)
	if entryMatch:
		report = wikiURL(entryMatch.group(1))
		authors = wikiURL(wikiWord(entryMatch.group(2)))
		title = wikiURL(entryMatch.group(3))
		venue = wikiURL(wikiWord(entryMatch.group(4)))
		print('{0}|{1}|{2}|{3}'.format(report, authors, title, venue))

def header():
	print("Report Number | Author(s) | Title | Venue\n---|---|---|---")

def main():
	header()
	with open('all-reports.twiki') as wiki:
		for line in wiki:
			doEntry(line)

main()