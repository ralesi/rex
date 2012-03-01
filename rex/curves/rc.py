# module: curves.rc
# set up common options for matplotlibs rcParams

# Original Author: Varun Hiremath <vh63@cornell.edu>
# Maintained by : Rich Alesi
# Last Change: 2012 Jan 19

from pylab import rcParams
import math

# Symbols
symbols = ['-','--','-.',':','.',',','o','^','v','<','>','s','+','x','D','d','1','2','3','4','h','H','p']
# Symbols + line
lps = [k+'-' for k in [',','.','o','^','v','<','>','s','+','x','D','d','1','2','3','4','h','H','p']]
# Colors
colors= ['b','g','r','c','m','y','k','w']

def get_figsize(fig_width_pt):
    inches_per_pt = 1.0/72.0                # Convert pt to inch
    golden_mean = (math.sqrt(5)-1.0)/2.0    # Aesthetic ratio
    fig_width = fig_width_pt*inches_per_pt  # width in inches
    fig_height = fig_width*golden_mean      # height in inches
    fig_size =  [fig_width,fig_height]      # exact figsize
    return fig_size

def golden_height(number):
    golden_mean = (math.sqrt(5)-1.0)/2.0    # Aesthetic ratio
    return (golden_mean * number)

# Publishable quality image settings for 2-column papers

modes = {

'compact': {'backend': 'WXAgg',
           'axes.labelsize': 8,
           'font.family':'serif',
           'font.sansserif':'Times New Roman',
           'text.fontsize': 8,
           'xtick.labelsize': 8,
           'ytick.labelsize': 8,
           'legend.pad': 0.1,    # empty space around the legend box
           'legend.fontsize': 5,
           'lines.markersize': 3,
           'font.size': 8,
           'figure.subplot.bottom': 0.18,
           'figure.subplot.left': 0.22,
           'figure.subplot.right': 0.93,
           'figure.subplot.top': 0.91,
           'figure.figsize': [2, 2]},

'medium': {'backend': 'WXAgg',
           'axes.labelsize': 8,
           'text.fontsize': 8,
           'xtick.labelsize': 8,
           'ytick.labelsize': 8,
           'legend.pad': 0.1,     # empty space around the legend box
           'legend.fontsize': 8,
           'lines.markersize': 3,
           'font.size': 8,
           'figure.subplot.bottom': 0.08000000000000001,
           'figure.subplot.left': 0.08,
           'figure.subplot.right': 0.95,
           'figure.subplot.top': 0.95,
           'figure.figsize': get_figsize(500)},

'default': {'backend': 'TkAgg',
        'axes.labelsize': 10,
        'axes.titlesize': 11,
        'font.family':'serif',
        'font.serif':'Times New Roman',
        'font.size': 10,
        'legend.axespad': 0.3,
        'axes.labelsize': 10,
        'legend.borderpad': 0.3,
        'legend.fancybox':True,
        'legend.fontsize': 10,
        'legend.pad': 0.2,     # empty space around the legend box
        'lines.linewidth': 2,
        'lines.markersize': 3,
        'text.fontsize': 10,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'figure.subplot.bottom': 0.08,
        'figure.subplot.left': 0.08,
        'figure.subplot.right': 0.95,
        'figure.subplot.top': 0.95,
        'lines.antialiased': 'yes',
        'figure.figsize': get_figsize(800)},

'double_high': {'backend': 'TkAgg',
        'font.family':'serif',
        'font.serif':'Times New Roman',
        'axes.labelsize': 11,
        'text.fontsize': 11,
        'legend.fontsize': 11,
        'xtick.labelsize': 11,
        'ytick.labelsize': 11,
        'figure.subplot.bottom': 0.14,
        'figure.subplot.left': 0.12,
        'figure.subplot.right': 0.95,
        'figure.subplot.top': 0.93,
        'figure.figsize': (3,5)},

'double': {'backend': 'TkAgg',
        'font.family':'serif',
        'font.serif':'Times New Roman',
        'axes.labelsize': 11,
        'text.fontsize': 11,
        'legend.fontsize': 11,
        'xtick.labelsize': 11,
        'ytick.labelsize': 11,
        'figure.subplot.bottom': 0.14,
        'figure.subplot.left': 0.12,
        'figure.subplot.right': 0.95,
        'figure.subplot.top': 0.93,
        'figure.figsize': (6,4)},

'john': {'backend': 'TkAgg',
        'font.family':'serif',
        'font.serif':'Times New Roman',
        'axes.labelsize': 11,
        'text.fontsize': 11,
        'legend.fontsize': 11,
        'xtick.labelsize': 11,
        'ytick.labelsize': 11,
        'figure.subplot.bottom': 0.14,
        'figure.subplot.left': 0.18,
        'figure.subplot.right': 0.95,
        'figure.subplot.top': 0.93,
        'figure.figsize': (3,4)},

'little_john': {'backend': 'TkAgg',
        'font.family':'serif',
        'font.serif':'Times New Roman',
        'legend.pad': 0.1,     # empty space around the legend box
        'axes.labelsize': 11,
        'text.fontsize': 11,
        'legend.fontsize': 8,
        'legend.frameon': True,
        'legend.fancybox':True,
        'xtick.labelsize': 11,
        'ytick.labelsize': 11,
        'figure.subplot.bottom': 0.14,
        'figure.subplot.left': 0.22,
        'figure.subplot.right': 0.94,
        'figure.subplot.top': 0.93,
        'figure.figsize': (3,4)},

'square': {'backend': 'TkAgg',
        'font.family':'serif',
        'font.serif':'Times New Roman',
        'axes.labelsize': 11,
        'text.fontsize': 11,
        'legend.fontsize': 11,
        'xtick.labelsize': 11,
        'ytick.labelsize': 11,
        'figure.subplot.bottom': 0.14,
        'figure.subplot.left': 0.18,
        'figure.subplot.right': 0.95,
        'figure.subplot.top': 0.93,
        'figure.figsize': (3,3)},

'present': {'backend': 'WXAgg',
           'figure.subplot.bottom': 0.08000000000000001,
           'figure.subplot.left': 0.08,
           'figure.subplot.right': 0.95,
           'figure.subplot.top': 0.95,
           'figure.figsize': (8,5.5)
           }}

