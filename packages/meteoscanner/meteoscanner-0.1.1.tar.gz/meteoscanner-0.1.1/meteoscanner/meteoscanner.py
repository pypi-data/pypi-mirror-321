import xarray as xr, matplotlib.pyplot as plt, numpy as np, metpy as mp, matplotlib.animation as animation
from metpy.interpolate import cross_section, geodesic
import cartopy.crs as ccrs 
import cartopy.feature as cfeature
import matplotlib.colors as mplc
from IPython import display
from functools import partial
from Coordinfo import Coordinfo
from scipy.interpolate import interp1d

#Take this for reference!
#Move to json?

def default():
    pv_cmap = list(reversed(['#f80000', '#fa2c0c', '#fc4017', '#fe5121', '#ff5f2c', '#ff6d36', '#ff7a40', 
               '#ff864a', '#ff9153', '#ff9c5d', '#ffa666', '#ffb070', '#ffba79', '#ffc383', 
               '#d5b17c', '#b29e73', '#968965', '#867152', '#845336', '#9b0000']))
    w_cmap = list(reversed(['#00007f', '#2f278e', '#49469c', '#5f65aa', '#7485b8', '#8aa5c5', '#a4c6d1', '#fbfbdc', '#fbfbdc', '#ffdea4', '#ffcd88', '#ffbb6c', '#ffa952', '#ff9538', '#ff7f1f', '#ff6600']))
    pv_cmap = mplc.ListedColormap(pv_cmap)
    w_cmap = mplc.ListedColormap(w_cmap)

    default={'contour':{
                    'thta':{'level': np.arange(250, 450, 3),
                            'color':'red',
                            'linewidths':1,
                            'title':"Potential temperature (K)",
                            'linestyle': 'dashed'},
                        'z':{'level': np.arange(0, 150000, 60),
                            'color':'black',
                            'linewidths':1, 
                            'title': "Geopotential height (m)"},
                        't':{'level': np.arange(0, 400, 3),
                            'color':'black',
                            'linewidths':1, 
                            'title': "Temperature (K)"}},
                'fill':{
                    'vo':{'level': np.arange(5e-5,40e-5,5e-5),
                            'cmap':plt.cm.YlOrRd,
                            'title': "Relative vorticity(s^-1)",
                            'extend': "max"},
                        'pv':{'level': np.arange(-1e-6,9.1e-6,0.5e-6),
                            'cmap':pv_cmap,
                            'title': "Potential vorticity(PVU)"},
                        'w':{'level': np.arange(-4, 4.1, 0.5),
                            'cmap':w_cmap,
                            'extend': 'both',
                            'title': "Omega(Pa/s)"}}}
    return default
  


def selection(dataset,  vrbs, extent=None, plevel=None, tidx=None):
    r'''
    Parameters
    ----------
    dataset: 'xarray.Dataset' 
        The dataset imported before.
    vrbs: 'list'
        Variables want to keep in the new xarray dataset. Should be a list of names consistent with the name of variable in the xarray.Dataset (Or what resutns by doing list(dataset.keys())).
        Example:['t', 'z', 'w']
    extent=None: 'list'
        Should be 2 pairs of lat, lon values in a least, use the dataset's span in lat&lon if not specified.
        (Example: [-130,-60,20, 52] (This is a CONUS view!))
    plevel:'int'
        The pressure level want to keep in the new dataset.
        (One level only)
    tidx:'int'
        Time index in the old dataset that you want to keep in the new dataset.
        (One time only)
    
    Returns
    -------
    'xarray.Dataset'
        The filtered dataset. 
    '''
    if extent==None:
        extent=[dataset.lon.values[0], dataset.lon.values[-1], dataset.lat.values[-1], dataset.lat.values[0]]
    if plevel!=None:
        temp=dataset[vrbs]
        dataset=temp.sel(pressure=plevel, lat=slice(extent[3], extent[2]), lon=slice(extent[0], extent[1]))
    else: 
        temp=dataset[vrbs]
        dataset=temp.sel(lat=slice(extent[3], extent[2]), lon=slice(extent[0], extent[1]))
    if tidx==None:
        return dataset
    else:
        return dataset.isel(time=tidx)
    
def decimal(catagory):
    number = catagory["level"][0]
    out = len("{:.20f}".format(float(number)).strip("0").split(".")[1])
    return out
    
