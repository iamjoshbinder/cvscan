#!/usr/bin/env python
"""

Utility functions that uses language processing to extract useful information

"""
import pickle
import logging
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import dirpath

logging.basicConfig(level=logging.DEBUG)

__author__ = 'lakshmanaram'
__license__ = 'http://opensource.org/licenses/MIT'
__email__ = 'lakshmanaram.n@gmail.com'
__maintainer__ = 'lakshmanaram'


"""

Utility function that cleans the resume_text.
Params: resume_text type: string
returns: cleaned text ready for processing

"""
def clean_resume(resume_text):

  cleaned_resume = []

  # replacing newlines and punctuations with space
  resume_text =resume_text.replace('\t',' ').replace('\n',' ').replace('.',' ')
  resume_text = resume_text.replace(',',' ').replace('/',' ').replace('(',' ')
  resume_text = resume_text.replace(')',' ').replace('|',' ').replace('!',' ')
  resume_text = resume_text.split()

  # removing stop words and Stemming the remaining words in the resume
  stemmer = SnowballStemmer("english")
  for word in resume_text:
    if word not in stopwords.words('english') and not word.isdigit():
      cleaned_resume.append(word.lower())#stemmer.stem(word))
          
  cleaned_resume = ' '.join(cleaned_resume)
  return cleaned_resume


"""

Utility function that fetches the skills from resume
Params: cleaned_resume Type: string
returns: skill_set Type: List

"""
def fetch_skills(cleaned_resume):
  with open(dirpath.PKGPATH + '/data/skills/skills','rb') as fp:
    skills = pickle.load(fp)

  skill_set = []
  for skill in skills:
    # stem_skill = skill.split()
    # for word in skill:
    #   stem_skill.append(stemmer.stem(word))
    # stem_skill = ' '.join(stem_skill)
    skill = ' '+skill+' '
    if skill.lower() in cleaned_resume:
      skill_set.append(skill)
  return skill_set


"""

Utility function that fetches the current employer from resume
Params: resume_text Type: string
returns: current_employer Type: string

"""
def fetch_emplyer(resume_text, job_positions):
  organizations = []
  # get all organizations in the resume_text
  # if any of this organization is beside a job position, assume it as an emplyer
  
  return current_employer


"""

Utility function that fetches the Person Name from resume
Params: resume_text Type: string
returns: name Type: string

Returns the first Person entity found by tokenizing each sentence
If no such entities are found, returns "Applicant name couldn't be processed"

"""
def fetch_name(resume_text):
  tokenized_sentences = nltk.sent_tokenize(resume_text)

  for sentence in tokenized_sentences:
    for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentence), tagset='universal')):
      if hasattr(chunk,'label'):# and chunk.label() == 'PERSON':
        chunk = chunk[0]  
      (name,tag) = chunk
      if tag == 'NOUN':
        return name

  return "Applicant name couldn't be processed"