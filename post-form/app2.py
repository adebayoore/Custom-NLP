from flask import Flask, render_template, url_for, request
import re
import pandas as pd
import spacy
from spacy import displacy
from spacy.pipeline import EntityRuler
import en_core_web_sm
import json
from flask_cors import CORS
import sys
from dateutil.parser import parse

job_title_nlp = spacy.load('en_core_web_sm')
skills_other_nlp = spacy.load('en_core_web_sm')

rulerTitle = EntityRuler(job_title_nlp, overwrite_ents=True).from_disk("./Title.jsonl")
rulerTitle.name = 'rulerTitle'
job_title_nlp.add_pipe(rulerTitle)

rulerSkills = EntityRuler(skills_other_nlp, overwrite_ents=True).from_disk("./skillPattern.jsonl")
rulerSkills.name = 'rulerSkills'
skills_other_nlp.add_pipe(rulerSkills)

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "App Working"

@app.route('/process', methods=["POST"])
def process():
    if request.method == 'POST':
        try:
            rawtext = request.form['rawtext']
            job_title_doc = job_title_nlp(rawtext.lower())
            skills_other_doc = skills_other_nlp(rawtext.lower())
            custom_named_entities = [(entity.text, entity.label_)
                                    for entity in job_title_doc.ents]
            custom_named_entities_skills_other_info = [(entity.text, entity.label_)
                                     for entity in skills_other_doc.ents]
            titleDict = {v: k for k, v in dict(custom_named_entities).items()}
            result = dict(custom_named_entities_skills_other_info)
            result.update({titleDict['TITLE']: 'TITLE'})
            dateSpan = ''
            typeDate = ''
            targetOpenings = ''
            titlePos = ''
            Location = ''
            for index,  token in enumerate(skills_other_doc.ents):
                try:
                    if token.label_ == "CARDINAL":
                        allText = [t.text for t in skills_other_doc]
                        textIndex = allText.index(
                            str(skills_other_doc.ents[index].text.split(" ")[-1]))
                        numSpan = str(skills_other_doc.ents[index])
                        wordsBefore = allText[textIndex - 1]
                        wordsAfter = allText[textIndex + 1]
                        if (wordsBefore == "openings" or wordsBefore == "positions"
                            or wordsBefore == "position" or wordsAfter == "positions"
                                or wordsAfter == "openings" or wordsAfter == "position"):
                            result.update(
                                {str(numSpan): str("targetOpenings")})

                    if token.label_ == "DATE":
                        allText = [t.text for t in skills_other_doc]
                        textIndex = allText.index(
                            str(skills_other_doc.ents[index].text.split(" ")[-1]))
                        dateSpan = str(skills_other_doc.ents[index])
                        sp_len = len(skills_other_doc.ents[index].text.split(" "))
                        wordsBefore = allText[textIndex - sp_len]

                        
                        if (wordsBefore == "for" or wordsBefore == "to" or wordsBefore == "until") and "months" in dateSpan:
                            typeDate = "duration"
                        elif wordsBefore == "from" or wordsBefore == "on" or wordsBefore == "starting" or wordsBefore == "the":
                            typeDate = "startDate"
                        if (typeDate == "duration"):
                            result.update({str(dateSpan): str(typeDate)})
                        if (typeDate == "startDate"):
                            dt = parse(dateSpan)
                            result.update({str(dt.date()): str(typeDate)})
                except:
                    print('Exception', sys.exc_info())
                    
            # Mutation for finding the target Openings
            for ent in job_title_doc.ents:
                try:
                    if ent.label_ == "TITLE":
                        titlePos = ent.start_char
                    for ent in job_title_doc.ents:
                        try:
                            if ent.label_ == "CARDINAL" and ent.end_char < (titlePos):
                                targetOpenings = ent.text
                        except:
                            pass
                except:
                    print('Exception for job title')
            # Location Entity Mapping
            for ent in skills_other_doc.ents:
                try:
                    if ent.label_ == "LOC" or ent.label_ == "GPE":
                        Location = ent.text
                except:
                    print('Exception for the location')
            result.update({str(targetOpenings): str("targetOpenings")})
            result.update({str(Location): str("Location")})
            return result
            console.log(custom_named_entities)
        except:
            print('no result', sys.exc_info())
            return ''

if __name__ == '__main__':
    app.run(debug=True)