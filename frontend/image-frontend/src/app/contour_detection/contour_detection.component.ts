import { OnInit, Component, Input, Output, EventEmitter } from "@angular/core";
import { ToastrService } from 'ngx-toastr';

import { FormGroup, FormControl, Validators } from '@angular/forms';

import { Contour } from './contour_detection.template';
import { ContourServices } from '../services/contour_detection.service';

@Component({
  selector: 'contour_detection',
  templateUrl: './contour_detection.component.html',
  styleUrls: ['./contour_detection.component.scss'],
  providers: [ContourServices]
})
export class ContourComponent implements OnInit {

  @Input() file;

  @Output() output_image = new EventEmitter<string>();


  httpOptions = null

  constructor(private contourservice: ContourServices,
    private toaster: ToastrService) {

  }

  response: any;
  errors: any;

  /* constants */
  approximations = { 'CHAIN_APPROX_NONE': 1, 'CHAIN_APPROX_SIMPLE': 2 }
  retrievelmodes = {
    'RETR_EXTERNAL': 0, 'RETR_LIST': 1, 'RETR_CCOMP': 2,
    'RETR_TREE': 3, 'RETR_FLOODFILL': 4
  }
  thresholdings = {
    'THRESH_BINARY': 0, 'THRESH_BINARY_INV': 1, 'THRESH_TRUNC': 2, 'THRESH_TOZERO': 3,
    'THRESH_TOZERO_INV': 4, 'THRESH_MASK': 7, 'THRESH_OTSU': 8, 'THRESH_BINARY_INV+THRESH_OTSU': 9
  }


  contour_modal = new Contour(false, 3, 9, 1, 0,
    ({
      index: 1, thickness: 3, sort_reverse: true,
      color: { red: 64, blue: 186, green: 201 }
    }));


  ngOnInit() {
    console.log(this.file)
    // this.contourForm = new FormGroup({
    //   'kernal': new FormControl(this.contour_modal.kernal, [
    //     Validators.required,
    //     Validators.minLength(4),
    //   ]),
    // });
  }

  submitted = false;

  onSubmit() {
    console.log(this.file)
    if (!this.file) {
      this.toaster.error('Please upload a file', 'File Not Uploaded');
      return
    }

    let formData = new FormData();
    formData.append("file", this.file);
    formData.append("name", this.file.name);
    for (let [key, values] of Object.entries(this.contour_modal)) {
      formData.append(key, JSON.stringify(values))
    }
    this.contourservice.contour_detection(formData)
      .subscribe(
        response => {
          this.response = response;
          this.output_image.emit(this.response.output_image)
          // this.toaster.success(`Detected ${this.response.no_contours} contours`, 'Contour detection Successfull')
        },
        error => {
          this.errors = error;
          console.log(this.errors)
          this.output_image.emit(null)
          this.toaster.error(this.errors.error, 'Error Occured');
        })
  }

  keyDownFunction(event) {
    if(event.keyCode == 13) {
      this.onSubmit()
    }
  }

}