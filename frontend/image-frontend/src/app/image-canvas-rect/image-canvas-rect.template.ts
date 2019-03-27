interface BoundingBoxConfig {
    start_point_x : number,
    start_point_y : number,

    end_point_x : number,
    end_point_y : number,

    view : boolean,

    value ?: string 
}

export class ImageBoundingBoxes {

    constructor(
        public join_lines: BoundingBoxConfig[],

        public form_name? : string
    ) { }

}