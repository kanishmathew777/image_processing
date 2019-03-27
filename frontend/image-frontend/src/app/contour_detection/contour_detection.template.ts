interface Color {
  red: number,
  green: number,
  blue: number
}

interface ContorConfig {
  index: number,
  thickness: number,
  sort_reverse: boolean,
  color: Color
}

export class Contour {

  constructor(
    public join_lines: boolean,

    public kernal: number,

    public thresholding: number,

    public approximation_method: number,

    public retrievelmode: number,

    public contour: ContorConfig,
  ) { }

}