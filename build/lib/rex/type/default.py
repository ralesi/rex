#!/usr/bin/env python

from rex.experiment import Experiment

EXPERIMENT_DB = None

class Default(Experiment):
    """
    Analysis method that contains all pertinent information
    for NETL-MS data.
    Most information comes from Experiment.__init__() with a few exceptions
    procedure contains all pertinent information needed to calculate additional _curves

    """
    def __init__(self,
            xlfile=EXPERIMENT_DB,
            sheet='',
            prompt=None,
            debug=0):


#        self._raw_columns = {'Curve', [column, 'label']
#                }

        self._raw_columns = {
            }

        Experiment.__init__(self,
                xlfile = xlfile,
                sheet = sheet,
                prompt = prompt,
                delim = '\t',
                txt_col = 6,
                dat = None,
                debug = debug)

        # save information from Excel file
        row = self._row

        row_params = {
            }

        self.init_param(row_params)

        # construct experiment name
        self.set_param('Name', '%s-%s.%i' % (row[1], row[2], row[3]))

        # initial date and time (for reference)
        dcol = 1 # date column in txt file
        tcol = 2 # time column in txt file

        self.get_init(self._data_array[dcol][0], self._data_array[tcol][0])

        # we do all plots based off relative time
        self.get_reltimes()
        self.add_curve('rel_hr',[float(sec)/3600 for sec in self._curves['rel_sec']], 'Relative Time [hr]')

        self._labels = {}

