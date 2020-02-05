import { Component, OnInit } from '@angular/core';
import {MatDialog} from '@angular/material/dialog';
import { DialogSettingsComponent } from './dialog-settings/dialog-settings.component';
import { Preference } from './preference.enum';
import { FormBuilder, FormGroup } from '@angular/forms';


@Component({
  selector: 'app-settings',
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.scss']
})
export class SettingsComponent implements OnInit {

  
  constructor(private dialog: MatDialog) {}
  
  openDialog(): void {
    const dialogRef = this.dialog.open(DialogSettingsComponent, {
      width: '250px',
      data: {}
    });

    dialogRef.afterClosed().subscribe(result => {
      //SEND RESULT TO API
    });
  }

  ngOnInit() {
  }
}