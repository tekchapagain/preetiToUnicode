# -*- coding: utf-8 -*-
import argparse
import os
import sys

unicodeatoz=["ब","द","अ","म","भ","ा","न","ज","ष्","व","प","ि","फ","ल","य","उ","त्र","च","क","त","ग","ख","ध","ह","थ","श"]
unicodeAtoZ=["ब्","ध","ऋ","म्","भ्","ँ","न्","ज्","क्ष्","व्","प्","ी","ः","ल्","इ","ए","त्त","च्","क्","त्","ग्","ख्","ध्","ह्","थ्","श्"]
unicode0to9=["ण्","ज्ञ","द्द","घ","द्ध","छ","ट","ठ","ड","ढ"]
symbolsDict=\
{
    "~":"ञ्",
    "`":"ञ",
    "!":"१",
    "@":"२",
    "#":"३",
    "$":"४",
    "%":"५",
    "^":"६",
    "&":"७",
    "*":"८",
    "(":"९",
    ")":"०",
    "-":"(",
    "_":")",
    "+":"ं",
    "[":"ृ",
    "{":"र्",
    "]":"े",
    "}":"ै",
    "\\":"्",
    "|":"्र",
    ";":"स",
    ":":"स्",
    "'":"ु",
    "\"":"ू",
    ",":",",
    "<":"?",
    ".":"।",
    ">":"श्र",
    "/":"र",
    "?":"रु",
    "=":".",
    "ˆ":"फ्",
    "Î":"ङ्ख",
    "å":"द्व",
    "÷":"/"
}


def normalizePreeti(preetitext):
    normalized=''
    previoussymbol=''
    preetitxt=preetitext.replace('qm','s|')
    preetitxt=preetitext.replace('f]','ो')
    preetitxt=preetitext.replace('km','फ')
    preetitxt=preetitext.replace('0f','ण')
    preetitxt=preetitext.replace('If','क्ष')
    preetitxt=preetitext.replace('if','ष')
    preetitxt=preetitext.replace('cf','आ')
    index=-1
    while index+1 < len(preetitext):
        index+=1
        character=preetitext[index]
        try:
            if preetitxt[index+2] == '{':
                if preetitext[index+1] == 'f' or preetitext[index+1] == 'ो':
                    normalized+='{'+character+preetitext[index+1]
                    index+=2
                    continue
            if preetitext[index+1] == '{':
                if character!='f':
                    normalized+='{'+character
                    index+=1
                    continue
        except IndexError:
            pass
        if character=='l':
            previoussymbol='l'
            continue
        else:
            normalized+=character+previoussymbol
            previoussymbol=''
    return normalized

def convert(inputfile):
    preeti = inputfile

    converted=''
    normalizedpreeti=normalizePreeti(preeti)
    for index, character in enumerate(normalizedpreeti):
        try:
            if ord(character) >= 97 and ord(character) <= 122:
                converted+=unicodeatoz[ord(character)-97]
            elif ord(character) >= 65 and ord(character) <= 90:
                converted+=unicodeAtoZ[ord(character)-65]
            elif ord(character) >= 48 and ord(character) <= 57:
                converted+=unicode0to9[ord(character)-48]
            else:
                converted+=symbolsDict[character]
        except KeyError:
            converted+=character

    return converted

inputword = input("Enter The Word To Convert To Unicode :")
output = convert(inputword) 
print(output)
