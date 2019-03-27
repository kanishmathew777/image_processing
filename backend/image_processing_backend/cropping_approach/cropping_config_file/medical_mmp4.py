from cropping_approach.constants.config_fields_constants import NAME, PAGE, FIELDS, PARENT, PROCESS, RESULT, \
    SAVED_FOLDER, NUMPY_ARRAY, SAVED_IMAGE_NAME, SAVED_PATH, OUTPUT_FOLDER, IMAGE_PATH, CROPPED_STATUS, \
    PROCESS_PARAMS, PARENT_FOLDER, VERTICAL_HORIZONTAL_COMBINE_APPROACH, APPROACH, CONTOUR_SORT_APPROACH

from cropping_approach.constants.medical_mmp4_field_names import MEDICAL_PLAN, PATIENT_DETAILS, MEDICAL_ID, \
    MEDICARE, PATIENT_NAME, PATIENT_ADDRESS, PATIENT_ANOTHER_PHONE_NO, PATIENT_CITY, PATIENT_COUNTY, PATIENT_DOB, \
    PATIENT_ESRD, PATIENT_PHONE_NO, PATIENT_SEX, PATIENT_STATE,  PATIENT_ZIP_CODE


fieldname_index = {
    MEDICAL_PLAN: 0,
    PATIENT_DETAILS: 1,
    MEDICAL_ID: 2,
    MEDICARE: 3,
    PATIENT_NAME: 4,
    PATIENT_DOB: 5,
    PATIENT_SEX: 6,
    PATIENT_PHONE_NO: 7,
    PATIENT_ANOTHER_PHONE_NO: 8,
    PATIENT_ESRD: 9,
    PATIENT_ADDRESS: 10,
    PATIENT_CITY: 11,
    PATIENT_STATE: 12,
    PATIENT_ZIP_CODE: 13,
    PATIENT_COUNTY: 14,
}


def medical_mmp4_getfieldindex(fieldname):
    try:
        index = fieldname_index[fieldname]
    except KeyError:
        index = None
    return index


