import { OnInit, Component, ViewChild } from "@angular/core";
import { MatSidenav } from '@angular/material/sidenav';

import { environment } from '../../environments/environment';

declare var Tiff: any;


@Component({
  selector: 'dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})

export class DashboardComponent implements OnInit {

  menu_bar_activated: boolean = false
  events: string[] = [];
  navcomponent = null
  opened: boolean = true;
  image_file = null;
  file_content = null;
  processed_image = null;

  enableTiff = false

  default_image: any = '../../assets/images/default.jpg'
  operation_selections = ["contour", "horizontal-line", "vertical-line"];

  operation_name = {
    "contour": "Contour detection",
    "horizontal-line": "Horizontal line detection",
    "vertical-line": "Vertical Line detection"
  }

  @ViewChild('sidenav') sidenav: MatSidenav;

  constructor() { }

  ngOnInit() {
    this.sidenav.open()
    this.navcomponent = this.operation_selections[0]
  }

  /* sidenav functions */
  close() {
    this.sidenav.close();
  }
  toggle() {
    this.sidenav.toggle();
  }
  /* upload image */
  onFileChange(event) {
    this.image_file = null
    if (event.target.files.length > 0) {
      let files = event.target.files;
      if (files) {
        let reader = new FileReader();
        reader.onload = (e: any) => {
          this.image_file = e.target.result;
          this.display_tiff(this.image_file)
        }
        this.file_content = event.target.files[0];
        reader.readAsDataURL(files[0]);
      }
    }
  }

  display_tiff(image_file) {
    this.enableTiff = true;
    let xhr = new XMLHttpRequest();
    xhr.responseType = 'arraybuffer';
    xhr.open('GET', image_file);
    xhr.onload = function (e) {
      var tiff = new Tiff({ buffer: xhr.response });
      var canvas = tiff.toCanvas();
      document.getElementById("image-file").appendChild(canvas);
      document.getElementsByTagName('canvas')[0].style.width = "100%";
      document.getElementsByTagName('canvas')[0].style.height = "100%";
    };
    xhr.send();

  }

  /* default option checked */
  default_check(oprtn) {
    if (this.navcomponent == oprtn)
      return 'checked'
    return ''
  }

  /* image operations params */
  operation_selection(event) {
    for (let key of Object.keys(this.operation_name)) {
      if (event.target.value == key) {
        this.navcomponent = key
      }
    }
  }

  receiveMessage($event) {
    if ($event)
      this.processed_image = `${environment.apiUrl}${$event}`
    else
      this.processed_image = null
  }

  OptionName(name) {
    return this.operation_name[name]
  }

  check(navcomponent, name) {
    if (navcomponent == name)
      return true
    return false
  }
}