import { Component, Input, ElementRef, AfterViewInit, ViewChild } from '@angular/core';
import { fromEvent } from 'rxjs';
import 'rxjs/add/operator/map';

@Component({
  selector: 'app-canvas',
  templateUrl: './canvas-move.component.html',
  styles: ['canvas { border: 1px solid #000; }']
})

export class CanvasMoveComponent implements AfterViewInit {

  start_coordinates = {x: null, y: null};
  end_coordinates = {x: null, y:null};
  mouse_down = false;

  @Input() public width = 400;
  @Input() public height = 400;

  @ViewChild('canvas') public canvas: ElementRef;
  private cx: CanvasRenderingContext2D;

  public ngAfterViewInit() {
    const canvasEl: HTMLCanvasElement = this.canvas.nativeElement;
    this.cx = canvasEl.getContext('2d');

    canvasEl.width = this.width;
    canvasEl.height = this.height;

    this.cx.lineWidth = 3;
    this.cx.lineCap = 'round';
    this.cx.strokeStyle = '#000';
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
        this.cx.fillRect(this.end_coordinates.x, this.end_coordinates.y,2,2);
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
      this.cx.fillRect(this.start_coordinates.x, this.start_coordinates.y,2,2);
    });

  }
  private drawOnCanvas() {
    if (!this.cx) { return; }

    if (this.start_coordinates.x != null && this.start_coordinates.y != null
      && this.end_coordinates.x != null && this.end_coordinates.y !=null) {
      console.log(`start_coordinates : ${this.start_coordinates.x}, ${this.start_coordinates.y}, 
      end_coordinates : ${this.end_coordinates.x}, ${this.end_coordinates.y}` )


      this.cx.beginPath();
      let width = this.end_coordinates.x - this.start_coordinates.x;
      let height = this.end_coordinates.y - this.start_coordinates.y;
      this.cx.rect(this.start_coordinates.x, this.start_coordinates.y, width, height);
      this.cx.strokeStyle = 'black';
      this.cx.lineWidth = 1;
      this.cx.stroke();

      this.start_coordinates.x = null;
      this.start_coordinates.y = null;
      this.end_coordinates.x = null;
      this.end_coordinates.y = null;
    }
  }

}