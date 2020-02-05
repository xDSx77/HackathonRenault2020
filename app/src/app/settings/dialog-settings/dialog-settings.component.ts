import { Component, OnInit } from '@angular/core';
import {MatDialog, MatDialogRef} from '@angular/material/dialog';
import {MatCheckboxModule} from '@angular/material/checkbox';
import {MatRadioModule} from '@angular/material/radio';
import { FormBuilder, FormGroup } from '@angular/forms';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { Preference } from '../preference.enum';


@Component({
  selector: 'app-dialog-settings',
  templateUrl: './dialog-settings.component.html',
  styleUrls: ['./dialog-settings.component.scss']
})
export class DialogSettingsComponent implements OnInit {

  public settingForm: FormGroup;

  transportPref = { marche: true,
    autotaxi : true,
    velo: true,
    metro: true};

preference: Preference = Preference.Fastest;

  constructor(public dialogRef: MatDialogRef<DialogSettingsComponent>, private formBuilder: FormBuilder) {
    this.settingForm = this.formBuilder.group({
      metro: true,
      velo: true,
      marche: true,
      autotaxi: true,
      preference: "fastest"
    });

    this.settingForm.get("metro").valueChanges.subscribe(
      data => {
        this.transportPref.metro = data;
      });
    this.settingForm.get("marche").valueChanges.subscribe(
      data => {
        this.transportPref.marche = data;
      });
    this.settingForm.get("autotaxi").valueChanges.subscribe(
      data => {
        this.transportPref.autotaxi = data;
      });
    this.settingForm.get("velo").valueChanges.subscribe(
      data => {
        this.transportPref.velo = data;
      });
    this.settingForm.get("preference").valueChanges.subscribe(
      data => {
        this.preference = data;
      });
   }

  onNoClick(): void {

    this.dialogRef.close({
      transportPref: this.transportPref,
      preference: this.preference
    });
  }

  ngOnInit() {
  }

}
