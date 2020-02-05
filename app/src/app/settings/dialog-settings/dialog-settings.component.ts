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
      transportPref: '',
      preference: ''
    });
   }

  onNoClick(): void {
    this.dialogRef.close();
  }

  ngOnInit() {
  }

}
