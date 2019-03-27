import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';


import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/observable/throw';


@Injectable()
export class BaseService {

    apiUrl = environment.apiUrl

    constructor(private http: HttpClient) { }

    getMethod(Url: string): Observable<any> {
        return this.http.get(`${this.apiUrl}${Url}`)
            .map((response: Response) => response)
            .catch((e: any) => Observable.throw((e)));
    }

    postMethod(Url: string, data: any): Observable<any> {
        return this.http.post(`${this.apiUrl}${Url}`, data)
            .map((response: Response) => response)
            .catch((e: any) => Observable.throw((e)));
    }

}


// .subscribe(
//     (data: Config) => this.config = { ...data }, // success path
//     error => this.error = error // error path
//   );