def core(self, ax, colorbar = True):
        x = self.x
        y = self.y
        dataset = self.dataset
        plotfile = self.plotfile
        ax.add_feature(cfeature.LAND, facecolor='0.8')
        countries=cfeature.NaturalEarthFeature(category="cultural", scale="110m", 
                                            facecolor="none", name="admin_0_boundary_lines_land")
        ax.add_feature(countries, linewidths=2, edgecolor="black")
        ax.add_feature(cfeature.STATES.with_scale('50m'), linewidths=0.5)
        ax.coastlines(color='k')
        
        title=' ' #Making initial space to the title, 
                # IMPORTANT: everytime a new variable is read, a new string is added. 
        
        ###Part for plotting, based on the format of plotfile, the variable in the dataset can be referenced to 
        #either plotted by contourf or just contour. 
        for i in list(dataset.keys()):
            #See if the parameter is in the 'contour catagory of the plotfile
            if i.lower() in list(plotfile['contour'].keys()): #A safety measure for matching the case between the variable name in the dataset and the plot parameters.
                renders=plotfile['contour'][i.lower()] #making all the parameters in this sub-dictionary of this plot to under one variable, so there is less length when reference later.
                #Actual plotting
                fix = 1
                min_title = renders['title']
                if decimal(renders) > 2:
                    fix = 10**decimal(renders)
                    loc = renders["title"].find("(")
                    min_title = renders["title"][:loc+1] + f"10e-{decimal(renders)}" + renders["title"][loc+1:]
                #Optional!
                lstyle = renders['linestyle'] if 'linestyle' in renders else 'solid'
                etd = renders['extend'] if 'extend' in renders else 'neither'
                graph=ax.contour(x, y, dataset[i]*fix,    
                            levels=renders['level']*fix, colors=renders['color'], linewidths=renders['linewidths'], 
                            linestyles = lstyle, extend = etd)
                #Adding label on the contour
                graph.clabel(graph.levels[1::2], fontsize=8, colors=renders['color'], inline=1,
                            inline_spacing=8, fmt='%i', rightside_up=True, use_clabeltext=True)
                
                #Adding the variable to the title extracted from the pre set file.
                title+=min_title+'('+renders['color']+'), '
                
            #See if the parameter is in the fill catagory of the plotfile
            elif i.lower() in list(plotfile['fill'].keys()):
                renders=plotfile['fill'][i.lower()]
                #Actual plotting
                fix = 1
                min_title = renders['title']
                if decimal(renders) > 2:
                    fix = 10**decimal(renders)
                    loc = renders["title"].find("(")
                    min_title = renders["title"][:loc+1] + f"10e-{decimal(renders)}" + renders["title"][loc+1:]
                #Optional!
                etd = renders['extend'] if 'extend' in renders else 'neither'
                graph=ax.contourf(x, y, dataset[i]*fix,
                            levels=renders['level']*fix, cmap=renders['cmap'], extend=etd)
                im_ratio = len(x)/len(y)
                if colorbar == True:
                    clb=plt.colorbar(graph, orientation='vertical', ax=ax,fraction=0.03*im_ratio, pad=0.01)
                    clb.ax.locator_params(nbins=len(renders['level']))
                    clb.set_label(label=min_title, fontsize=12) 
                
                #Adding the variable to the title extracted from the pre set file.
                title+=min_title+', '
        return title, ax
    
def baseplot(dataset,plotfile = 'default', info = False, fig = None):
    
    if plotfile == 'default':
        plotfile = default()

    #Parameter extraction:
    for i in list(dataset.coords):
        if i.lower() in 'latitudes':
            y=dataset[i].values
        elif i.lower() in 'longitudes':
            x=dataset[i].values
        elif i.lower() in ['pressure', 'isobaricinhpa'] or  i.lower() in 'pressure':
            z=dataset[i]
        else: 
            continue

    #Base plot setting:
    if fig == None:
        length = 8*round(abs(float(x[-1]) - float(x[0]))/abs(float(y[-1]) - float(y[0]))*5)/5
        fig, ax=plt.subplots(1,1, figsize=(length+2,8), subplot_kw={'projection':ccrs.PlateCarree()})
    else:
        plt.clf()
        ax = fig.add_subplot(111, projection=ccrs.PlateCarree())
    
    mapinfo = Coordinfo(x = x, y = y, dataset = dataset, plotfile=plotfile)
    graph = None
    title, graph = core(mapinfo, ax)
            
    #Adding the suptitle, since every variable bring a comma when attached to the title string. slice out the last comma and add a space here.
    plt.suptitle(title[:-2]+' ', fontsize=14)
    #Adding the time, this is in datetime format!!!
    graph.set_title("Valid time:"+ str(dataset["time"].dt.strftime("%Y-%m-%d %H:%MZ").values), loc='right')
    #Adding the level
    graph.set_title(z.attrs['long_name'].capitalize()+' level: '
              +str(int(dataset.pressure.values))+z.attrs['units'], loc='left')
            
    #Obtaining interval for lat/lon (5 degs):
    x_int=round(5/(abs(x[0]-x[1])))
    y_int=round(5/(abs(y[0]-y[1])))
    #Set up x, y labels , ticks.
    plt.xticks(ticks=x[::x_int], labels=[str(i) for i in x[::x_int]]) 
    plt.yticks(ticks=y[::y_int], labels=[str(i) for i in y[::y_int]])
    plt.xlabel("Longitude (Deg)", fontsize=12)
    plt.ylabel("Latitude (Deg)", fontsize=12)
    if info != False:
        return graph, mapinfo
    return graph

