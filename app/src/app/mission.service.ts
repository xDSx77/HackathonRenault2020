import { Injectable } from '@angular/core';
import { Subject, Observable } from 'rxjs';
import { MissionData } from './mission-data';
import { MatDialog } from '@angular/material';
import { MissionDialogComponent } from './mission-dialog/mission-dialog.component';
import { environment } from '../environments/environment';
import { HttpClient } from '@angular/common/http';

const missionApiURL: string = environment.customApiUrl + 'foobar';

// In milliseconds
const missionRefreshInterval = 5000;

interface ApiMissionResponse {
  mission: MissionData;
}

@Injectable({
  providedIn: 'root'
})
export class MissionService {
  currentMission: MissionData | null = null;
  currentMission$: Subject<MissionData> = new Subject<MissionData>();

  fetchingMission = false;

  constructor(
    public dialog: MatDialog,
    private http: HttpClient,
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

    this.fetchCurrentMission();
    setInterval(() => this.fetchCurrentMission(), missionRefreshInterval);
  }

  private fetchCurrentMission(): void {
    if (this.fetchingMission) {
      return;
    }
    this.fetchingMission = true;
    this.http.get<ApiMissionResponse>(missionApiURL)
      .toPromise()
      .then(missionResponse => {
        this.currentMission = missionResponse.mission;
        this.currentMission$.next(missionResponse.mission);
      })
      .finally(() => this.fetchingMission = false);
  }

  getCurrentMission$(): Observable<MissionData> {
    return this.currentMission$.asObservable();
  }

  getCurrentMission(): null | MissionData {
    return this.currentMission;
  }

  openMissionDialog(mission: MissionData): void {
    const dialogRef = this.dialog.open(MissionDialogComponent, {
      closeOnNavigation: false,
      disableClose: true,
      data: mission
    });
  }
}
