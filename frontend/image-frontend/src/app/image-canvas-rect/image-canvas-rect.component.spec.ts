import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ImageCanvasRectComponent } from './image-canvas-rect.component';

describe('ImageCanvasRectComponent', () => {
  let component: ImageCanvasRectComponent;
  let fixture: ComponentFixture<ImageCanvasRectComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ImageCanvasRectComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ImageCanvasRectComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
