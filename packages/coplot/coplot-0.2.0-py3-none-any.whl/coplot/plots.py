# -*- coding: utf-8 -*-

from . import utils
from . import plot_settings as pls
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import math


# fiducial_colors = ['#006FED','#E03424','#33b540','#f68712','#1f77a4','#595657','m','#bdbcbc','#ad9f0a', '#ff7f0e', 'k']
# fiducial_colors = ['#006FED','#E03424','#33b540','#ff7f0e','#1f77a4','#595657','m','#bdbcbc','#ad9f0a', '#ff7f0e', 'k']
fiducial_colors = ['#006FED','#E03424','#33b540','#595657','#ff7f0e','#1f77a4','m','#bdbcbc','#ad9f0a', '#ff7f0e', 'k']

fiducial_colors_2 = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']


fiducial_line_styles = ['-', '--', ':', '-.', '-', '--', ':', '-.']
markers = ['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', '8', 's', 'p', 'P', '*', 'h', 'H', '+', 'x', 'X', 'D', 'd', '|', '_']

def get_fiducial_colors(num):
    if num < len(fiducial_colors):
        fc = fiducial_colors[:num]
    else:
        fc = list( np.random.choice(fiducial_colors, num) )
    return fc

def get_fiducial_line_styles(num):
    if num < len(fiducial_line_styles):
        fl = fiducial_line_styles[:num]
    else:
        fl = list( np.random.choice(fiducial_line_styles, num) )
    return fl


def makeList(roots):
    """Checks if the given parameter is a list, if not, creates a list with the parameter as an item in it.
    
    Parameters
    ----------
    roots : object
        The parameter to be checked.

    Returns
    -------
    list
        A list containing the parameter.
    """
    if isinstance(roots, (list, tuple)):
        return roots
    else:
        return [roots]

def makeListList(roots):
    """Checks if the element of the given parameter is a list, if not, creates a list with the parameter as an item in it.
    
    Parameters
    ----------
    roots : object
        The parameter to be checked.

    Returns
    -------
    list
        A list containing the parameter.
    """
    if isinstance(roots[0], (list, tuple)):
        return roots
    else:
        return [roots]

#to be improved
class Plots:
    def __init__(self, set_figsize=True):
        self.set_figsize = set_figsize
    
    def plot_lines(self):
        pass
    
    def plot_dots(self):
        pass
    
    def plot_errbars(self):
        pass
    
    def plot_fillBetween(self):
        pass
    
    def plot_hist(self):
        pass
    
    def siglePlot(self, location=None,lims=None,labels=None,ticks_size=None,
                  major_locator_N=None,minor_locator=True,minor_locator_N=None,
                  lines=None,line_labels=None,line_styles=None,line_colors=None,line_width=None,
                  dots=None,dot_labels=None,dot_styles=None,dot_colors=None,
                  errbars=None,errbar_line_width=None,errbar_colors=None,xerr=True,yerr=True,errbars_fmt=None,errbar_labels=None,
                  fill_between=None,fill_between_line_width=None,fill_between_line_styles=None,fill_between_colors=None,fill_between_labels=None,fill_between_alphas=None,
                  hist=None,hist_bins=None,hist_colors=None,hist_alpha=None,hist_labels=None,
                  legend=False,legend_location=None,title=None,title_size=None):
        """Plot dots, lines, error bars, fill between, histogram, etc.
        
        Parameters
        ----------
        location : tuple or list, optional
            The location of the panel, location=(1,2,2) or [1,2,2].
        lims : list, optional
            The limits of X and Y axis: [min_x, max_x, min_y, max_y].
        labels : list, optional
            The labels of the panel. e.g. [r'$x$',r'$y$']
        ticks_size : int, optional
            The font size of ticks.
        major_locator_N : int, optional
            The number of major locators.
        minor_locator : bool, optional
            If True(False), show(don't show) the minor locators.
        minor_locator_N : int, optional
            The number of minor locators.
        
        Returns
        -------
        object
            fig or ax
        """
        if self.set_figsize:
            fig_rate = 1
            fig = plt.figure(figsize=(6*fig_rate, 4.5*fig_rate))
        
        if ticks_size is None:
            ticks_size = 12
        ax = pls.PlotSettings().setting(location=location,lims=lims,labels=labels,\
        ticks_size=ticks_size,major_locator_N=major_locator_N,\
        minor_locator=minor_locator,minor_locator_N=minor_locator_N)
                
        # plot dots
        if dots is not None:
            dots = makeList(dots)
            if dot_styles is None:
                dot_styles = ['.' for i in range(len(dots))]
            else:
                dot_styles = makeList(dot_styles)
            if dot_colors is None:
                dot_colors = fiducial_colors
            else:
                dot_colors = makeList(dot_colors)
            if dot_labels is None:
                dot_labels = ['dot' for i in range(len(dots))]
