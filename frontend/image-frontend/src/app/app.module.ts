import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule, HttpClient } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { NavBarComponent } from './nav-bar/nav-bar.component'; 
import { DashboardComponent } from './dashboard/dashboard.component';
import { ContourComponent } from './contour_detection/contour_detection.component';
import { HorizontalLineComponent } from './horizontal_lines/horizontal_lines.component';
import { VerticalLineComponent } from './vertical_lines/vertical_lines.component';
import { PageNotFoundComponent } from './notfound.component';

import { MatSidenavModule } from '@angular/material/sidenav';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ToastrModule } from 'ngx-toastr';
import { CanvasMoveComponent } from './canvas-move/canvas-move.component';
import { ImageCanvasComponent } from './image-canvas/image-canvas.component';
import { ImageCanvasRectComponent } from './image-canvas-rect/image-canvas-rect.component';


@NgModule({
  declarations: [
    AppComponent,

    DashboardComponent,
    NavBarComponent,
    ContourComponent,
    VerticalLineComponent,
    HorizontalLineComponent,
    PageNotFoundComponent,
    CanvasMoveComponent,
    ImageCanvasComponent,
    ImageCanvasRectComponent

  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    MatSidenavModule,
    BrowserAnimationsModule,
    FormsModule,
    ToastrModule.forRoot()
    
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