def set_mode(mode):
    if mode in modes.keys():
        rcParams.update(modes[mode])

def set_figsize(fig_width_pt,fig_height_pt=None):
    rcParams['figure.figsize'] = get_figsize(fig_width_pt)

def set_figsize_in(fig_width, fig_height=None):
    if fig_height is None:
        fig_height = golden_height(fig_width)
    rcParams['figure.figsize'] = (fig_width, fig_height)


rcParams.update(modes['default'])


### MATPLOTLIBRC FORMAT

# This is a sample matplotlib configuration file - you can find a copy
# of it on your system in
# site-packages/matplotlib/mpl-data/matplotlibrc.  If you edit it
# there, please note that it will be overridden in your next install.
# If you want to keep a permanent local copy that will not be
# over-written, place it in HOME/.matplotlib/matplotlibrc (unix/linux
# like systems) and C:\Documents and Settings\yourname\.matplotlib
# (win32 systems).
#
# This file is best viewed in a editor which supports python mode
# syntax highlighting. Blank lines, or lines starting with a comment
# symbol, are ignored, as are trailing comments.  Other lines must
# have the format
#    key : val # optional comment
#
# Colors: for the color values below, you can either use - a
# matplotlib color string, such as r, k, or b - an rgb tuple, such as
# (1.0, 0.5, 0.0) - a hex string, such as ff00ff or #ff00ff - a scalar
# grayscale intensity such as 0.75 - a legal html color name, eg red,
# blue, darkslategray

#### CONFIGURATION BEGINS HERE

# the default backend; one of GTK GTKAgg GTKCairo CocoaAgg FltkAgg
# MacOSX QtAgg Qt4Agg TkAgg WX WXAgg Agg Cairo GDK PS PDF SVG Template
# You can also deploy your own backend outside of matplotlib by
# referring to the module name (which must be in the PYTHONPATH) as
# 'module://my_backend'
# backend      : GTKAgg

# If you are using the Qt4Agg backend, you can choose here
# to use the PyQt4 bindings or the newer PySide bindings to
# the underlying Qt4 toolkit.
#backend.qt4 : PyQt4        # PyQt4 | PySide

# Note that this can be overridden by the environment variable
# QT_API used by Enthought Tool Suite (ETS); valid values are
# "pyqt" and "pyside".  The "pyqt" setting has the side effect of
# forcing the use of Version 2 API for QString and QVariant.

