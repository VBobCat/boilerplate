import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RaizComponent } from './raiz.component';

describe('RaizComponent', () => {
  let component: RaizComponent;
  let fixture: ComponentFixture<RaizComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RaizComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RaizComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
