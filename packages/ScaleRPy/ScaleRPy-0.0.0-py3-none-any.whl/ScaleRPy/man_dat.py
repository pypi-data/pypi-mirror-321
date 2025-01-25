"""
Contains SpatGalDat and GalDat classes

Copyright 2025 Bryanne McDonough
Apache License, Version 2.0
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import src.ScaleRPy.fitting.fit_funcs as fit
"""
Functions to add:
    rem_low : remove low s_mass from the sample

    
"""

class GalDat:
    """
    Class for handling pre-processed global (i.e., integrated) galaxy parameters
    Measure the slopes of global scaling relationships
    Produce publication-quality plots
    """
    def __init__(self):
        self.parameters = {}
        self.labels = {}

    def add_parameter(self, name, values, label):
        """Add a parameter to the galaxy data
        name: string, the name of the parameter
        values: array, the values of the parameter
        label: string, the label for the parameter, for plot labels
        """
        self.parameters[name] = values
        self.labels[name] = label

    def add_parameters(self, params_dict):
        """Add multiple parameters to the galaxy data
        params_dict: dictionary, keys are the parameter names, values are tuples of the form (values, label)"""
        for name, (values, label) in params_dict.items():
            self.add_parameter(name, values, label)

    def get_parameters(self):
        """Return a list of the parameter names"""
        return list(self.parameters.keys())

    def get_label(self, name):
        """Return the label for the parameter name"""
        return self.labels.get(name, "")

    def compute_relationship(self, param1, param2, linefit='double', **kwarg):
        """Compute the relationship between two parameters
        param1: string, the name of the first parameter
        param2: string, the name of the second parameter
        linefit: string, the type of line fit to perform, 'double' or 'single'
        kwarg: keyword arguments to pass to find_ridge
        """
        xlab = self.labels[param1]
        ylab = self.labels[param2]
        x = self.parameters[param1]
        y = self.parameters[param2]
        hist, ridgept, histvals, xedges, yedges = fit.find_ridge(x, y, xlabel=xlab, ylabel=ylab, **kwarg)
        fitax = hist[1]
        if linefit=='double':
            params, paramerr = fit.fit_double(ridgept)
            yfit = fit.doubline(ridgept[0,:], *params)
        elif linefit == 'single':   
            params, paramerr = fit.fit_single(ridgept)
            yfit = fit.line(ridgept[0,:], *params)
        fitax.plot(ridgept[0,:], yfit, color = 'yellow')
        return hist, params, paramerr


class SpatGalDat:
    """
    Class for handling pre-processed 'spaxel' data from spatially-resolved galaxies
    Measure the slopes of spatially resolved scaling relationships
    Produce publication-quality plots

    """

    def __init__(self, s_mass=[], sfr=[], gas=[], scale='log'):
        """Instance variables should be arrays or lists. 
        At least two variables should be defined as non-empty arrays.
        Default assumes spaxel values are already in base-10 log space"""

        # ADD ERROR: check that at least two arrays are non-empty and the same length
      
        #initialize variables, ensure any non-finite values are handled as NaNs
        self.s_mass = np.where(np.isfinite(s_mass),s_mass, np.nan*np.array(s_mass))
        self.sfr = np.where(np.isfinite(sfr), sfr, np.nan*np.array(sfr))
        self.g_mass = np.where(np.isfinite(gas), gas, np.nan*np.array(gas))

        if scale != 'log':
            #take the base10 log and replace zeros with NaNs
            self.s_mass = np.log10(self.s_mass, out = np.nan*self.s_mass, where = (self.s_mass>0))
            self.sfr = np.log10(self.sfr, out = np.nan*self.sfr, where = (self.sfr>0))
            self.g_mass = np.log10(self.g_mass, out = np.nan*self.g_mass, where = (self.g_mass>0))
        
        self.s_mass_unit = r'$M_\odot \mathrm{kpc}^{-2}$'
        self.sfr_unit = r'$M_\odot \mathrm{yr}^{-1} \mathrm{kpc}^{-2}$'
        self.gas_unit = r'$M_{\mathrm{gas}} \mathrm{kpc}^{-2}$'
        #self.s_mass_label = r'log$_{10}$[$\Sigma_*$ / ($M_\odot$ kp$\mathrm{c}^{-2}$)]'
        
    

    
    def SFMS_ridge(self, linefit='double', **kwarg):
        """Identify the 'ridge' of data for the star-forming main sequence
            Keyword arguments passed to find_ridge"""
        xlab = r'log$_{10} (\Sigma_* / $ [%s])' % self.s_mass_unit
        ylab = r'log$_{10} (\Sigma_{\mathrm{SFR}}/$ [%s])' % self.sfr_unit
        self.SFMS_hist, self.SFMS_ridgept, self.SFMS_histval, \
              self.SFMS_xedges, self.SFMS_yedges = fit.find_ridge(
                  self.s_mass, self.sfr, xlabel = xlab, ylabel=ylab, **kwarg)
        self.SFMS_fitax = self.SFMS_hist[1]
        if linefit == 'double':
            self.SFMS_params, self.SFMS_paramerr = fit.fit_double(self.SFMS_ridgept)
            yfit = fit.doubline(self.SFMS_ridgept[0,:], *self.SFMS_params)
            
        elif linefit == 'single':
            self.SFMS_params, self.SFMS_paramerr = fit.fit_single(self.SFMS_ridgept)
            yfit = fit.line(self.SFMS_ridgept[0,:], *self.SFMS_params)

        self.SFMS_fitax.plot(self.SFMS_ridgept[0,:], yfit, color = 'yellow')
        return(self.SFMS_hist, self.SFMS_params, self.SFMS_paramerr)

    def KS_ridge(self,linefit = 'double', **kwarg):
        xlab = r'log$_{10} (\Sigma_{\mathrm{gas}} /$ [%s])' % self.gas_unit
        ylab = r'log$_{10} (\Sigma_{\mathrm{SFR}}/$ [%s])' % self.sfr_unit
        self.KS_hist, self.KS_ridgept , self.KS_histvals= fit.find_ridge(self.g_mass, self.sfr, xlabel=xlab, ylabel= ylab, **kwarg)
        self.KS_fitax = self.KS_hist[1]
        if linefit=='double': 
            self.KS_params, self.KS_paramerr = fit.fit_double(self.KS_ridgept)
            yfit = fit.doubline(self.KS_ridgept[0,:],*self.KS_params)
        elif linefit == 'single':
            self.KS_params, self.KS_paramerr = fit.fit_single(self.KS_ridgept)
            yfit = fit.line(self.KS_ridgept[0,:], *self.KS_params)
        
        self.KS_fitax.plot(self.KS_ridgept[0,:], yfit, color = 'yellow')
        return(self.KS_hist, self.KS_params, self.KS_paramerr)
    
    def MGMS_ridge(self,linefit = 'double', **kwarg):
        xlab = r'log$_{10} (\Sigma_* /$ [%s])' % self.s_mass_unit
        ylab = r'log$_{10} (\Sigma_{\mathrm{gas}} /$ [%s])' % self.gas_unit
        self.MGMS_hist, self.MGMS_ridgept, self.MGMS_histvals = fit.find_ridge(self.s_mass, self.g_mass, xlabel=xlab, ylabel=ylab, **kwarg)
        self.MGMS_fitax = self.MGMS_hist[1]
        if linefit=='double': 
            self.MGMS_params, self.MGMS_paramerr = fit.fit_double(self.MGMS_ridgept)
            yfit=fit.doubline(self.MGMS_ridgept[0,:], *self.MGMS_params)
        elif linefit == 'single':
            self.mGMS_params, self.MGMS_paramerr = fit.fit_single(self.MGMS_ridgept)
            yfit = fit.line(self.MGMS_ridgept[0,:], *self.MGMS_params)

        self.MGMS_fitax.plot(self.MGMS_ridgept[0,:], yfit, color = 'yellow')
                    
        return(self.MGMS_hist, self.MGMS_params, self.MGMS_paramerr)

        """
        if fittype != 'Gauss': fyerr=None
        
        if fitline == '1line': popt,pcov = curve_fit(line, fx, fy, sigma=fyerr, nan_policy='omit')
        elif fitline == '2line': 
            #set bounds such that x0 is within xrange
            bounds = ((-1*np.inf, -1*np.inf, -1*np.inf, xrange[0]), (np.inf, np.inf, np.inf, xrange[1]))
            popt, pcov = curve_fit(doubline, fx, fy, sigma=fyerr, nan_policy='omit', bounds=bounds)
        # obtain errors from the covariant matrix
        perr = np.sqrt(np.diag(pcov))

        #if not savefitparams is None: np.savetxt(savefitparams, np.vstack((popt,perr)).T)

        #if not savefitfig is None:
        ax.scatter(fx, fy, c='black', marker='o', zorder=2)
        if fitline == '1line': ax.plot(fx, line(fx, popt[0],popt[1]), color = 'cyan')
        elif fitline == '2line': ax.plot(fx, doubline(fx, popt[0],popt[1],popt[2],popt[3]), color='cyan')
            #plt.savefig(savefitfig)

        return(popt, perr, hist, )
        #update returns to feed into a wrapper function for specific relations
        #wrapper will return fit and save variables to the class
        #specifically, pass then save figure, ridge points, fit params
        """

#add a double gauss??


