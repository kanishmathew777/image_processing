interface BoundingBoxConfig {
    index: number,
    start_point_x: number,
    start_point_y: number,

    end_point_x: number,
    end_point_y: number,

    width: number,
    height: number,

    view: boolean,

    value?: string
}

export class ImageBoundingBoxes {

    constructor(
        public box_params: BoundingBoxConfig[],

        public form_name?: string
    ) { }

    public appending_box_params(index, start_point_x, start_point_y, 
        end_point_x, end_point_y, width, height,
        view = false, value = "") {

        this.box_params.push({
            'index': index,
            'start_point_x': start_point_x,
            'start_point_y': start_point_y,
            'end_point_x': end_point_x,
            'end_point_y': end_point_y,
            'width': width,
            'height': height,
            'view': view,
            'value': value
        })
    }

}