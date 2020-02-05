import { Component } from '@angular/core';
import { MatIconRegistry } from '@angular/material/icon';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'HackathonRenault2020Front';
  isMap = true;
  buttonText = "Changer de trajet";

  constructor(
    private matIconRegistry: MatIconRegistry,
    private domSanitizer: DomSanitizer
  ) {
    // Weather icons
    this.matIconRegistry.addSvgIcon('weather-normal', this.domSanitizer.bypassSecurityTrustResourceUrl('../assets/svg/sun.svg'));
    this.matIconRegistry.addSvgIcon('weather-rain', this.domSanitizer.bypassSecurityTrustResourceUrl('../assets/svg/rain.svg'));
    this.matIconRegistry.addSvgIcon('weather-snow', this.domSanitizer.bypassSecurityTrustResourceUrl('../assets/svg/snowing.svg'));
    this.matIconRegistry.addSvgIcon('weather-heat wave', this.domSanitizer.bypassSecurityTrustResourceUrl('../assets/svg/thermometer.svg'));

    // Air quality icons
    this.matIconRegistry.addSvgIcon('air-normal', this.domSanitizer.bypassSecurityTrustResourceUrl('../assets/svg/heart.svg'));
    this.matIconRegistry.addSvgIcon('air-pollution peak', this.domSanitizer.bypassSecurityTrustResourceUrl('../assets/svg/co2.svg'));
  }

  changeView() {
    this.isMap = !this.isMap;
    if (this.isMap)
      this.buttonText = "Changer de trajet";
    else
      this.buttonText = "Retour";
  }
}
