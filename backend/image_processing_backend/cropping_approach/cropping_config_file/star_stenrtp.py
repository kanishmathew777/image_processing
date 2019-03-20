from cropping_approach.constants.config_fields_constants import NAME, PAGE, FIELDS, PARENT, PROCESS, RESULT, \
    SAVED_FOLDER, NUMPY_ARRAY, SAVED_IMAGE_NAME, SAVED_PATH, OUTPUT_FOLDER, IMAGE_PATH, CROPPED_STATUS, \
    PROCESS_PARAMS, PARENT_FOLDER, CONTOUR_SORT_APPROACH, VERTICAL_HORIZONTAL_COMBINE_APPROACH, CONTOUR_APPROACH, \
    APPROACH

from cropping_approach.constants.star_stenrtp_field_names import DOCTOR_NAMES, MEDICAL_DOCTORS, MEDICAL_PLAN, MEMBER_NAME, \
    MEMBER_DETAILS, PLAN_FIRST_CHOICE, PLAN_SECOND_CHOICE

fieldname_index = {
    MEDICAL_PLAN: 0,
    MEDICAL_DOCTORS: 1,
    MEMBER_NAME: 2,
    DOCTOR_NAMES: 3,
    MEMBER_DETAILS: 4,
    PLAN_FIRST_CHOICE: 5,
    PLAN_SECOND_CHOICE: 6,
}


def starstenrtp_getfieldindex(fieldname):
    try:
        index = fieldname_index[fieldname]
    except KeyError:
        index = None
    return index


def starstenrtp_config(image_path, output_folder, form_name, page=1):
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
                        "top_distance": 0.23,
                        "bottom_distance": 0.55,
                        "left_distance": 0,
                        "right_distance": 0,
                        "contour_min_height": 10,
                        "contour_min_width": 10,
                        "contour_min_area": 0.15
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
                    APPROACH: VERTICAL_HORIZONTAL_COMBINE_APPROACH,
                    PROCESS_PARAMS: {
                        "top_distance": 0.56,
                        "bottom_distance": 0.69,
                        "left_distance": 0,
                        "right_distance": 0,
                        "contour_min_height": 0,
                        "contour_min_width": 0,
                        "contour_min_area": 0.08
                    }
                },
                PARENT: None,
                CROPPED_STATUS: False
            },
            {
                NAME: MEMBER_NAME,
                RESULT: {
                    SAVED_FOLDER: "{}/{}/page_{}".format(output_folder, form_name, page),
                    SAVED_IMAGE_NAME: "{}.png".format(MEMBER_NAME),
                    SAVED_PATH: "{}/{}/page_{}/{}.png".format(output_folder, form_name, page, MEMBER_NAME),
                    NUMPY_ARRAY: None
                },
                PROCESS: {
                    APPROACH: CONTOUR_SORT_APPROACH,
                    PROCESS_PARAMS: {
                        "top_distance": 0.0,
                        "bottom_distance": 1.0,
                        "left_distance": 0.0,
                        "right_distance": 0.28,
                        "contour_min_height": 0,
                        "contour_min_width": 0,
                        "contour_min_area": 0.20
                    }
                },
                PARENT: MEDICAL_DOCTORS,
                CROPPED_STATUS: False
            },
            {
                NAME: DOCTOR_NAMES,
                RESULT: {
                    SAVED_FOLDER: "{}/{}/page_{}".format(output_folder, form_name, page),
                    SAVED_IMAGE_NAME: "{}.png".format(DOCTOR_NAMES),
                    SAVED_PATH: "{}/{}/page_{}/{}.png".format(output_folder, form_name, page, DOCTOR_NAMES),
                    NUMPY_ARRAY: None
                },
                PROCESS: {
                    APPROACH: CONTOUR_SORT_APPROACH,
                    PROCESS_PARAMS: {
                        "top_distance": 0.0,
                        "bottom_distance": 1.0,
                        "left_distance": 0.24,
                        "right_distance": 1.0,
                        "contour_min_height": 0,
                        "contour_min_width": 0,
                        "contour_min_area": 0.20
                    }
                },
                PARENT: MEDICAL_DOCTORS,
                CROPPED_STATUS: False
            },
            {
                NAME: MEMBER_DETAILS,
                RESULT: {
                    SAVED_FOLDER: "{}/{}/page_{}".format(output_folder, form_name, page),
                    SAVED_IMAGE_NAME: "{}.png".format(MEMBER_DETAILS),
                    SAVED_PATH: "{}/{}/page_{}/{}.png".format(output_folder, form_name, page, MEMBER_DETAILS),
                    NUMPY_ARRAY: None
                },
                PROCESS: {
                    APPROACH: CONTOUR_SORT_APPROACH,
                    PROCESS_PARAMS: {
                        "inner_boxes": True,
                        "top_distance": 0.40,
                        "bottom_distance": 1.0,
                        "left_distance": 0.0,
                        "right_distance": 0.47,
                        "contour_min_height": 0,
                        "contour_min_width": 0,
                        "contour_min_area": 0.03,
                    }
                },
                PARENT: MEDICAL_PLAN,
                CROPPED_STATUS: False
            },
            {
                NAME: PLAN_FIRST_CHOICE,
                RESULT: {
                    SAVED_FOLDER: "{}/{}/page_{}".format(output_folder, form_name, page),
                    SAVED_IMAGE_NAME: "{}.png".format(PLAN_FIRST_CHOICE),
                    SAVED_PATH: "{}/{}/page_{}/{}.png".format(output_folder, form_name, page, PLAN_FIRST_CHOICE),
                    NUMPY_ARRAY: None
                },
                PROCESS: {
                    APPROACH: CONTOUR_SORT_APPROACH,
                    PROCESS_PARAMS: {
                        "inner_boxes": True,
                        "top_distance": 0.40,
                        "bottom_distance": 1.0,
                        "left_distance": 0.45,
                        "right_distance": 0.74,
                        "contour_min_height": 0,
                        "contour_min_width": 0,
                        "contour_min_area": 0.03,
                    }
                },
                PARENT: MEDICAL_PLAN,
                CROPPED_STATUS: False
            },
            {
                NAME: PLAN_SECOND_CHOICE,
                RESULT: {
                    SAVED_FOLDER: "{}/{}/page_{}".format(output_folder, form_name, page),
                    SAVED_IMAGE_NAME: "{}.png".format(PLAN_SECOND_CHOICE),
                    SAVED_PATH: "{}/{}/page_{}/{}.png".format(output_folder, form_name, page, PLAN_SECOND_CHOICE),
                    NUMPY_ARRAY: None
                },
                PROCESS: {
                    APPROACH: CONTOUR_SORT_APPROACH,
                    PROCESS_PARAMS: {
                        "inner_boxes": True,
                        "top_distance": 0.40,
                        "bottom_distance": 1.0,
                        "left_distance": 0.72,
                        "right_distance": 1.0,
                        "contour_min_height": 0,
                        "contour_min_width": 0,
                        "contour_min_area": 0.03,
                    }
                },
                PARENT: MEDICAL_PLAN,
                CROPPED_STATUS: False
            },
        ]
    }

    return form_config
