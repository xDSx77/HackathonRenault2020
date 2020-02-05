import { Component, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { MissionData } from '../mission-data';

@Component({
  selector: 'app-mission-dialog',
  templateUrl: './mission-dialog.component.html',
  styleUrls: ['./mission-dialog.component.scss']
})
export class MissionDialogComponent {

  constructor(
    public dialogRef: MatDialogRef<MissionDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: MissionData
  ) { }

  onClick(): void {
    this.dialogRef.close();
  }
}