#                dot_labels = ['' for i in range(len(dots))]
            for i in range(len(dots)):
                ax.plot(dots[i][:,0],dots[i][:,1],dot_styles[i],color=dot_colors[i],\
                label=dot_labels[i])
        
        # plot lines
        if lines is not None:
            lines = makeList(lines)
            if line_colors is None:
                line_colors = fiducial_colors
            else:
                line_colors = makeList(line_colors)
            if line_styles is None:
                line_styles = fiducial_line_styles
            else:
                line_styles = makeList(line_styles)
            if line_width is None:
                line_width = 1.618
            if line_labels is None:
                line_labels = ['line' for i in range(len(lines))]
#                line_labels = ['' for i in range(len(lines))]
            for i in range(len(lines)):
                ax.plot(lines[i][:,0],lines[i][:,1],color=line_colors[i],\
                linestyle=line_styles[i],linewidth=line_width,label=line_labels[i])
        
        # plot error bars
        if errbars is not None:
            if errbars_fmt is None:
                errbars_fmt = ['.' for i in range(len(errbars))]
            if errbar_labels is None:
                errbar_labels = ['errbar' for i in range(len(errbars))]
#                errbar_labels = ['' for i in range(len(errbars))]
            
            errbars = makeList(errbars)
            if errbar_colors is None:
                errbar_colors = fiducial_colors
            else:
                errbar_colors = makeList(errbar_colors)
            if errbar_line_width is None:
                errbar_line_width = 1.618
            for i in range(len(errbars)):
                if xerr is False and yerr is True:
                    ax.errorbar(errbars[i][:,0],errbars[i][:,1],yerr=errbars[i][:,2],\
                    fmt=errbars_fmt[i], color=errbar_colors[i],label=errbar_labels[i])
                elif xerr is True and yerr is False:
                    ax.errorbar(errbars[i][:,0],errbars[i][:,1],xerr=errbars[i][:,2],\
                    fmt=errbars_fmt[i], color=errbar_colors[i],label=errbar_labels[i])
                elif xerr is True and yerr is True:
                    ax.errorbar(errbars[i][:,0],errbars[i][:,1],xerr=errbars[i][:,2],\
                    yerr=errbars[i][:,3],fmt=errbars_fmt[i],color=errbar_colors[i],\
                    linewidth=errbar_line_width,label=errbar_labels[i])
        
        # plot fill between
        if fill_between is not None:
            fill_between = makeList(fill_between)
            if fill_between_line_width is None:
                fill_between_line_width = 1.618
            if fill_between_line_styles is None:
                fill_between_line_styles = fiducial_line_styles
            else:
                fill_between_line_styles = makeList(fill_between_line_styles)
            if fill_between_colors is None:
                fill_between_colors = fiducial_colors
            else:
                fill_between_colors = makeList(fill_between_colors)
            if fill_between_alphas is None:
                fill_between_alphas = [0.3 for i in range(len(fill_between))]
            if fill_between_labels is None:
                fill_between_labels = ['fill between' for i in range(len(fill_between))]
#                fill_between_labels = ['' for i in range(len(fill_between))]
            for i in range(len(fill_between)):
                ax.fill_between(fill_between[i][:,0],fill_between[i][:,1]-fill_between[i][:,2],\
                fill_between[i][:,1]+fill_between[i][:,2],color=fill_between_colors[i],\
                alpha=fill_between_alphas[i],linewidth=0,label='fill between')
                ax.plot(fill_between[i][:,0],fill_between[i][:,1],color=fill_between_colors[i],\
                linestyle=fill_between_line_styles[i], linewidth=fill_between_line_width)
        
        # plot histogram
        if hist is not None:
            hist = makeList(hist)
            if hist_bins is None:
                hist_bins = 30
            if hist_colors is None:
                hist_colors = fiducial_colors
            else:
                hist_colors = makeList(hist_colors)
            if hist_alpha is None:
                hist_alpha = [1 for i in range(len(hist))]
            if hist_labels is None:
                hist_labels = ['histogram' for i in range(len(hist))]
