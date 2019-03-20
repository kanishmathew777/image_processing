from cropping_approach.constants.config_fields_constants import NAME, PAGE, FIELDS, PARENT, PROCESS, RESULT, \
    SAVED_FOLDER, NUMPY_ARRAY, SAVED_IMAGE_NAME, SAVED_PATH, OUTPUT_FOLDER, IMAGE_PATH, CROPPED_STATUS, \
    PROCESS_PARAMS, PARENT_FOLDER, CONTOUR_APPROACH, APPROACH

from cropping_approach.constants.medical_etf_field_names import PATIENT_DETAILS, MEDICAL_DOCTORS, MEDICAL_PLAN


fieldname_index = {
    PATIENT_DETAILS: 0,
    MEDICAL_PLAN: 1,
    MEDICAL_DOCTORS: 2,
}


def medical_etf_getfieldindex(fieldname):
    try:
        index = fieldname_index[fieldname]
    except KeyError:
        index = None
    return index


def medical_etf_config(image_path, output_folder, form_name, page=1):
    form_config = {
        IMAGE_PATH: image_path,
        NAME: form_name,
        PAGE: page,
        PARENT_FOLDER: "{}/{}/".format(output_folder, form_name),
        OUTPUT_FOLDER: output_folder,
        FIELDS: [
            {
                NAME: PATIENT_DETAILS,
                RESULT: {
                    SAVED_FOLDER: "{}/{}/page_{}".format(output_folder, form_name, page),
                    SAVED_IMAGE_NAME: "{}.png".format(PATIENT_DETAILS),
                    SAVED_PATH: "{}/{}/page_{}/{}.png".format(output_folder, form_name, page, PATIENT_DETAILS),
                    NUMPY_ARRAY: None
                },
                PROCESS: {
                    APPROACH: CONTOUR_APPROACH,
                    PROCESS_PARAMS: {
                        "top_distance": 0.12,
                        "bottom_distance": 0.22,
                        "left_distance": 0,
                        "right_distance": 1.0,
                        "contour_min_height": 10,
                        "contour_min_width": 10,
                        "contour_min_area": 0.01
                    }
                },
                PARENT: None,
                CROPPED_STATUS: False
            },
            {
                NAME: MEDICAL_PLAN,
                RESULT: {
                    SAVED_FOLDER: "{}/{}/page_{}".format(output_folder, form_name, page),
                    SAVED_IMAGE_NAME: "{}.png".format(MEDICAL_PLAN),
                    SAVED_PATH: "{}/{}/page_{}/{}.png".format(output_folder, form_name, page, MEDICAL_PLAN),
                    NUMPY_ARRAY: None
                },
                PROCESS: {
                    APPROACH: CONTOUR_APPROACH,
                    PROCESS_PARAMS: {
                        "top_distance": 0.20,
                        "bottom_distance": 0.30,
                        "left_distance": 0,
                        "right_distance": 1.0,
                        "contour_min_height": 0,
                        "contour_min_width": 0,
                        "contour_min_area": 0.01
                    }
                },
                PARENT: None,
                CROPPED_STATUS: False
            },
            {
                NAME: MEDICAL_DOCTORS,
                RESULT: {
                    SAVED_FOLDER: "{}/{}/page_{}".format(output_folder, form_name, page),
                    SAVED_IMAGE_NAME: "{}.png".format(MEDICAL_DOCTORS),
                    SAVED_PATH: "{}/{}/page_{}/{}.png".format(output_folder, form_name, page, MEDICAL_DOCTORS),
                    NUMPY_ARRAY: None
                },
                PROCESS: {
                    APPROACH: CONTOUR_APPROACH,
                    PROCESS_PARAMS: {
                        "top_distance": 0.285,
                        "bottom_distance": 0.82,
                        "left_distance": 0,
                        "right_distance": 1.0,
                        "contour_min_height": 0,
                        "contour_min_width": 0,
                        "contour_min_area": 0.01
                    }
                },
                PARENT: None,
                CROPPED_STATUS: False
            }
        ]
    }

    return form_config
