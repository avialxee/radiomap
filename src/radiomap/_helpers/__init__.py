#     rad_helpers.py 
from astroquery.vizier import Vizier
from astropy import coordinates, units as ut


#--------------     vizier      ------------#
def vz_query(c, r, wcs):
    """
    query from vizier for NVSS and TGSS.
    ----------------------------------
    
    Input:
    ------
        coordinate : astropy coordinate,
        Radius  : astropy angle as radius of sky in float,
        wcs     : astropy wcs

    returns:
    --------
        MajorAxis (unitless) (Vizier : arcsec),
        MinorAxis (unitless) (Vizier : arcsec),
        PA  (unitless) (Vizier : deg),
        pixel based position (single arguement)
    """
    _tgss_viz, _nvss_viz, info = [None]*3
    try:
        try:
            _tviz = Vizier(columns=vzc_dict('tgss')).query_region(
                c, r, catalog=vzb_dict('tgss'))
            _tra = _tviz[0]['RAJ2000']  # *ut.deg
            _tdec = _tviz[0]['DEJ2000']  # *ut.deg
            _tMaj = _tviz[0]['Maj']
            _tMin = _tviz[0]['Min']
            if "PA" in _tviz[0].columns:
                _tPA = _tviz[0]["PA"]
            else:
                _tPA = 0
            _center_tgss = coordinates.SkyCoord(ra=_tra, dec=_tdec)
            _center_tgss_px = wcs.world_to_pixel(_center_tgss)
            _tgss_viz = [_tMaj, _tMin, _tPA, _center_tgss_px]
        finally:
            _nviz = Vizier(columns=vzc_dict('nvss')).query_region(
                c, r, catalog=vzb_dict('nvss'))
            _nra = coordinates.Angle(
                _nviz[0]['RAJ2000'], unit=ut.hour)  # .deg
            _ndec = coordinates.Angle(
                _nviz[0]['DEJ2000'], unit=ut.deg)  # .deg
            #_nrad = coordinates.Angle(_nviz[0]['RAJ2000'], unit=ut.hour).deg
            #_ndecd = coordinates.Angle(_nviz[0]['DEJ2000'], unit=ut.deg).deg for scatter plots
            _nMaj = _nviz[0]["MajAxis"]
            _nMin = _nviz[0]["MinAxis"]
            if "PA" in _nviz[0].columns:
                _nPA = _nviz[0]["PA"]
            else:
                _nPA = 0
            _center_nvss = coordinates.SkyCoord(ra=_nra, dec=_ndec)
            _center_nvss_px = wcs.world_to_pixel(_center_nvss)
            _nvss_viz = [_nMaj, _nMin, _nPA, _center_nvss_px]
    except:
        info = " no data in catalog"

    return _tgss_viz, _nvss_viz , info

def vzb_dict(svy):
    """
    vizier base dictionary
    dictionary for NVSS, TGSS catalog using vizier
    """
    base = {'tgss': 'J/A+A/598/A78/table3',
            'nvss': 'VIII/65/nvss'
            }
    if svy in base:
        return base[svy]
    elif svy == '*':
        return base
    elif svy == 'v':
        return base.values()
    elif svy == 'k':
        return base.keys()
    else:
        return "'{}' is not a valid survey. please choose one from {} or use any of '*' 'v' 'k' ".format(svy, base.keys())


def vzc_dict(svy):
    """
    vizier column dictionary
    dictionary for NVSS, TGSS column using vizier
    TODO: add column for errors too
    """
    columns = {'tgss': ['RAJ2000', 'DEJ2000', 'Maj', 'Min', 'PA'],
                'nvss': ['RAJ2000', 'DEJ2000', 'MajAxis', 'MinAxis', 'PA', '+NVSS']
                }
    if svy in columns:
        return columns[svy]
    elif svy == '*':
        return columns
    elif svy == 'v':
        return columns.values()
    elif svy == 'k':
        return columns.keys()
    else:
        return "'{}' is not a valid survey. please choose one from {} or use any of '*' 'v' 'k' ".format(svy, columns.keys())


def cli():
    pass
