import numpy as np


from rail.core import common_params


class CatalogConfigBase:

    sub_classes = {}

    tag = None
    bandlist = ''
    maglims = []
    band_template = ''
    band_err_template = ''
    ref_band = ''
    redshift_col = ''

    _active_tag = None
    _active_class = None
    
    def __init_subclass__(cls, **kwargs):        
        cls.sub_classes[cls.tag] = cls

    @classmethod
    def active_tag(cls):
        return cls._active_tag

    @classmethod
    def active_class(cls):
        return cls._active_class

    @classmethod
    def apply(cls, tag):
        cls._active_tag = tag
        cls._active_class = cls.sub_classes[tag]
        cls._active_class._apply()
        
    @classmethod
    def _apply(cls):
        base_dict = cls._build_base_dict()
        common_params.set_param_defaults(**base_dict)
        cls._apply_hook()
        
    @classmethod
    def _apply_hook(cls):
        return 

    @classmethod
    def band_name_dict(cls):
        return {band: cls.band_template.format(band=band) for band in cls.bandlist}

    @classmethod
    def _build_maglim_dict(cls):
        maglim_dict = {}
        for band, limx in zip(cls.bandlist, cls.maglims):
            maglim_dict[cls.band_template.format(band=band)] = limx
        return maglim_dict

    @classmethod
    def _build_a_env_dict(cls):
        a_env_dict = {}
        for band, limx in zip(cls.bandlist, cls.a_env):
            a_env_dict[cls.band_template.format(band=band)] = limx
        return a_env_dict

    @classmethod
    def _build_band_names(cls):
        return [cls.band_template.format(band=band) for band in cls.bandlist]

    @classmethod
    def _build_band_err_names(cls):
        return [cls.band_err_template.format(band=band) for band in cls.bandlist]

    @classmethod
    def _build_ref_band(cls, ref_band='i'):
        return cls.band_template.format(band=ref_band)
    
    @classmethod
    def _build_base_dict(cls):
        base_dict = {}
        base_dict.update(
            bands=cls._build_band_names(),
            err_bands=cls._build_band_err_names(),
            mag_limits=cls._build_maglim_dict(),
            band_a_env=cls._build_a_env_dict(),
            ref_band=cls._build_ref_band(cls.ref_band),
            redshift_col=cls.redshift_col,
            nondetect_val=np.nan,
            hdf5_groupname=cls.hdf5_groupname,
        )
        return base_dict

        
class HscCatalogConfig(CatalogConfigBase):

    tag = 'hsc'
    bandlist = 'grizy'
    maglims = [27.66, 27.25, 26.6, 26.24, 25.35]
    a_env = [3.64, 2.70, 2.06, 1.58, 1.31]    
    band_template = 'HSC{band}_cmodel_dered'
    band_err_template = '{band}_cmodel_magerr' 
    ref_band = 'i'
    redshift_col = 'specz_redshift'
    hdf5_groupname = ''

    
class Dc2CatalogConfig(CatalogConfigBase):

    tag = 'dc2'
    bandlist = 'ugrizy'
    maglims = [24., 27.66, 27.25, 26.6, 26.24, 25.35]
    a_env = [4.81, 3.64, 2.70, 2.06, 1.58, 1.31]    
    band_template = "mag_{band}_lsst"
    band_err_template = "mag_err_{band}_lsst"
    ref_band = 'i'
    redshift_col='true_redshift'
    hdf5_groupname = ''


class RubinCatalogConfig(CatalogConfigBase):

    tag = 'rubin'
    bandlist = 'ugrizy'
    maglims = [24., 27.66, 27.25, 26.6, 26.24, 25.35]
    a_env = [4.81, 3.64, 2.70, 2.06, 1.58, 1.31]
    band_template = "LSST_obs_{band}"
    band_err_template ="LSST_obs_{band}_err"
    ref_band = 'i'
    redshift_col='true_redshift'
    hdf5_groupname = ''


class RomanRubinCatalogConfig(CatalogConfigBase):

    tag = 'roman_rubin'
    bandlist = 'ugrizy'
    maglims = [24., 27.66, 27.25, 26.6, 26.24, 25.35]
    a_env = [4.81, 3.64, 2.70, 2.06, 1.58, 1.31]
    band_template = "LSST_obs_{band}"
    band_err_template ="LSST_obs_{band}_err"
    ref_band = 'i'
    redshift_col='redshift'
    hdf5_groupname = ''



class RomanPlusRubinCatalogConfig(CatalogConfigBase):

    tag = 'roman_plus_rubin'
    bandlist = 'ugrizy'
    maglims = [24., 27.66, 27.25, 26.6, 26.24, 25.35]
    a_env = [4.81, 3.64, 2.70, 2.06, 1.58, 1.31]
    band_template = "LSST_obs_{band}"
    band_err_template ="LSST_obs_{band}_err"
    ref_band = 'i'
    redshift_col='redshift'
    hdf5_groupname = ''

    @classmethod
    def band_name_dict(cls):
        bands = super().band_name_dict()
        bands['f'] = 'ROMAN_obs_F184'
        bands['h'] = 'ROMAN_obs_H158'
        bands['j'] = 'ROMAN_obs_J129'
        bands['y'] = 'ROMAN_obs_Y106'
        return bands
        
    @classmethod
    def _build_maglim_dict(cls):
        maglim_dict = super()._build_maglim_dict()
        maglim_dict['ROMAN_obs_F184'] = 27.5
        maglim_dict['ROMAN_obs_H158'] = 28.1
        maglim_dict['ROMAN_obs_J129'] = 27.8
        maglim_dict['ROMAN_obs_Y106'] = 27.6
        return maglim_dict

    @classmethod
    def _build_a_env_dict(cls):
        a_env_dict = super()._build_a_env_dict()
        a_env_dict['ROMAN_obs_F184'] = 1.1
        a_env_dict['ROMAN_obs_H158'] = 1.2
        a_env_dict['ROMAN_obs_J129'] = 1.3
        a_env_dict['ROMAN_obs_Y106'] = 1.4
        return a_env_dict

    @classmethod
    def _build_band_names(cls):
        bands = [cls.band_template.format(band=band) for band in cls.bandlist]
        bands += ['ROMAN_obs_F184', 'ROMAN_obs_H158', 'ROMAN_obs_J129', 'ROMAN_obs_Y016']
        return bands

    @classmethod
    def _build_band_err_names(cls):
        band_errs = [cls.band_err_template.format(band=band) for band in cls.bandlist]
        band_errs += ['ROMAN_obs_F184_err', 'ROMAN_obs_H158_err', 'ROMAN_obs_J129_err', 'ROMAN_obs_Y106_err']
        return band_errs

    @classmethod
    def _build_ref_band(cls, ref_band='i'):
        return cls.band_template.format(band=ref_band)

    
apply_defaults = CatalogConfigBase.apply
