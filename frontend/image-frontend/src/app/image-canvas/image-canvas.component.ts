import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';

@Component({
  selector: 'app-image-canvas',
  templateUrl: './image-canvas.component.html',
  styleUrls: ['./image-canvas.component.scss']
})
export class ImageCanvasComponent implements OnInit {

  default_image: any = '../../assets/images/default.jpg';
  image_file = null;
  file_content = null;
  context: CanvasRenderingContext2D;

  @ViewChild('fileInput') fileInput: any;
  @ViewChild('myCanvas') myCanvas: ElementRef;

  constructor() { }

  ngOnInit() {
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
      // this.onsubmit()
    }
  }

  canvas_view(width, height, e) {
    console.log(width, height)
    let canvas = this.myCanvas.nativeElement;
    this.context = canvas.getContext("2d");

    var ctx = this.context;
    ctx.canvas.width = width;
    ctx.canvas.height = height;
    var img = new Image();
    img.src = e.target.result;
    ctx.drawImage(img, 0, 0);
  } 
}