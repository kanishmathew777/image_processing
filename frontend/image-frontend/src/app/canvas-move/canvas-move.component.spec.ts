import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CanvasMoveComponent } from './canvas-move.component';

describe('CanvasMoveComponent', () => {
  let component: CanvasMoveComponent;
  let fixture: ComponentFixture<CanvasMoveComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CanvasMoveComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CanvasMoveComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
