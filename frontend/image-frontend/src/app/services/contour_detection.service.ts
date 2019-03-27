import { Observable, Subject } from 'rxjs';
import { Injectable } from "@angular/core";
import { BaseService } from './baseservice.service';


@Injectable()
export class ContourServices extends BaseService{
    
    contour_detection_options(): Observable<any>{
        return this.getMethod('/image/contour/');
    }

    contour_detection(data): Observable<any>{
        return this.postMethod('/image/contour/', data);
    }

}