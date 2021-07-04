#-- author: @avialxee ---#--#
#from radmap import rad_helpers
from ._helpers import vz_query
import numpy as np


class RadioMap:

    def __init__(self, position='', radius=float(0.12)) -> None:
        self.position = str(position)
        self.radius = float(radius)

        self.wcs = None
        self.status = 403
        self.info = 'not available yet'
        self.msg = []

    def throw_output(self):
        """
        returns output showing status of output. 
        """
        return {'status' : self.status, 'info': self.info, 'message':str(self.msg)}

    def spectral_index(self, tgss, nvss):
        """
        
        alpha =  - log(tgss_s/nvss_s)/log(tgss_v/nvss_v)
        TODO: error calculations.
        """
        factor = 150/1420 # tgss_v/nvss_v
        px = []
        try:
            tgss, nvss, dim = self._sanitize_svy(tgss,nvss)
            self.status = 200
            self.info = 'success'
            si = -np.round(np.log(np.divide(tgss, nvss))/np.log(factor), 3)
            self.msg.append({'max spectral index': np.max(np.reshape(si, dim))})
            return np.reshape(si, dim)
        except Exception as e:
            self.status = 417
            self.info = 'failed'
            self.msg.append({'exception': str(e)})
            return 'failed'
    
    @staticmethod
    def _sanitize_svy(tgss, nvss):
        tgss, nvss = np.array(tgss), np.array(nvss)
        dim = tgss.shape
        tgss, nvss = tgss.flat, nvss.flat
        return tgss, nvss, dim


#tgss = [[1, 12, 3], [2, 22, 32]]
#nvss = [[12, 2, 13], [12, 2, 0.2]]
#tgss = np.array(tgss)
#ins = RadioMap()
#
#print(tgss)
#print(nvss)
#print(ins.spectral_index(tgss, nvss))
#print(ins.throw_output())