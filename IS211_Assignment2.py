#!/usr/bin/en python
# -*- coding: utf-8 -*-
"""IS211 Assignment2: A simple application for data processing."""

import urllib2
import csv
import datetime
import logging
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--url', help="Enter URL.")
args =  parser.parse_args()
logging.basicConfig(filename='errors.log', level=logging.ERROR)

def downloadData(url):
    """Downloads data from a URL.

    Args:
        url (string): A link for a web address.

    Returns:
        datafile (csv): The data file from the link supplied by the argument.

    Example:
        >>> downloadData('https://s3.amazonaws.com/cuny-is211-spring2015
        /birthdays100.csv')
        <addinfourl at 51039328 whose fp = <socket._fileobject
        object at 0x030A84F0>>
    """
    getfile = urllib2.urlopen(url)
    return getfile


def processData(datafile):
    """A function to process data from downloadData.

    Args:
        datafile (file): Data from downloadData function.

    Returns:
        newdict (dictionary): Retunrs a dictionary of the data from downloadData function.

    Example:
        >>> abc = downloadData('https://s3.amazonaws.com/cuny-is211-spring2015
        /birthdays100.csv')
        >>> processData(abc)
        {'24': ('Stewart Bond', datetime.datetime(2008, 2, 15, 0, 0))
        , '25': ('Colin Turner', datetime.datetime(1994, 6, 6, 0, 0))
        , '26': ('Pippa Glover', datetime.datetime(2001, 8, 15, 0, 0))
    """
    getfile = csv.DictReader(datafile)
    persondict = {}

    for row, line in enumerate(getfile):
        try:
            dob = datetime.datetime.strptime(line['birthday'], '%d/%m/%Y')
            persondict[line['id']] = (line['name'], dob)
        except:
            logger = logging.getLogger('Assignment2')
            logging.error('Error processing line %{} for ID# {}'.format(
                row, line['id']))

    return persondict


def displayPerson(id, personData):
    """A function to print the the data supplied in the URL.

    Args:
        id (int): The ID number associated to the the person.
        personData (str) : The data of the person in the dictionary.

    Returns:
        (str): A string displaying the person and the date of birth.

    Examples:
        >>> csvData = downloadData('https://s3.amazonaws.com/cuny-is211-spring2015
        /birthdays100.csv')
        >>> personData = processData(csvData)
        >>> person_id = 15
        >>> displayPerson(11, personData)
        Person #11 is Angela Watson with a brthday of 1994-04-15
        >>> displayPerson(25, personData)
        Person #25 is Colin Turner with a brthday of 1994-06-06
    """
    id_num = str(id)
    if id_num in personData.keys():
        print 'Person #{} is {} with a brthday of {}.'.format(
            id, personData[id_num][0],
            datetime.datetime.strftime(personData[id_num][1], '%Y-%m-%d'))
    else:
        print 'ID not found.'


def main():
    """A function to download data from URL, process data from CSV file,
    and display associated data in CSV file from the command line.
    """
    if args.url:
        csvData = dowbload(arg.url)
        personData = processData(csvData)
        person_id  = raw_input('Please enter ID Number: ')
        print person_id
        person_id = int(person_id)
        if person_id >= 1:
            displayPerson(person_id, personData)
        else:
            print 'ID number not found. Program closed.'
            sys.exit()
    else:
        print 'Please enter URL with --url parameter.'

if __name__ == '__main__':
    main()
