import { Component, OnInit } from '@angular/core';
import { Weather } from '../weather.enum';
import { Observable } from 'rxjs';
import { ContextService } from '../context.service';

@Component({
  selector: 'app-current-weather',
  templateUrl: './current-weather.component.html',
  styleUrls: ['./current-weather.component.scss']
})
export class CurrentWeatherComponent implements OnInit {
  currentWeather$: Observable<Weather>;

  constructor(private contextService: ContextService) { }

  ngOnInit() {
    this.currentWeather$ = this.contextService.getCurrentWeather$();
  }
}