# if you are runing pyplot inside a GUI and your backend choice
# conflicts, we will automatically try to find a compatible one for
# you if backend_fallback is True
#backend_fallback: True

#interactive  : False
#toolbar      : toolbar2   # None | classic | toolbar2
#timezone     : UTC        # a pytz timezone string, eg US/Central or Europe/Paris

# Where your matplotlib data lives if you installed to a non-default
# location.  This is where the matplotlib fonts, bitmaps, etc reside
#datapath : /home/jdhunter/mpldata


### LINES
# See http://matplotlib.sourceforge.net/api/artist_api.html#module-matplotlib.lines for more
# information on line properties.
#lines.linewidth   : 1.0     # line width in points
#lines.linestyle   : -       # solid line
#lines.color       : blue
#lines.marker      : None    # the default marker
#lines.markeredgewidth  : 0.5     # the line width around the marker symbol
#lines.markersize  : 6            # markersize, in points
#lines.dash_joinstyle : miter        # miter|round|bevel
#lines.dash_capstyle : butt          # butt|round|projecting
#lines.solid_joinstyle : miter       # miter|round|bevel
#lines.solid_capstyle : projecting   # butt|round|projecting
#lines.antialiased : True         # render lines in antialised (no jaggies)

### PATCHES
# Patches are graphical objects that fill 2D space, like polygons or
# circles.  See
# http://matplotlib.sourceforge.net/api/artist_api.html#module-matplotlib.patches
# information on patch properties
#patch.linewidth        : 1.0     # edge width in points
#patch.facecolor        : blue
#patch.edgecolor        : black
#patch.antialiased      : True    # render patches in antialised (no jaggies)

### FONT
#
# font properties used by text.Text.  See
# http://matplotlib.sourceforge.net/api/font_manager_api.html for more
# information on font properties.  The 6 font properties used for font
# matching are given below with their default values.
#
# The font.family property has five values: 'serif' (e.g. Times),
# 'sans-serif' (e.g. Helvetica), 'cursive' (e.g. Zapf-Chancery),
# 'fantasy' (e.g. Western), and 'monospace' (e.g. Courier).  Each of
# these font families has a default list of font names in decreasing
# order of priority associated with them.
#
# The font.style property has three values: normal (or roman), italic
# or oblique.  The oblique style will be used for italic, if it is not
# present.
#
# The font.variant property has two values: normal or small-caps.  For
# TrueType fonts, which are scalable fonts, small-caps is equivalent
# to using a font size of 'smaller', or about 83% of the current font
# size.
#
# The font.weight property has effectively 13 values: normal, bold,
# bolder, lighter, 100, 200, 300, ..., 900.  Normal is the same as
# 400, and bold is 700.  bolder and lighter are relative values with
# respect to the current weight.
#
# The font.stretch property has 11 values: ultra-condensed,
# extra-condensed, condensed, semi-condensed, normal, semi-expanded,
# expanded, extra-expanded, ultra-expanded, wider, and narrower.  This
# property is not currently implemented.
#
# The font.size property is the default font size for text, given in pts.
# 12pt is the standard value.
#
#font.family         : sans-serif
#font.style          : normal
#font.variant        : normal
#font.weight         : medium
#font.stretch        : normal
# note that font.size controls default text sizes.  To configure
# special text sizes tick labels, axes, labels, title, etc, see the rc
# settings for axes and ticks. Special text sizes can be defined
# relative to font.size, using the following values: xx-small, x-small,
# small, medium, large, x-large, xx-large, larger, or smaller
#font.size           : 12.0
#font.serif          : Bitstream Vera Serif, New Century Schoolbook, Century Schoolbook L, Utopia, ITC Bookman, Bookman, Nimbus Roman No9 L, Times New Roman, Times, Palatino, Charter, serif
#font.sans-serif     : Bitstream Vera Sans, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif
#font.cursive        : Apple Chancery, Textile, Zapf Chancery, Sand, cursive
#font.fantasy        : Comic Sans MS, Chicago, Charcoal, Impact, Western, fantasy
#font.monospace      : Bitstream Vera Sans Mono, Andale Mono, Nimbus Mono L, Courier New, Courier, Fixed, Terminal, monospace

### TEXT
# text properties used by text.Text.  See
# http://matplotlib.sourceforge.net/api/artist_api.html#module-matplotlib.text for more
# information on text properties