def medical_mmp4_config(image_path, output_folder, form_name, page=1):
    form_config = {
        IMAGE_PATH: image_path,
        NAME: form_name,
        PAGE: page,
        PARENT_FOLDER: "{}/{}/".format(output_folder, form_name),
        OUTPUT_FOLDER: output_folder,
        FIELDS: [
            {
                NAME: MEDICAL_PLAN,
                RESULT: {
                    SAVED_FOLDER: "{}/{}/page_{}".format(output_folder, form_name, page),
                    SAVED_IMAGE_NAME: "{}.png".format(MEDICAL_PLAN),
                    SAVED_PATH: "{}/{}/page_{}/{}.png".format(output_folder, form_name, page, MEDICAL_PLAN),
                    NUMPY_ARRAY: None
                },
                PROCESS: {
                    APPROACH: VERTICAL_HORIZONTAL_COMBINE_APPROACH,
                    PROCESS_PARAMS: {
                        "top_distance": 0.38,
                        "bottom_distance": 0.50,
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
                NAME: PATIENT_DETAILS,
                RESULT: {
                    SAVED_FOLDER: "{}/{}/page_{}".format(output_folder, form_name, page),
                    SAVED_IMAGE_NAME: "{}.png".format(PATIENT_DETAILS),
                    SAVED_PATH: "{}/{}/page_{}/{}.png".format(output_folder, form_name, page, PATIENT_DETAILS),
                    NUMPY_ARRAY: None
                },
                PROCESS: {
                    APPROACH: VERTICAL_HORIZONTAL_COMBINE_APPROACH,
                    PROCESS_PARAMS: {
                        "top_distance": 0.54,
                        "bottom_distance": 1.00,
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
                NAME: MEDICAL_ID,
                RESULT: {
                    SAVED_FOLDER: "{}/{}/page_{}".format(output_folder, form_name, page),
                    SAVED_IMAGE_NAME: "{}.png".format(MEDICAL_ID),
                    SAVED_PATH: "{}/{}/page_{}/{}.png".format(output_folder, form_name, page, MEDICAL_ID),
                    NUMPY_ARRAY: None
                },
                PROCESS: {
                    APPROACH: CONTOUR_SORT_APPROACH,
                    PROCESS_PARAMS: {
                        "inner_boxes": True,
                        "top_distance": 0.00,
                        "bottom_distance": 0.18,
                        "left_distance": 0.00,
                        "right_distance": 0.52,
                        "contour_min_height": 0,
                        "contour_min_width": 0,
                        "contour_min_area": 0.01,
                    }
                },
                PARENT: PATIENT_DETAILS,
                CROPPED_STATUS: False
            },
            {
                NAME: MEDICARE,
                RESULT: {
                    SAVED_FOLDER: "{}/{}/page_{}".format(output_folder, form_name, page),
                    SAVED_IMAGE_NAME: "{}.png".format(MEDICARE),
                    SAVED_PATH: "{}/{}/page_{}/{}.png".format(output_folder, form_name, page, MEDICARE),
                    NUMPY_ARRAY: None
                },
                PROCESS: {
                    APPROACH: CONTOUR_SORT_APPROACH,
                    PROCESS_PARAMS: {
                        "inner_boxes": True,
                        "top_distance": 0.00,
                        "bottom_distance": 0.18,
                        "left_distance": 0.49,
                        "right_distance": 1.00,
                        "contour_min_height": 0,
                        "contour_min_width": 0,
                        "contour_min_area": 0.01,
                    }
                },
                PARENT: PATIENT_DETAILS,
                CROPPED_STATUS: False
            },
            {
                NAME: PATIENT_NAME,
                RESULT: {
                    SAVED_FOLDER: "{}/{}/page_{}".format(output_folder, form_name, page),
                    SAVED_IMAGE_NAME: "{}.png".format(PATIENT_NAME),
                    SAVED_PATH: "{}/{}/page_{}/{}.png".format(output_folder, form_name, page, PATIENT_NAME),
                    NUMPY_ARRAY: None
                },
                PROCESS: {
                    APPROACH: CONTOUR_SORT_APPROACH,
                    PROCESS_PARAMS: {
                        "inner_boxes": True,
                        "top_distance": 0.13,
                        "bottom_distance": 0.33,
                        "left_distance": 0.00,
                        "right_distance": 1.00,
                        "contour_min_height": 0,
                        "contour_min_width": 0,
                        "contour_min_area": 0.01,
                    }
                },
                PARENT: PATIENT_DETAILS,
                CROPPED_STATUS: False
            },
            {
                NAME: PATIENT_DOB,
                RESULT: {
                    SAVED_FOLDER: "{}/{}/page_{}".format(output_folder, form_name, page),
                    SAVED_IMAGE_NAME: "{}.png".format(PATIENT_DOB),
                    SAVED_PATH: "{}/{}/page_{}/{}.png".format(output_folder, form_name, page, PATIENT_DOB),
                    NUMPY_ARRAY: None
                },
                PROCESS: {
                    APPROACH: CONTOUR_SORT_APPROACH,
                    PROCESS_PARAMS: {
                        "inner_boxes": True,
                        "top_distance": 0.29,
                        "bottom_distance": 0.53,
                        "left_distance": 0.00,
                        "right_distance": 0.40,
                        "contour_min_height": 0,
                        "contour_min_width": 0,
                        "contour_min_area": 0.01,
                    }
                },
                PARENT: PATIENT_DETAILS,
                CROPPED_STATUS: False
            },
            {
                NAME: PATIENT_SEX,
                RESULT: {
                    SAVED_FOLDER: "{}/{}/page_{}".format(output_folder, form_name, page),
                    SAVED_IMAGE_NAME: "{}.png".format(PATIENT_SEX),
                    SAVED_PATH: "{}/{}/page_{}/{}.png".format(output_folder, form_name, page, PATIENT_SEX),
                    NUMPY_ARRAY: None
                },
                PROCESS: {
                    APPROACH: CONTOUR_SORT_APPROACH,
                    PROCESS_PARAMS: {
                        "inner_boxes": True,
                        "top_distance": 0.29,
                        "bottom_distance": 0.53,
                        "left_distance": 0.38,
                        "right_distance": 1.00,
                        "contour_min_height": 0,
                        "contour_min_width": 0,
                        "contour_min_area": 0.01,
                    }
                },
                PARENT: PATIENT_DETAILS,
                CROPPED_STATUS: False
            },
            {
                NAME: PATIENT_PHONE_NO,
                RESULT: {
                    SAVED_FOLDER: "{}/{}/page_{}".format(output_folder, form_name, page),
                    SAVED_IMAGE_NAME: "{}.png".format(PATIENT_PHONE_NO),
                    SAVED_PATH: "{}/{}/page_{}/{}.png".format(output_folder, form_name, page, PATIENT_PHONE_NO),
                    NUMPY_ARRAY: None
                },
                PROCESS: {
                    APPROACH: CONTOUR_SORT_APPROACH,
                    PROCESS_PARAMS: {
                        "inner_boxes": True,
                        "top_distance": 0.48,
                        "bottom_distance": 0.70,
                        "left_distance": 0.00,
                        "right_distance": 0.19,
                        "contour_min_height": 0,
                        "contour_min_width": 0,
                        "contour_min_area": 0.01,
                    }
                },
                PARENT: PATIENT_DETAILS,
                CROPPED_STATUS: False
            },
            {
                NAME: PATIENT_ANOTHER_PHONE_NO,
                RESULT: {
                    SAVED_FOLDER: "{}/{}/page_{}".format(output_folder, form_name, page),
                    SAVED_IMAGE_NAME: "{}.png".format(PATIENT_ANOTHER_PHONE_NO),
                    SAVED_PATH: "{}/{}/page_{}/{}.png".format(output_folder, form_name, page, PATIENT_ANOTHER_PHONE_NO),
                    NUMPY_ARRAY: None
                },
                PROCESS: {
                    APPROACH: CONTOUR_SORT_APPROACH,
                    PROCESS_PARAMS: {
                        "inner_boxes": True,
                        "top_distance": 0.48,
                        "bottom_distance": 0.70,
                        "left_distance": 0.18,
                        "right_distance": 0.40,
                        "contour_min_height": 0,
                        "contour_min_width": 0,
                        "contour_min_area": 0.01,
                    }
                },
                PARENT: PATIENT_DETAILS,
                CROPPED_STATUS: False
            },
            {
                NAME: PATIENT_ESRD,
                RESULT: {
                    SAVED_FOLDER: "{}/{}/page_{}".format(output_folder, form_name, page),
                    SAVED_IMAGE_NAME: "{}.png".format(PATIENT_ESRD),
                    SAVED_PATH: "{}/{}/page_{}/{}.png".format(output_folder, form_name, page, PATIENT_ESRD),
                    NUMPY_ARRAY: None
                },
                PROCESS: {
                    APPROACH: CONTOUR_SORT_APPROACH,
                    PROCESS_PARAMS: {
                        "inner_boxes": True,
                        "top_distance": 0.48,
                        "bottom_distance": 0.70,
                        "left_distance": 0.38,
                        "right_distance": 1.00,
                        "contour_min_height": 0,
                        "contour_min_width": 0,
                        "contour_min_area": 0.01,
                    }
                },
                PARENT: PATIENT_DETAILS,
                CROPPED_STATUS: False
            },
            {
                NAME: PATIENT_ADDRESS,
                RESULT: {
                    SAVED_FOLDER: "{}/{}/page_{}".format(output_folder, form_name, page),
                    SAVED_IMAGE_NAME: "{}.png".format(PATIENT_ADDRESS),
                    SAVED_PATH: "{}/{}/page_{}/{}.png".format(output_folder, form_name, page, PATIENT_ADDRESS),
                    NUMPY_ARRAY: None
                },
                PROCESS: {
                    APPROACH: CONTOUR_SORT_APPROACH,
                    PROCESS_PARAMS: {
                        "inner_boxes": True,
                        "top_distance": 0.66,
                        "bottom_distance": 0.87,
                        "left_distance": 0.00,
                        "right_distance": 1.00,
                        "contour_min_height": 0,
                        "contour_min_width": 0,
                        "contour_min_area": 0.01,
                    }
                },
                PARENT: PATIENT_DETAILS,
                CROPPED_STATUS: False
            },
            {
                NAME: PATIENT_CITY,
                RESULT: {
                    SAVED_FOLDER: "{}/{}/page_{}".format(output_folder, form_name, page),
                    SAVED_IMAGE_NAME: "{}.png".format(PATIENT_CITY),
                    SAVED_PATH: "{}/{}/page_{}/{}.png".format(output_folder, form_name, page, PATIENT_CITY),
                    NUMPY_ARRAY: None
                },
                PROCESS: {
                    APPROACH: CONTOUR_SORT_APPROACH,
                    PROCESS_PARAMS: {
                        "inner_boxes": True,
                        "top_distance": 0.82,
                        "bottom_distance": 1.00,
                        "left_distance": 0.00,
                        "right_distance": 0.27,
                        "contour_min_height": 0,
                        "contour_min_width": 0,
                        "contour_min_area": 0.01,
                    }
                },
                PARENT: PATIENT_DETAILS,
                CROPPED_STATUS: False
            },
            {
                NAME: PATIENT_STATE,
                RESULT: {
                    SAVED_FOLDER: "{}/{}/page_{}".format(output_folder, form_name, page),
                    SAVED_IMAGE_NAME: "{}.png".format(PATIENT_STATE),
                    SAVED_PATH: "{}/{}/page_{}/{}.png".format(output_folder, form_name, page, PATIENT_STATE),
                    NUMPY_ARRAY: None
                },
                PROCESS: {
                    APPROACH: CONTOUR_SORT_APPROACH,
                    PROCESS_PARAMS: {
                        "inner_boxes": True,
                        "top_distance": 0.82,
                        "bottom_distance": 1.00,
                        "left_distance": 0.25,
                        "right_distance": 0.35,
                        "contour_min_height": 0,
                        "contour_min_width": 0,
                        "contour_min_area": 0.01,
                    }
                },
                PARENT: PATIENT_DETAILS,
                CROPPED_STATUS: False
            },
            {
                NAME: PATIENT_ZIP_CODE,
                RESULT: {
                    SAVED_FOLDER: "{}/{}/page_{}".format(output_folder, form_name, page),
                    SAVED_IMAGE_NAME: "{}.png".format(PATIENT_ZIP_CODE),
                    SAVED_PATH: "{}/{}/page_{}/{}.png".format(output_folder, form_name, page, PATIENT_ZIP_CODE),
                    NUMPY_ARRAY: None
                },
                PROCESS: {
                    APPROACH: CONTOUR_SORT_APPROACH,
                    PROCESS_PARAMS: {
                        "inner_boxes": True,
                        "top_distance": 0.82,
                        "bottom_distance": 1.00,
                        "left_distance": 0.33,
                        "right_distance": 0.46,
                        "contour_min_height": 0,
                        "contour_min_width": 0,
                        "contour_min_area": 0.01,
                    }
                },
                PARENT: PATIENT_DETAILS,
                CROPPED_STATUS: False
            },
            {
                NAME: PATIENT_COUNTY,
                RESULT: {
                    SAVED_FOLDER: "{}/{}/page_{}".format(output_folder, form_name, page),
                    SAVED_IMAGE_NAME: "{}.png".format(PATIENT_COUNTY),
                    SAVED_PATH: "{}/{}/page_{}/{}.png".format(output_folder, form_name, page, PATIENT_COUNTY),
                    NUMPY_ARRAY: None
                },
                PROCESS: {
                    APPROACH: CONTOUR_SORT_APPROACH,
                    PROCESS_PARAMS: {
                        "inner_boxes": True,
                        "top_distance": 0.82,
                        "bottom_distance": 1.00,
                        "left_distance": 0.44,
                        "right_distance": 1.00,
                        "contour_min_height": 0,
                        "contour_min_width": 0,
                        "contour_min_area": 0.01,
                    }
                },
                PARENT: PATIENT_DETAILS,
                CROPPED_STATUS: False
            },

        ]
    }

    return form_config
