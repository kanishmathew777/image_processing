from cropping_approach.constants.config_fields_constants import NAME, PAGE, FIELDS, PARENT, PROCESS, RESULT, \
    SAVED_FOLDER, NUMPY_ARRAY, SAVED_IMAGE_NAME, SAVED_PATH, OUTPUT_FOLDER, IMAGE_PATH, CROPPED_STATUS, \
    PROCESS_PARAMS, PARENT_FOLDER, CONTOUR_SORT_APPROACH, VERTICAL_HORIZONTAL_COMBINE_APPROACH, APPROACH

from cropping_approach.constants.dental_deenr_field_names import DOCTOR_NAMES, DENTAL_DOCTORS, DENTAL_PLAN, \
    MEMBER_NAME, MEMBER_DETAILS, PLAN_FIRST_CHOICE, PLAN_SECOND_CHOICE


fieldname_index = {
    DENTAL_PLAN: 0,
    DENTAL_DOCTORS: 1,
    MEMBER_DETAILS: 2,
    PLAN_FIRST_CHOICE: 3,
    PLAN_SECOND_CHOICE: 4,
    MEMBER_NAME: 5,
    DOCTOR_NAMES: 6,
}


def dental_deenr_getfieldindex(fieldname):
    try:
        index = fieldname_index[fieldname]
    except KeyError:
        index = None
    return index


def dental_deenr_config(image_path, output_folder, form_name, page=1):
    form_config = {
        IMAGE_PATH: image_path,
        NAME: form_name,
        PAGE: page,
        PARENT_FOLDER: "{}/{}/".format(output_folder, form_name),
        OUTPUT_FOLDER: output_folder,
        FIELDS: [
            {
                NAME: DENTAL_PLAN,
                RESULT: {
                    SAVED_FOLDER: "{}/{}/page_{}".format(output_folder, form_name, page),
                    SAVED_IMAGE_NAME: "{}.png".format(DENTAL_PLAN),
                    SAVED_PATH: "{}/{}/page_{}/{}.png".format(output_folder, form_name, page, DENTAL_PLAN),
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
                        "contour_min_area": 0.08
                    }
                },
                PARENT: None,
                CROPPED_STATUS: False
            },
            {
                NAME: DENTAL_DOCTORS,
                RESULT: {
                    SAVED_FOLDER: "{}/{}/page_{}".format(output_folder, form_name, page),
                    SAVED_IMAGE_NAME: "{}.png".format(DENTAL_DOCTORS),
                    SAVED_PATH: "{}/{}/page_{}/{}.png".format(output_folder, form_name, page, DENTAL_DOCTORS),
                    NUMPY_ARRAY: None
                },
                PROCESS: {
                    APPROACH: VERTICAL_HORIZONTAL_COMBINE_APPROACH,
                    PROCESS_PARAMS: {
                        "top_distance": 0.48,
                        "bottom_distance": 0.62,
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
                        "top_distance": 0.30,
                        "bottom_distance": 1.0,
                        "left_distance": 0.0,
                        "right_distance": 0.525,
                        "contour_min_height": 0,
                        "contour_min_width": 0,
                        "contour_min_area": 0.03,
                    }
                },
                PARENT: DENTAL_PLAN,
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
                        "top_distance": 0.30,
                        "bottom_distance": 1.0,
                        "left_distance": 0.50,
                        "right_distance": 0.77,
                        "contour_min_height": 0,
                        "contour_min_width": 0,
                        "contour_min_area": 0.03,
                    }
                },
                PARENT: DENTAL_PLAN,
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
                        "top_distance": 0.30,
                        "bottom_distance": 1.0,
                        "left_distance": 0.735,
                        "right_distance": 1.0,
                        "contour_min_height": 0,
                        "contour_min_width": 0,
                        "contour_min_area": 0.03,
                    }
                },
                PARENT: DENTAL_PLAN,
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
                PARENT: DENTAL_DOCTORS,
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
                PARENT: DENTAL_DOCTORS,
                CROPPED_STATUS: False
            },
        ]
    }

    return form_config
