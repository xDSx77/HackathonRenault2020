import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CurrentAirComponent } from './current-air.component';

describe('CurrentAirComponent', () => {
  let component: CurrentAirComponent;
  let fixture: ComponentFixture<CurrentAirComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CurrentAirComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CurrentAirComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
