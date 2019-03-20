from cropping_approach.constants.config_fields_constants import NAME, PAGE, FIELDS, PARENT, PROCESS, RESULT, \
    SAVED_FOLDER, NUMPY_ARRAY, SAVED_IMAGE_NAME, SAVED_PATH, OUTPUT_FOLDER, IMAGE_PATH, CROPPED_STATUS, \
    PROCESS_PARAMS, PARENT_FOLDER, CONTOUR_SORT_APPROACH, VERTICAL_HORIZONTAL_COMBINE_APPROACH, CONTOUR_APPROACH, \
    APPROACH

from cropping_approach.constants.star_kids_field_names import MEDICAL_PLAN, MEMBER_DETAILS, \
    PLAN_FIRST_CHOICE, PLAN_SECOND_CHOICE


fieldname_index = {
    MEDICAL_PLAN: 0,
    MEMBER_DETAILS: 1,
    PLAN_FIRST_CHOICE: 2,
    PLAN_SECOND_CHOICE: 3,
}


def star_kids_getfieldindex(fieldname):
    try:
        index = fieldname_index[fieldname]
    except KeyError:
        index = None
    return index


def star_kids_config(image_path, output_folder, form_name, page=1):
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
                        "contour_min_area": 0.12
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