#text.color          : black

### LaTeX customizations. See http://www.scipy.org/Wiki/Cookbook/Matplotlib/UsingTex
#text.usetex         : False  # use latex for all text handling. The following fonts
                              # are supported through the usual rc parameter settings:
                              # new century schoolbook, bookman, times, palatino,
                              # zapf chancery, charter, serif, sans-serif, helvetica,
                              # avant garde, courier, monospace, computer modern roman,
                              # computer modern sans serif, computer modern typewriter
                              # If another font is desired which can loaded using the
                              # LaTeX \usepackage command, please inquire at the
                              # matplotlib mailing list
#text.latex.unicode : False # use "ucs" and "inputenc" LaTeX packages for handling
                            # unicode strings.
#text.latex.preamble :  # IMPROPER USE OF THIS FEATURE WILL LEAD TO LATEX FAILURES
                            # AND IS THEREFORE UNSUPPORTED. PLEASE DO NOT ASK FOR HELP
                            # IF THIS FEATURE DOES NOT DO WHAT YOU EXPECT IT TO.
                            # preamble is a comma separated list of LaTeX statements
                            # that are included in the LaTeX document preamble.
                            # An example:
                            # text.latex.preamble : \usepackage{bm},\usepackage{euler}
                            # The following packages are always loaded with usetex, so
                            # beware of package collisions: color, geometry, graphicx,
                            # type1cm, textcomp. Adobe Postscript (PSSNFS) font packages
                            # may also be loaded, depending on your font settings

#text.dvipnghack : None      # some versions of dvipng don't handle alpha
                             # channel properly.  Use True to correct
                             # and flush ~/.matplotlib/tex.cache
                             # before testing and False to force
                             # correction off.  None will try and
                             # guess based on your dvipng version

#text.hinting : True # If True, text will be hinted, otherwise not.  This only
                     # affects the Agg backend.

# The following settings allow you to select the fonts in math mode.
# They map from a TeX font name to a fontconfig font pattern.
# These settings are only used if mathtext.fontset is 'custom'.
# Note that this "custom" mode is unsupported and may go away in the
# future.
#mathtext.cal : cursive
#mathtext.rm  : serif
#mathtext.tt  : monospace
#mathtext.it  : serif:italic
#mathtext.bf  : serif:bold
#mathtext.sf  : sans
#mathtext.fontset : cm # Should be 'cm' (Computer Modern), 'stix',
                       # 'stixsans' or 'custom'
#mathtext.fallback_to_cm : True  # When True, use symbols from the Computer Modern
                                 # fonts when a symbol can not be found in one of
                                 # the custom math fonts.

#mathtext.default : it # The default font to use for math.
                       # Can be any of the LaTeX font names, including
                       # the special name "regular" for the same font
                       # used in regular text.

### AXES
# default face and edge color, default tick sizes,
# default fontsizes for ticklabels, and so on.  See
# http://matplotlib.sourceforge.net/api/axes_api.html#module-matplotlib.axes
#axes.hold           : True    # whether to clear the axes by default on
#axes.facecolor      : white   # axes background color
#axes.edgecolor      : black   # axes edge color
#axes.linewidth      : 1.0     # edge linewidth
#axes.grid           : False   # display grid or not
#axes.titlesize      : large   # fontsize of the axes title
#axes.labelsize      : medium  # fontsize of the x any y labels
#axes.labelweight    : normal  # weight of the x and y labels
#axes.labelcolor     : black
#axes.axisbelow      : False   # whether axis gridlines and ticks are below
                              # the axes elements (lines, text, etc)
#axes.formatter.limits : -7, 7 # use scientific notation if log10
                               # of the axis range is smaller than the
                               # first or larger than the second
#axes.formatter.use_locale : False # When True, format tick labels
                                   # according to the user's locale.
                                   # For example, use ',' as a decimal
                                   # separator in the fr_FR locale.
#axes.unicode_minus  : True    # use unicode for the minus symbol
                               # rather than hypen.  See
                               # http://en.wikipedia.org/wiki/Plus_sign
#axes.color_cycle    : b, g, r, c, m, y, k  # color cycle for plot lines
                                            # as list of string colorspecs:
                                            # single letter, long name, or
                                            # web-style hex

#polaraxes.grid      : True    # display grid on polar axes
#axes3d.grid         : True    # display grid on 3d axes

