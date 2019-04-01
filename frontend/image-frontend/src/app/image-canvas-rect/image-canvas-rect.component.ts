import { Component, ElementRef, ViewChild, OnInit } from '@angular/core';
import { fromEvent } from 'rxjs';
import { saveAs } from "file-saver";

import { ImageBoundingBoxes, box_options } from './image-canvas-rect.template';

@Component({
  selector: 'app-image-canvas-rect',
  templateUrl: './image-canvas-rect.component.html',
  styleUrls: ['./image-canvas-rect.component.scss']
})
export class ImageCanvasRectComponent implements OnInit {

  default_image: any = '../../assets/images/default.jpg';
  image_file = null;
  file_content = null;
  context: CanvasRenderingContext2D;

  start_coordinates = { x: null, y: null };
  end_coordinates = { x: null, y: null };

  mouse_down = false;

  image_width = null;
  image_height = null;
  image_name = null;

  box_index = 0;

  public box_options = box_options;

  public json_box_type = "word";

  boudingbox = new ImageBoundingBoxes([])

  @ViewChild('backgroundCanvas') public bgcanvas: ElementRef;
  @ViewChild('foregroundCanvas') public fgcanvas: ElementRef;
  @ViewChild('fileInput') fileInput: any;

  private bgcx: CanvasRenderingContext2D;
  private fgcx: CanvasRenderingContext2D;

  constructor() {
  }

  ngOnInit() {
  }

  update_initial_values() {
    this.image_name = null;
    this.image_file = null;
    this.image_width = 0;
    this.image_height = 0;
    this.boudingbox = new ImageBoundingBoxes([]);
  }

  public onFileChange(event) {
    this.update_initial_values()
    if (event.target.files.length > 0) {
      let files = event.target.files;
      if (files) {
        this.image_name = event.target.files[0].name;
        let reader = new FileReader();
        reader.onload = (e: any) => {
          this.image_file = e.target.result;
          // get image width height

          var img = new Image();
          img.src = e.target.result;
          img.onload = () => {
            this.image_width = img.width;
            this.image_height = img.height;

            this.canvas_view()
            console.log(`image width-${this.image_width} height-${this.image_height}`)
          }
        }
        this.file_content = event.target.files[0];
        reader.readAsDataURL(files[0]);
      }
      this.fileInput.nativeElement.value = '';
    }
  }

  private canvas_view() {
    const bgcanvasEl: HTMLCanvasElement = this.bgcanvas.nativeElement;
    const fgcanvasEl: HTMLCanvasElement = this.fgcanvas.nativeElement;

    this.bgcx = bgcanvasEl.getContext('2d');
    this.fgcx = fgcanvasEl.getContext('2d');

    bgcanvasEl.width = this.image_width;
    bgcanvasEl.height = this.image_height;

    fgcanvasEl.width = this.image_width;
    fgcanvasEl.height = this.image_height;

    this.bgcx.lineWidth = 2;
    this.bgcx.lineCap = 'round';
    this.bgcx.strokeStyle = '#000';

    var img = new Image();
    img.onload = () => {
      this.bgcx.drawImage(img, 0, 0);
      this.load_rectangles();
      this.CheckUncheckView();
    }
    img.src = this.image_file;

    this.captureEvents(fgcanvasEl);
  }

  private captureEvents(canvasEl: HTMLCanvasElement) {

    const MouseUp = fromEvent(canvasEl, 'mouseup');
    MouseUp.subscribe((evt: MouseEvent) => {
      if (this.mouse_down) {
        this.end_coordinates = {
          x: evt.layerX,
          y: evt.layerY
        };
        this.fgcx.fillRect(this.end_coordinates.x, this.end_coordinates.y, 5, 5);
        this.drawOnCanvas()
        this.mouse_down = false;
        this.canvas_view();
      }
    });


    const MouseDown = fromEvent(canvasEl, 'mousedown');
    MouseDown.subscribe((event: MouseEvent) => {
      this.mouse_down = true;
      this.start_coordinates = {
        x: event.layerX,
        y: event.layerY
      };
      this.fgcx.fillRect(this.start_coordinates.x, this.start_coordinates.y, 5, 5);
    });

    const MouseMove = fromEvent(canvasEl, 'mousemove');
    MouseMove.subscribe((event: MouseEvent) => {

      if (this.mouse_down == true) {
        let width = event.layerX - this.start_coordinates.x;
        let height = event.layerY - this.start_coordinates.y;

        let { start_x, start_y, end_x, end_y } = this.start_end_points(width, height,
          this.start_coordinates.x, this.start_coordinates.y, event.layerX, event.layerY)
        this.fgcx.clearRect(0, 0, this.image_width, this.image_height);
        this.load_rectangles();
        this.CheckUncheckView();

        this.fgcx.beginPath();
        this.fgcx.strokeStyle = 'black';
        this.fgcx.lineWidth = 2;
        this.fgcx.strokeRect(start_x, start_y, Math.abs(width), Math.abs(height));
        this.fgcx.closePath();
      }
    });
  }