#                hist_labels = ['' for i in range(len(hist))]
            for i in range(len(hist)):
                ax.hist(hist[i][:],bins=hist_bins,color=hist_colors[i],\
                alpha=hist_alpha[i],label=hist_labels[i])
        
        # add legend
        if legend_location is None:
            # legend_location = 'upper(lower) right(left or center)' or 'center right(left)'
            legend_location = 'upper right'
        
        legend_size = ticks_size
        if legend is True:
            ax.legend(loc=legend_location, fontsize=legend_size)
            
        # add title
        if title is not None:
            if title_size is None:
                title_size = ticks_size
            ax.set_title(label=title, fontsize=title_size)
        
        if self.set_figsize is True:
            return fig
        else:
            return ax

def savefig(path, fig_name, fig, dpi='figure', bbox=None):
    '''
    dpi: float or 'figure'. The resolution in dots per inch. 
        If 'figure', use the figure's dpi value.
    bbox: None, str, or Bbox
        Bbox in inches. Only the given portion of the figure is saved. 
        If 'tight', try to figure out the tight bbox of the figure. 
        If None, use 'tight'. Default: None
        This can be used to remove white space around the figure, e.g:
            Here we will cut one inch off each side of the figure, to change the 10in x 8in figure to 8in x 6in
            bbox = fig.bbox_inches.from_bounds(1, 1, 8, 6).
    '''
    if bbox is None:
        bbox = 'tight'
    if path:
        utils.mkdir(path)
        fig.savefig(path + '/' + fig_name, dpi=dpi, bbox_inches=bbox)
    else:
        fig.savefig(fig_name, dpi=dpi, bbox_inches=bbox)


#%% multiple panels
#to be improved
class MultiplePanels(object):
    """Plot a figure with multiple panels.
    
    Parameters
    ----------
    panel_model : object
        An instance that can provide datasets and panel model (it should contain two methods: 'panels_data' and 'panel').
    lat_n : int, optional
        The number of panels in latitude (or transverse) direction. Default: 3
    """
    def __init__(self, panel_model, lat_n=3):
        self.datasets = panel_model.panels_data()
        self.panel_model = panel_model
        self.panel_n = len(self.datasets)
        self._lat_n = lat_n
    
    @property
    def lat_n(self):
        """ The number of panels in latitude (or transverse) direction. """
        if self.panel_n<self._lat_n:
            return self.panel_n
        else:
            return self._lat_n
    
    @property
    def lon_n(self):
        """ The number of panels in longitude (or longitudinal) direction. """
        return int(math.ceil(self.panel_n/float(self.lat_n)))
    
    def plot(self, panel_size=(4, 3), layout_adjust=[0.3, 0.25], ticks_size=12, 
             title='', title_x=0.5, title_y=0.98, title_fontsize=None, title_color='k'):
        if len(layout_adjust)==2:
            wspace, hspace = layout_adjust
            left, bottom, right, top = 0, 0, 1, 1
        elif len(layout_adjust)==6:
            left, bottom, right, top, wspace, hspace = layout_adjust
        if title_fontsize is None:
            title_fontsize = ticks_size * 1.20833
        fig = plt.figure(figsize=(panel_size[0]*self.lat_n, panel_size[1]*self.lon_n))
        fig.subplots_adjust(left=left,bottom=bottom,right=right,top=top,wspace=wspace,hspace=hspace)
        fig.suptitle(title, x=title_x, y=title_y, fontsize=title_fontsize, color=title_color)
        
        for i in range(self.lon_n):
            for j in range(self.lat_n):
                if i*self.lat_n+j+1 > self.panel_n:
                    break
                data = self.datasets[i*self.lat_n+j]
                if data:
                    #attribute of PlotSettings
                    lims = data['lims'] if 'lims' in data.keys() else None
                    labels = data['labels'] if 'labels' in data.keys() else None
                    rotation = data['rotation'] if 'rotation' in data.keys() else None
                    auto_locator = data['auto_locator'] if 'auto_locator' in data.keys() else False
                    major_locator_N = data['major_locator_N'] if 'major_locator_N' in data.keys() else None
                    major_locator_length = data['major_locator_length'] if 'major_locator_length' in data.keys() else None
                    major_locator_integers = data['major_locator_integers'] if 'major_locator_integers' in data.keys() else [False,False]
                    minor_locator = data['minor_locator'] if 'minor_locator' in data.keys() else True
                    minor_locator_N = data['minor_locator_N'] if 'minor_locator_N' in data.keys() else None
                    show_xticks = data['show_xticks'] if 'show_xticks' in data.keys() else True
                    show_yticks = data['show_yticks'] if 'show_yticks' in data.keys() else True
                    show_xticklabels = data['show_xticklabels'] if 'show_xticklabels' in data.keys() else True
                    show_yticklabels = data['show_yticklabels'] if 'show_yticklabels' in data.keys() else True
                    show_xlabel = data['show_xlabel'] if 'show_xlabel' in data.keys() else True
                    show_ylabel = data['show_ylabel'] if 'show_ylabel' in data.keys() else True
                    
                    ax = pls.PlotSettings().setting(ax=None,location=[self.lon_n, self.lat_n, i*self.lat_n+j+1], lims=lims, labels=labels,
                                                    ticks_size=ticks_size, rotation=rotation, auto_locator=auto_locator, major_locator_N=major_locator_N,
                                                    major_locator_length=major_locator_length, major_locator_integers=major_locator_integers,
                                                    minor_locator=minor_locator,minor_locator_N=minor_locator_N,show_xticks=show_xticks,
                                                    show_yticks=show_yticks,show_xticklabels=show_xticklabels,show_yticklabels=show_yticklabels,
                                                    show_xlabel=show_xlabel,show_ylabel=show_ylabel)
                    
                    self.panel_model.panel(data, fig, ax)
        return fig

