import pandas as pd
from bs4 import BeautifulSoup
from requests import get

#takes in title name (cleaned); saves word count csv
def word_count_table(transcript_title, season_num, episode_num): #for paired episodes, `episode_num` will be the number for the first of the two episodes
    url = 'https://lostpedia.fandom.com/wiki/'+transcript_title+'_transcript'
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    containers = html_soup.find_all('div', 'mw-body-content mw-content-ltr')
    transcript = containers[0].text.split('Contents')[1]

    dialogue_transcript = transcript.replace(']','[').split('[') #list of things outside of stage directions
    for substring in dialogue_transcript:
        if substring[:15].split(':')[0]!=substring[:15].split(':')[0].upper() and substring[:8]!='Subtitle':
            dialogue_transcript.remove(substring)
    dialogue_transcript = list(filter(None, "".join(dialogue_transcript).split('\n')))

    english_transcript = []
    for dialogue in dialogue_transcript:
        if dialogue.count(':')>1 and 'Subtitle:' not in dialogue:
            dialogue = dialogue[::-1].replace(':','',dialogue.count(':')-1)[::-1] # keep only first colon in a dialogue
        if ':' not in dialogue: #ignore lines with no colons (e.g., "Act 2"), or scraps from dialogue with accidental return carriages in them
            continue
        elif "Subtitle:" in dialogue:
            if dialogue.count(':')==1:
                continue
            else:
                english_transcript.append(dialogue.split(': ')[0]+':'+dialogue.split(':')[2])
        elif not dialogue.replace('\u2026','').replace('\u2014','').isascii(): #if non-english characters are detected (other than ellipsis and em-dashes)
            if '(' not in dialogue:
                continue
            elif not dialogue.split('(')[0].isascii(): # if the parentheses included are acting as subtitles 
                english_transcript.append(dialogue.split(':')[0]+': '+dialogue.split('(')[1][:-1])
            #otherwise the parentheses are acting as stage directions, and we choose to allow them in the word count to make my life easier    
        else:
            english_transcript.append(dialogue)

    character_names = [dialogue.split(':')[0].strip() for dialogue in english_transcript]
    character_lines = [dialogue.split(':')[1] for dialogue in english_transcript]
    character_wordcounts = [len(line.split(' ')) for line in character_lines]
    df = pd.DataFrame({'Character':character_names, 'Word Count':character_wordcounts})
    df = df.groupby('Character')['Word Count'].sum().reset_index()

    csv_filename = 'S'+str(season_num)+'E'+str(episode_num)+'.csv'
    folder_name = 'Season '+str(season_num)+'/'
    df.to_csv('./Word Count Tables/' + folder_name + csv_filename, index=False)