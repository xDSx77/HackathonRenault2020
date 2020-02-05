import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';
import { MissionData } from './mission-data';
import { MatDialog } from '@angular/material';
import { MissionDialogComponent } from './mission-dialog/mission-dialog.component';

@Injectable({
  providedIn: 'root'
})
export class MissionService {
  currentMission$: Subject<MissionData> = new Subject<MissionData>();

  constructor(
    public dialog: MatDialog
  ) {
    // Placeholder mission while the service is not fully created
    setTimeout(() => this.currentMission$.next({
      mission: 'Votre mission, si vous l\'acceptez, consiste à passer par l\'ensemble des points ci dessous.',
      positions: [
        {
          x: 0.1,
          y: 0.3
        },
        {
          x: 1.0,
          y: 2.1
        }
      ]
    }), 1000);
  }

  getCurrentMission$() {
    return this.currentMission$.asObservable();
  }

  openMissionDialog(mission: MissionData): void {
    const dialogRef = this.dialog.open(MissionDialogComponent, {
      closeOnNavigation: false,
      disableClose: true,
      data: mission
    });
  }
}
