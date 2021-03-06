#!/usr/bin/env python

import xlwt as xw
import xlrd as xr
import os.path
#from rex.settings import *

def prompted(xlfile, sheet):
    """
    Prompt for experimental information and return selected experiment (file is excel file name + path)
    """

    print xlfile
    print sheet
    array = excel_to_array(filename=xlfile, sheet=sheet)
    entries = []
    listing = []

    for y,x in enumerate(range(5,len(array[:][0]))):
        if array[x][0] == '':
            # break upon coming to blank line
            break
        # list pertinent information for each experiment
        entries.append(u'%s-%s.%s    -    %s' % (array[x][0],
                array[x][1], str(array[x][2])[0],
                array[x][(len(array[0][:]) - 2)]))
        listing.append(y)
        #Print out listing of #) entries
        print "%s) %s" % (listing[y], entries[y])

    # Prompt for entry
    prompt = input("Choose selection ")
    if prompt > y:
        exit()
    return prompt


def parse_ascii(ascii, delim='\t', header=True):
    """        Parse all information from csv or tab delimited data and return as array """

    whole = open(ascii).read().split('\n')

    # find number of cols in middle and only save information from sections that have that many columns
    ncols = len(whole[-10].split(delim))

    # initialize data_array matrix
    data_array = []
    for i in range(0,ncols):
        data_array.append([])

    for line in whole:
        line_split = line.split(delim)
        if len(line_split) == ncols:
            if header is True:
                header = False
            else:
                for i, split in enumerate(line_split):
                    data_array[i].append(split)
    return data_array

def parse_jdx(file):
    """ Open jdx file and process parameters to obtain transmittance and frequency """
    import re

    file = open(file).readlines()

    x = [] ; y = []

    dx = None
    is_trans = 1
    yfact = 1

    for line in file:
        if re.search('DELTAX',line) is not None:
            dx = float(line.split('=')[-1])
        if re.search('##YUNITS\=ABSORBANCE',line) is not None:
            is_trans = 0
        if re.search('##YFACTOR',line) is not None:
            yfact = float(line.split('=')[-1])
        # Actual Data ( x y y y y y y y )
        if re.search('##',line) is None and dx:
            iline = map(float, line.split())
            xis = [iline[0]]
            yis = iline[1:]
            for i in range(len(yis)-1): #@UnusedVariable
                xis.append(xis[-1] + dx)
            x.extend(xis)
            y.extend(yis)

    xc = [xi*0.9613 for xi in x]
    if is_trans == 1:
        tran = [yi*yfact for yi in y]
        abso = [1/yi for yi in y]
    else:
        abso = [yi*yfact for yi in y]
        tran = [1/yi for yi in y]
    n_tran = [yi/max(tran) for yi in tran]
    n_abs = [yi/max(abso) for yi in abso]

    return [x, xc, tran, abso, n_tran, n_abs]

def array_to_excel(data, filename, sheet='data'):
    """
    save information stored in array to file

    data -- list
    filename -- string
    """
    wb = xw.Workbook(encoding='utf')

    ws = wb.add_sheet(sheet)

    #set to landscape for printing
    ws.portrait = 0

    for r,lst in enumerate(data):
        for c,cell in enumerate(lst):
            ws.write(r,c,cell)

    wb.save(filename)

def excel_to_array(filename, sheet):
    """
    Pull information from excel and put into array of lists
    """
    if not os.path.exists(filename):
        raise Exception('Excel file does not exist.')

    wb = xr.open_workbook(filename=filename, encoding_override='latin')
    ws = wb.sheet_by_name(sheet)

    array = []

    for i in range(0,ws.nrows):
        row = []
        for j in range(0,ws.ncols):
            row.append(ws.cell_value(i,j))
        array.append(row)

    return array

