#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Receives a Bibtex file and produces the markdown files for academic-hugo theme

@author: Petros Aristidou
@contact: p.aristidou@ieee.org
@date: 19-10-2017
@version: alpha
"""

import bibtexparser
import json
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
import os, sys, getopt

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def supetrim(string):
    return string.replace("\\" , "").replace("{" , "").replace("}" , "").replace("\n"," ")


def month_string_to_number(string):
    m = {
        'jan':1,
        'feb':2,
        'mar':3,
        'apr':4,
        'may':5,
        'jun':6,
        'jul':7,
        'aug':8,
        'sep':9,
        'oct':10,
        'nov':11,
        'dec':12
        }
    s = string.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')


# You can add the name of a co-author and their website and it will create a link on the publications website
def get_author_link(string):
    web = {
        'A. Anantha Ramakrishnan':'https://scholar.google.com/citations?user=MzL-WnEAAAAJ&hl=en',
        'S. X Huang':'https://scholar.google.com/citations?user=iTtzc1UAAAAJ&hl=en',
        'D. Lee':'https://scholar.google.com/citations?hl=en',
        }

    out = ''
    try:
        out = web[string]
    except:
        print("Author's "+string+" website is missing.")

    return out

def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:u:", ["ifile="])
    except getopt.GetoptError:
        print('parse_bib.py -i <inputfile> -u <url_array> 1')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('parse_bib.py -i <inputfile> -u <url_array> 2')
            sys.exit()
        elif opt in ("-u"):
            urls_path = arg
        elif opt in ("-i", "--ifile"):
            inputfile = arg
    return inputfile, urls_path


if __name__ == "__main__":
    inputfile, urls_path = main(sys.argv[1:])

    with open(urls_path) as jsonfile:
        urls = json.load(jsonfile)

    try:
        with open(inputfile, encoding="utf8") as bibtex_file:
            bibtex_str = bibtex_file.read()
    except EnvironmentError:  # parent of IOError, OSError *and* WindowsError where available
        print('File '+inputfile+' not found or some other error...')

    # It takes the type of the bibtex entry and maps to a corresponding category of the academic theme
    # Publication type.
    # Legend:
    # 0 = Uncategorized
    # 1 = Conference paper
    # 2 = Journal article
    # 3 = Preprint / Working Paper
    # 4 = Report
    # 5 = Book
    # 6 = Book section
    # 7 = Thesis
    # 8 = Patent
    pubtype_dict = {
        'phdthesis': '"7"',
        'mastersthesis': '"7"',
        'Uncategorized': '"0"',
        'inproceedings': '"1"',
        'conference': '"1"',
        'article': '"2"',
        'submitted': '"3"',
        'techreport': '"4"',
        'book': '"5"',
        'incollection': '"6"',
    }
    
    bib_database = bibtexparser.loads(bibtex_str)
    for entry in bib_database.entries:
        filedir = 'content/publication/'+entry['ID'] 
        if not os.path.exists(filedir):
            os.mkdir(filedir)
        filenm = 'content/publication/'+entry['ID']+'/index.md'
        
        # If the same publication exists, then skip the creation. I customize the .md files later, so I don't want them overwritten. Only new publications are created.
        #if os.path.isfile(filenm):
        #    pass
        #else:
        with open(filenm, 'w', encoding='utf8') as the_file:
            the_file.write('---\n')
            the_file.write('title: "'+supetrim(entry['title'])+'"\n')
            print('Parsing ' + entry['ID'])
            
            if 'year' in entry:
                date = entry['year']
                if 'month' in entry:
                    if RepresentsInt(entry['month']):
                        month = entry['month']
                    else:
                        month = str(month_string_to_number(entry['month']))
                    date = date+'-'+ month.zfill(2)
                else:
                    date = date+'-01'
                the_file.write('date: "'+date+'-01"\n')
                
            # Treating the authors
            if 'author' in entry:
                authors = entry['author'].split(' and ')
                the_file.write('authors:\n')
                authors_str = ''
                for author in authors:
                    author_strip = supetrim(author)
                    author_split = author_strip.split(',')
                    if len(author_split)==2:
                        author_strip = author_split[1].strip() + ' ' +author_split[0].strip()
                    author_split = author_strip.split(' ')
                    author_strip = author_split[0][0]+'. '+' '.join(map(str, author_split[1:]))
                    author_web = get_author_link(author_strip)

                    authors_str = authors_str + "  - " + author_strip + "\n"                        
                    # else:
                    #     authors_str = authors_str+ '"'+author_strip+'",'
                the_file.write(authors_str[:-1]+'\n')
            
            # Treating the keywords
            if 'keywords' in entry:
                the_keywords = entry['keywords'].split(';')
                the_file.write('tags: \n')
                keyword_str = ''
                for keyword in the_keywords:
                    keyword_strip = supetrim(keyword)
                    keyword_str = keyword_str + "- " + keyword_strip.lower() + "\n"
                the_file.write(keyword_str[:-1]+']\n')
            # else:
            #     the_file.write('tags = []\n')
            
            # Treating the publication type
            if 'ENTRYTYPE' in entry:
                if 'booktitle' in entry and ('Seminar' in supetrim(entry['booktitle'])):
                    the_file.write('publication_types: ['+pubtype_dict['conference']+']\n')
                elif 'booktitle' in entry and ('Workshop' in supetrim(entry['booktitle'])):
                    the_file.write('publication_types: ['+pubtype_dict['conference']+']\n')
                elif 'note' in entry and ('review' in supetrim(entry['note'])):
                    the_file.write('publication_types: ['+pubtype_dict['submitted']+']\n')
                elif 'note' in entry and ('Conditional' in supetrim(entry['note'])):
                    the_file.write('publication_types: ['+pubtype_dict['submitted']+']\n')
                else:
                    the_file.write('publication_types: ['+pubtype_dict[entry['ENTRYTYPE']]+']\n')
            
            # Treating the publication journal, conference, etc.
            if 'booktitle' in entry:
                the_file.write('publication:"_'+supetrim(entry['booktitle'])+'_"\n')
            elif 'journal' in entry:
                the_file.write('publication: "_'+supetrim(entry['journal'])+'_"\n')
            elif 'school' in entry:
                the_file.write('publication: "_'+supetrim(entry['school'])+'_"\n')
            elif 'institution' in entry:
                the_file.write('publication: "_'+supetrim(entry['institution'])+'_"\n')
                
            # I never put the short version. In the future I will use a dictionary like the authors to set the acronyms of important conferences and journals
            the_file.write('publication_short: ""\n')
            
            # Add the abstract if it's available in the bibtex
            if 'abstract' in entry:
                the_file.write('abstract: "'+supetrim(entry['abstract'])+'"\n')
            
            # Some features are disabled. I activate them later
            the_file.write('summary: ""\n')
            if 'featured' in entry:
                the_file.write('featured: true\n')
            else:
                the_file.write('featured: false\n')

            if 'projects' in entry:
                the_projects = entry['projects'].split(';')
                the_file.write('projects: [')
                project_str = ''
                for project in the_projects:
                    project_strip = supetrim(project)
                    project_str = project_str+ '"'+project_strip.lower()+'",'
                the_file.write(project_str[:-1]+']\n')
            else:
                the_file.write('projects: []\n')

  
            the_file.write('slides: ""\n')

            # I add urls to the pdf and the DOI
            # the_file.write('url_pdf: "/publication/'+entry['ID']+'/manuscript.pdf"\n')
            # the_file.write('url_pdf: "/publication/'+entry['ID']+'/manuscript.pdf"\n')
            the_file.write('links:\n- name: Arxiv\n  url: ' + urls[entry["ID"]]["arxiv"] + "\n\n")
            the_file.write('url_dataset: ' + urls[entry["ID"]]["dataset"] + '\n')
            if 'doi' in entry:
                the_file.write('doi: "'+supetrim(entry['doi'])+'"\n')
            # the_file.write('url_code: ""\nurl_dataset = ""\nurl_posterxt = ""\nurl_slides = ""\nurl_source = ""\nurl_video = ""\n')
            
            # Default parameters that can be later customized
            the_file.write('math: true\n')
            the_file.write('highlight: true\n')
            # the_file.write('[image]\n')
            # the_file.write('image: ""\n')
            # the_file.write('caption: ""\n')

            
            # I keep in my bibtex file a parameter called award for publications that received an award (e.g., best paper, etc.)
            if 'award' in entry:
                the_file.write('award: "true"\n')
            
            # I put the individual .bib entry to a file with the same name as the .md to create the CITE option
            db = BibDatabase()
            db.entries =[entry]
            writer = BibTexWriter()
            with open('content/publication/'+entry['ID']+'/cite.bib', 'w', encoding='utf8') as bibfile:
                bibfile.write(writer.write(db))

            the_file.write('---\n\n')
            
            # Any notes are copied to the main document
            if 'note' in entry:
                strTemp = supetrim(entry['note'])
                the_file.write(strTemp + "\n")