### TICKS
# see http://matplotlib.sourceforge.net/api/axis_api.html#matplotlib.axis.Tick
#xtick.major.size     : 4      # major tick size in points
#xtick.minor.size     : 2      # minor tick size in points
#xtick.major.pad      : 4      # distance to major tick label in points
#xtick.minor.pad      : 4      # distance to the minor tick label in points
#xtick.color          : k      # color of the tick labels
#xtick.labelsize      : medium # fontsize of the tick labels
#xtick.direction      : in     # direction: in or out

#ytick.major.size     : 4      # major tick size in points
#ytick.minor.size     : 2      # minor tick size in points
#ytick.major.pad      : 4      # distance to major tick label in points
#ytick.minor.pad      : 4      # distance to the minor tick label in points
#ytick.color          : k      # color of the tick labels
#ytick.labelsize      : medium # fontsize of the tick labels
#ytick.direction      : in     # direction: in or out


### GRIDS
#grid.color       :   black   # grid color
#grid.linestyle   :   :       # dotted
#grid.linewidth   :   0.5     # in points

### Legend
#legend.fancybox      : False  # if True, use a rounded box for the
                               # legend, else a rectangle
#legend.isaxes        : True
#legend.numpoints     : 2      # the number of points in the legend line
#legend.fontsize      : large
#legend.pad           : 0.0    # deprecated; the fractional whitespace inside the legend border
#legend.borderpad     : 0.5    # border whitspace in fontsize units
#legend.markerscale   : 1.0    # the relative size of legend markers vs. original
# the following dimensions are in axes coords
#legend.labelsep      : 0.010  # deprecated; the vertical space between the legend entries
#legend.labelspacing  : 0.5    # the vertical space between the legend entries in fraction of fontsize
#legend.handlelen     : 0.05   # deprecated; the length of the legend lines
#legend.handlelength  : 2.     # the length of the legend lines in fraction of fontsize
#legend.handleheight  : 0.7     # the height of the legend handle in fraction of fontsize
#legend.handletextsep : 0.02   # deprecated; the space between the legend line and legend text
#legend.handletextpad : 0.8    # the space between the legend line and legend text in fraction of fontsize
#legend.axespad       : 0.02   # deprecated; the border between the axes and legend edge
#legend.borderaxespad : 0.5   # the border between the axes and legend edge in fraction of fontsize
#legend.columnspacing : 2.    # the border between the axes and legend edge in fraction of fontsize
#legend.shadow        : False
#legend.frameon       : True   # whether or not to draw a frame around legend

### FIGURE
# See http://matplotlib.sourceforge.net/api/figure_api.html#matplotlib.figure.Figure
#figure.figsize   : 8, 6    # figure size in inches
#figure.dpi       : 80      # figure dots per inch
#figure.facecolor : 0.75    # figure facecolor; 0.75 is scalar gray
#figure.edgecolor : white   # figure edgecolor

# The figure subplot parameters.  All dimensions are fraction of the
# figure width or height
#figure.subplot.left    : 0.125  # the left side of the subplots of the figure
#figure.subplot.right   : 0.9    # the right side of the subplots of the figure
#figure.subplot.bottom  : 0.1    # the bottom of the subplots of the figure
#figure.subplot.top     : 0.9    # the top of the subplots of the figure
#figure.subplot.wspace  : 0.2    # the amount of width reserved for blank space between subplots
#figure.subplot.hspace  : 0.2    # the amount of height reserved for white space between subplots

### IMAGES
#image.aspect : equal             # equal | auto | a number
#image.interpolation  : bilinear  # see help(imshow) for options
#image.cmap   : jet               # gray | jet etc...
#image.lut    : 256               # the size of the colormap lookup table
#image.origin : upper             # lower | upper
#image.resample  : False

### CONTOUR PLOTS
#contour.negative_linestyle :  dashed # dashed | solid

### Agg rendering
### Warning: experimental, 2008/10/10
#agg.path.chunksize : 0           # 0 to disable; values in the range
                                  # 10000 to 100000 can improve speed slightly
                                  # and prevent an Agg rendering failure
                                  # when plotting very large data sets,
                                  # especially if they are very gappy.
                                  # It may cause minor artifacts, though.
                                  # A value of 20000 is probably a good
                                  # starting point.
### SAVING FIGURES
#path.simplify : True   # When True, simplify paths by removing "invisible"
                        # points to reduce file size and increase rendering
                        # speed
