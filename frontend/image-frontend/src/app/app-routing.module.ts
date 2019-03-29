import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';


import { DashboardComponent } from './dashboard/dashboard.component';
import { PageNotFoundComponent } from './notfound.component';
import { ImageCanvasComponent } from './image-canvas/image-canvas.component';
import { CanvasMoveComponent } from './canvas-move/canvas-move.component';
import { ImageCanvasRectComponent } from './image-canvas-rect/image-canvas-rect.component';


import { ContourComponent } from './contour_detection/contour_detection.component';
import { HorizontalLineComponent } from './horizontal_lines/horizontal_lines.component';
import { VerticalLineComponent } from './vertical_lines/vertical_lines.component';



const routes: Routes = [
  { path: '', redirectTo: '/image_rect_canvas', pathMatch: 'full' },
  {
    path: 'dashboard', component: DashboardComponent,
  //   children: [
  //   { path: '', component: ContourComponent },
  //   { path: 'contour', component: ContourComponent },
  //   { path: 'horizontal-line', component: HorizontalLineComponent },
  //   { path: 'vertical-line', component: VerticalLineComponent }
  // ]
  },
  { path: 'image_canvas', component: ImageCanvasComponent },
  { path: 'rect_canvas', component: CanvasMoveComponent },
  { path: 'image_rect_canvas', component: ImageCanvasRectComponent },
  { path: '**', component: PageNotFoundComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