#%% 
class MultipleGroupPanels(object):
    """Plot a figure with multiple panels. The difference between this class with :class:`MultiplePanels`
    is that this class split the total panels into several subplot groups using ``matplotlib.gridspec``.
    
    The main idea of this class is to split the figure into several groups with 
    each group contains several panels. Each group will be plotted one-by-one.
    
    Parameters
    ----------
    panel_model : object
        An instance that can provide datasets and panel model (it should contain two methods: 'panels_data' and 'panel').
    lat_n : int or list, optional
        The number of panels in latitude (or transverse) direction. Default: 3
    """
    #https://matplotlib.org/3.5.0/tutorials/intermediate/gridspec.html
    #https://stackoverflow.com/questions/24738578/control-wspace-for-matplotlib-subplots
    def __init__(self, panel_model, lat_n=3):
        self.datasets = panel_model.panels_data()
        self.panel_model = panel_model
        self.group_n = len(self.datasets)
        self.panel_n = [len(self.datasets[i]) for i in range(self.group_n)]
        self._lat_n = [lat_n for i in range(self.group_n)] if type(lat_n) is int else lat_n
    
    @property
    def lat_n(self):
        """ The number of panels in latitude (or transverse) direction. """
        lat_n = []
        for i in range(self.group_n):
            if self.panel_n[i]<self._lat_n[i]:
                lat_n.append(self.panel_n[i])
            else:
                lat_n.append(self._lat_n[i])
        return lat_n
    
    @property
    def lon_n(self):
        """ The number of panels in longitude (or longitudinal) direction. """
        lon_n = []
        for i in range(self.group_n):
            lon_n.append(int(math.ceil(self.panel_n[i]/float(self.lat_n[i]))))
        return lon_n
    
    def plot(self, panel_size=(4, 3), group_layout_type='up_down', figsize=None,
             gridspec_kwargs=None, ticks_size=12, title='', title_x=0.5, 
             title_y=0.98, title_fontsize=None, title_color='k'):
        """

        Parameters
        ----------
        panel_size : tuple or list, optional
            The size of each panel. Default: (4, 3)
        group_layout_type : str, optional
            The group layout type, which can be up and down ('up_down'), 
            left and right ('left_right'). Default: 'up_down'
        figsize : None or tuple, optional
            The figure size. If given, the ``group_layout_type`` will be ignored. Default: None
        gridspec_kwargs : None or list, optional
            Keyword arguments will be passed to `matplotlib.gridspec.GridSpec``.
            If not None, a list contains a seres of dictionaries should be given,
            where the number of dictionaries should be equal to the number of groups. Default: None
        ticks_size : int or float, optional
            The size of ticks. Default: 12
        title : str, optional
            The suptitle text. Default: ''
        title_x : float, optional
            The x location of the text in figure coordinates. Default: 0.5
        title_y : float, optional
            The y location of the text in figure coordinates. Default: 0.98
        title_fontsize : None, float or int, optional
            The font size of the suptitle text. Default: None
        title_color : str, optional
            The color of the suptitle text. Default:'k'
            
        """
        if type(panel_size[0]) is int or float:
            panel_size = [panel_size for i in range(self.group_n)]
        if title_fontsize is None:
            title_fontsize = ticks_size * 1.20833
        
        if figsize is None:
            if group_layout_type=='up_down':
                fig_w = panel_size[0][0]*self.lat_n[0]
                fig_h = sum([panel_size[i][1]*self.lon_n[i] for i in range(self.group_n)])
            elif group_layout_type=='left_right':
                fig_w = sum([panel_size[i][0]*self.lat_n[i] for i in range(self.group_n)])
                fig_h = panel_size[0][1]*self.lon_n[0]
            figsize = (fig_w, fig_h)
        if gridspec_kwargs is None:
            kw = {'left':None, 'right':None, 'bottom':None, 'top':None, 'wspace':None, 'hspace':None}
            gridspec_kwargs = [kw for i in range(self.group_n)]
            
        fig = plt.figure(figsize=figsize, constrained_layout=False)
        fig.suptitle(title, x=title_x, y=title_y, fontsize=title_fontsize, color=title_color)
        
        gs_all = []
        for g in range(self.group_n):
            gs = gridspec.GridSpec(self.lon_n[g], self.lat_n[g], figure=None, **gridspec_kwargs[g])
            gs_all.append(gs)
            for i in range(self.lon_n[g]):
                for j in range(self.lat_n[g]):
                    if i*self.lat_n[g]+j+1 > self.panel_n[g]:
                        break
                    data = self.datasets[g][i*self.lat_n[g]+j]
                    if data:
                        ax = fig.add_subplot(gs[i,j])
                        #attribute of PlotSettings
                        lims = data['lims'] if 'lims' in data.keys() else None
                        labels = data['labels'] if 'labels' in data.keys() else None
                        rotation = data['rotation'] if 'rotation' in data.keys() else None
                        auto_locator = data['auto_locator'] if 'auto_locator' in data.keys() else False
                        major_locator_N = data['major_locator_N'] if 'major_locator_N' in data.keys() else None
                        major_locator_length = data['major_locator_length'] if 'major_locator_length' in data.keys() else None
                        major_locator_integers = data['major_locator_integers'] if 'major_locator_integers' in data.keys() else [False,False]
                        minor_locator = data['minor_locator'] if 'minor_locator' in data.keys() else True
                        minor_locator_N = data['minor_locator_N'] if 'minor_locator_N' in data.keys() else None
                        show_xticks = data['show_xticks'] if 'show_xticks' in data.keys() else True
                        show_yticks = data['show_yticks'] if 'show_yticks' in data.keys() else True
                        show_xticklabels = data['show_xticklabels'] if 'show_xticklabels' in data.keys() else True
                        show_yticklabels = data['show_yticklabels'] if 'show_yticklabels' in data.keys() else True
                        show_xlabel = data['show_xlabel'] if 'show_xlabel' in data.keys() else True
                        show_ylabel = data['show_ylabel'] if 'show_ylabel' in data.keys() else True
                                
                        ax = pls.PlotSettings().setting(ax=ax,location=None, lims=lims, labels=labels,
                                                        ticks_size=ticks_size, rotation=rotation, auto_locator=auto_locator, major_locator_N=major_locator_N,
                                                        major_locator_length=major_locator_length, major_locator_integers=major_locator_integers,
                                                        minor_locator=minor_locator,minor_locator_N=minor_locator_N,show_xticks=show_xticks,
                                                        show_yticks=show_yticks,show_xticklabels=show_xticklabels,show_yticklabels=show_yticklabels,
                                                        show_xlabel=show_xlabel,show_ylabel=show_ylabel)
                        
                        self.panel_model.panel(data, fig, ax)
        return fig


