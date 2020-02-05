import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatCheckboxModule} from '@angular/material/checkbox';
import {MatRadioModule} from '@angular/material/radio';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import {MatExpansionModule} from '@angular/material/expansion';


import {
  MatToolbarModule,
  MatIconModule,
  MatDialogModule,
  MatButtonModule,
  MatListModule
} from '@angular/material';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SettingsComponent } from './settings/settings.component';
import { DialogSettingsComponent } from './settings/dialog-settings/dialog-settings.component';
import { CurrentWeatherComponent } from './current-weather/current-weather.component';
import { CurrentAirComponent } from './current-air/current-air.component';
import { MapComponent } from './map/map.component';
import { WaysComponent } from './ways/ways.component';
import {MatFormFieldModule} from '@angular/material/form-field';
import { MissionDialogComponent } from './mission-dialog/mission-dialog.component';


@NgModule({
  declarations: [
    AppComponent,
    SettingsComponent,
    DialogSettingsComponent,
    CurrentWeatherComponent,
    CurrentAirComponent,
    MapComponent,
    WaysComponent,
    MissionDialogComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MatToolbarModule,
    MatIconModule,
    MatDialogModule,
    MatCheckboxModule,
    MatRadioModule,
    MatFormFieldModule,
    MatExpansionModule,
    BrowserAnimationsModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    MatButtonModule,
    MatListModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
  entryComponents: [
    DialogSettingsComponent,
    MissionDialogComponent
  ]
})
export class AppModule { }
