import { Component, OnInit } from '@angular/core';
import {MatExpansionModule} from '@angular/material/expansion';
import {MatFormFieldModule} from '@angular/material/form-field';
import { Way } from './wayModel';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';


@Component({
  selector: 'app-ways',
  templateUrl: './ways.component.html',
  styleUrls: ['./ways.component.scss']
})
export class WaysComponent implements OnInit {

  ways: Way[] = [{time: "50min", transports: ["metro", "velo", "marche", "autotaxi"], transportTime: ["10min", "5min", "15min", "20min"]},
                {time: "10min", transports: ["metro", "autotaxi"], transportTime: ["15min", "20min"]}
];

  constructor(private http: HttpClient) {
    //this.fetchWays("toto"); //URI TO GET WAYS)
   }

  fetchWays(uri: string) {
    this.http.get(environment.baseApiUrl + uri).subscribe((data: Way[]) => {
      this.ways = data;
    });
   }

  ngOnInit() {
  }

}
