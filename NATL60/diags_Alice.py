
# coding: utf-8

# In[1]:

# import modules
import xarray as xr
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy.ma as ma
import numpy as np
import netCDF4 as nc4
from scipy.io import netcdf
get_ipython().magic(u'matplotlib inline')


# In[4]:

fdir = "/home/albert/Data/NATL60/NATL60-CJM165-S/1di/2012/"
Ffile = fdir + 'NATL60-CJM165_1d_alteLABgridiF_20120813-20120813.nc'
Tfile = fdir + 'NATL60-CJM165_1d_alteLABgridiT_20120813-20120813.nc'


# In[11]:

dxu = xr.open_dataset(Tfile)['dxu'][0]
dyv = xr.open_dataset(Tfile)['dyv'][0]
dyu = xr.open_dataset(Ffile)['dyu'][0]
dxv = xr.open_dataset(Ffile)['dxv'][0]

dxug = xr.open_dataset(Tfile)['dxug'][0]
dyvg = xr.open_dataset(Tfile)['dyvg'][0]
dyug = xr.open_dataset(Ffile)['dyug'][0]
dxvg = xr.open_dataset(Ffile)['dxvg'][0]

navlon = xr.open_dataset(Tfile)['nav_lon']
navlat = xr.open_dataset(Tfile)['nav_lat']


# In[6]:

dxu.shape


# In[21]:

def cartes_dxyuv(zk):
 plt.figure(figsize=(20,40))
 plt.subplot(4,2,1)
 plt.pcolormesh(navlon,navlat,ma.masked_invalid(dxu[zk]),cmap='seismic',vmin=-0.00003,vmax=0.00003)
 plt.autoscale(tight=True)
 plt.colorbar(orientation='horizontal',ticks=[-0.00003,-0.00002,-0.00001,0,0.00001,0.00002,0.00003])
 plt.title('dxu at z='+np.string_(zk)+' in 20120813')
 plt.subplot(4,2,2)
 plt.pcolormesh(navlon,navlat,ma.masked_invalid(dxug[zk]),cmap='seismic',vmin=-0.00003,vmax=0.00003)
 plt.autoscale(tight=True)
 plt.colorbar(orientation='horizontal',ticks=[-0.00003,-0.00002,-0.00001,0,0.00001,0.00002,0.00003])
 plt.title('dxug at z='+np.string_(zk)+' in 20120813')
 plt.subplot(4,2,3)
 plt.pcolormesh(navlon,navlat,ma.masked_invalid(dyu[zk]),cmap='seismic',vmin=-0.00003,vmax=0.00003)
 plt.autoscale(tight=True)
 plt.colorbar(orientation='horizontal',ticks=[-0.00003,-0.00002,-0.00001,0,0.00001,0.00002,0.00003])
 plt.title('dyu at z='+np.string_(zk)+' in 20120813')
 plt.subplot(4,2,4)
 plt.pcolormesh(navlon,navlat,ma.masked_invalid(dyug[zk]),cmap='seismic',vmin=-0.00003,vmax=0.00003)
 plt.autoscale(tight=True)
 plt.colorbar(orientation='horizontal',ticks=[-0.00003,-0.00002,-0.00001,0,0.00001,0.00002,0.00003])
 plt.title('dyug at z='+np.string_(zk)+' in 20120813')
 plt.subplot(4,2,5)
 plt.pcolormesh(navlon,navlat,ma.masked_invalid(dxv[zk]),cmap='seismic',vmin=-0.00003,vmax=0.00003)
 plt.autoscale(tight=True)
 plt.colorbar(orientation='horizontal',ticks=[-0.00003,-0.00002,-0.00001,0,0.00001,0.00002,0.00003])
 plt.title('dxv at z='+np.string_(zk)+' in 20120813')
 plt.subplot(4,2,6)
 plt.pcolormesh(navlon,navlat,ma.masked_invalid(dxvg[zk]),cmap='seismic',vmin=-0.00003,vmax=0.00003)
 plt.autoscale(tight=True)
 plt.colorbar(orientation='horizontal',ticks=[-0.00003,-0.00002,-0.00001,0,0.00001,0.00002,0.00003])
 plt.title('dxvg at z='+np.string_(zk)+' in 20120813')
 plt.subplot(4,2,7)
 plt.pcolormesh(navlon,navlat,ma.masked_invalid(dyv[zk]),cmap='seismic',vmin=-0.00003,vmax=0.00003)
 plt.autoscale(tight=True)
 plt.colorbar(orientation='horizontal',ticks=[-0.00003,-0.00002,-0.00001,0,0.00001,0.00002,0.00003])
 plt.title('dyv at z='+np.string_(zk)+' in 20120813')
 plt.subplot(4,2,8)
 plt.pcolormesh(navlon,navlat,ma.masked_invalid(dyvg[zk]),cmap='seismic',vmin=-0.00003,vmax=0.00003)
 plt.autoscale(tight=True)
 plt.colorbar(orientation='horizontal',ticks=[-0.00003,-0.00002,-0.00001,0,0.00001,0.00002,0.00003])
 plt.title('dyvg at z='+np.string_(zk)+' in 20120813')

 plt.savefig('/home/albert/Data/NATL60/NATL60-CJM165-PLOTS/cartes_z'+np.string_(zk)+'_dxyuv_dxyugvg_y2012m11d07.png')


# In[17]:

zk=0
np.string_(zk)


# In[22]:

cartes_dxyuv(0)


# In[23]:

cartes_dxyuv(10)


# In[24]:

cartes_dxyuv(100)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



