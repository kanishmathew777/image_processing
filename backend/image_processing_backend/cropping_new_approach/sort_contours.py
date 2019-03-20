import cv2


def sort_contours(cnts, sort_top_bottom=True, sort_left_right=True):

    def get_sort_keys(to_sort_list, top_bottom=True, left_right=True):
        sort_keys = [to_sort_list[1][1], to_sort_list[1][0]]
        if not top_bottom:
            sort_keys = [-to_sort_list[1][1]]
        if not left_right:
            sort_keys = [-to_sort_list[1][0]]
        if not top_bottom and not left_right:
            sort_keys = [-to_sort_list[1][1], -to_sort_list[1][0]]

        return tuple(sort_keys)

    boundingboxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingboxes) = zip(*sorted(zip(cnts, boundingboxes),
                                        key=lambda value_list: (get_sort_keys(value_list,
                                                                              left_right=sort_left_right,
                                                                              top_bottom=sort_top_bottom
                                                                              )
                                                                )
                                        ))

    # return the list of sorted contours and bounding boxes
    return cnts, boundingboxes
