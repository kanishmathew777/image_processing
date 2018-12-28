import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';

import { PageNotFoundComponent } from './notfound.component';

import { ContourComponent } from './contour_detection/contour_detection.component';
import { HorizontalLineComponent } from './horizontal_lines/horizontal_lines.component';
import { VerticalLineComponent } from './vertical_lines/vertical_lines.component';



const routes: Routes = [
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
  {
    path: 'dashboard', component: DashboardComponent,
  //   children: [
  //   { path: '', component: ContourComponent },
  //   { path: 'contour', component: ContourComponent },
  //   { path: 'horizontal-line', component: HorizontalLineComponent },
  //   { path: 'vertical-line', component: VerticalLineComponent }
  // ]
  },
  { path: '**', component: PageNotFoundComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
