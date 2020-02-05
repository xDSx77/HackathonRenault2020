import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatCheckboxModule} from '@angular/material/checkbox';
import {MatRadioModule} from '@angular/material/radio';

import {
  MatToolbarModule,
  MatIconModule,
  MatDialogModule
} from '@angular/material';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SettingsComponent } from './settings/settings.component';
import { DialogSettingsComponent } from './settings/dialog-settings/dialog-settings.component';
import { CurrentWeatherComponent } from './current-weather/current-weather.component';
import { CurrentAirComponent } from './current-air/current-air.component';

@NgModule({
  declarations: [
    AppComponent,
    SettingsComponent,
    DialogSettingsComponent,
    CurrentWeatherComponent,
    CurrentAirComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MatToolbarModule,
    MatIconModule,
    MatDialogModule,
    MatCheckboxModule,
    MatRadioModule,
    BrowserAnimationsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent],
  entryComponents: [DialogSettingsComponent]
})
export class AppModule { }
