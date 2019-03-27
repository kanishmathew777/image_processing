from .star_stenr import starstenr_config, starstenr_getfieldindex
from .star_stenrtp import starstenrtp_config, starstenrtp_getfieldindex
from .star_plus_spenrd import starplus_spenrd_config, starplus_spenrd_getfieldindex
from .star_plus_spenrm import starplus_spenrm_config, starplus_spenrm_getfieldindex
from .star_kids import star_kids_config, star_kids_getfieldindex

from .dental_deenr import dental_deenr_config, dental_deenr_getfieldindex
from .dental_dtf import dental_dtf_config, dental_dtf_getfieldindex

from .medical_etf import medical_etf_config, medical_etf_getfieldindex
from .medical_mmp4 import medical_mmp4_config, medical_mmp4_getfieldindex

from .constant_form_names import STAR_KIDS, STAR_PLUS_SPENRD, STAR_PLUS_SPENRM, STAR_STENR, STAR_STENRTP, \
    DENTAL_DEENR, DENTAL_DTF, MEDICAL_ETF, MEDICAL_MMP4


def get_field_index(fieldname, form_name):
    switcher = {
        STAR_STENR: starstenr_getfieldindex,
        STAR_STENRTP: starstenrtp_getfieldindex,
        STAR_PLUS_SPENRD: starplus_spenrd_getfieldindex,
        STAR_PLUS_SPENRM: starplus_spenrm_getfieldindex,
        STAR_KIDS: star_kids_getfieldindex,

        DENTAL_DEENR: dental_deenr_getfieldindex,
        DENTAL_DTF: dental_dtf_getfieldindex,

        MEDICAL_ETF: medical_etf_getfieldindex,
        MEDICAL_MMP4: medical_mmp4_getfieldindex,
    }

    func = switcher.get(form_name, lambda: None)

    return func(fieldname)


def initialise_form_config(image_path, output_folder, form_name, page=1):

    switcher = {
        STAR_STENR: starstenr_config,
        STAR_STENRTP: starstenrtp_config,
        STAR_PLUS_SPENRD: starplus_spenrd_config,
        STAR_PLUS_SPENRM: starplus_spenrm_config,
        STAR_KIDS: star_kids_config,

        DENTAL_DEENR: dental_deenr_config,
        DENTAL_DTF: dental_dtf_config,

        MEDICAL_ETF: medical_etf_config,
        MEDICAL_MMP4: medical_mmp4_config
    }

    func = switcher.get(form_name, lambda: [])

    return func(image_path, output_folder, form_name, page=page)
