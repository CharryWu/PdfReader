#!/usr/bin/env python
from docx import opendocx, getdocumenttext
import sys

def main():
    infil = opendocx(sys.argv[1])
    outfil = open(sys.argv[2], 'w')
    paragraphs = getdocumenttext(opendocx('a.docx'))

    # For Unicode handling.
    new_paragraphs = []
    for paragraph in paragraphs:
        new_paragraphs.append(paragraph.encode("utf-8"))

    open('output.txt','w').write('\n'.join(new_paragraphs))



if __name__ == '__main__':
    main()