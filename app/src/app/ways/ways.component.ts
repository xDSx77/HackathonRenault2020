import { Component, OnInit } from '@angular/core';
import {MatExpansionModule} from '@angular/material/expansion';
import {MatFormFieldModule} from '@angular/material/form-field';
import { Way } from './wayModel';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { catchError } from 'rxjs/operators';


@Component({
  selector: 'app-ways',
  templateUrl: './ways.component.html',
  styleUrls: ['./ways.component.scss']
})
export class WaysComponent implements OnInit {

  currentWay = 0;
  ways: Way[]; //= [{time: "50min", transports: ["metro", "velo", "marche", "autotaxi"], transportTime: ["10min", "5min", "15min", "20min"]},
 //               {time: "30min", transports: ["metro", "autotaxi"], transportTime: ["15min", "20min"]}
//];

cos = -1;

  constructor(private http: HttpClient) {
    this.fetchWays("toto");
   }

   cost(way: Way) {
    let res = 0;
    way.total_cost.forEach(element => {
      res += element;
    });
    return res;
   }

   move() {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json',
      })
    };
     this.http.post<number>(environment.baseApiUrl + "uri", this.currentWay, httpOptions).subscribe();
  }

  fetchWays(uri: string) {
    this.http.get(environment.baseApiUrl + uri).subscribe((data: Way[]) => {
      this.ways = data;
    });
   }

  ngOnInit() {
  }

}