def estimation(dataset, locations = [], width = 7, steps = 25, plotfile='default'):
    
    r'''
    Parameters
    ----------
    dataset: 'xarray.Dataset' 
        The dataset imported before.
    locations: 'list'
        Pairs of lat, lon values in a list.
        This is the initial point!!!
    width: 
        Width of the cross section, default is 7 degrees.
    steps:
        Number of cross sections you want to take between the start and the end, default is 25 steps.
    plotfile: 'dict' or 'str: ("default" only)'
        A dictionary of plotting parameters that explained in README!
        If input is default, the default setting dictionary will be used
        
    Returns
    -------
    'tuple'
        A tuple storing the coordinate of 3 critical points for the scanner. 
    '''
    
    ax, mapinfo= baseplot(dataset, plotfile=plotfile, info=True)
    if locations != []:

        #Marking the wanted location for crossection
        lats = []
        lons = []
        for i in range(len(locations)//2):
            if type(locations[2*i])in [int, float]  and type(locations[2*i+1])in [int, float] :
                if i == 0:
                    ax.scatter(marker='.', x=locations[2*i+1], y=locations[2*i], transform=ccrs.PlateCarree(), s=500, c='red', edgecolors ='w', zorder=5)
                    lats.append(locations[2*i])
                    lons.append(locations[2*i+1])
                elif i == len(locations)//2-1:
                    ax.scatter(marker='.', x=locations[2*i+1], y=locations[2*i], transform=ccrs.PlateCarree(), s=500, c='Teal', edgecolors ='w', zorder=5)
                    lats.append(locations[2*i])
                    lons.append(locations[2*i+1])
                else:
                    ax.scatter(marker='.', x=locations[2*i+1], y=locations[2*i], transform=ccrs.PlateCarree(), s=500, c='orange', edgecolors ='w', zorder=5)
                    lats.append(locations[2*i])
                    lons.append(locations[2*i+1])
            # if type(pos1[0])in [int, float] and type(pos1[1])in [int, float] :
            #     ax.scatter(marker='.', x=pos1[1], y=pos1[0], transform=ccrs.PlateCarree(), s=500, c='Red', edgecolors ='w',zorder=5)
            # if type(pos2[0])in [int, float]  and type(pos2[1])in [int, float] :
            #     ax.scatter(marker='.', x=pos2[1], y=pos2[0], transform=ccrs.PlateCarree(), s=500, c='Orange', edgecolors ='w',zorder=5)
            # if type(pos3[0])in [int, float]  and type(pos3[1])in [int, float] :
            #     ax.scatter(marker='.', x=pos3[1], y=pos3[0], transform=ccrs.PlateCarree(), s=500, c='Teal', edgecolors ='w', zorder=5)
                
        lons = np.array(lons)
        lats = np.array(lats)
        if len(lats) == 2:
            X_Y_Spline = interp1d(lats, lons, kind='linear')
            X_ = np.linspace(lons.min(), lons.max(), steps)
            Y_ = X_Y_Spline(X_)

        else:
            if (lons[0] != min(lons) and lons[0] != max(lons)) or (lons[-1] != min(lons) and lons[-1] != max(lons)):
                X_Y_Spline = interp1d(lats, lons, kind='quadratic')
                X_ = np.linspace(lats.min(), lats.max(), steps)
                Y_ = X_Y_Spline(X_)
                dum = X_
                X_ = Y_
                Y_ = dum

            else:
                X_Y_Spline = interp1d(lons, lats, kind='quadratic')
                X_ = np.linspace(lons.min(), lons.max(), steps)
                Y_ = X_Y_Spline(X_)

        Xout = []
        Yout = []
        width = width/2
        for i in range(len(X_) - 2):
            dx = X_[i+2] - X_[i]
            dy = Y_[i+2] - Y_[i]
            ang = np.arctan2(dy, dx)
            Xout.append([X_[i+1] - width*np.sin(ang), X_[i+1] + width*np.sin(ang)]) #sin(90deg - x) = cos(x)
            Yout.append([Y_[i+1] + width*np.cos(ang), Y_[i+1] - width*np.cos(ang)])
            ax.plot(Xout[i], Yout[i], lw = 1, color ='k', transform=ccrs.PlateCarree())
            ax.scatter(marker='.', x=Xout[i][0], y=Yout[i][0], transform=ccrs.PlateCarree(), s=250, c='k', edgecolors ='w', zorder=5)
            ax.scatter(marker='.', x=Xout[i][1], y=Yout[i][1], transform=ccrs.PlateCarree(), s=250, c='k', edgecolors ='w', zorder=5)

        plt.plot(X_, Y_, transform=ccrs.PlateCarree())
        
    plt.show()
    
    #Confirmation
    confirm=input("No change/Exit? [y/n]: ")
    
    if confirm.lower()=='y': #You can also put a capital Y! 
        if locations == []:
            return None
        else:
            start = []
            end = []
            for k in range(len(Xout)): #Formatting the output for future function
                start.append([Yout[k][0], Xout[k][0]])
                end.append([Yout[k][1], Xout[k][1]])
            #plt.clf() 
            print("Output: (lat/lon1, lat/lon2)"+f'({locations[0]}/{locations[1]}, {locations[-2]}/{locations[-1]})') #Print out for reference if forget to assign variable
            return [start, end], mapinfo
        
    else: #Ask for new coordinate info for draw the map again.
        fix=input('Type change:').split(',')
        plt.clf() 
        #Typing the distance should be in a following format: 
        #[Start point lat,lon pair, Initial crossection end point lat, lon pair, track end point lat, lon pair]
        locations = []
        for value in fix:
            locations.append(float(value))

        #Deviding the typed location into paird for function to recognize 
        print("Current: (lat/lon1, lat/lon2)"+f'({locations[0]}/{locations[1]}, {locations[-2]}/{locations[-1]})')
        return estimation(dataset=dataset, locations = locations, plotfile=plotfile)

def estimation_3pts(dataset, pos1=[None, None], pos2=[None, None], pos3=[None, None], plotfile='default'):
    
    r'''
    Parameters
    ----------
    dataset: 'xarray.Dataset' 
        The dataset imported before.
    pos1: 'list'
        A pair of lat, lon values in a list.
        This is the initial point!!!
    pos2: 'list'
        A pair of lat, lon values in a list.
        This is the end point of your initial crossection!!!
    pos3: 'list'
        A pair of lat, lon values in a list.
         This is the start point of the last cross section!!!
    plotfile: 'dict' or 'str: ("default" only)'
        A dictionary of plotting parameters that explained in README!
        If input is default, the default setting dictionary will be used
        
    Returns
    -------
    'tuple'
        A tuple storing the coordinate of 3 critical points for the scanner. 
    '''
    
    ax, mapinfo= baseplot(dataset, plotfile=plotfile, info=True)
    

    #Marking the wanted location for crossection
    #Your initial point (pos1) in red, 
    #Your initial crossection end (pos2) in yellow, 
    #Your end of scanning (pos3) in teal
    if type(pos1[0])in [int, float] and type(pos1[1])in [int, float] :
        ax.scatter(marker='.', x=pos1[1], y=pos1[0], transform=ccrs.PlateCarree(), s=500, c='Red', edgecolors ='w',zorder=5)
    if type(pos2[0])in [int, float]  and type(pos2[1])in [int, float] :
        ax.scatter(marker='.', x=pos2[1], y=pos2[0], transform=ccrs.PlateCarree(), s=500, c='Orange', edgecolors ='w',zorder=5)
    if type(pos3[0])in [int, float]  and type(pos3[1])in [int, float] :
        ax.scatter(marker='.', x=pos3[1], y=pos3[0], transform=ccrs.PlateCarree(), s=500, c='Teal', edgecolors ='w', zorder=5)
        
    
    plt.show()
    
    #Confirmation
    confirm=input("No change/Exit? [y/n]: ")
    
    if confirm.lower()=='y': #You can also put a capital Y! 
        outcoord=[pos1[0], pos1[1], pos2[0], pos2[1], pos3[0], pos3[1]] #Formatting the output for future function
        #plt.clf() 
        print("Output: (lat/lon1, lat/lon2, lat/lon3)"+str(outcoord))#Print out for reference if forget to assign variable
        return tuple(outcoord), mapinfo
    else: #Ask for new coordinate info for draw the map again.
        coord=pos1+pos2+pos3
        fix=input('Type change:').split(',')
        plt.clf() 
        #Typing the distance should be in a following format: 
        #[Start point lat,lon pair, Initial crossection end point lat, lon pair, track end point lat, lon pair]
        for i in range(6):
            try :
                new=float(fix[i])
            except:
                continue
            coord[i]=new

        #Deviding the typed location into paird for function to recognize 
        print("Current: (lat/lon1, lat/lon2, lat/lon3)"+str(tuple(coord)))
        return estimation_3pts(dataset=dataset, pos1=coord[:2], pos2=coord[2:4], pos3=coord[4:6], plotfile=plotfile)

def scanner(slice_idx, dataset, coords, steps='default', plotfile="default", plot=True, prec = None):
    r'''
    Parameters
    ------
    slice_idx: 'int' or 'None'
        The index for the cross section steps. Make video when slice = None
    
    dataset: 'xarray.Dataset'
        The dataset you use for final scanner.

    coords: 'list'
        A list of array of coordinates used for cross-sections. 
        
    steps: 'str' or 'int'
        Number of points you want to take crossection between start and end. 

    plotfile: 'dict' or 'str'
        A dictionary of plotting parameters that explained in README!
        default is "default", which will use the default dictionary mentioned in the README!

    plot: 'bool'
        Return a plot if True, return a video if False. 
    
    prec: 'None' or 'Coordinfo.Coordinfo object'
        None for not printing the tracking plot, the other for showing it.
        
    Returns
    -------
    A video, a plot, or a matplotlib.pyplot.axes object.
    '''
    
    if plotfile == 'default':
        plotfile = default()

    if prec != None:
        lats = []
        lons = []
        for k in range(len(coords[0])):
            lats.append(coords[0][k][0])
            lats.append(coords[1][k][0])
            lons.append(coords[0][k][1])
            lons.append(coords[1][k][1])

        minlat = min(lats) - 2
        maxlat = max(lats) + 2
        minlon = min(lons) - 2
        maxlon = max(lons) + 2
        prec.fix_extent([minlon, maxlon, minlat, maxlat])

    #Clear previous plot (Especially value able when ploting for frame)
    plt.clf()
    
    #Guideing to the option of output as frame in video
    if plot==False and type(slice_idx)==int:
        global fig #Calling the global variable fig

    #Guideing to the option of output as video 
    elif plot==False and slice_idx==None:  
        #print(coords)
        fig=plt.figure(figsize=(12,8))
        #Making animation
        ani = animation.FuncAnimation(fig, partial(scanner, dataset=dataset, coords=coords, steps=steps, plotfile=plotfile, plot=False, prec=prec), 
                                      repeat=False, frames=len(coords[0])-1, interval=200)
        video = ani.to_html5_video() 
        html = display.HTML(video)
        plt.close()
        return  display.display(html)
        
    #Guideing to the option of output as one plot
    elif plot==True:
        fig=plt.figure(figsize=(12,8))

    #Raise error of putting something weird.
    else:
        raise ValueError('Set slice_idx as a number for returning plot, None and also settingtrue for printing the tracking plot plot=False for return video')
    
    #Processing the data, parse and squeeze in order to let metpy to read related pyproj information.
    #This step is referenced by Metpy's corssection page: 
    dataset=dataset.metpy.parse_cf().squeeze()
    #print(coords[0][slice_idx], coords[1][slice_idx])
    cross = cross_section(dataset, 
                          coords[0][slice_idx], 
                          coords[1][slice_idx]).set_coords(('lat', 'lon'))
    cross = cross.metpy.quantify()
    
    #Extractig the dimension in crossection
    
    #I think the new dimension, which is called as 'index' for indexing lat and lon value, is always behind the existing dimension, 
    #so I can utlize this feature to do an arbitrary indexing.
    x=cross[list(cross.dims.keys())[1]]
    y=cross[list(cross.dims.keys())[0]]
    
    #Adding Subplot:
    if prec!=None:
        ax = fig.add_subplot(111)
        bx = fig.add_axes([0.076, 0.68, 0.27, 0.2], projection=ccrs.PlateCarree())
        title, graph = core(prec, bx, colorbar=False)
        lonA = coords[0][slice_idx][1]
        latA = coords[0][slice_idx][0]
        lonB = coords[1][slice_idx][1]
        latB = coords[1][slice_idx][0]
        sign_Y = (latA - latB)/abs(latA - latB)
        sign_X = (lonA - lonB)/abs(lonA - lonB)
        slope = np.arctan(abs((latA - latB)/(lonA - lonB)))
        bx.plot([lonB, lonA],  [latB, latA], lw=2, color='k')
        
        print(f"Currently slicing: ({latA}, {lonA}), ({latB}, {lonB})")
        bx.annotate("A", (lonA -0.75 + 1*np.cos(slope)*sign_X, latA -0.75+ 1*np.sin(slope)*sign_Y),  #X, Y
                    color='k', weight = 'bold', fontsize = 14) 
        bx.annotate("B", (lonB -0.75 - 1*np.cos(slope)*sign_X, latB -0.75- 1*np.sin(slope)*sign_Y), 
                    color='k', weight = 'bold', fontsize = 14)
        
    else:
        ax = fig.add_subplot(111)
    
    title=' ' #Making initial space to the title, 
              # IMPORTANT: everytime a new variable is read, a new string is added. 
    
    ###Part for plotting, based on the format of plotfile, the variable in the crossection can be referenced to 
    #either plotted by contourf or just contour. 
    for i in list(cross.keys()):
            #See if the parameter is in the 'contour catagory of the plotfile
            if i.lower() in list(plotfile['contour'].keys()): #A safety measure for matching the case between the variable name in the dataset and the plot parameters.
                renders=plotfile['contour'][i.lower()] #making all the parameters in this sub-dictionary of this plot to under one variable, so there is less length when reference later.
                #Actual plotting
                fix = 1
                min_title = renders['title']
                if decimal(renders) > 2:
                    fix = 10**decimal(renders)
                    loc = renders["title"].find("(")
                    min_title = renders["title"][:loc+1] + f"10e-{decimal(renders)}" + renders["title"][loc+1:]
                #Optional!
                lstyle = renders['linestyle'] if 'linestyle' in renders else 'solid'
                etd = renders['extend'] if 'extend' in renders else 'neither'
                graph=ax.contour(x, y, cross[i]*fix,    
                            levels=renders['level']*fix, colors=renders['color'], linewidths = renders['linewidths'], 
                            linestyles = lstyle, extend = etd)
                #Adding label on the contour
                graph.clabel(graph.levels[1::2], fontsize=8, colors=renders['color'], inline=1,
                            inline_spacing=8, fmt='%i', rightside_up=True, use_clabeltext=True)
                
                #Adding the variable to the title extracted from the pre set file.
                title+=min_title+'('+renders['color']+'), '
                
            #See if the parameter is in the fill catagory of the plotfile
            elif i.lower() in list(plotfile['fill'].keys()):
                renders=plotfile['fill'][i.lower()]
                #Actual plotting
                fix = 1
                min_title = renders['title']
                if decimal(renders) > 2:
                    fix = 10**decimal(renders)
                    loc = renders["title"].find("(")
                    min_title = renders["title"][:loc+1] + f"10e-{decimal(renders)}" + renders["title"][loc+1:]
                #Optional!
                etd = renders['extend'] if 'extend' in renders else 'neither'
                graph=ax.contourf(x, y, cross[i]*fix,
                            levels=renders['level']*fix, cmap=renders['cmap'], extend=etd)
                im_ratio = len(x)/len(y)
                clb=plt.colorbar(graph, orientation='vertical', ax=ax,fraction=0.03*im_ratio, pad=0.01)
                clb.ax.locator_params(nbins=len(renders['level']))
                clb.set_label(label=min_title, fontsize=12) 
                
                #Adding the variable to the title extracted from the pre set file.
                title+=min_title+', '
    
    ###Part of final annotation on labels and titles.
    
    #Annotating the start and end point 
    ax.text(0, -0.04, 'A', fontsize=14, transform=ax.transAxes, weight='bold')
    ax.text(0.98, -0.04, 'B', fontsize=14, transform=ax.transAxes, weight='bold')  
    #If y axis is pressure, reverse the whole y axis:
    if list(cross.dims.keys())[0].lower()=='pressure':
        ax.set_ylim(y[0], y[-1])
        ax.set_yscale('symlog')
        ax.set_yticks(np.arange(1000, 50, -100))
        ax.set_yticklabels(np.arange(1000, 50, -100))
    #Set y axis laebls by the attributes (influding name and color).
    ax.set_ylabel(y.attrs['long_name'].capitalize()+" ("+y.attrs['units']+") ", fontsize=12)
    ax.set_xticks([]) 

        
    #Adding the sup title, since every variable bring a comma when attached to the title string. slice out the last comma and add a space here.
    plt.suptitle(title[:-2]+' ', fontsize=14)
    #Adding the time, this is in datetime format!!!
    ax.set_title(f"Valid time:"+ str(dataset["time"].dt.strftime("%Y-%m-%d %H:%MZ").values), loc='right')

    #Last part is to attach the start and end location   
    #Aviod the number to be generated in sci notation:
    np.set_printoptions(suppress=True)
    #Merge the start and the end together
    #the resulted list looks like this: [lat1, lon1, lat2, lon2]
    ori_des=np.concatenate((np.around(coords[0][slice_idx], decimals=2), np.around(coords[1][slice_idx], decimals=2)))
    #Prepare for the final position string list for appending when all the rounded coordinates is properly convereted.
    position=[]
    
    #Doing so by the ERA5 format's lat/lon representation (North is positive for lat , east is positive for lon)
    for i in range(4): #I know that the coordinate can only made by 2 lat&lon pairs or 4 numbers!!!
        if i%2==0: #odd/even difference to discern wheather a lat or a lon
            if ori_des[i]>=0: 
                lat=str(ori_des[i])+" N"
            else: 
                lat=str(ori_des[i])+" S"
            position.append(lat) #Appending the string, not doing + is because the arrangement later.
        else: 
            if ori_des[i]>=0:
                lon=str(ori_des[i])+" E"
            else:
                lon=str(ori_des[i])+" W"
            position.append(lon)
    #Final arrange ment of position, explains why not simply adding the string for the stitle. 
    ax.set_title("From: "+position[0]+", "+position[1]+", to: "+position[2]+", "+position[3]+"", loc='Left')
    return ax

def scanner_rect(slice_idx, dataset, coords, steps='default', plotfile="default", plot=True, prec = None):
    r'''
    Parameters
    ------
    slice_idx: 'int' or 'None'
        The index for the cross section steps. Make video when slice = None
    
    dataset: 'xarray.Dataset'
        The dataset you use for final scanner.

    coords: 'list'
        A list of array of coordinates seperated by the initial and end points for the scanner. 
        
    steps: 'str' or 'int'
        Number of points you want to take crossection between start and end. 

    plotfile: 'dict' or 'str'
        A dictionary of plotting parameters that explained in README!
        default is "default", which will use the default dictionary mentioned in the README!

    plot: 'bool'
        Return a plot if True, return a video if False. 
    
    prec: 'None' or 'Coordinfo.Coordinfo object'
        None for not printing the tracking plot, the other for showing it.
        
    Returns
    -------
    A video, a plot, or a matplotlib.pyplot.axes object.
    '''
    
    if plotfile == 'default':
        plotfile = default()

    if type(coords) == tuple:
        #if no steps defined, the default number of step is magnitude in degrees between the start and end point.
        if steps=='default':
            steps=np.round(((coords[0]-coords[4])**2+(coords[1]-coords[5])**2)**0.5)
        #Calculate min and max for extent
        minlat = min([coords[0], coords[2], coords[4]]) - 2
        maxlat = max([coords[0], coords[2], coords[4]]) + 2
        minlon = min([coords[1], coords[3], coords[5]]) - 2
        maxlon = max([coords[1], coords[3], coords[5]]) + 2
        if prec != None:
            prec.fix_extent([minlon, maxlon, minlat, maxlat])
        #Calculate the difference between initial crossection start/end points lat&lon difference.
        difference=[coords[0]-coords[2], coords[1]-coords[3]]
        #Obtaining the crs inforamtion for geodesic() to calculate the intermidiate points
        temp_vrb=dataset.metpy.parse_cf().squeeze()[list(dataset.keys())[0]] #Need to parse inforamtion from the dataset
        cdata=temp_vrb.metpy.pyproj_crs # Obtaining info of first data array in the dataset since the .pyproj_crs works only for dataarray type.
        coord1=geodesic(cdata, coords[:2],  coords[4:], steps=steps)#metpy.interpolate.geodesic for calculating the intermidate points. 
        #The out put is in a weird sequence ([lon, lat]) so reverse the sequence by advanced list slicing.
        coord1[:, [0,1]]=coord1[: ,[1,0]]
        #making an array for another side of the crossection by simple matrix calculation.
        coord2=coord1-difference
        coords=list([coord1, coord2]) #Returning start/end points in a list[start points, end points]
    else:
        pass
    
    #Clear previous plot (Especially value able when ploting for frame)
    plt.clf()
    
    #Guideing to the option of output as frame in video
    if plot==False and type(slice_idx)==int:
        global fig #Calling the global variable fig

    #Guideing to the option of output as video 
    elif plot==False and slice_idx==None:  
        #print(coords)
        fig=plt.figure(figsize=(12,8))
        #Making animation
        ani = animation.FuncAnimation(fig, partial(scanner_rect, dataset=dataset, coords=coords, steps=steps, plotfile=plotfile, plot=False, prec=prec), 
                                      repeat=False, frames=len(coords[0])-1, interval=200)
        video = ani.to_html5_video() 
        html = display.HTML(video)
        plt.close()
        return  display.display(html)
        
    #Guideing to the option of output as one plot
    elif plot==True:
        fig=plt.figure(figsize=(12,8))

    #Raise error of putting something weird.
    else:
        raise ValueError('Set slice_idx as a number for returning plot, None and also settingtrue for printing the tracking plot plot=False for return video')
    
    #Processing the data, parse and squeeze in order to let metpy to read related pyproj information.
    #This step is referenced by Metpy's corssection page: 
    dataset=dataset.metpy.parse_cf().squeeze()
    #print(coords[0][slice_idx], coords[1][slice_idx])
    cross = cross_section(dataset, 
                          coords[0][slice_idx], 
                          coords[1][slice_idx]).set_coords(('lat', 'lon'))
    cross = cross.metpy.quantify()
    
    #Extractig the dimension in crossection
    
    #I think the new dimension, which is called as 'index' for indexing lat and lon value, is always behind the existing dimension, 
    #so I can utlize this feature to do an arbitrary indexing.
    x=cross[list(cross.dims.keys())[1]]
    y=cross[list(cross.dims.keys())[0]]
    
    #Adding Subplot:
    if prec!=None:
        ax = fig.add_subplot(111)
        bx = fig.add_axes([0.076, 0.68, 0.27, 0.2], projection=ccrs.PlateCarree())
        title, graph = core(prec, bx, colorbar=False)
        lonA = coords[0][slice_idx][1]
        latA = coords[0][slice_idx][0]
        lonB = coords[1][slice_idx][1]
        latB = coords[1][slice_idx][0]
        sign_Y = (latA - latB)/abs(latA - latB)
        sign_X = (lonA - lonB)/abs(lonA - lonB)
        slope = np.arctan(abs((latA - latB)/(lonA - lonB)))
        bx.plot([lonB, lonA],  [latB, latA], lw=2, color='k')

        print(f"Currently slicing: ({latA}, {lonA}), ({latB}, {lonB})")
        bx.annotate("A", (lonA -0.75 + 1*np.cos(slope)*sign_X, latA -0.25+ 1.5*np.sin(slope)*sign_Y),  #X, Y
                    color='k', weight = 'bold', fontsize = 14) 
        bx.annotate("B", (lonB -0.75 - 1*np.cos(slope)*sign_X, latB  -0.25- 1.5*np.sin(slope)*sign_Y), 
                    color='k', weight = 'bold', fontsize = 14)
    else:
        ax = fig.add_subplot(111)
    
    title=' ' #Making initial space to the title, 
              # IMPORTANT: everytime a new variable is read, a new string is added. 
    
    ###Part for plotting, based on the format of plotfile, the variable in the crossection can be referenced to 
    #either plotted by contourf or just contour. 
    for i in list(cross.keys()):
            #See if the parameter is in the 'contour catagory of the plotfile
            if i.lower() in list(plotfile['contour'].keys()): #A safety measure for matching the case between the variable name in the dataset and the plot parameters.
                renders=plotfile['contour'][i.lower()] #making all the parameters in this sub-dictionary of this plot to under one variable, so there is less length when reference later.
                #Actual plotting
                fix = 1
                min_title = renders['title']
                if decimal(renders) > 2:
                    fix = 10**decimal(renders)
                    loc = renders["title"].find("(")
                    min_title = renders["title"][:loc+1] + f"10e-{decimal(renders)}" + renders["title"][loc+1:]
                #Optional!
                lstyle = renders['linestyle'] if 'linestyle' in renders else 'solid'
                etd = renders['extend'] if 'extend' in renders else 'neither'
                graph=ax.contour(x, y, cross[i]*fix,    
                            levels=renders['level']*fix, colors=renders['color'], linewidths=renders['linewidths'], 
                            linestyles = lstyle, extend = etd)
                #Adding label on the contour
                graph.clabel(graph.levels[1::2], fontsize=8, colors=renders['color'], inline=1,
                            inline_spacing=8, fmt='%i', rightside_up=True, use_clabeltext=True)
                
                #Adding the variable to the title extracted from the pre set file.
                title+=min_title+'('+renders['color']+'), '
                
            #See if the parameter is in the fill catagory of the plotfile
            elif i.lower() in list(plotfile['fill'].keys()):
                renders=plotfile['fill'][i.lower()]
                #Actual plotting
                fix = 1
                min_title = renders['title']
                if decimal(renders) > 2:
                    fix = 10**decimal(renders)
                    loc = renders["title"].find("(")
                    min_title = renders["title"][:loc+1] + f"10e-{decimal(renders)}" + renders["title"][loc+1:]
                #Optional!
                etd = renders['extend'] if 'extend' in renders else 'neither'
                graph=ax.contourf(x, y, cross[i]*fix,
                            levels=renders['level']*fix, cmap=renders['cmap'], extend=etd)
                im_ratio = len(x)/len(y)
                clb=plt.colorbar(graph, orientation='vertical', ax=ax,fraction=0.03*im_ratio, pad=0.01)
                clb.ax.locator_params(nbins=len(renders['level']))
                clb.set_label(label=min_title, fontsize=12) 
                
                #Adding the variable to the title extracted from the pre set file.
                title+=min_title+', '
    
    ###Part of final annotation on labels and titles.
    
    #Annotating the start and end point 
    ax.text(0, -0.04, 'A', fontsize=14, transform=ax.transAxes, weight='bold')
    ax.text(0.98, -0.04, 'B', fontsize=14, transform=ax.transAxes, weight='bold')  
    #If y axis is pressure, reverse the whole y axis:
    if list(cross.dims.keys())[0].lower()=='pressure':
        ax.set_ylim(y[0], y[-1])
        ax.set_yscale('symlog')
        ax.set_yticks(np.arange(1000, 50, -100))
        ax.set_yticklabels(np.arange(1000, 50, -100))
    #Set y axis laebls by the attributes (influding name and color).
    ax.set_ylabel(y.attrs['long_name'].capitalize()+" ("+y.attrs['units']+") ", fontsize=12)
    ax.set_xticks([]) 

        
    #Adding the sup title, since every variable bring a comma when attached to the title string. slice out the last comma and add a space here.
    plt.suptitle(title[:-2]+' ', fontsize=14)
    #Adding the time, this is in datetime format!!!
    ax.set_title(f"Valid time:"+ str(dataset["time"].dt.strftime("%Y-%m-%d %H:%MZ").values), loc='right')

    #Last part is to attach the start and end location   
    #Aviod the number to be generated in sci notation:
    np.set_printoptions(suppress=True)
    #Merge the start and the end together
    #the resulted list looks like this: [lat1, lon1, lat2, lon2]
    ori_des=np.concatenate((np.around(coords[0][slice_idx], decimals=2), np.around(coords[1][slice_idx], decimals=2)))
    #Prepare for the final position string list for appending when all the rounded coordinates is properly convereted.
    position=[]
    
    #Doing so by the ERA5 format's lat/lon representation (North is positive for lat , east is positive for lon)
    for i in range(4): #I know that the coordinate can only made by 2 lat&lon pairs or 4 numbers!!!
        if i%2==0: #odd/even difference to discern wheather a lat or a lon
            if ori_des[i]>=0: 
                lat=str(ori_des[i])+" N"
            else: 
                lat=str(ori_des[i])+" S"
            position.append(lat) #Appending the string, not doing + is because the arrangement later.
        else: 
            if ori_des[i]>=0:
                lon=str(ori_des[i])+" E"
            else:
                lon=str(ori_des[i])+" W"
            position.append(lon)
    #Final arrange ment of position, explains why not simply adding the string for the stitle. 
    ax.set_title("From: "+position[0]+", "+position[1]+", to: "+position[2]+", "+position[3]+"", loc='Left')
    return ax

def scanner_p(slice_idx, dataset, coords = "all", TtoB = True, plotfile="default"):
    r'''
    Parameters
    ------
    slice_idx: 'int' or 'None'
        The index for the dataset section steps. Make video when slice = None
    
    dataset: 'xarray.Dataset'
        The dataset you use for final scanner.

    coords: 'list'
        A list of 2 arrays of coordinates seperated by the initial and end points for the scanner. 
        
    TtoB: 'Bool'
        A boolean input for determining the orientiation of scanning.

    plotfile: 'dict' or 'str'
        A dictionary of plotting parameters that explained in README!
        default is "default", which will use the default dictionary mentioned in the README!

    plot: 'bool'
        Return a plot if True, return a video if False. 
        
    Returns
    -------
    A video.
    '''
    
    if plotfile == 'default':
        plotfile = default()

    #Clear previous plot (Especially value able when ploting for frame)
    plt.clf()

    pres = False
    for i in list(dataset.coords):
        if i.lower() in 'latitudes':
            y = dataset[i]
        elif i.lower() in 'longitudes':
            x = dataset[i]
        elif i.lower() in 'pressure':
            if i!= 'pressure':
                dataset = dataset.rename({i: 'pressure'})
            pres = True
        else: 
            continue

    if pres == False:
        raise ValueError('Please set the vertical coordinate name as "pressure" to continue')
    
    if coords == "all":
        coords = [float(y.max().values), float(x.min().values), float(y.min().values), float(x.max().values)]
    

    if type(slice_idx)==int:
        global fig #Calling the global variable fig

    elif slice_idx == None: 
        #'47.0, -125.0, 25.0, -102.0'

        length = 8*round(abs((float(coords[3]) - float(coords[1])))/abs(float(coords[0]) - float(coords[2]))*5)/5
        fig=plt.figure(figsize=(length+2,8))
        # for h in list(dataset.coords):
        #     if h.lower() in ['pressure', 'isobaricinhpa'] or  h.lower() in 'pressure':
        #         temp = dataset.rename({h:"pressure"})
        temp = dataset.sel(lat = slice(max(coords[0], coords[2]), min(coords[0], coords[2])),
                lon = slice(min(coords[1], coords[3]), max(coords[1], coords[3])))
        #     else: 
        #         continue
        #Making animation
        ani = animation.FuncAnimation(fig, partial(scanner_p, dataset=temp, coords = coords, TtoB = TtoB, plotfile=plotfile), 
                                        repeat=False, frames=len(temp.pressure)-1, interval=200)
        video = ani.to_html5_video() 
        html = display.HTML(video)
        plt.close()
        return  display.display(html)
            
    #Raise error of putting something weird.
    else:
        raise ValueError('Set slice_idx as a number for returning plot, None and also settingtrue for printing the tracking plot plot=False for return video')

    if TtoB == True:
        ds = dataset.sel(pressure = dataset.pressure.values[slice_idx])
    else:
        ds = dataset.sel(pressure = dataset.pressure.values[len(dataset.pressure)-slice_idx-1])
    
    ax = fig.add_subplot(111, projection = ccrs.PlateCarree())
    mapinfo = Coordinfo(x = x, y = y, dataset = ds, plotfile=plotfile)
    title, graph = core(mapinfo, ax)

    np.set_printoptions(suppress=True)
    ###Part of final annotation on labels and titles.
    #Set axis laebls by the attributes (influding name and color).
    x_int=round(5/(abs(float(x[0])-float(x[1]))))
    y_int=round(5/(abs(float(y[0])-float(y[1]))))
    plt.xlabel("Longitude (Deg)", fontsize=12)
    plt.ylabel("Latitude (Deg)", fontsize=12)
    plt.xticks(ticks=x.values[::x_int], labels=[str(i) for i in x.values[::x_int]]) 
    plt.yticks(ticks=y.values[::y_int], labels=[str(i) for i in y.values[::y_int]])

        
    #Adding the suptitle, since every variable bring a comma when attached to the title string. slice out the last comma and add a space here.
    plt.suptitle(title[:-2]+' ', fontsize=14)
    #Adding the time, this is in datetime format!!!
    ax.set_title(f"Valid time:"+ str(dataset["time"].dt.strftime("%Y-%m-%d %H:%MZ").values), loc='right')

    #Last part is to attach the start and end location   
    #Aviod the number to be generated in sci notation:
    #Final arrange ment of position, explains why not simply adding the string for the stitle. 
    ax.set_title(f"Pressure level: {int(ds.pressure)} hPa", loc='Left')
    return ax

def timeLapse(slice_idx, dataset, timerange = None, plotfile='default'):
    
    r'''
    Parameters
    ----------
    dataset: 'xarray.Dataset' 
        The dataset imported before.

    timerange: None or 'list'
        The time range for time lapse. None input will generate a preview plot 
        (first time in the input dataset), and then time range is asked.

    plotfile: 'dict' or 'str: ("default" only)'
        A dictionary of plotting parameters that explained in README!
        If input is default, the default setting dictionary will be used
        
    Returns
    A video, a plot, or a matplotlib.pyplot.axes object.
    -------
    
    '''


    #Parameter extraction:
    for i in list(dataset.coords):
        if i.lower() in 'latitudes':
            y=dataset[i].values
        elif i.lower() in 'longitudes':
            x=dataset[i].values
        elif i.lower() in ['pressure', 'isobaricinhpa'] or  i.lower() in 'pressure':
            if i!= 'pressure':
                dataset = dataset.rename({i: 'pressure'})
            z=dataset[i]
        else: 
            continue
        
    if not isinstance(timerange, (xr.DataArray, np.ndarray, list, set, tuple)):
        try:
            timerange = dataset.time
        except:
            raise KeyError("Please name you time dimension as 'time'!") 
        
     #Clear previous plot (Especially valuable when plotting for frame)
    plt.clf()
    
    if isinstance(slice_idx, int):
        global fig #Calling the global variable fig
        ax = fig.add_subplot(111, projection=ccrs.PlateCarree())
        print("Processing time: " + str(dataset["time"].dt.strftime("%Y-%m-%d %H:%MZ").values))
    elif slice_idx == None: 
        length = 8*round(abs(float(x[-1]) - float(x[0]))/abs(float(y[-1]) - float(y[0]))*5)/5
        fig, ax = plt.subplots(1,1, figsize=(length+2,8), subplot_kw={'projection':ccrs.PlateCarree()})
        ani = animation.FuncAnimation(fig, partial(timeLapse, dataset=dataset, timerange = timerange, plotfile=plotfile), 
                                        repeat=False, frames=len(timerange), interval=200)
        video = ani.to_html5_video() 
        html = display.HTML(video)
        plt.close()
        return  display.display(html)
            
    #Raise error of putting something weird.
    else:
        raise ValueError('Set slice_idx as a number for returning plot, None and also settingtrue for printing the tracking plot plot=False for return video')
    
    if plotfile == 'default':
        plotfile = default()

    dataset = dataset.isel(time = slice_idx) 
    ax = baseplot(dataset, plotfile=plotfile, fig = fig)
        
    return ax 
