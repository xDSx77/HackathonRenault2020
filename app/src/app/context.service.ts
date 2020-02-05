import { Injectable } from '@angular/core';
import { environment } from '../environments/environment';
import { HttpClient } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';
import { Weather } from './weather.enum';
import { Air } from './air.enum';

const baseApiContextUrl: string = environment.baseApiUrl + 'context/api/context';
const baseApiContextWeatherUrl: string = baseApiContextUrl + '/weather/current';
const baseApiContextAirUrl: string = baseApiContextUrl + '/air/current';

// In milliseconds
const contextRefreshInterval = 5000;

interface ApiContextWeatherResponse {
  condition: Weather;
}

interface ApiContextAirResponse {
  condition: Air;
}

@Injectable({
  providedIn: 'root'
})
export class ContextService {
  private lastKnownWeather: null | Weather;
  private lastKnownAir: null | Air;

  private currentWeatherSubject$: Subject<Weather> = new Subject<Weather>();
  private currentAirSubject$: Subject<Air> = new Subject<Air>();

  private fetchingWeather = false;
  private fetchingAir = false;

  constructor(private http: HttpClient) {
    this.fetchContext();
    setInterval(() => this.fetchContext(), contextRefreshInterval);
  }

  private fetchContext(): void {
    this.fetchCurrentAir();
    this.fetchCurrentWeather();
  }

  private fetchCurrentWeather(): void {
    if (this.fetchingWeather) {
      return;
    }
    this.fetchingWeather = true;
    this.http.get<ApiContextWeatherResponse>(baseApiContextWeatherUrl)
      .toPromise()
      .then(weatherResponse => {
        this.lastKnownWeather = weatherResponse.condition;
        this.currentWeatherSubject$.next(weatherResponse.condition);
      })
      .finally(() => this.fetchingWeather = false);
  }

  private fetchCurrentAir(): void {
    if (this.fetchingAir) {
      return;
    }
    this.fetchingAir = true;
    this.http.get<ApiContextAirResponse>(baseApiContextAirUrl)
      .toPromise()
      .then(airResponse => {
        this.lastKnownAir = airResponse.condition;
        this.currentAirSubject$.next(airResponse.condition);
      })
      .finally(() => this.fetchingAir = false);
  }

  public getCurrentWeather(): null | Weather {
    return this.lastKnownWeather;
  }

  public getCurrentAir(): null | Air {
    return this.lastKnownAir;
  }

  public getCurrentWeather$(): Observable<Weather> {
    return this.currentWeatherSubject$.asObservable();
  }

  public getCurrentAir$(): Observable<Air> {
    return this.currentAirSubject$.asObservable();
  }
}