  private start_end_points(width, height, draw_start_x, draw_start_y, draw_end_x, draw_end_y) {
    let start_x = null;
    let start_y = null;
    let end_x = null;
    let end_y = null;
    if (width >= 0 && height >= 0) {
      start_x = draw_start_x;
      start_y = draw_start_y;
      end_x = draw_end_x;
      end_y = draw_end_y;
    }
    else if (width < 0 && height < 0) {
      start_x = draw_end_x;
      start_y = draw_end_y;
      end_x = draw_start_x;
      end_y = draw_start_y;
    }
    else if (width > 0 && height < 0) {
      start_x = draw_start_x;
      start_y = draw_end_y;
      end_x = draw_end_x;
      end_y = draw_start_y;
    }
    else if (width < 0 && height > 0) {
      start_x = draw_end_x;
      start_y = draw_start_y;
      end_x = draw_start_x;
      end_y = draw_end_y;
    }

    return { start_x, start_y, end_x, end_y }

  }

  public update_text() {
    this.fgcx.clearRect(0, 0, this.image_width, this.image_height);
    this.load_rectangles();
    this.CheckUncheckView();
  }

  private drawOnCanvas() {
    if (!this.fgcx) { return; }

    if (this.start_coordinates.x != null && this.start_coordinates.y != null
      && this.end_coordinates.x != null && this.end_coordinates.y != null) {
      console.log(`start_coordinates : ${this.start_coordinates.x}, ${this.start_coordinates.y}, 
      end_coordinates : ${this.end_coordinates.x}, ${this.end_coordinates.y}`)

      // draw boxes
      let width = this.end_coordinates.x - this.start_coordinates.x;
      let height = this.end_coordinates.y - this.start_coordinates.y;
      let { start_x, start_y, end_x, end_y } = this.start_end_points(width, height,
        this.start_coordinates.x, this.start_coordinates.y, this.end_coordinates.x, this.end_coordinates.y)

      this.box_index += 1
      //appending to the bounding boxes
      this.boudingbox.appending_box_params(
        this.box_index, start_x, start_y, end_x, end_y, Math.abs(width), Math.abs(height)
      )
      this.fgcx.beginPath();
      this.fgcx.strokeStyle = 'black';
      this.fgcx.lineWidth = 2;
      this.fgcx.strokeRect(start_x, start_y, Math.abs(width), Math.abs(height));
      this.fgcx.closePath();

      // reset start and end coordiantes
      this.start_coordinates.x = null;
      this.start_coordinates.y = null;
      this.end_coordinates.x = null;
      this.end_coordinates.y = null;
    }
  }

  public deletebox(delindex) {
    console.log(this.boudingbox.box_params);
    var delete_index = this.boudingbox.box_params.findIndex(el => el.index === delindex);
    console.log(delete_index);

    this.boudingbox.box_params.splice(delete_index, 1);
    this.canvas_view();

  }

  private load_rectangles() {
    for (let val of this.boudingbox.box_params) {
      this.fgcx.beginPath();
      this.fgcx.rect(val.start_point_x, val.start_point_y,
        val.width, val.height);
      this.fgcx.strokeStyle = 'black';
      this.fgcx.lineWidth = 2;
      this.fgcx.fillStyle = '#c10d47';
      this.fgcx.font = "30px Arial";
      this.fgcx.fillText(val.value, val.start_point_x + 10, val.start_point_y + 25);
      this.fgcx.stroke();
      this.fgcx.closePath();
    }

  }

  public on_download() {

    console.log(this.json_box_type)
    let download_json = [];
    for (let val of this.boudingbox.box_params) {
      download_json.push({
        "start_x": val.start_point_x,
        "start_y": val.start_point_y,
        "end_x": val.end_point_x,
        "end_y": val.end_point_y,
        "width": val.width,
        "height": val.height,
        "value": val.value
      })

    }
    let theJSON = JSON.stringify(download_json);
    var blob = new Blob([theJSON], { type: 'text/json' });
    if (this.image_name) {
      let trimmed_file_name = this.image_name.split('.').slice(0, -1).join('.')
      saveAs(blob, `${this.json_box_type}-${trimmed_file_name}.json`);
    }
    else {
      saveAs(blob, `${this.json_box_type}-bounding_box.json`);
      console.log(this.boudingbox.box_params)
    }
  }

  public CheckUncheckView() {
    for (let val of this.boudingbox.box_params) {
      this.fgcx.beginPath();

      if (val.view)
        this.fgcx.strokeStyle = 'yellow';
      else
        this.fgcx.strokeStyle = 'black';

      this.fgcx.lineWidth = 2;
      this.fgcx.strokeRect(val.start_point_x, val.start_point_y,
        val.width, val.height);
      this.fgcx.closePath();
    }
  }
}