#path.simplify_threshold : 0.1  # The threshold of similarity below which
                                # vertices will be removed in the simplification
                                # process
#path.snap : True # When True, rectilinear axis-aligned paths will be snapped to
                  # the nearest pixel when certain criteria are met.  When False,
                  # paths will never be snapped.

# the default savefig params can be different from the display params
# Eg, you may want a higher resolution, or to make the figure
# background white
#savefig.dpi       : 100      # figure dots per inch
#savefig.facecolor : white    # figure facecolor when saving
#savefig.edgecolor : white    # figure edgecolor when saving
#savefig.extension : auto     # what extension to use for savefig('foo'), or 'auto'

#cairo.format      : png      # png, ps, pdf, svg

# tk backend params
#tk.window_focus   : False    # Maintain shell focus for TkAgg

# ps backend params
#ps.papersize      : letter   # auto, letter, legal, ledger, A0-A10, B0-B10
#ps.useafm         : False    # use of afm fonts, results in small files
#ps.usedistiller   : False    # can be: None, ghostscript or xpdf
                                          # Experimental: may produce smaller files.
                                          # xpdf intended for production of publication quality files,
                                          # but requires ghostscript, xpdf and ps2eps
#ps.distiller.res  : 6000      # dpi
#ps.fonttype       : 3         # Output Type 3 (Type3) or Type 42 (TrueType)

# pdf backend params
#pdf.compression   : 6 # integer from 0 to 9
                       # 0 disables compression (good for debugging)
#pdf.fonttype       : 3         # Output Type 3 (Type3) or Type 42 (TrueType)

# svg backend params
#svg.image_inline : True       # write raster image data directly into the svg file
#svg.image_noscale : False     # suppress scaling of raster data embedded in SVG
#svg.fonttype : 'path'         # How to handle SVG fonts:
#    'none': Assume fonts are installed on the machine where the SVG will be viewed.
#    'path': Embed characters as paths -- supported by most SVG renderers
#    'svgfont': Embed characters as SVG fonts -- supported only by Chrome,
#               Opera and Safari

# docstring params
#docstring.hardcopy = False  # set this when you want to generate hardcopy docstring

# Set the verbose flags.  This controls how much information
# matplotlib gives you at runtime and where it goes.  The verbosity
# levels are: silent, helpful, debug, debug-annoying.  Any level is
# inclusive of all the levels below it.  If your setting is "debug",
# you'll get all the debug and helpful messages.  When submitting
# problems to the mailing-list, please set verbose to "helpful" or "debug"
# and paste the output into your report.
#
# The "fileo" gives the destination for any calls to verbose.report.
# These objects can a filename, or a filehandle like sys.stdout.
#
# You can override the rc default verbosity from the command line by
# giving the flags --verbose-LEVEL where LEVEL is one of the legal
# levels, eg --verbose-helpful.
#
# You can access the verbose instance in your code
#   from matplotlib import verbose.
#verbose.level  : silent      # one of silent, helpful, debug, debug-annoying
#verbose.fileo  : sys.stdout  # a log filename, sys.stdout or sys.stderr

# Event keys to interact with figures/plots via keyboard.
# Customize these settings according to your needs.
# Leave the field(s) empty if you don't need a key-map. (i.e., fullscreen : '')

#keymap.fullscreen : f               # toggling
#keymap.home : h, r, home            # home or reset mnemonic
#keymap.back : left, c, backspace    # forward / backward keys to enable
#keymap.forward : right, v           #   left handed quick navigation
#keymap.pan : p                      # pan mnemonic
#keymap.zoom : o                     # zoom mnemonic
#keymap.save : s                     # saving current figure
#keymap.grid : g                     # switching on/off a grid in current axes
#keymap.yscale : l                   # toggle scaling of y-axes ('log'/'linear')
#keymap.xscale : L, k                # toggle scaling of x-axes ('log'/'linear')
#keymap.all_axes : a                 # enable all axes

# Control downloading of example data. Various examples download some
# data from the Matplotlib git repository to avoid distributing extra
# files, but sometimes you want to avoid that. In that case set
# examples.download to False and examples.directory to the directory
# where you have a checkout of https://github.com/matplotlib/sample_data

#examples.download : True  # False to bypass downloading mechanism
#examples.directory : ''   # directory to look in if download is false
