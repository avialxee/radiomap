#-- author: @avialxee ---#--#
#from radmap import rad_helpers
from rad_helpers import vz_query


class RadioMap:

    def __init__(self, position='', radius=float(0.12)) -> None:        
        self.position = str(position)
        self.radius = float(radius)

        self.wcs = None
        self.status = 403
        self.info = 'not available yet'
        self.otext = ''

    def throw_output(self):
        """
        returns output showing status of output. 
        """
        return self.status, self.info, self.otext

    def spectral_index(self, tgss, nvss):
        pass
