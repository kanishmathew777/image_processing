import { Component, ElementRef, ViewChild, OnInit } from '@angular/core';
import { fromEvent } from 'rxjs';

import { ImageBoundingBoxes } from './image-canvas-rect.template';

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

  boudingbox = new ImageBoundingBoxes([])

  @ViewChild('myCanvas') public canvas: ElementRef;
  @ViewChild('fileInput') fileInput: any;

  private cx: CanvasRenderingContext2D;

  ngOnInit() {

    console.log(this.boudingbox)
  }

  onFileChange(event) {
    this.image_file = null;
    let w, h = 0;
    if (event.target.files.length > 0) {
      let files = event.target.files;
      if (files) {
        let reader = new FileReader();
        reader.onload = (e: any) => {
          this.image_file = e.target.result;
          // get image width height
          var img = new Image();
          img.src = e.target.result;
          img.onload = () => {
            w = img.width;
            h = img.height;

            this.canvas_view(w, h, e)
            console.log(`image width-${w} height-${h}`)
          }
        }
        this.file_content = event.target.files[0];
        reader.readAsDataURL(files[0]);
      }
      this.fileInput.nativeElement.value = '';
    }
  }

  canvas_view(width, height, e) {
    const canvasEl: HTMLCanvasElement = this.canvas.nativeElement;
    this.cx = canvasEl.getContext('2d');

    canvasEl.width = width;
    canvasEl.height = height;

    this.cx.lineWidth = 3;
    this.cx.lineCap = 'round';
    this.cx.strokeStyle = '#000';

    var img = new Image();
    img.src = e.target.result;
    this.cx.drawImage(img, 0, 0);

    this.captureEvents(canvasEl);
  }

  captureEvents(canvasEl: HTMLCanvasElement) {

    const MouseUpMove = fromEvent(canvasEl, 'mouseup');
    MouseUpMove.subscribe((evt: MouseEvent) => {
      if (this.mouse_down) {
        this.end_coordinates = {
          x: evt.layerX,
          y: evt.layerY
        };
        this.cx.fillRect(this.end_coordinates.x, this.end_coordinates.y, 5, 5);
        this.drawOnCanvas()
      }
    });


    const MouseDownMove = fromEvent(canvasEl, 'mousedown');
    MouseDownMove.subscribe((event: MouseEvent) => {
      this.mouse_down = true;
      this.start_coordinates = {
        x: event.layerX,
        y: event.layerY
      };
      this.cx.fillRect(this.start_coordinates.x, this.start_coordinates.y, 5, 5);
    });

  }
  private drawOnCanvas() {
    if (!this.cx) { return; }

    if (this.start_coordinates.x != null && this.start_coordinates.y != null
      && this.end_coordinates.x != null && this.end_coordinates.y != null) {
      console.log(`start_coordinates : ${this.start_coordinates.x}, ${this.start_coordinates.y}, 
      end_coordinates : ${this.end_coordinates.x}, ${this.end_coordinates.y}`)

      // draw boxes
      this.cx.beginPath();
      let width = this.end_coordinates.x - this.start_coordinates.x;
      let height = this.end_coordinates.y - this.start_coordinates.y;
      console.log(width, height)
      if (width >= 0 && height >= 0)
        this.cx.rect(this.start_coordinates.x, this.start_coordinates.y, width, height);
      else
        this.cx.rect(this.end_coordinates.x, this.end_coordinates.y,
          Math.abs(width), Math.abs(height));
      this.cx.strokeStyle = 'black';
      this.cx.lineWidth = 1;
      this.cx.stroke();


      // reset start and
      this.start_coordinates.x = null;
      this.start_coordinates.y = null;
      this.end_coordinates.x = null;
      this.end_coordinates.y = null;
    }
  }

}